# Crack files

% bruteforce, crack, files

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

## ZIP - fcrackzip
```
fcrackzip -u -D -p <wordlist> <file>.zip
```

## ZIP - john
```
zip2john <file>.zip > zip.john;
john zip.john
```

## 7z - 7za
```
cat <wordlist> | 7za t <file>.7z
```

## 7z - john
```
./7z2john.pl <file>.7z > 7zhash.john;
john 7zhash.john
```

## PDF - pdfcrack
```
pdfcrack <file>.pdf -w <wordlist>
```

## PDF decrypt - qpdf
```
qpdf --password=<PASSWORD> --decrypt <encrypted_pdf>.pdf <plaintext_pdf>.pdf
```

= wordlist: /usr/share/wordlists/rockyou.txt
