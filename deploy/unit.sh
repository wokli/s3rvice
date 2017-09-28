#/usr/bin/env sh
source deploy/image.sh
docker run --rm $DHUB/$IMAGE pytest