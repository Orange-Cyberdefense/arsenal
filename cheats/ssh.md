# ssh

% ssh, 22

## Start ssh agent
```
eval "$(ssh-agent -s)"; ssh-add
```

## SSH local port forwarding (get remote_port on local)
```
ssh -L <local_port>:<remote_host>:<remote_port> <user>@<ip>
```

## SSH remote port forwarding (send local port to remote) (need GatewayPorts yes)
```
ssh -R <remote_binding>:<remote_port>:<local_host>:<local_port> <user>@<ip>
```

## SSH proxysocks
```
ssh -D <socks_port> <user>@<ip>
```

## get public ssh key of server
```
ssh-keyscan -t rsa <IP> -p <PORT>
```

## msf - bruteforce username
```
msfconsole -x "use scanner/ssh/ssh_enumusers; set RHOSTS <ip>; set USER_FILE <user_file>; set CHECK_FALSE true; exploit"
```
