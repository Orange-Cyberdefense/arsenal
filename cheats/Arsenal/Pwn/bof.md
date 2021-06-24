# bof

% bof, buffer overflow
#plateform/linux #target/local #cat/PWN

## bof, pattern creation
```
msf-pattern_create -l <size>
```

## bof, pattern offset
```
msf-pattern_offset -l <size> -q <pattern>
```

## bof, nasm - show opcode from asm
```
msf-nasm_shell # nasm > jmp esp
```

% bof, ropgadget

## ropgadget - Specify a binary filename to analyze
```
ROPgadget --binary <binary>
```

## ropgagdet - Enable the ROP chain generation
```
ROPgadget --binary <binary> --ropchain
```

## ropgagdet - Search opcode in executable segment
```
ROPgadget --binary <binary> --opcode <opcode>
```

## ropgadget - Search string between two addresses (0x...-0x...)
```
ROPgadget --binary <binary> --string <string> --range <start_address>-<end_address>
```

## ropgadget - Only show specific instructions
```
ROPgadget --binary <binary> --only="<instructions>"
```

## ropgadget - Suppress specific mnemonics
```
ROPgadget --binary <binary> --filter="<instructions>"
```

% bof, mona

## mona - Show all loaded modules and their properties
```
!mona modules
```

## mona - Configure the log directory (no need to create it)
```
!mona config -set workingfolder <path|c:\logs\%p>
```

## mona - Verify the current the log directory
```
!mona config -get workingfolder
```

## mona - Create a cyclic pattern of a given size
```
!mona pc <pattern_size|400>
```

## mona - Find cyclic pattern in memory
```
!mona findmsp
```

## mona - Find location (offset) of 4 bytes in a cyclic pattern
```
!mona po <pattern_value|41346541>
```

## mona - Find bytes in memory (ex: eggs)
```
!mona find -s <pattern_value|"w00tw00t">
```

## mona - Find pointers that will allow you to jump to a register (without null bytes)
```
!mona jmp -r <reg_name|esp> -n
```

## mona - Find a function in IAT
```
!mona getiat -s <function_name|*strcpy*>
```

## mona - Show the current SEH chain
```
!mona sehchain
```

## mona - Set a breakpoint on all current SEH Handler function pointers
```
!mona bpseh
```

## mona - Find pointers to assist with SEH overwrite exploits (default: no aslr, no rebase, no safeseh)
```
!mona seh
```

## mona - Badchar hunting step 1 - Creates a byte array
```
!mona bytearray -cpb <excluded_bytes|'\x00\x0a\x0d'>
```

## mona - Badchar hunting step 2 - sync the exploit
```
bytearray = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f"
"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
binfile=open("C:\\BadChars\\bytearray.bin","wb")
binfile.write(bytearray)
binfile.close
```

## mona - Badchar hunting step 3 - compare until "!!! Hooray, normal shellcode unmodified !!!" message
```
!mona compare -f <input_file|C:\BadChars\bytearray.bin> -a <bytesarray_address|esp>
```

## mona - Finds gadgets that can be used in a ROP exploit and do ROP magic with them (Note : can take 20 minutes)
```
!mona rop -cm aslr=false,rebase=false
```

## mona - Finds stackpivots (move stackpointer to controlled area)
```
!mona stackpivot -cm os=true -distance <min,max|12,12>
```

## mona - Show pointers to pointers to the pattern (might take a while !)
```
!mona find -type file -s <input_file|C:\stackpivot.txt> -p2p
```
