# AppBoxo Todo Application
Take home assignment for verifying Python, Django, REST API, Docker skills sufficient for creating simple CRUD application  

# Prerequisites
- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Local Development
Copy .env.example file and set following env vars if needed:
- SECRET_KEY
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_DB

[comment]: <> (MEMCACHIER_SERVERS=server)

[comment]: <> (MEMCACHIER_USERNAME=username)

[comment]: <> (MEMCACHIER_PASSWORD=password)

Start the dev server for local development:
```bash
docker-compose up
```

# Deploying to Heroku
TODO

# REST API Documentation
Link to API will be at i.e **'localhost:8000/api/docs/'**