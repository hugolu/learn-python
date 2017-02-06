# Environment

## Docker

Pull a docker image @host
```
$ docker pull dylanmei/zeppelin
```

> https://hub.docker.com/r/dylanmei/zeppelin/

Run/execute the docker container @host
```
$ export MYHOME=$HOME/github/learn-python
$ docker run --name python -p 8080:8080 -v $MYHOME:/learn-python -e "MYHOME=/learn-python" -d dylanmei/zeppelin
$ docker exec -it python bash
```
