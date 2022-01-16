# gowitness

#plateform/linux #target/remote #cat/RECON #tag/scan

## gowitness - web screenshots (nmap xml file)
```
docker run --rm -v $(pwd):/data -p7171:7171 leonjza/gowitness gowitness nmap -f /data/<nmap_file>.xml
```

## gowitness - web screenshots (file containing urls)
```
docker run --rm -v $(pwd):/data -p7171:7171 leonjza/gowitness gowitness file -f /data/<file>
```

