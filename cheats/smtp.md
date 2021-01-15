# SMTP

% smtp, 25

## smtp nmap enumeration
```
nmap -p25 --script smtp-commands <ip>
```

## smtp nmap ntlm information disclosure
```
nmap -p25 --script smtp-ntlm-info <ip>
```

## nmap - smtp user enum
```
nmap –script smtp-enum-users.nse <ip>
```

## smtp user enum
```
smtp-user-enum -M VRFY -U <userlist> -t <ip>
```

## msf - smtp user enum
```
msfconsole -x "use auxiliary/scanner/smtp/smtp_enum; set RHOSTS <ip>; exploit"
```
