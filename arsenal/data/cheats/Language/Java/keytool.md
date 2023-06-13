# keytool

% java keytool, certificate, encryption

#platform/linux #target/local  #cat/UTILS 

## Generate a Java keystore and key pair
```
keytool -genkey -alias <ALIAS> -keyalg RSA -keystore <OUTPUT_JKS> -keysize <RSA_LENGTH>
```

## Generate a certificate signing request (CSR) for an existing Java keystore
```
keytool -certreq -alias <ALIAS> -keystore <INPUT_JKS> -file <OUTPUT_CSR>
```

## Import a root or intermediate CA certificate to an existing Java keystore
```
keytool -import -trustcacerts -alias root -file <INPUT_CRT> -keystore <INPUT_JKS>
```

## Import a signed primary certificate to an existing Java keystore
```
keytool -import -trustcacerts -alias <ALIAS> -file <INPUT_CRT> -keystore <INPUT_JKS>
```

## Generate a keystore and self-signed certificate
```
keytool -genkey -keyalg RSA -alias <ALIAS> -keystore <OUTPUT_JKS> -storepass <PASSWORD> -validity <VALIDITY> -keysize <RSA_LENGTH>
```

## Check a stand-alone certificate
```
keytool -printcert -v -file <INPUT_CRT>
```

## Check which certificates are in a Java keystore
```
keytool -list -v -keystore <INPUT_JKS>
```

## Check a particular keystore entry using an alias
```
keytool -list -v -keystore <INPUT_JKS> -alias <ALIAS>
```

## Remove a certificate from a keystore
```
keytool -delete -alias <ALIAS> -keystore <INPUT_JKS>
```

## Change the password of a keystore
```
keytool -storepasswd -keystore <INPUT_JKS> -new <NEW_PASSWORD>
```

## Export a certificate from a keystore
```
keytool -export -alias <ALIAS> -file <OUTPUT_CRT> -keystore <INPUT_JKS>
```

## List the trusted CA Certs from the default Java Trusted Certs Keystore
```
keytool -list -v -keystore $JAVA_HOME/jre/lib/security/cacerts
```

## Import New Certificate Authority into the default Java Trusted Certs Keystore
```
keytool -import -trustcacerts -file <INPUT_PEM> -alias <ALIAS> -keystore $JAVA_HOME/jre/lib/security/cacerts
```
