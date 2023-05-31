# john the ripper

% password recovery, password cracking

#platform/linux  #target/local  #cat/CRACKING/PASSWORD 

## john LM
```
john --wordlist=<wordlist> --format=lm hash.txt
```

## john NTLM
```
john --wordlist=<wordlist> --format=nt hash.txt
```

## john NTLMv1
```
john --wordlist=<wordlist> --format=netntlm hash.txt
```

## john NTLMv2
```
john --wordlist=<wordlist> --format=netntlmv2 hash.txt
```

## john ssh convert key 
```
python /usr/share/john/ssh2john.py <ssh_key> > <ssh_hash|sshkey.hash>
```

## john ssh
```
john --wordlist=<wordlist> <ssh_hash|sshkey.hash>
```

= wordlist: /usr/share/wordlist/rockyou.lst
