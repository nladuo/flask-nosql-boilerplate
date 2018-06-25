# flask-nosql-boilerplate
A pure backend boilerplate for Flask using  mongodb and redis.


## Deployment
### Nginx
check [fnb.conf](fnb.conf)

### uWSGI
``` sh
nohup uwsgi fnb.ini &
```


## For Ubuntu
``` sh
sudo apt-get install libpcre3 libpcre3-dev
```

## LICENSE
MIT