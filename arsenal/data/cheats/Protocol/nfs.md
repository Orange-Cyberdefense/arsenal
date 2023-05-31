# nfs

% nfs, showmount, 2049
#platform/linux  #target/remote  #protocol/nfs #port/2049

## nfs showmount
#cat/RECON 
```
showmount -e <ip>
```

## nfs - nmap showmount
#cat/RECON 
```
nmap -sV --script=nfs-showmount <ip>
```

## nfs - mount
#cat/ATTACK/CONNECT 
```
mount -t nfs <ip>:<shared_folder> <mount_point> -o nolock
```

## nfs - mount with v2 (no authenrt=)
#cat/ATTACK/CONNECT 
```
mount -t nfs -o vers=2 <ip>:<shared_folder> <mount_point> -o nolock
```
