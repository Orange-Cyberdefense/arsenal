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

## rpcclient - get user sid
```
rpcclient <ip> -c "lookupnales <name>; wmic useraccount get name,sid; quit"
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

## rpcclient - enum (Enum commands list)
```
rpcclient <ip> -U "<user>%<pass>" -c "enum;quit"
```

## rpcclient - enumdomains (Current domain)
```
rpcclient <ip> -U "<user>%<pass>" -c "enumdomains;quit"
```

## rpcclient - enumdomgroups (Enum Domain groups)
```
rpcclient <ip> -U "<user>%<pass>" -c "enumdomgroups;quit"
```

## rpcclient - querygroup (Enum Group Information)
```
rpcclient <ip> -U "<user>%<pass>" -c "querygroup <RID>;quit"
```

## rpcclient - querygroupmem (Enum Group Membership)
```
rpcclient <ip> -U "<user>%<pass>" -c "querygroupmem <RID>;quit"
```

## rpcclient - queryuser (Enumerate specific User/ computer information by RID)
```
rpcclient <ip> -U "<user>%<pass>" -c "queryuser <RID>;quit"
```

## rpcclient - getusrdompwinfo (User password policies)
```
rpcclient <ip> -U "<user>%<pass>" -c "getusrdompwinfo <RID>;quit"
```

## rpcclient - lsaenumsid (Local Users LSA Enum SID)
```
rpcclient <ip> -U "<user>%<pass>" -c "lsaenumsid;quit"
```

## rpcclient - lookupsid (Local Users Lookup SID)
```
rpcclient <ip> -U "<user>%<pass>" -c "lookupsid <SID>;quit"
```

## rpcclient - setuserinfo2 (Reset AD user password)
```
rpcclient <ip> -U "<user>%<pass>" -c "setuserinfo2 <LOGIN> 23 '<NEWPASSWORD>';quit"
```

