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

# hashcat

% passwords, brute force, cewl

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

= wordlist: /usr/share/wordlist/rockyou.lst
