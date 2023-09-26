This is a bare-bones blog skeleton.

Here's what you need to know to use it:
- Entries are markdown files in `/web/entries` and are served at `/<post_id>`.
- Static resources are stored in `/web/img`, `/web/css`, `/web/js` and are served at `/<type>/<name>`.
- Post metadata is stored in `/web/blog.db`. Run `.schema` in sqlite3 for a list of tables/columns.

It is recommended to run this app using Docker. You can do this quickly using the following steps:
- Install Docker.
- Clone this repository.
- Change directory into the cloned repo.
- Run `docker run -p <your_port>:8080 -v ./web:/data/app/web -d frpzzd/bare-bones-blog:latest`.
	- `-p <your_port>:8080` binds port `8080` of the container to `<your_port>` on your machine
	- `-v ./web:/data/app/web` binds the directory `./web` of this repo to `/data/app/web` in the container
	- `-d` runs the container in the background and prints the container ID
	- `frpzzd/bare-bones-blog:latest` is my personal build of this project
- Visit (or curl) `http://localhost:<your_port>` on the same machine as the one running the app.
