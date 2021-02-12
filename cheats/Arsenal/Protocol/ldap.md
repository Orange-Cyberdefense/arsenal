# ldap

#plateform/linux  #target/remote  #protocol/ldap  #port/639 #port/389

## ldap nmap
#cat/RECON 
```
nmap -n -sV --script "ldap* and not brute" -p 389 <ip>
```

## ldapsearch base
#cat/ATTACK/CONNECT 
```
ldapsearch -x -h <ip> -s base
```

## ldapsearch with base dn
#cat/ATTACK/CONNECT 
```
ldapsearch -x -h <ip> -b <basedn>
```

## ldapsearch base with authentication
#cat/ATTACK/CONNECT 
```
ldapsearch -x -h <ip> -D <domain>\\<username> -w <password> -b 'DC=<domain>,DC=<path>'
```

## ldapdomaindump
#cat/ATTACK/CONNECT 
```
ldapdomaindump --no-json --no-grep --authtype SIMPLE -o ldap_dump -r <ip> -u <domain>\\<username> -p <password>
```