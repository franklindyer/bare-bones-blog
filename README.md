A bare-bones blog skeleton for the sis.

To create a new markdown post, add your markdown file to the `entries` folder. Then you need to add some information about this post into your database `blog.db`, in the table `entries`. You can do this using a command like `INSERT INTO entries (name, filename) VALUES ("Name of Post", "name_of_markdown_file");`. When you do this, the post will automatically be assigned an id and a timestamp.

Additional static resources, like images, css stylesheets, and javascript, are served at the paths `/img`, `/css`, and `/js`, and they draw from the folders `img`, `css`, and `js`.
