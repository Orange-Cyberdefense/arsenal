# cheatsheet name

% tag1, tag2

#cat/INTERNAL

```
#platform/linux
#platform/windows
#platform/mac
#platform/multiple

#target/local 
#target/remote

#cat/UTILS
#cat/RECON
#cat/ATTACK
#cat/ATTACK/BRUTEFORCE-SPRAY
#cat/ATTACK/LISTEN-SERVE
#cat/ATTACK/FILE_TRANSFERT
#cat/ATTACK/CONNECT
#cat/ATTACK/EXPLOIT
#cat/ATTACK/MITM
#cat/ATTACK/REVERSE_SHELL
#cat/ATTACK/INJECTION
#cat/CODE
#cat/CODE/SAMPLE
#cat/CODE/WHITEBOX
#cat/CRACKING
#cat/CRACKING/PASSWORD
#cat/PIVOT
#cat/PIVOT/TUNNEL-PORTFW
#cat/PRIVESC
#cat/POSTEXPLOIT
#cat/POSTEXPLOIT/CREDS_RECOVER
#cat/PERSIST

#port/<portnum>
```

Tags are used to categorize the cheat sheet
Command tags start with a #tag the level1 tags are overridden by other tags commands tags are in the form : #key/value

## Command description
Lines beginning with `#` represents the command main description
The command need to written between ` ``` `
you could add additional description inside the paragraph

## Variables
<variable_name> represents variable in the command it will be fill by user

## Executable variable prefill
```
$ variable_name: ls /tmp
```
--> prefill the variable <variable_name> with '$(ls /tmp)'

## Constant variable prefill
```
= variable_name: /tmp/wordlist.txt
```
--> prefill the variable <variable_name> with '/tmp/wordlist.txt'

# cheat_sample

% cheat, sample

## cheat sample command
```
command <arg1> <arg2>
```

Additional description
