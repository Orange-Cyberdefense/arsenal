# WEB

% web

## extract links from an url
#platform/linux #target/remote #cat/RECON 
```
curl -k -s <url> | grep -o 'http://[^"]*' | cut -d "/" -f 3 | sort -u
```
