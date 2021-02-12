# pop

% pop, pop3, 110, 995
#plateform/linux  #target/remote  #protocol/pop #port/110 #port/995

## nmap - pop3 infos
#cat/RECON 
```
nmap --script "pop3-capabilities or pop3-ntlm-info" -sV -port <port> <ip>
```
