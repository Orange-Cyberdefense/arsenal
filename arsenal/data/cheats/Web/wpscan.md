# WPSCAN

% wpscan, wordpress

#plateform/linux #target/remote #cat/RECON 
## wpscan with docker and burp proxy
```
sudo docker run -it --network host --rm wpscanteam/wpscan --proxy http://127.0.0.1:8080 --url <url> --disable-tls-checks -e ap,tt,cb,dbe,u1-20,m --api-token <wpscan_apitoken>
```
