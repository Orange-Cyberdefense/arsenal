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
