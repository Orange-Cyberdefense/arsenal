# DNS

% dns, host, 53

## host find name server
#platform/linux  #target/remote  #cat/RECON  
```
host -t ns <domain>
```

## host find mail server
#platform/linux  #target/remote  #cat/RECON
```
host -t mx <domain>
```

% dns, dig, 53

## dig dns lookup
#platform/linux  #target/remote  #cat/RECON
```
dig <domain_name> @1.1.1.1
```

## dig any information
#platform/linux  #target/remote  #cat/RECON
```
dig ANY <domain_name> @<dns_ip>
```

## dig reverse lookup
#platform/linux  #target/remote  #cat/RECON
```
dig -x <ip> @<dns_ip>
```

## dig zone transfer
#platform/linux  #target/remote  #cat/RECON
```
dig axfr <domain_name> @<name_server>
```

## dig, find external, public IP address
#platform/linux  #target/remote  #cat/RECON
```
dig +short <domain_name> @resolver1.opendns.com
```

## dig, find domains file ip address value
#platform/linux  #target/remote  #cat/RECON
```
dig -f <domains.txt> +noall +answer
```

## dig, find domains file MX ip record
#platform/linux  #target/remote  #cat/RECON
```
dig -f <domains.txt> MX +noall +answer
```

% dns, dnsrecon, 53

## dnsrecon standard enum on domain
#platform/linux  #target/remote  #cat/RECON
```
dnsrecon -d <domain>
```

## dnsrecon zone transfer
#platform/linux  #target/remote  #cat/RECON
```
dnsrecon -d <domain> -t axfr
```

## dnsrecon reverse lookup start/end ip
#platform/linux  #target/remote  #cat/RECON
```
dnsrecon -r <startip>-<endip> -n <domain_name_server>
```

## dnsrecon reverse lookup network range ip
#platform/linux  #target/remote  #cat/RECON
```
dnsrecon -r <ip_with_network_mask> -n <domain_name_server>
```

## dnsrecon domain bruteforce
#platform/linux  #target/remote  #cat/RECON
```
dnsrecon -d <domain> -D <wordlist> -t brt
```

% dns, dnsenum, 53
#platform/linux  #target/remote  #cat/RECON
```
dnsenum <domain>
```

% dns, nmap, 53

## nmap grab banner
#platform/linux  #target/remote  #cat/RECON
```
nmap -sV -p 53 --script dns-nsid <ip>
```

## nmap dns tcp
#platform/linux  #target/remote  #cat/RECON
```
nmap -n -sV --script "(*dns* and (default or (discovery and safe))) or dns-random-txid or dns-random-srcport" -p 53 <ip>
``` 

## nmap dns udp
#platform/linux  #target/remote  #cat/RECON
```
nmap -n -sV -sU --script ""(*dns* and (default or (discovery and safe))) or dns-random-txid or dns-random-srcport" -p 53 <ip>
``` 

## nmap activedirectory enum
#platform/linux  #target/remote  #cat/RECON
```
nmap --script dns-srv-enum --script-args "dns-srv-enum.domain='<domain>'"
```

## nmap dnssec 
#platform/linux  #target/remote  #cat/RECON
```
nmap -sSU -p53 --script dns-nsec-enum --script-args dns-nsec-enum.domains=<domain> <ip>
```

% dns, msf, 53

## dns metasploit enumeration
#platform/linux  #target/remote  #cat/RECON
```
msfconsole -x "use auxiliary/gather/enum_dns; set domain <domain>; set ns <dns_server>; exploit"
```

% dns, sublist3r , 53

## dns sublist3r - subdomain enumeration
#platform/linux  #target/remote  #cat/RECON
```
sublist3r -d <domain> -v
```

## dns sublist3r - subdomain enumeration with bruteforce module enabled
#platform/linux  #target/remote  #cat/RECON
```
sublist3r -b -d <domain>
```
