
# crunch

% wordlist, bruteforce, dict

## crunch - generate wordlist hex
#plateform/linux #target/local #cat/UTILS  
```bash
crunch <min|2> <max|8> 0123456789ABCDEF -o <output.txt>
```

## crunch - generate wordlist charset
#plateform/linux #target/local #cat/UTILS 
```bash
crunch <min> <max> -f /usr/share/crunch/charset.lst <charset|mixalpha-numeric> -o <output.txt>
```

## crunch - generate wordlist Upper(,) lower(@)x3 numeric(%)x3 special(^)x1
#plateform/linux #target/local #cat/UTILS 
- @ will insert lower case characters
- , will insert upper case characters
- % will insert numbers
- ^ will insert symbols
	 
```bash
crunch 8 8 -t <pattern|,@@@%%%^> -o <output.txt>
```

## crunch - generate wordlist contain "password", 2 numbers and 1 special char
#plateform/linux #target/local #cat/UTILS 
```bash
crunch 8 8 -t password%%^ -o <output.txt>
```
