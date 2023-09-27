from bottle import route, run, template, static_file, error, redirect, request, install, get
import os
import datetime
import markdown
import sys

# sqlite plugin for bottle routes
from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='/data/app/web/blog.db'))

# turns SQL query results into dictionaries
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# page not found
@error(404)
def error404(error):
    return("<html><body><p>Nothin' to see here...</p></body><html>")

# internal server error
@error(500)
def error500(error):
    return("<html><body><p>Oops, something went wrong!</p></body></html>")

# home page
@route('/')
def index(db): # the SQL database is passed to the route so that information about posts can appear on the homepage

    # get the 10 most recent blog entries
    recent = db.execute('SELECT * FROM entries ORDER BY created DESC LIMIT 5')
    
    # return the homepage template, passing it some recent posts
    return template('/data/app/web/tpl/index.tpl', recent=recent)

# specific markdown blog post
@route('/post/<post_id>')
def index(db, post_id): # the SQL database is passed so that the function can find the post with the given id

    # turns query results into dictionaries
    db.row_factory = dict_factory

    # get the blog entry with the given id
    result = db.execute("SELECT * FROM entries WHERE id = ?", (post_id,))
    post = result.fetchone()

    # open the corresponding markdown file
    f = open("web/entries/" + post["filename"] + ".md", "r")

    # convert the markdown to html
    proc = markdown.Markdown(extensions=['mdx_math'])
    fr = f.read()
    f.close()
    entry = proc.convert(fr)

    # return the post template, passing in the entry content and title
    return template('/data/app/web/tpl/post.tpl', entry=entry, title=post['name'])

# post display route
@route('/posts')
def posts(db):

    db.row_factory = dict_factory
    result = db.execute("SELECT * FROM entries ORDER BY created DESC")
    posts = result.fetchall()

    return template('/data/app/web/tpl/posts.tpl', posts=posts)

# other files, like css, images, javascript, etc.
@get("/<dir:re:(css|img|js|file)>/<filename>")
def serve_image(dir, filename):
    return static_file(filename, root="/data/app/web/"+dir)

# run the server and listen on port 8080
portnum = int(sys.argv[1])
run(host="0.0.0.0", port=portnum, debug=True, reloader=True)
