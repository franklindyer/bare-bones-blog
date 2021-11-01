from bottle import route, run, template, static_file, error, redirect, request, install, get
import os
import datetime
import markdown

# sqlite plugin for bottle routes
from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='course.db'))

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

## these routes (below) catch valid http requests and return the appropriate templates/pages

# home page
@route('/')
def index(db): # the SQL database is passed to the route so that information about posts can appear on the homepage

    # get all non-hidden units, ordered by level
    units = db.execute('SELECT * FROM units WHERE hidden = 0 ORDER BY level ASC')
    
    # return the homepage template, passing it the list of units
    return template('tpl/home.tpl', units=units)

@route('/unit/<unit_id>')
def index(db, unit_id):
    
    # get the lessons of the given unit, so long as they aren't hidden
    unit = list(db.execute('SELECT * FROM units WHERE id = ? AND hidden = 0', (unit_id,)))[0]
    lessons = db.execute('SELECT * FROM lessons WHERE unit = ? AND hidden = 0 ORDER BY level ASC', (unit_id,))

    # return the template for a unit page, passing lessons from that unit
    return template('tpl/unit.tpl', lessons=lessons, unit=unit)

# specific lesson, could be markdown or html
@route('/lesson/<lesson_id>')
def index(db, lesson_id): # the SQL database is passed so that the function can find the post with the given id

    # turns query results into dictionaries
    db.row_factory = dict_factory

    # get the lesson with the given id
    result = db.execute("SELECT * FROM lessons WHERE id = ? AND hidden = 0", (lesson_id,))
    lesson = result.fetchone()

    # open the corresponding file (file ending must be specified)
    f = open("entries/" + lesson["filename"], "r")

    # convert the markdown to html
    proc = markdown.Markdown()
    fr = f.read()
    f.close()
    entry = proc.convert(fr)

    # return the post template, passing in the entry content and title
    return template('tpl/lesson.tpl', entry=entry, title=lesson['name'], unit=lesson['unit'])

# other files, like css, images, javascript, etc.
@get("/<dir:re:(css|img|js|file)>/<filename>")
def serve_image(dir, filename):
    return static_file(filename, root=dir)

# run the server and listen on port 4000
run(host="localhost", port=4000, debug=True, reloader=True)
run
