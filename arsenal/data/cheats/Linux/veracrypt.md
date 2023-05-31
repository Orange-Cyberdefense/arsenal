# veracrypt

% veracrypt

#platform/linux

## Create veracrypt volume for Linux
```
veracrypt -t --create <file> --hash sha512 --encryption AES --filesystem ext4 --volume-type normal -k "" --pim 0 --size <size>
```

## Open veracrypt volume
```
veracrypt <file> <mount>
```

## Lock veracrypt volume
```
veracrypt -d <file>
```


## Lock all veracrypt volume
```
veracrypt -d
```
