#/usr/bin/env sh
source deploy/image.sh
sed "s@__IMAGE__@$DHUB/$IMAGE@" $TARGET-$PRJ.hcl | docker run -i nmd:latest run -