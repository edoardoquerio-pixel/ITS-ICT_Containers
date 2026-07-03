# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking.pdf`
**Tipo:** `.pdf`
**Dimensione:** 825.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

Cloud SpecialistUnità Formativa (UF): Containers Microservizi ServerlessDocente: Denis MaggiorottoTitolo argomento: Container networking


Gestione della rete all'interno dei container

None network
46


None network
47
$ dockerrun-d --net none busyboxsleep10003a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3$ dockerexec-it3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3 /bin/ash/ # ping8.8.8.8PING 8.8.8.8 (8.8.8.8): 56 data bytesping: sendto: Network isunreachable/ # ifconfiglo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1

Bridge network
48


Bridge network
49
$ dockernetwork lsNETWORK ID          NAME                DRIVER              SCOPE8dae0c4d0380        bridge              bridgelocal22530231e5cd        hosthostlocalbd5e44929d16        none                nulllocal

Bridge network
50
IP Range: 172.17.0.0 –172.17.255.255

Bridge network
51
$ dockerexec-itcontainer_1 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:11:00:02inetaddr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:10 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:796 (796.0 B)  TX bytes:0 (0.0 B)lo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
$ dockerrun-d --namecontainer_1 busyboxsleep100034886a41f5212abd8cd3aa4062479028899e78f32b44103bade6b67d88b76f75

Bridge network
52
$ dockerrun-d --namecontainer_2 busyboxsleep1000c8c34dad781a7a5778852de2e40fe922f6b4113759b94928d81c4753f7631b9a$ dockerexec-itcontainer_2 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:11:00:04inetaddr:172.17.0.4  Bcast:172.17.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:10 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:796 (796.0 B)  TX bytes:0 (0.0 B)lo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---

Bridge network
53
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---2 packets transmitted, 2 packets received, 0% packet lossround-trip min/avg/max = 0.069/0.072/0.076 ms$ dockerexec-itcontainer_1 ping8.8.8.8PING 8.8.8.8 (8.8.8.8): 56 data bytes64 bytesfrom8.8.8.8: seq=0 ttl=117 time=33.251 ms---8.8.8.8 pingstatistics---1 packetstransmitted, 1 packetsreceived, 0% packetlossround-trip min/avg/max= 33.251/33.251/33.251ms

