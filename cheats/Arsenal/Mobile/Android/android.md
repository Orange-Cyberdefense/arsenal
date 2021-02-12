# Android Debug Bridge (adb)

% android, device, adb, bridge

#plateform/linux #target/local #cat/ANDROID

## Get property
adb -s <device> shell getprop <property>

## Install APK
adb -s <device> install -r <path>

## Uninstall package
adb -s <device> uninstall -r <package>

## Clear user data for package
adb -s <device> shell pm clear <package>

## Dispatch a deep-link / open URI
adb -s <device> shell am start <uri>

## Download apk
adb pull "$(adb shell pm path "$(adb shell pm list packages | grep <package> | cut -d : -f 2)" | cut -d : -f 2)" .

## Sign apk with Uber-apk-signer
java -jar uber-apk-signer-1.1.0.jar -a <app>