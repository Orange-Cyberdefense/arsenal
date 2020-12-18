# QR code

% qr code

## Create a QR code with some content
```
echo <content> | curl -F-=\<- qrenco.de
```

## json

% json

## convert JSON to YAML
```
cat <json_file> | ruby -ryaml -rjson -e 'puts YAML.dump(JSON.load(ARGF))'
```

# linux 

% misc, linux

## Convert multi line to one line
grep <pattern> <file> | tr '\n' ' '

## grep nmap protocol from file and get ips in one line
grep <pattern> <file>.gnmap|cut -d ' ' -f 2 | tr '\n' ' '
