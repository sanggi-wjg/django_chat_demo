### Install packages
```
$ yum install net-tools wget git
$ yum update
```

### Setup Python
Install Python
```
$ yum install gcc openssl-devel libffi-devel bzip2-devel
$ yum install mariadb-devel
$ pip install mysqlclient

$ mkdir /home/temp
$ cd /home/temp

$ wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
$ tar zxf Python-3.8.3.tgz

$ cd Python-3.8.3

$ ./configure --enable-optimizations
$ make altinstall

$ vi /root/.bashrc

(@paste below)
alias python="/usr/local/bin/python3.8"

$ source /root/.bashrc

$ check python
$ python -V
```

Install pip
```
$ cd /home/temp

$ wget https://bootstrap.pypa.io/get-pip.py

$ python get-pip.py

$ pip --version
$ pip list
```