# enum4linux

% enum4linux, samba, smb, 445

## enum4linux - all except dictionnary based share name listing (default)
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
enum4linux -u <user> -p <pass> <ip>
```

## enum4linux - list Users
```
enum4linux -U <ip> |grep 'users:'
```
