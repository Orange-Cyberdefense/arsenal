# Objection

% objection, android, ios, frida,
#platform/linux #target/local #cat/ANDROID
## Patch the app
objection patchapk -s <package>

## Patch the app without resource decoding
objection patchapk -D -s <package>

## Patch the app with debug flag
objection patchapk -d -s <package>

## Launch explore
objection explore

## Launch explore with startup command
objection explore -s <command>

## Launch explore without default ssl pinning bypass
objection explore -s "android sslpinning disable"

## Launch explore with startup script
objection explore -S <patch_to_script>
