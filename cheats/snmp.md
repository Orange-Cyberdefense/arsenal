# snmap

% snmp, 161

## nmap, snmap scan
```
nmap -sU --open -p 161 <ip_raange> -oG <file.txt>
```

## onesixtyone
```
echo public > community; echo private >> community; echo manager >> community; onesixtyone -c community -i ips; rm community
```

## snmpwalk entire tree
```
snmpwalk -c public -v1 <ip>
```


