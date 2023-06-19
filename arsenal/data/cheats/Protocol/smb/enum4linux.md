# enum4linux

% smb, samba

#plateform/linux  #target/remote  #port/445 #protocol/smb #cat/RECON 

## enum4linux - all except dictionary based share name listing (default)
```
enum4linux -a <ip>
```

## enum4linux - verbose
```
enum4linux -v <ip>
```

## enum4linux - null access
```
enum4linux -u "" -p "" <ip>
```

## enum4linux - guest access
```
enum4linux -u "guest" -p "" <ip>
```

## enum4linux - with authentication
```
enum4linux -u <user> -p <password> <ip>
```

## enum4linux - list Users
```
enum4linux -U <ip> |grep 'user:'
```
