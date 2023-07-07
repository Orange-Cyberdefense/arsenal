# WPSCAN

% wpscan, wordpress

## wpsan - enumerate all plugins
#platform/linux #target/remote #cat/RECON 
```
wpsan --url <target_url|http://> --enumerate ap --plugins-detection aggressive -o <out_file|outfile.txt>
```

## wpscan with docker and burp proxy
```
sudo docker run -it --network host --rm wpscanteam/wpscan --proxy http://127.0.0.1:8080 --url <url> --disable-tls-checks -e ap,tt,cb,dbe,u1-20,m --api-token <wpscan_apitoken>
```
