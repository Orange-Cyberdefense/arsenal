# nodejs

% whitebox, nodejs

#platform/linux #target/local  #cat/CODE/WHITEBOX 

## command execution
```
grep -rn --include "*.js" -e "^\(.*\s\|.*child_process.*|\)\(exec\|spawn\|eval\|execSync\|spawnSync\|execFileSync\)(" --color
```

## require
```
grep -rn --include "*.js" -e "^\(.*\s\|\)\(require\)(" --color
```

## file
```
grep -rn --include "*.js" -e "^\(.*\s\|\)\(appendFile\|open\|readFile\|WriteFile\\|unlink\|rename\|formidable)(" --color
```

## unserialize
```
grep -rn --include "*.js" -e "unserialize(" --color