Bridge network
54
$ dockernetwork create --driver bridge my_bridge_network3d84cfb644d945ec14b1c9ed7f9e9fde10ae66edf41ce26d39fb60f16e00d16f$ dockernetwork inspectmy_bridge_network[{"Name": "my_bridge_network","Id": "3d84cfb644d945ec14b1c9ed7f9e9fde10ae66edf41ce26d39fb60f16e00d16f","Created": "2019-02-08T16:40:38.916055692Z","Scope": "local","Driver": "bridge","EnableIPv6": false,"IPAM": {"Driver": "default","Options": {},"Config": [{"Subnet": "172.19.0.0/16","Gateway": "172.19.0.1"

Bridge network
55
$ dockerrun-d --namecontainer_3  --net my_bridge_network busyboxsleep1000Dee203a2804a63935bea37f53d51f1b35b8e769124ca302351c4d192e1c94187$ dockerexec-itcontainer_3 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:13:00:02inetaddr:172.19.0.2  Bcast:172.19.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:16 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:1312 (1.2 KiB)  TX bytes:0 (0.0 B)…$ dockerstart container_1container_1$ dockerexec-itcontainer_1 ifconfig…eth0      Link encap:Ethernet  HWaddr02:42:AC:11:00:02inetaddr:172.17.0.2Bcast:172.17.255.255  Mask:255.255.0.0…$ dockerexec-itcontainer_3 ping172.17.0.2PING 172.17.0.2 (172.17.0.2): 56 data bytes…---172.17.0.2 ping statistics ---424 packets transmitted, 0 packets received, 100% packet loss

Bridge network
56
$ docker network connect bridge container_3$ dockerexec-itcontainer_3 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:13:00:02inetaddr:172.19.0.2  Bcast:172.19.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:36 errors:0 dropped:0 overruns:0 frame:0TX packets:434 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:2432 (2.3 KiB)  TX bytes:41972 (40.9 KiB)eth1      Link encap:Ethernet  HWaddr02:42:AC:11:00:04inetaddr:172.17.0.4  Bcast:172.17.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:9 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:726 (726.0 B)  TX bytes:0 (0.0 B)lo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)$ dockerexec-itcontainer_3 ping172.17.0.2PING 172.17.0.2 (172.17.0.2): 56 data bytes64 bytesfrom172.17.0.2: seq=0 ttl=64 time=0.489 ms64 bytesfrom172.17.0.2: seq=1 ttl=64 time=0.116 ms---172.17.0.2 pingstatistics---2 packetstransmitted, 2 packetsreceived, 0% packetlossround-trip min/avg/max= 0.082/0.160/0.489 ms$ dockernetwork disconnect bridge container_3

Host network
57
$ dockerrun-d --namecontainer_6 --net hostbusyboxsleep1000Baad65ed37ad53ab705bf9f9bbf50c779736bbda128859111f28fad24473421b$ dockerexec-itcontainer_6 ifconfigbr-3d84cfb644d9 Link encap:Ethernet  HWaddr02:42:4C:D0:FD:D5inetaddr:172.19.0.1  Bcast:172.19.255.255  Mask:255.255.0.0inet6 addr: fe80::42:4cff:fed0:fdd5/64 Scope:LinkUP BROADCAST MULTICAST  MTU:1500  Metric:1RX packets:434 errors:0 dropped:0 overruns:0 frame:0TX packets:26 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:35896 (35.0 KiB)  TX bytes:1676 (1.6 KiB)br-6b74b77377ec Link encap:Ethernet  HWaddr02:42:51:A1:81:6Binetaddr:172.18.0.1  Bcast:172.18.255.255  Mask:255.255.0.0UP BROADCAST MULTICAST  MTU:1500  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

Host network
58
docker0   Link encap:Ethernet  HWaddr02:42:25:25:B1:24inetaddr:172.17.0.1  Bcast:172.17.255.255  Mask:255.255.0.0inet6 addr: fe80::42:25ff:fe25:b124/64 Scope:LinkUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:103 errors:0 dropped:0 overruns:0 frame:0TX packets:220 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:128663 (125.6 KiB)  TX bytes:18397 (17.9 KiB)eth0      Link encap:Ethernet  HWaddr08:00:27:2E:6E:CEinetaddr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0inet6 addr: fe80::a00:27ff:fe2e:6ece/64 Scope:LinkUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:146537 errors:0 dropped:0 overruns:0 frame:0TX packets:10959 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:204339347 (194.8 MiB)  TX bytes:1083768 (1.0 MiB)

LAB
59
https://github.com/sunnyvale-academy/ITS-ICT_ContainersLab 08 –DockernetworkingAssignment02 -Multi-network Wordpressinstallation

Esposizione delle porte di un container

Esposizione di porte da un container
61
Prendiamo come esempio i seguenti container:
$ dockerrun--network bridge --namecontainer_1 httpd:latest…  
$ dockerrun--network bridge  --namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL

Esposizione di porte da un container
62
XXBridge network
I container creati con una network di tipo «bridge», di default nonespongono le porte di rete sul dockerhost

Esposizione di porte da un container
63
Bridge network
Per poter accedere ai servizi, occorre rimapparele porte dei container su porte libere del dockerhost

Esposizione di porte da un container
64
Per farlo, usiamo il parametro –pseguito da una coppia di porte separate dal carattere :
$ dockerrun–p8080:80 --network bridge --namecontainer_1 httpd:latest…  
$ dockerrun–p6603:3306 --network bridge  --namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL
Porta su dockerhost: porta del container 
Porta su dockerhost: porta del container 

Esposizione di porte da un container
65


Esposizione di porte da un container
66
Prendiamo come esempio i seguenti container:
$ dockerrun--network host--namecontainer_1 httpd:latest…  
$ dockerrun--network host--namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL

Esposizione di porte da un container
67
Host network
I container creati con una network di tipo «host», di default espongono le porte di rete sul dockerhost

Esposizione di porte da un container
68
Prendiamo come esempio i seguenti container:
$ dockerrun--network none --namecontainer_1 httpd:latest…  
$ dockerrun--network none  --namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL

Esposizione di porte da un container
69
None network
I container creati con una network di tipo «none», di default nonespongono servizi sall’esterno
XX

LAB
70
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 09 –Containers ports
