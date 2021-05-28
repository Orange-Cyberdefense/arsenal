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

% bof, mona

## mona show modules info
```
!mona modules
```

## mona - find JMP ESP
```
!mona find -s "\xff\xe4" -m <dll_file>
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