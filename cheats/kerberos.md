# kerberos

% kerberos

## Kerbrute usersenum
```
./kerbrute_linux_amd64 userenum -d <domain> --dc <ip> <users_file>
```

## kerberos enum users
```
nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='<domain>'" <ip>
```

## kerberos enum users (with user list)
```
nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='<domain>',userdb=<users_list_file>" <ip>
```


