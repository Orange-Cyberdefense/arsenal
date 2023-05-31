# chisel

% chisel

## chisel server (server on local machine)
#platform/linux  #target/remote  #cat/PIVOT 
All commands on arsenal are done with server on kali machine and client on the target.
Client or Server can also be launch on windows with chisel.exe
```
./chisel server -v -p <server_port|8000> --reverse
```

## chisel reverse port forwarding (client on remote machine) - forward client port on server
#platform/linux  #target/remote  #cat/PIVOT 

This forward {clientside-host}:{clientside-port} to server {local-port}
To get the port of the client machine locally on serverside.
ex: R:2222:localhost:22 to get the client 22 (ssh) on the port 2222 of the server
| server | - 2222 <-----  |client|-127.0.0.1:22
on server : ssh -p 2222 127.0.0.1

```
./chisel client -v <server_ip>:<server_port|8000> R:<serverside-port>:<clientside-host|localhost>:<clientside-port>
```

## chisel remote port forwarding (client on remote machine) - forward server port on client
#platform/linux  #target/remote  #cat/PIVOT 

To expose server port remotely (useful to expose your listener)
This forward {serverside-host}:{serverside-port} from the server to {clientside-host}:{clientside-port}
ex : 0.0.0.0:4445:127.0.0.1:4444 expose the server 4444 listener to client 4445
| server | - 4444 ------->  |client|-4445 : *   <-

```
./chisel client -v <server_ip>:<server_port|8000> <clientside-host|0.0.0.0>:<clientside-port>:<serverside-host|127.0.0.1>:<serverside-port>
```
	
## chisel socks proxy (client on remote machine)
#platform/windows  #target/remote  #cat/PIVOT 

If the server is launch with --reverse you can specify R: socks to get a proxy socks on server machine (port 1080)
On server with proxychains set on port 1080 you can proxy socks request on the client.

```
./chisel client <server_ip>:<server_port> R:socks
```



