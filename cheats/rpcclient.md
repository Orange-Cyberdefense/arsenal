# rpcclient

% rpcclient, rpc, windows

## rpcclient - enumdomusers
```
rpcclient <ip> -U "<user>%<pass>" -c "enumdomusers;quit"
```

## rpcclient - srvinfo
```
rpcclient <ip> -U "<user>%<pass>" -c "srvinfo;quit"
```

## rpcclient - querydominfo
```
rpcclient <ip> -U "<user>%<pass>" -c "querydominfo;quit"
```

## rpcclient - getdompwinfo  (password policy)
```
rpcclient <ip> -U "<user>%<pass>" -c "getdompwinfo;quit"
```

## rpcclient - netshareenum  (password policy)
```
rpcclient <ip> -U "<user>%<pass>" -c "netshareenum;quit"
```

## Trying all username as password from list of users
```
for u in `cat <file>`; do echo -n "user: $u " && rpcclient -U "$u%$u" -c "getusername;quit" <ip>; done
```