# QR code

% qr code

## Create a QR code with some content
#platform/linux #target/local #cat/UTILS 

```
echo <content> | curl -F-=\<- qrenco.de
```

## json

% json

## convert JSON to YAML
#platform/linux #target/local #cat/UTILS
```
cat <json_file> | ruby -ryaml -rjson -e 'puts YAML.dump(JSON.load(ARGF))'
```

# linux 

% misc, linux

## Convert multi line to one line
#platform/linux #target/local #cat/UTILS 
```
grep <pattern> <file> | tr '\n' ' '
```

## grep nmap protocol from file and get ips in one line
#platform/linux #target/local #cat/UTILS 
```
grep <pattern> <file>.gnmap|cut -d ' ' -f 2 | tr '\n' ' '
```

% scanner

## find service on port
#platform/linux #target/remote #cat/RECON 
```
amap -d <ip> <port>
```

