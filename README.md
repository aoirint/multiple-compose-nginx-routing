# Cascaded nginx routing with multiple distributed docker-compose files
Sample project
including really-simple `Article API Server` and `Comment API Server`
that respond with `application/json` document.

Use `./compose.sh` instead `docker-compose` command in repository root.

## Repository root

In directory `multiple-compose-nginx-routing`,
you can start both `Article API Server` and `Comment API Server` at host port 8080
with `./compose.sh` command.

`Article API Server` can be accessed with `http://localhost:8080/article/`.
Host port 8081 is closed.

`Comment API Server` can be accessed with `http://localhost:8080/comment/`.
Host port 8082 is closed.

## article-api
In directory `article-api`,
you can start `Article API Server` at host port 8082
with `docker-compose` command.

`Article API Server` can be accessed with `http://localhost:8082/`

## comment-api
In directory `comment-api`,
you can start `Comment API Server` at host port 8081
with `docker-compose` command.

`Comment API Server` can be accessed with `http://localhost:8081/`
