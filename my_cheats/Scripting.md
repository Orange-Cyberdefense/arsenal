# Scripting
% OWN

## nmap - extract open ports from namp scan and print comma seperated list
```
grep "open" <file_name> | awk '{print $1}' | cut -d '/' -f 1 | paste -sd "," | tee >(xclip)
```