# gpg

% gpg

#platform/linux #target/local #cat/UTILS

## gpg version
```
gpg --version
```

## gpg generate key
```
gpg --gen-key
```

## list keys
```
gpg --list-keys
```

## distribute public key to key server
```
gpg --keyserver <key_server> --send-keys <public_key>
```

## export public key
```
gpg --output <filename_gpg> --export <key_name>
```

## import public key
```
gpg --import <filename_gpg>
```

## encrypt document
```
gpg --output <output_filename_gpg> --encrypt --recipient <public_key> <input_filename>
```

## decrypt document
```
gpg --output <filename> --decrypt <filename_gpg>
```

## make a signature
```
gpg --output <filename_sig> --sign <filename>
```

## verify signature
```
gpg --output <filename> <filename> --decrypt <filename_sig>
```

## clearsign documents
```
gpg --clearsign <filename>
```

## detach signature
```
gpg --output <filename_sig> --detach-sig <filename>
```
