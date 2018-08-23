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
docker stop <NAME>
