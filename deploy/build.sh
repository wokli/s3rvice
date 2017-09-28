#/usr/bin/env sh
source deploy/image.sh
echo $IMAGE > VERSION
docker build -t $DHUB/$IMAGE .
