Software Studio @ cs.hanynag

Duplicated in [GitHub](https://github.com/MaybeS/ITE3068) for sort out my tasks.

- [x] [Assignment: Using billboard.js](https://hconnect.hanyang.ac.kr/SW_studio2_2017/ITE3068)
- [x] [Project](https://hconnect.hanyang.ac.kr/SW_studio2_2017/2015004584)

## Project Requirements

- [x] Use [Docker](https://www.docker.com/) (10pts)
- [x] Performance Comparison (using [arcus](http://naver.github.io/arcus/)) (20pts)
- [x] Use [nBase-ARC](https://github.com/naver/nbase-arc) (20pts)
- [x] Use multi-node (10pts)
- [x] Use [Hubblemon](https://github.com/naver/hubblemon) (10pts)
- [x] Use [nGrinder](http://naver.github.io/ngrinder/) (10pts)
- [x] [Naver Open Source](https://github.com/naver) Contribution
    - Oppend Issues
        1. [arcus-python-client: `Pypi's arcus package seems to have expired`](https://github.com/naver/arcus-python-client/issues/11)
        2. [arcus-python-client: `Not working in macOS`](https://github.com/naver/arcus-python-client/issues/12)
        3. [arcus: `Support docker`](https://github.com/naver/arcus/issues/35)
    - Pull Requests
        1. [hubblemon: `update dependency`](https://github.com/naver/hubblemon/pull/22)
        2. [arcus-python-client: `Update Poller for darwin(macOS)`](https://github.com/naver/arcus-python-client/pull/13)
        3. [arcus: `Update dockerfile`](https://github.com/naver/arcus/pull/36)

## Project

Using [Docker](https://www.docker.com/) with [arcus](https://hub.docker.com/r/ruo91/arcus/), [MySQL](https://hub.docker.com/_/mysql/), [nBase-ARC](https://hub.docker.com/r/hyeongseok05/nbase-arc/).

API app is simple flask app for performance comparison.

All settings are stored in `settings.json`. you can change enviroments for you own service.

### API App (for performance comparison)
Powered by flask, support simple RestfulAPI for performance comparison.

API Lists

- `GET`: `/init`
    Initialize database, create testset table, and insert some records.
- `GET`: `/mysql` 
    Select some integer from mysql (range 0 - testsize)
- `GET`: `/arcus`
    Select some integer from arcus if missed, select from mysql and add to arcus
- `GET`: `/nbase`
    Select some integer from nbase if missed, select from mysql and add to nbase

### MySQL

Pulling from public mysql dockerfile(version `5.7`, but it can also `latest`).
There are some enviroments for mysql db.

- *MYSQL_ROOT_PASSWORD*: password
- *MYSQL_USER*: maybe
- *MYSQL_PASSWORD*: password
- *MYSQL_DATABASE*: ite3068

### Arcus

Pulling from [ruo91/arcus](https://hub.docker.com/r/ruo91/arcus/) and some appendix scripts for memcached server.
See `arcus/install.sh`. It provide arcus to memcached server list and set up zookeeper and memcached.
It automatically run after docker container started.

### nBase-ARC

Pulling from [hyeongseok05/nbase-arc](https://hub.docker.com/r/hyeongseok05/nbase-arc/).
Dockerfile prepare all for start nbase-arc, so just start docker container is enough.

### Hubblemon

It's difficult to compose all of docker container in a single `docker-compose`. 
*Because, arcus and memcached require settins after container started.*

So, hubblemon run each `mysql`, `arcus`, `nbase`.
To do this, after each container started, process `hubblemon/install.sh`.

Script contains below

- Install depedency (It takes time depending on the internet(or repo server) speed)
- Clone hubblemon repository
- Copy each setting
- Install python dependency
- Run server

### nGrinder Test

nGrinder supports writing a script that sends an HTTP request and sends it to the agent for testing. 
The web server receives the HTTP request and can communicate with the mysql server or the arcus server. 
Now you can actually write those scripts through nGrinder to compare performance differences between using the mysql server directly and the arcus server.

You can test the performance in nGrinder by calling the api created in the flask app above.

## Usage 

Just run application, it uses docker service.

```
python app.py start
```

for stop service,

```
python app.py stop
```

Require `python3`, `docker` only.
