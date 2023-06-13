# [LINUX]

## zip - create password encrypted archive
```
zip --password <password> -r encrypted.zip <folder_path>
```

## dd - copy image to storage medium
```
dd if=<iso_path> of=<disk> bs=4096 status=progress && sync
```

## wget - execute remote script directly
```
wget http://<file_path> -O- | sh
```

## truncate - shorten file
```
truncate -s [-]<size_in_bytes> <file_path>
```

## VMware - mount a shared folder
```
/usr/bin/vmhgfs-fuse .host:/<shared_folder_name> <folder_path> -o subtype=vmhgfs-fuse 
```


# [LINUX][ENUM]

## find - search specific file
```
find / -iname <file_name> 2>/dev/null
```

## find writable directories
```
find / -type d -writable 2>/dev/null 
```

## find - SUID/SGID files
```
find / \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null
```

## find - all .log files
```
find / -name "*.log" 2>/dev/null
```

## find - all INTERESTING files
```
find / -regex '.*\.\(txt\|xml\|doc\|docx\)' 2>/dev/null
```

## find - owned by specific user
```
find / -user <user> 2>/dev/null
```

## find - readable iptables configuration
```
find / -name "*iptables*" -o -name "*nftables*" -readable 2>/dev/null
```

