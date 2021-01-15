# snmap

% snmp, 161

## nmap, snmp scan
```
nmap -sU --open -p 161 -sC -sV <ip>
```

## nmap, snmp brute
```
nmap -sU --open -p 161 --script=snmp-brute <ip> --script-args snmp-brute.communitiesdb=<snmp_community_strings_file>
```

## onesixtyone
```
echo public > community; echo private >> community; echo manager >> community; onesixtyone -c community -i ips; rm community
```

## snmpwalk entire tree
```
snmpwalk -c public -v1 <ip>
```

