# ssh

% ssh, 22
#plateform/linux  #target/remote  #protocol/ssh #port/22

## Start ssh agent
#target/local #cat/UTILS 
```
eval "$(ssh-agent -s)"; ssh-add
```

## SSH local port forwarding (get remote_port on local)
#cat/PIVOT/TUNNEL-PORTFW 
```
ssh -L <local_port>:<remote_host>:<remote_port> <user>@<ip>
```

## SSH dynamic port forwarding
Connect to remote and create a **D**ynamic port forwarding rule
```
ssh -Nf -D <local_ip|0.0.0.0>:<local_port|9999> <user>@<remote_ip>
```

## SSH REMOTE port forwarding (send local port to remote) (need GatewayPorts yes)
#cat/PIVOT/TUNNEL-PORTFW 
```
ssh -R <remote_binding>:<remote_port>:<local_host>:<local_port> <user>@<ip>
```

## SSH REMOTE dynamic port forwarding
```
ssh -Nf -R <kali_port|9998> kali@<ip>
```


## SSH proxysocks
#cat/PIVOT/TUNNEL-PORTFW 
```
ssh -D <socks_port> <user>@<ip>
```

## get public ssh key of server
#cat/UTILS 
```
ssh-keyscan -t rsa <IP> -p <PORT>
```

## msf - bruteforce username
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x "use scanner/ssh/ssh_enumusers; set RHOSTS <ip>; set USER_FILE <user_file>; set CHECK_FALSE true; exploit"
```

## SSH - old algorithm
#cat/UTILS 
```
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 <user>@<ip>
```

## SSH - connect to domain joined Linux machine with kerberos ticket
```
ssh -o GSSAPIAuthentication=yes user@domain.local
```