# grep

#platform/linux #target/local #cat/UTILS

## grep classic
```
grep <word> <file>
```

## grep without case
```
grep -i <word> <file>
```

## grep with file found
```
grep <word> <file> -H
```

## grep recursive on extension
```
grep -rn --include "*.<extension>" <word>
```

## grep word A or B
```
grep -e "\(<word_A>\|<word_B>\)" <file>
```

# grep hash

#platform/linux #target/local #cat/UTILS

## Extract md5 hashes ({32})
```
egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{32}([^a-fA-F0-9]|$)' *.txt | egrep -o '[a-fA-F0-9]{32}' > md5-hashes.txt
```

## Extract sha1 ({40})
```
egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{40}([^a-fA-F0-9]|$)' *.txt | egrep -o '[a-fA-F0-9]{40}' > sha1-hashes.txt
```

## Extract sha256({64})
```
egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{64}([^a-fA-F0-9]|$)' *.txt | egrep -o '[a-fA-F0-9]{64}' > sha256-hashes.txt
```

## Extract sha512({128})
```
egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{128}([^a-fA-F0-9]|$)' *.txt | egrep -o '[a-fA-F0-9]{128}' > sha512-hashes.txt
```

## Extract valid MySQL-Old hashes
```
grep -e "[0-7][0-9a-f]{7}[0-7][0-9a-f]{7}" *.txt > mysql-old-hashes.txt
```

## Extract blowfish hashes
```
grep -e "$2a\$\08\$(.){75}" *.txt > blowfish-hashes.txt
```

## Extract Joomla hashes
```
egrep -o "([0-9a-zA-Z]{32}):(w{16,32})" *.txt > joomla.txt
```

## Extract VBulletin hashes
```
egrep -o "([0-9a-zA-Z]{32}):(S{3,32})" *.txt > vbulletin.txt
```

## Extract phpBB3-MD5
```
egrep -o '$H$S{31}' *.txt > phpBB3-md5.txt
```

## Extract Wordpress-MD5
```
egrep -o '$P$S{31}' *.txt > wordpress-md5.txt
```

## Extract Drupal 7
```
egrep -o '$S$S{52}' *.txt > drupal-7.txt
```

## Extract old Unix-md5
```
egrep -o '$1$w{8}S{22}' *.txt > md5-unix-old.txt
```

## Extract md5-apr1
```
egrep -o '$apr1$w{8}S{22}' *.txt > md5-apr1.txt
```

## Extract sha512crypt, SHA512(Unix)
```
egrep -o '$6$w{8}S{86}' *.txt > sha512crypt.txt
```


# Others grep

#platform/linux #target/local #cat/UTILS

## Extract emails from file
```
grep -E -o "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b" <file>
```

## Extract valid IP addresses
```
grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" <file>
```

## Extract passwords
```
grep -i "pwd\|passw" <file>
```

## Extract users
```
grep -i "user\|invalid\|authentication\|login" <file>
```

## Extract HTTP URLS
```
grep -i http | grep -shoP 'http.*?[" >]' <file> > http-urls.txt
```

= file: file.txt
