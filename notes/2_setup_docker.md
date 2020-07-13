### Setup Docker
Install Docker
```
$ yum install docker docker-registry

$ systemctl enable docker
$ systemctl start docker
$ systemctl status docker
```

Download docker images
```
$ docker pull mariadb:10.4
$ docker pull redis:6.0

$ docker image ls
```

Launching MariaDB, Redis
```
$ docker run -d --name maria -p 33061:3306 -e MYSQL_ROOT_PASSWORD=wpdlwl -e MYSQL_DATABASE=backend mariadb:10.4
$ docker run -d --name my_redis -p 63791:6379 redis:6.0

$ docker ps -a
```