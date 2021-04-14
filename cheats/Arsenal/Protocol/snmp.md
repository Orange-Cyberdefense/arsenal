# snmp

% snmp, 161

#plateform/linux  #target/remote  #protocol/snmp #port/161

## nmap, snmp scan
#cat/RECON
```
nmap -sU --open -p 161 -sC -sV <ip>
```

## nmap, snmp brute
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
nmap -sU --open -p 161 --script=snmp-brute <ip> --script-args snmp-brute.communitiesdb=<snmp_community_strings_file>
```

## onesixtyone
#cat/RECON 
```
echo public > community; echo private >> community; echo manager >> community; onesixtyone -c community -i ips; rm community
```

## snmpwalk entire tree
#cat/RECON 
```
snmpwalk -c public -v1 <ip>
```

