# cewl

% passwords, brute force, wordlist, cewl

## cewl - wordlist creation
```
cewl -w <file> -d <deep> -m <min_word_size> <url>
```

## cewl - wordlist creation (default values)
```
cewl -w pass.txt -d 10 -m 5 <url>
```

# crunch

% passwords, brute force, crunch, generate

## crunch - generate wordlist hex
```
crunch <min> <max> 0123456789ABCDEF -o <output.txt>
```

## crunch - generate wordlist charset
```
crunch <min> <max> -f /usr/share/crunch/charset.lst -o <output.txt>
```

## crunch - generate wordlist Upper(,) lower(@)x3 numeric(%)x3 special(^)x1
```
crunch 8 8 -t ,@@@%%%^ -o <output.txt>
```

# jhon the ripper

% passwords, brute force, jhon

## john ntlmv2
```
john --format=netntlmv2 hash.txt
```

# hashcat

% passwords, brute force, hashcat

## hashcat - basic md5 (joomla/wordpress) - wordlist
```
hashcat -a 0 -m 400 hashes <wordlist>
```

## hashcat - basic md5 (joomla/wordpress) - wordlist with rules
```
hashcat -a 0 -m 400 hashes <wordlist> -r /usr/share/doc/hashcat/rules/best64.rule 
```

## hashcat - kerberos ticket
```
hashcat -m 18200 --force -a 0 hashes <wordlist> 
```

## hashcat - LM
```
hashcat -m 3000 -a 0 hashes <wordlist> 
```

## hashcat - NTLM
```
hashcat -m 1000 -a 0 hashes <wordlist> 
```

## hashcat - NTLMv1
```
hashcat -m 5500 -a 0 hashes <wordlist> 
```

## hashcat - NTLMv2
```
hashcat -m 5600 -a 0 hashes <wordlist> 
```

= wordlist: /usr/share/wordlist/rockyou.lst
