# yum

% yum
#platform/linux #target/local  #cat/UTILS 

## List all available packages
```
yum list available
```

## List all installed packages
```
yum list installed
```

## Info about package
```
yum info <package-name>
```

## Search in repository (packages and descriptions)
```
yum search <query>
```

## List all history actions (install, update and erase)
```
yum history list
```

## Check updates for installed packages
```
yum check-update
```

## Update all packages
```
yum update
```

## Update spesific/individual package
```
yum update <package-name>
```

## Downgrade package
```
yum downgrade <package-name>
```

## Install a package from repository
```
yum install <package-name>
```

## Remove/delete package
```
yum remove <package-name>
```

## Install local rpm package
```
yum localinstall <filepath-rpm>
```

## Install security updates
```
yum update --security
```

## List dependencies of package
```
yum deplist <package-name>
```

## Remove un-needed packages and dependencies
```
yum autoremove
```

## Whatprovides package/file/binary
```
yum whatprovides <query>
```

## List currently enabled repositories
```
yum repolist
```