# SMTP

% smtp, 25
#platform/linux  #target/remote  #protocol/smtp #port/25

## smtp nmap enumeration
#cat/RECON 
```
nmap -p25 --script smtp-commands <ip>
```

## smtp nmap ntlm information disclosure
#cat/RECON 
```
nmap -p25 --script smtp-ntlm-info <ip>
```

## nmap - smtp user enum
#cat/ATTACK/BRUTEFORCE-SPRAY  
```
nmap –script smtp-enum-users.nse <ip>
```

## smtp user enum
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
smtp-user-enum -M VRFY -U <userlist> -t <ip>
```

## msf - smtp user enum
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x "use auxiliary/scanner/smtp/smtp_enum; set RHOSTS <ip>; exploit"
```
