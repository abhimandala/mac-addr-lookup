Python program to query MAC address on https://macaddress.io/

- Build docker container
Note: Docker should be installed and in running state.

2) Clone git code
```bash
git clone https://github.com/abhimandala/mac-addr-lookup.git
```
3) Build Dockerfile
```bash
cd mac-addr-lookup
docker build -t mac-addr-lookup:public .
```

5) Run container
```bash
docker run -it <image id>
```

- Query MAC Address
```bash
root@bf94f5d524c8:~# python mac-addr.py 44:38:39:ff:ef:57
```




 
 
