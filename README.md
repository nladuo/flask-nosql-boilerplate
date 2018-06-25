# flask-nosql-boilerplate
A pure backend boilerplate for Flask when using mongodb and redis.

## Installation
``` sh
sudo apt-get install libpcre3 libpcre3-dev
pip install -r requirements.txt
```

## Deployment
### Nginx
check [fnb.conf](fnb.conf)

### uWSGI
``` sh
nohup uwsgi fnb.ini &
```


## LICENSE
MIT