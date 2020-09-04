# FTP

% ftp

## ftp - download all 
```
wget -m ftp://anonymous:anonymous@<ip>
```

## ftp download all (2)
```
wget -m --no-passive ftp://anonymous:anonymous@<ip>
```

## ftp - connect
```
ftp <ip>
```

## ftp - connect port
```
ftp <ip> <port>
```

## ftp - enum anonym
```
nmap -v -p 21 --script=ftp-anon.nse <ip>
```

## ftp - msf bruteforce login
```
msfconsole -x "use auxiliary/scanner/ftp/ftp_login; set RHOSTS <ip>; set USER_FILE <user_file>; set PASS_FILE <password_file>; exploit"
```

