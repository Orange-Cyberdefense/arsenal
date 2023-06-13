# ligolo-ng

% ligolo-ng, proxy

## ligolo-ng - initial setup on C2 server
#platform/linux #target/serve #cat/UTILS
```bash
sudo ip tuntap add user <user|kali> mode tun ligolo; sudo ip link set ligolo up
```

## ligolo-ng - add route to internal network
#platform/linux #target/serve #cat/UTILS
```bash
sudo ip route add <internal_net|172.16.186.0/24> dev ligolo
```