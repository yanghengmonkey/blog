### Docker
## Create docker image
docker build -t <Name> .
## Add user to docker group
sudo groupadd docker
sudo gpasswd -a ${USER} docker
# Restart docker service
sudo service docker restart
# Switch current context
newgrp - docker
## Stop docker
docker stop <container>

### Docker inspect

docker inspect <container>

### Update restart policy

docker update --restart=<restart_policy> <container>

### Enter running docker image

docker exec -ti <CONTAINER> bash