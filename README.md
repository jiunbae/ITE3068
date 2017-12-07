Software Studio @ cs.hanynag

Duplicated in [GitHub](https://github.com/MaybeS/ITE3068) for sort out my tasks.

- [x] [Assignment: Using billboard.js](https://hconnect.hanyang.ac.kr/SW_studio2_2017/ITE3068)
- [x] [Project](https://hconnect.hanyang.ac.kr/SW_studio2_2017/2015004584)

## Project Requirements

- [x] Use Docker (10pts)
- [x] Performance Comparison (using arcus) (20pts)
- [x] Use nBase-ARC (20pts)
- [x] Use multi-node (10pts)
- [ ] Use Hubblemon (10pts)
- [x] Use NGrinder (10pts)
- [x] [Naver Open Source](https://github.com/naver) Contribution
    - [x] [1 Contribution](https://github.com/naver/hubblemon/pull/22) (10pts)
    - [x] [2 Contribution](https://github.com/naver/arcus-python-client/pull/13) (15pts)
    - [ ] [3 Contribution](https://github.com/naver/arcus-python-client/issues/11) (20pts)

## Project

Using [Docker](https://www.docker.com/) with [arcus](https://hub.docker.com/r/ruo91/arcus/), [MySQL](https://hub.docker.com/_/mysql/), [nBase-ARC](https://hub.docker.com/r/hyeongseok05/nbase-arc/).

app is simple flask app for performance comparison.

### App (for performance comparison)
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

### nGrinder Test
nGrinder supports writing a script that sends an HTTP request and sends it to the agent for testing. 
The web server receives the HTTP request and can communicate with the mysql server or the arcus server. 
Now you can actually write those scripts through nGrinder to compare performance differences between using the mysql server directly and the arcus server.

You can test the performance in nGrinder by calling the api created in the flask app above.

