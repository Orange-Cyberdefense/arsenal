# All those misfits

## proxychains - speed up SOCKS proxy scanning with nmap
https://www.hackwhackandsmack.com/?p=1021
```
seq 1 1000 | xargs -P 50 -I{} proxychains nmap -p {} -sT -Pn --open -n -T4 --min-parallelism 100 --min-rate 1 <target_ip> > <outfile|proxychains_nmap.txt>
```

## mount - share with kerberos ticket (should be in /tmp/krb5cc_0)
```
sudo mount -t cifs -o sec=krb5,vers=3.0 '//SERVER.DOMAIN.LOCAL/SHARE' /mnt/share
```
## autorecon - scan single target
```
autorecon --single-target -o <output_folder> <target_ip>
```
