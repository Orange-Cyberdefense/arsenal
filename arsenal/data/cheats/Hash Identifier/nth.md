# Name-That-Hash

% Hashes, hash identification, hash function analysis

#plateform/linux  #target/local #cat/HASHES/HASH_TYPE_IDENTIFIER

https://github.com/HashPals/Name-That-Hash

## Standard Input Hash
```
nth --text '<hash-value>'
```

## Hash in a file
```
nth --file hash.txt
```

## Print hash in json format
```
nth --text '<hash-value>' --greppable
```

## Decode hashes in base64
```
nth --text '<base6d_encoded_hash>' -b64
```

## Print little information about hash
```
nth --text '<hash-value>' -a
```

## Enable verbosity/debug logs
```
nth --text '<hash-value>' -v
```