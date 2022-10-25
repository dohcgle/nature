# Nature


# Определение сетевых интерфейсов в Ubuntu 20.4 server
>ip link show

# Установка статичекого ip на Ubuntu 20.4 server
>sudo nano /etc/netplan/00-installer-config.yaml 

```
network:
  version: 2
  ethernets:
    ens33:
       addresses: [192.168.2.241/24]
       gateway4: 192.168.2.1
       nameservers:
         addresses: [4.4.4.4, 8.8.8.8]
```
>sudo netplan apply
****


***
# 1. Вариант. Настройка Docker (django+gunicorn+nginx)

## Установка docker
``` 
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

```

## Установка docker-compose
``` 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version

```



## Создайте Dockerfile в корневую папку приложения
``` 
FROM python:3.9-alpine

# set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./entrypoint.sh .



RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt


# copy project
COPY . .
ENTRYPOINT ["/app/entrypoint.sh"]
```
## Создайте docker-compose.yml в корневую папку приложения
``` 
version: '3.7'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    expose:
      - 8000
    volumes:
      - /home/ulugbek/nature/static:/app/static
      - /home/ulugbek/nature/mediafiles:/app/mediafiles
    entrypoint:
      - ./entrypoint.sh


  nginx:
    build: ./nginx

    volumes:
      - /home/ulugbek/nature/static:/app/static
      - /home/ulugbek/nature/mediafiles:/app/mediafiles
    ports:
      - 1447:80
    depends_on:
      - web
```

## Создайте каталог ngnix в корневую папку приложения. Добавьте 2 файла "default.conf" "Dockerfile"
### default.conf:
``` 
upstream web {
    server web:8000;
}

server {
    listen 80;
    server_name 192.168.2.241;


    location /static/ {
        alias /app/static/;
    }

    location /media/ {
        alias /app/media/;
    }


    location / {
        proxy_pass http://web;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}
```





### Dockerfile:
``` 
FROM nginx:1.19.0-alpine
COPY ./default.conf /etc/nginx/conf.d/default.conf
```



## Docker команды
```
docker-compose up -d --build
docker-compose down 
sudo docker exec -it <container_id> /bin/sh
```

## Docker autorun
``` 
sudo docker update --restart unless-stopped container_id
```



## Docker без sudo
``` 
sudo groupadd docker
sudo gpasswd -a $USER docker 
 ```

## Разрешиния доступа к корнивую папку
``` 
sudo chmod -R 755 ../nature
```

## Осторожно! Удаление всех образов! 
``` 
docker rmi $(docker images -q)
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

***