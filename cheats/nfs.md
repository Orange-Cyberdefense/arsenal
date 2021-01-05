# nfs

% nfs, showmount, 2049

## nfs showmount
```
showmount -e <ip>
```

## nfs - nmap showmount
```
nmap -sV --script=nfs-showmount <ip>
```

## nfs - mount
```
mount -t nfs <ip>:<shared_folder> <mount_point> -o nolock
```

## nfs - mount with v2 (no authenrt=)
```
mount -t nfs -o vers=2 <ip>:<shared_folder> <mount_point> -o nolock
```
