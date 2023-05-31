# Arsenal

% arsenal, internal

#platform/linux #target/local #cat/INTERNAL 

## List global variable
```
>show
```

## Clear all global variable
```
>clear
```

## Set commons global variable
```
>set LHOST=<LHOST> LPORT=<LPORT> RHOST=<RHOST> RPORT=<RPORT>
```

## Set user and password
```
>set user=<user> password=<password>
```

## Set ip global variable
```
>set ip=<ip>
```

## Set wordlist
wordlists (nbline): 
- password
/usr/share/seclists/Passwords/darkweb2017-top1000.txt (999)
/usr/share/wordlists/rockyou.txt (14M)

- Web
/usr/share/seclists/Discovery/Web-Content/common-and-french.txt (4906)
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt (220K)

```
>set wordlist=<wordlist>
```
## Set custom global variable
```
>set <GLOBALVAR>=<value>
```

## Exit
```
>exit
```

