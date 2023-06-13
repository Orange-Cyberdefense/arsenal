
# [HTTP]

## feroxbuster - simple scan, WORDLIST:common.txt
```
feroxbuster -u http://<target_ip>:<port|80>/<path|/> -w /usr/share/seclists/Discovery/Web-Content/common.txt -r -k -n -o <out_file>
```

## feroxbuster - expanded scan, common extensions WORDLIST:common.txt
```
feroxbuster -u http://<target_ip>:<port|80>/<path|/> -x "txt,html,php,asp,aspx,jsp" -w /usr/share/seclists/Discovery/Web-Content/common.txt -r -k -n -o <out_file>
```

## feroxbuster - simple scan, WORDLIST:big.txt
```
feroxbuster -u http://<target_ip>:<port|80>/<path|/> -w /usr/share/seclists/Discovery/Web-Content/big.txt -r -k -n -o <out_file>
```

## feroxbuster - expanded scan, common extensions WORDLIST:big.txt
```
feroxbuster -u http://<target_ip>:<port|80>/<path|/> -x "txt,html,php,asp,aspx,jsp" -w /usr/share/seclists/Discovery/Web-Content/big.txt -r -k -n -o <out_file>
```

## feroxbuster - simple scan, WORDLIST:directory-list-2.3-big.txt
```
feroxbuster -u http://<target_ip>:<port>/<path> -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -r -k -n -o <out_file>
```

## gobuster - quick subdomain enumeration
```
gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --no-tls-validation --append-domain -u <domain_name>:<port>
```

## gobuster - thourough subdomain enumeration
```
gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --no-tls-validation --append-domain -u <domain_name>:<port>
```


; TODO - add wordlist generation with cewl

; TODO - add downloading all image files for investigation