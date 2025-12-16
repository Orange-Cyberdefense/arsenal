# nuclei

% nuclei, scanner, web

#plateform/linux #target/remote #cat/RECON

## nuclei - basic scan
```
nuclei -u <url> -o <output_file>
```

## nuclei - scan multiple targets from list
```
nuclei -l <targets_list> -u <url> -o <output_file>
```

## nuclei - scan with specific template
```
nuclei -u <url> -t <template_path> -o <output_file>
```

## nuclei - scan with tags filter
```
nuclei -u <url> -tags <tags|cve,rce,lfi> -o <output_file>
```

## nuclei - basic scan with proxy
```
nuclei -u <url> -proxy <proxy_url> -o <output_file>
```

## nuclei - update templates
```
nuclei -update-templates -o <output_file>
```

## nuclei - scan specific protocol (http, dns, file, network, headless, ssl)
```
nuclei -u <url> -pt <protocol|http> -o <output_file>
```

## nuclei - headless scan
```
nuclei -u <url> -headless -o <output_file>
```