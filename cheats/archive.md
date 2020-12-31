# 7z

% archive, 7zip, 7z

## 7z create archive with password
```
7z a <archive_name>.7z -p<pasword> <file>
```

# tar

% archive, tar

## Create a tar containing files
```
tar cf <name>.tar <files>
```

## Extract the files from a tar
```
tar xf <tar_file>
```

## Create a tar with Gzip compression
```
tar czf <name>.tar.gz <files> 
```

## Extract a tar using Gzip
```
tar xzf <targz_file>
```

# gzip

% archive, gzip

## Compress file and appends .gz to its name
```
gzip <path>
```

## Decompress compressed file
```
gzip -d <gz_file>
```

# rar

% archive, rar

## Compress dir to rar file
```
rar a <dir>
```

# Decompress rar file
```
unrar x <file>.rar
```

# zip

% archive, zip

## create zip file
```
zip <file>.zip <files_to_zip>
```

## zip all the files of current directory
```
zip <file>.zip *
```

## zip folder
```
zip -r <file>.zip <folder>
```

## add file to a zip archive
```
zip -u <file>.zip <file_to_add>
```

## view zip content
```
zipinfo <file>.zip
```

## create zip file with symlink (usefull for path traversal)
```
zip --symlinks <file>.zip <symlink_file>
```

## list detailed zip file content
```
unzip -Z <file>.zip
```

## unzip file
```
unzip <file>.zip
```

## unzip file to directory
```
unzip <file>.zip -d <destination_folder>
```

