# Nuclei

% nuclei

## install nuclei
```
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

## Basic scan simple target
```
nuclei -target <url>
```

## Basic scan multiple targets
```
nuclei -targets <path>
```

## Basic network scan
```
nuclei -target <ip>/<netmask>
```

## Use custom template
```
nuclei -target <url> -t <path>
```

## Use template workflows
```
nuclei -target <url> -w <path>
```

## Passive scan
```
nuclei -passive -target <url>
```

## Connect Nuclei to ProjectDiscovery
```
nuclei -target <url> -dashboard
```