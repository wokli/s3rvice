#/usr/bin/env sh
if [ -z "$TAG" ]; then
    export COMMIT=$(git log --pretty=format:'%h' -n 1)
    export IMAGE=$PRJ:$COMMIT
else
    git checkout $TAG
    export IMAGE=$PRJ:$TAG
fi
env