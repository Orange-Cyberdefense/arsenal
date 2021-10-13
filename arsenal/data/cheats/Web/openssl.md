# openssl

% openssl, certificate, encryption

#plateform/linux #target/local #cat/UTILS 

## Create a new signing request and key
```
openssl req -new -newkey rsa:<RSA_LENGTH> -nodes -out <OUTPUT_CSR> -keyout <OUTPUT_KEY>
```

## Create a new self-signed certificate
```
openssl req -x509 -sha256 -nodes -days <VALIDITY> -newkey rsa:<RSA_LENGTH> -out <OUTPUT_CRT> -keyout <OUTPUT_KEY>
```

## Create a signing request from existing key
```
openssl req -out <OUTPUT_CSR> -key <INPUT_KEY> -new
```

## Create a signing request from existing certificate and key
```
openssl x509 -x509toreq -out <OUTPUT_CSR> -in <INPUT_CRT> -signkey <INPUT_KEY>
```

## Remove a passphrase from a private key
```
openssl rsa -in <INPUT_KEY> -out <OUTPUT_PLAINTEXT_KEY>
```

## Convert a DER encoded file to a PEM encoded file
```
openssl x509 -inform der -in <INPUT_CRT> -out <OUTPUT_PEM>
```

## Convert a PEM encoded file to a DER encoded file
```
openssl x509 -outform der -in <INPUT_PEM> -out <OUTPUT_CRT>
```

## Convert a PKCS12 encoded file containing a private key and certificates to PEM
```
openssl pkcs12 -in <INPUT_PKCS12> -out <OUTPUT_PEM> -nodes
```

## Extract the private key from a PKCS12 encoded file
```
openssl pkcs12 -in <INPUT_PKCS12> -out <OUTPUT_PEM> -nodes -nocerts
```

## Extract the certificate from a PKCS12 encoded file
```
openssl pkcs12 -in <INPUT_PKCS12> -out <OUTPUT_PEM> -nodes -nokeys
```

## Convert a PEM certificate file and a private key to PKCS12 encoded file
```
openssl pkcs12 -export -out <OUTPUT_PKCS12> -inkey <INPUT_KEY> -in <INPUT_CRT> -certfile <INPUT_CRT>
```

## Validate a certificate signing request
```
openssl req -text -noout -verify -in <OUTPUT_CSR>
```

## Validate a private key
```
openssl rsa -in <INPUT_KEY> -check
```

## Validate a certificate
```
openssl x509 -in <INPUT_CRT> -text -noout
```

## Validate a PKCS12 file (.pfx or .p12)
```
openssl pkcs12 -info -in <INPUT_PKCS12>
```

## Compare the MD5 hash of a certificate
```
openssl x509 -noout -modulus -in <INPUT_CRT> | openssl md5
```

## Compare the MD5 hash of a private key
```
openssl rsa -noout -modulus -in <INPUT_KEY> | openssl md5
```

## Compare the MD5 hash of a certificate signing request
```
openssl req -noout -modulus -in <INPUT_CSR> | openssl md5
```

## Display the server certificate chain
```
openssl s_client -connect <URL>:<PORT>
```