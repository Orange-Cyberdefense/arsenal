# redis-cli

#plateform/multiple #target/local

# redis-cli connect to host
```
redis-cli -h <IP_ADDRESS>
```

# redis-cli append a value to a key
```
redis-cli APPEND <KEY> <VALUE>
```

# redis-cli set value in key
```
redis-cli SET <KEY> <VALUE>
```

# redis-cli set if not exist value in key
```
redis-cli SETNX <KEY> <VALUE>
```

# redis-cli overwrite part of a string at key starting at the specified offset
```
redis-cli SETRANGE <KEY> <OFFSET> <VALUE>
```

# redis-cli get the length of the value stored in a key
```
redis-cli STRLEN <KEY>
```

# redis-cli get value in key
```
redis-cli GET <KEY>
```

# redis-cli get a substring value of a key and return its old value
```
redis-cli GETRANGE <KEY> <VALUE>
```

# redis-cli increment value in key
```
redis-cli INCR <KEY>
```

# redis-cli increment the integer value of a key by the given amount
```
redis-cli INCRBY <KEY> <INCREMENT>
```

# redis-cli increment the float value of a key by the given amount
```
redis-cli INCRBYFLOAT  <KEY> <INCREMENT>
```

# redis-cli decrement the integer value of key by one
```
redis-cli DECR <KEY>
```

# redis-cli decrement the integer value of a key by the given number
```
redis-cli DECRBY <KEY> <INCREMENT>
```

# redis-cli delete a key
```
redis-cli DEL <KEY>
```

# redis-cli expire a key
```
redis-cli EXPIRE <KEY> <TIME>
```

# redis-cli returns the number of seconds until a key is expired
```
redis-cli TTL <KEY>
```

# redis-cli put the new value at the end of the list
```
redis-cli RPUSH <KEY> <VALUE>
```

# redis-cli append a value to a list, only if the exists
```
redis-cli RPUSHX <KEY> <VALUE>
```

# redis-cli  put the new value at the start of the list
```
redis-cli LPUSH  <KEY> <VALUE>
```

# redis-cli give a subset of the list
```
redis-cli LRANGE <KEY> <START> <STOP>
```

# redis-cli get an element from a list by its index
```
redis-cli LINDEX  <KEY> <INDEX>
```

# redis-cli  return the current length of the list
```
redis-cli LLEN <KEY>
```

# redis-cli remove the first element from the list and returns it
```
redis-cli LDOP <KEY>
```

# redis-cli set the value of an element in a list by its index
```
redis-cli LSET <KEY> <INDEX> <VALUE>
```

# redis-cli trim a list to the specified range
```
redis-cli <KEY> <START> <STOP>
```

# redis-cli remove the last element in a list, prepend it to another list and return it
```
redis-cli RPOPLPUSH  <SOURCE> <DESTINATION>
```

# redis-cli add the given value to the set
```
redis-cli SADD <KEY> <MEMBER>
```

# redis-cli  get the number of members in a set
```
redis-cli SCARD <KEY>
```

# redis-cli  remove the given value from the set
```
redis-cli SREM <KEY> <MEMBER>
```

# redis-cli  test if the given value is in the set.
```
redis-cli SISMEMBER <MYSET> <VALUE>
```

# redis-cli  move a member from one set to another
```
redis-cli <SOURCE> <DESTINATION> <MEMBER>
```

# redis-cli  remove and return one  random members from a set
```
redis-cli SPOP <KEY>
```

# redis-cli  remove and return multiple  random members from a set
```
redis-cli SPOP <KEY> <COUNT>
```

# redis-cli  get the number of members in a sorted set
```
redis-cli ZCARD <KEY>
```

# redis-cli count the members in a sorted set with scores within the given values
```
redis-cli ZCOUNT <KEY> <MIN> <MAX>
```

# redis-cli increment the score of a member in a sorted set
```
redis-cli ZINCRBY  <KEY> <INCREMENT> <MEMBER>
```

# redis-cli returns a subset of the sorted set
```
redis-cli ZRANGE <KEY> <START> <STOP>
```

# redis-cli returns a subset of the sorted set with scores
```
redis-cli ZRANGE <KEY> <START> <STOP> <WITHSCORES>
```

# redis-cli determine the index of a member in a sorted set
```
redis-cli ZRANK <KEY> <MEMBER>
```

# redis-cli remove all members in a sorted set within the given indexes
```
redis-cli ZREMRANGEBYRANK <KEY> <START> <STOP>
```

# redis-cli remove all members in a sorted set, by index, with scores ordered from high to low
```
redis-cli ZREMRANGEBYSCORE <KEY> <MIN> <MAX>
```

# redis-cli get the score associated with the given mmeber in a sorted set
```
redis-cli ZSCORE <KEY> <MEMBER>
```

# redis-cli return a range of members in a sorted set
```
redis-cli ZRANGEBYSCORE <KEY> <MIN> <MAX>
```

# redis-cli return a range of members in a sorted set with scores
```
redis-cli ZRANGEBYSCORE <KEY> <MIN> <MAX> <WITHSCORES>
```

# redis-cli  get the value of a hash field
```
redis-cli HGET <KEY> <FIELD>
```

# redis-cli  get all the fields and values in a hash
```
redis-cli HGETALL <KEY>
```

# redis-cli set the string value of a hash field
```
redis-cli HSET <KEY> <FIELD> <VALUE>
```

# redis-cli set the string value of a hash field, only if the field does not exists
```
redis-cli HSETNX <KEY> <FIELD> <VALUE>
```

# redis-cli increment value in hash by X
```
redis-cli HINCRBY <KEY> <FIELD> <INCREMENT>
```

# redis-cli delete one hash field
```
redis-cli HDEL <KEY> <FIELD>
```

# redis-cli determine if a hash field exists
```
redis-cli HEXISTS <KEY> <FIELD>
```

# redis-cli get all the fields in a hash
```
redis-cli HKEYS <KEY>
```

# redis-cli Returns the number of fields contained in the hash stored
``` 
redis-cli HLEN <KEY>
```

# redis-cli get the length of the value of a hash field
```
redis-cli HSTRLEN <KEY> <FIELD>
```

# redis-cli  get all the values in a hash
```
redis-cli HVALS <KEY>
```

