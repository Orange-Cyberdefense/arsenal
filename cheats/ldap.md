#ldap

% windows, ldap, ldapsearch, 389


## ldap nmap
```
nmap -n -sV --script "ldap* and not brute" -p 389 <ip>
```

## ldapsearch base
```
ldapsearch -x -h <ip> -s base
```

## ldapsearch with base dn
```
ldapsearch -x -h <ip> -b <basedn>
```

## ldapsearch base with authentication
```
ldapsearch -x -h <ip> -D <domain>\\<username> -w <password> -b 'DC=<domain>,DC=<path>'
```

## ldapdomaindump
```
ldapdomaindump --no-json --no-grep --authtype SIMPLE -o ldap_dump -r <ip> -u <domain>\\<username> -p <password>
```