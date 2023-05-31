# JwtTool

% jwttool, token, jwt

## Jwt tool Mode all tests
#platform/linux #target/remote #cat/RECON
```
python3 jwt_tool.py -M at -t "<url>" -rh "Authorization: Bearer <JWT_Token>" -rh "<other_header>" -rc "<cookies>"
```

## Jwt tool reuse query id
#platform/linux #target/remote #cat/RECON
```
python3 jwt_tool.py -Q "<jwttool_id>"
```

## Jwt tool bruteforce key
#platform/linux #target/local #cat/RECON
```
python3 jwt_tool.py -d <wordlists.txt> <JWT_token>
```

