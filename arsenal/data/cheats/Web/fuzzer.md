# gobuster

% fuzzer, fuzz, gobuster

#platform/linux #target/remote #cat/ATTACK/FUZZ
## gobuster scan classic
```
gobuster dir -u <url> -w <wordlist>
```

## gobuster scan pentest classic fuzz
```
gobuster dir -u <url> -w <wordlist> -x json,html,php,txt,xml,md
```

## gobuster scan high rate
```
gobuster dir -u <url> -w <wordlist> -t 30
```

## gobuster scan with adding extension
```
gobuster dir -u <url> -w <wordlist> -x json,html,php,txt
```

# wfuzz

% fuzzer, fuzz, wfuzz
#platform/linux #target/remote #cat/ATTACK/FUZZ 
## wfuzz - show payload types
```
wfuzz -z help
```

## wfuzz - number after url ( url : http://site/ )
```
wfuzz -z range,1-1000 -u <url>FUZZ
```

## wfuzz - directory brute-force ( url : http://site/ )
```
wfuzz -z file,<file> -u <url>FUZZ
```

## wfuzz - post parameter only showing HTTP 200 OK
```
wfuzz -z file,<file> -X post -u <url> -d 'FUZZ=1&redirect=True' --sc 200
```

## wfuzz - get parameter, to output file
```
wfuzz -z file,<file> -f <out_file|out.txt> http://10.10.10.37/?s=FUZZ
```

# Dirb

% fuzzer, fuzz, dirb
#platform/linux #target/remote #cat/ATTACK/FUZZ
## dirb commons
```
dirb <url> -w /usr/share/wordlists/dirb/common.txt
```

# ffuf

% fuzzer, fuzz, ffuf
#platform/linux #target/remote #cat/ATTACK/FUZZ
## ffuf fuzz keyword in url
```
ffuf -w <wordlist> -u <url>/FUZZ
```

## ffuf fuzz Host filter response size
```
ffuf -w <wordlist> -u <url> -H "Host: FUZZ" -fs <response_size>
```

## ffuf GET parameter fuzzing
```
ffuf -w <wordlist> -u <url>?<param>=FUZZ -fs <response_size>
```

## ffuf POST parameter fuzzing and filter response code 401
```
ffuf -w <wordlist> -u <url> -X POST -d "username=admin\&password=FUZZ" -fc 401
```

# nikto

% fuzzer, fuzz, nikto
#platform/linux #target/remote #cat/ATTACK/FUZZ
## nikto - first vuln scan
```
nikto -C all -h <url>
```

= wordlist: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt