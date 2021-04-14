# rpcclient

% rpcclient, rpc, windows

## rpcclient - enumdomusers
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <ip> -U "<user>%<password>" -c "enumdomusers;quit"
```

## rpcclient - srvinfo
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <ip> -U "<user>%<password>" -c "srvinfo;quit"
```

## rpcclient - get user sid
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <ip> -c "lookupnales <name>; wmic useraccount get name,sid; quit"
```

## rpcclient - querydominfo
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <ip> -U "<user>%<password>" -c "querydominfo;quit"
```

## rpcclient - getdompwinfo  (password policy)
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <ip> -U "<user>%<password>" -c "getdompwinfo;quit"
```

## rpcclient - netshareenum  (password policy)
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <ip> -U "<user>%<password>" -c "netshareenum;quit"
```

## Trying all username as password from list of users
#plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY  
```
for u in `cat <file>`; do echo -n "user: $u " && rpcclient -U "$u%$u" -c "getusername;quit" <ip>; done
```
