# php grep 

% php, whitebox

#platform/linux #target/local  #cat/CODE/WHITEBOX 

## php grep include
```
grep -rn --include "*.php" -e "^\(.*\s\|\)\(include\|require\|virtual\|require_once\|include_once\)\(\s\|(\).*\\$" --color
```

## php grep path traversal
```
grep -rn --include "*.php" -e "^\(.*\s\|\)\(readfile\|file_get_contents\|stream_get_contents\|show_source\|fopen\|file\|fpassthru\|gzopen\|gzfile\|gzpassthru\|readgzfile\)\(\s\|(\).*\\$" --color
```

## php grep exec
```
grep -rn --include "*.php" -e "^\(.*\s\|\)\(eval\|popen\|pcntl_exec\|assert\|proc_open\|create_function\|call_user_func\|call_user_func_array\|exec\|shell_exec\|system\|passthru\|virtual\)([^)]*\\$" --color
```

## php grep replace
```
grep -rn --include "*.php" -e "^\(.*\s\|\)\(preg_replace\|ereg_replace\|eregi_replace\|mb_ereg_replace\|mb_eregi_replace\)(.*\\$" --color
```

## php grep unserialize
```
grep -rn --include "*.php" -e "^\(.*\s\|\)unserialize(.*\\$" --color
```

## php grep ldap
```
grep -rn --include "*.php" -e "^\(.*\s\|\)ldap_search(.*\\$" --color
```

## php grep xpath
```
grep -rn --include "*.php" -e "^\(.*\s\|\)xpath.*\\$" --color
```

## php grep mail
```
grep -rn --include "*.php" -e "^\(.*\s\|\)mail(.*\\$" --color
```

## php grep echo
```
grep -rn --include "*.php" -e "^\(.*\s\|\)\(echo\|printf\|print\)\(\s\|(\).*\\$" --color
```

## php grep weak comparison
```
grep -rn --include "*.php" -e "\(\\\$[^=]\|0\)\s*==\s*\(0\|\\\$[^=]\\)" --color
```

## php grep entry points
```
grep -rn --include "*.php" -e "\(\$_GET\|\$_POST\|\$_FILES\|\$REQUEST\|\$_COOKIES\|\$_SESSION\|\$_SERVER\|\$_GLOBALS\)" --color
```

## php grep callbacks
```
grep -rn --include "*.php" -e "^\(.*\s\|\)\(ob_start\|array_diff_uassoc\|array_diff_ukey\|array_filter\|array_intersect_uassoc\|array_intersect_ukey\|array_map\|array_reduce\|array_udiff_assoc\|array_udiff_uassoc\|array_udiff\|array_uintersect_assoc\|array_uintersect_uassoc\|array_uintersect\|array_walk_recursive\|array_walk\|assert_options\|uasort\|uksort\|usort\|preg_replace_callback\|spl_autoload_register\|iterator_apply\|register_shutdown_function\|register_tick_function\|set_error_handler\|set_exception_handler\|session_set_save_handler\|sqlite_create_aggregate\|sqlite_create_function\)(.*\\$"
```

## php grep curl
```
grep -rn --include "*.php" -e "curl_exec" --color
```

## php grep where or query
```
grep -rni --include "*.php" -e "\(where\|query\).*\\$"
```

## php grep file not contain an auth file include
```
for f in *.php; do grep "/include/auth.php" $f || echo $f; done |grep -v include | grep -v require
```

## php wrapper lfi
```
curl <url>?<param>=php://filter/read=convert.base64-encode/resource=<file>.php
```
