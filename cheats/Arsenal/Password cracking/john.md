# john the ripper

% password recovery, password cracking

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

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


= wordlist: /usr/share/wordlist/rockyou.lst
