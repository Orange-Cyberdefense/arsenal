# gobuster

% fuzzer, fuzz, gobuster

#plateform/linux #target/remote #cat/ATTACK/FUZZ
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
#plateform/linux #target/remote #cat/ATTACK/FUZZ
## wfuzz with number on url ( url : http://site/ )
```
wfuzz -z range,1-1000 -u <url>FUZZ
```

## wfuzz with wordlist on url ( url : http://site/ )
```
wfuzz -z file,<file> -u <url>FUZZ
```

## wfuzz on post parameter
```
wfuzz -z file,<file> -X post -u <url> -d 'FUZZ=1'
```

# Dirb

% fuzzer, fuzz, dirb
#plateform/linux #target/remote #cat/ATTACK/FUZZ
## dirb commons
```
dirb <url> -w /usr/share/wordlists/dirb/common.txt
```

# ffuf

% fuzzer, fuzz, ffuf
#plateform/linux #target/remote #cat/ATTACK/FUZZ
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
#plateform/linux #target/remote #cat/ATTACK/FUZZ
## nikto - first vuln scan
```
nikto -C all -h <url>
```

# feroxbuster

% fuzzer, fuzz, ffuf, dirsearch, gobuster, dirb
#plateform/linux #target/remote #cat/ATTACK/FUZZ

## default scan
```
feroxbuster --url <URL>
```

## default scan with wordlist
```
feroxbuster --url <URL> -w <wordlist>
```

## Multiple headers:
```
./feroxbuster -u http://127.1 -H Accept:application/json "Authorization: Bearer {token}"
```

## IPv6, non-recursive scan with INFO-level logging enabled:
```
./feroxbuster -u http://[::1] --no-recursion -vv
```

## Read urls from STDIN; pipe only resulting urls out to another tool
```
cat targets | ./feroxbuster --stdin --silent -s 200 301 302 --redirects -x js | fff -s 200 -o js-files
```

## Proxy traffic through Burp
```
./feroxbuster -u http://127.1 --burp
```

## Proxy traffic through a SOCKS proxy
```
./feroxbuster -u http://127.1 --proxy socks5://127.0.0.1:9050
```

## Pass auth token via query parameter
```
./feroxbuster -u http://127.1 --query token=0123456789ABCDEF
```

## Ludicrous speed... go!
```
./feroxbuster -u http://127.1 --threads 200
```
        
## Limit to a total of 60 active requests at any given time (threads * scan limit)
```
./feroxbuster -u http://127.1 --threads 30 --scan-limit 2
```
    
## Send all 200/302 responses to a proxy (only proxy requests/responses you care about)
```
./feroxbuster -u http://127.1 --replay-proxy http://localhost:8080 --replay-codes 200 302 --insecure
```
        
## Abort or reduce scan speed to individual directory scans when too many errors have occurred
```
./feroxbuster -u http://127.1 --auto-bail
```

= wordlist: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
