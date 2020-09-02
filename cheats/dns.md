# DNS

% dns, host, 53

## host find name server
```
host -t ns <domain>
```

## host find mail server
```
host -t mx <domain>
```

% dns, dig, 53

## dig dns lookup
```
dig <domain_name> @1.1.1.1
```

## dig any information
```
dig ANY <domain_name> @<dns_ip>
```

## dig reverse lookup
```
dig -x <ip> @<dns_ip>
```

## dig zone transfert
```
dig axfr <domain_name> @<name_server>
```

## dig, find external, public IP address
```
dig +short <domain_name> @resolver1.opendns.com
```

% dns, dnsrecon, 53

## dnsrecon standard enum on domain
```
dnsrecon -d <domain>
```

## dnsrecon zone transfert
```
dnsrecon -d <domain> -t axfr
```

## dnsrecon reverse lookup start/end ip
```
dnsrecon -r <startip>-<endip> -n <domain_name_server>
```

## dnsrecon reverse lookup network range ip
```
dnsrecon -r <ip_with_network_mask> -n <domain_name_server>
```

## dnsrecon domain bruteforce
```
dnsrecon -d <domain> -D <wordlist> -t brt
```

% dns, dnsenum, 53
```
dnsenum <domain>
```

% dns, nmap, 53

## nmap grab banner
```
nmap -sV -p 53 --script dns-nsid <ip>
```

## nmap dns tcp
```
nmap -n -sV --script "(*dns* and (default or (discovery and safe))) or dns-random-txid or dns-random-srcport" -p 53 <ip>
``` 

## nmap dns udp
```
nmap -n -sV -sU --script ""(*dns* and (default or (discovery and safe))) or dns-random-txid or dns-random-srcport" -p 53 <ip>
``` 

## nmap activedirectory enum
```
nmap --script dns-srv-enum --script-args "dns-srv-enum.domain='<domain>'"
```

## nmap dnssec 
```
nmap -sSU -p53 --script dns-nsec-enum --script-args dns-nsec-enum.domains=<domain> <ip>
```

% dns, msf, 53

## dns metasploit enumeration
```
msfconsole -x "use auxiliary/gather/enum_dns; set domain <domain>; set ns <dns_server>; exploit"
```
