# WEB

% web

## extract links from an url
```
curl -k -s <url> | grep -o 'http://[^"]*' | cut -d "/" -f 3 | sort -u
```
