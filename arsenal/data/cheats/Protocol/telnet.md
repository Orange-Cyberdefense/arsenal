# telnet 

% telnet, 23
#plateform/linux  #target/remote  #protocol/telnet #port/23

## nmap - telnet
#cat/RECON 
```
nmap -n -sV -Pn --script "*telnet* and safe" -p 23 <ip>
```