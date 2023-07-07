# Android Debug Bridge (adb)

% android, device, adb, bridge

#platform/linux #target/local #cat/ANDROID

## Connect to specific device
```
adb -s <target_ip>:<adb_port|5555> shell
```

## Activate adb over network (while cable connected)
```
adb tcpip <adb_port|5555>
```

## Connect to device over network
```
adb connect <target_ip|192.168.178.80>:<adb_port|5555>
```

## Get property
```
adb -s <device> shell getprop <property>
```

## Get device architecture
```
adb shell getprop ro.product.cpu.abi
```

## List installed packages
```
adb shell cmd package list packages
```

## Install APK
```
adb -s <device> install -r <path>
```

## Get location of specific package
```
adb shell pm path package:com.mobisec.pincode
```

## Log activity of specific app
```
adb logcat | grep -F "`adb shell ps | grep <full_app_name> | tr -s [:space:] ' ' | cut -d' ' -f2`" |tee <out_file|log.txt>
```

## Uninstall package
```
adb -s <device> uninstall -r <package>
```

## Clear user data for package
```
adb -s <device> shell pm clear <package>
```

## Dispatch a deep-link / open URI
```
adb -s <device> shell am start <uri>
```

## Download apk
```
adb pull "$(adb shell pm path "$(adb shell pm list packages | grep <package> | cut -d : -f 2)" | cut -d : -f 2)" .
```

## Sign apk with Uber-apk-signer
```
java -jar uber-apk-signer-1.1.0.jar -a <app>
```