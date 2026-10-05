
# Networking Notes — From Fundamentals to Security

> **Purpose:** Structured networking notes arranged in a learning sequence: **network basics → OSI → addressing → local delivery → routing → network services → application protocols → security concepts → tools → troubleshooting**.
>
> Use scanning, packet capture, service testing, and authentication testing only on systems, labs, CTFs, or networks you own or are explicitly authorized to test.

---

## Table of Contents

1. [Networking Fundamentals](#1-networking-fundamentals)
2. [OSI Model](#2-osi-model)
3. [Network Types](#3-network-types)
4. [Networking Devices](#4-networking-devices)
5. [Ethernet, Wi-Fi, and MAC Addresses](#5-ethernet-wi-fi-and-mac-addresses)
6. [IPv4 Addressing](#6-ipv4-addressing)
7. [Private and Public IP Addresses](#7-private-and-public-ip-addresses)
8. [Subnet Mask and CIDR](#8-subnet-mask-and-cidr)
9. [Default Gateway and Routing](#9-default-gateway-and-routing)
10. [DHCP](#10-dhcp)
11. [ARP](#11-arp)
12. [ICMP and Ping](#12-icmp-and-ping)
13. [NAT, PAT, and Port Forwarding](#13-nat-pat-and-port-forwarding)
14. [Home Router](#14-home-router)
15. [Phone Hotspot](#15-phone-hotspot)
16. [TCP and UDP](#16-tcp-and-udp)
17. [Ports and Sockets](#17-ports-and-sockets)
18. [DNS](#18-dns)
19. [nslookup](#19-nslookup)
20. [dig](#20-dig)
21. [WHOIS](#21-whois)
22. [HTTP and HTTPS](#22-http-and-https)
23. [TLS and SSL](#23-tls-and-ssl)
24. [Telnet and SSH](#24-telnet-and-ssh)
25. [FTP, FTPS, and SFTP](#25-ftp-ftps-and-sftp)
26. [SMTP](#26-smtp)
27. [POP3 and IMAP](#27-pop3-and-imap)
28. [Cleartext vs Encrypted Protocols](#28-cleartext-vs-encrypted-protocols)
29. [Sniffing](#29-sniffing)
30. [Spoofing](#30-spoofing)
31. [Scanning and Enumeration](#31-scanning-and-enumeration)
32. [Eavesdropping and MITM](#32-eavesdropping-and-mitm)
33. [Phishing and Pharming](#33-phishing-and-pharming)
34. [DoS, DDoS, and Credential Attacks](#34-dos-ddos-and-credential-attacks)
35. [Complete End-to-End Example](#35-complete-end-to-end-example)
36. [Troubleshooting Method](#36-troubleshooting-method)
37. [Practical Commands](#37-practical-commands)
38. [SOC L1 Takeaways](#38-soc-l1-takeaways)
39. [Port Cheat Sheet](#39-port-cheat-sheet)
40. [Final Memory Map](#40-final-memory-map)
41. [Revision Questions](#41-revision-questions)

---

# 1. Networking Fundamentals

## 1.1 What is a network?

A **computer network** is a group of connected devices that can exchange data and share services/resources.

Example:

~~~text
                    Internet
                       |
                    ISP / ONT
                       |
                Home Wi-Fi Router
                /       |       \
               /        |        \
           Laptop      Phone      TV
        192.168.1.10   .11       .12
~~~

The communication can involve several layers:

~~~text
Application  -> DNS / HTTP / SMTP / FTP
Transport    -> TCP / UDP / ports
Network      -> IP / routing
Data Link    -> Ethernet / Wi-Fi / MAC
Physical     -> cable / radio / optical signal
~~~

## 1.2 Protocol

A **protocol** is a set of rules that defines how systems communicate.

Examples:

- IP
- TCP
- UDP
- DNS
- DHCP
- ARP
- ICMP
- HTTP
- HTTPS
- FTP
- SMTP
- IMAP
- POP3
- SSH

Memory:

~~~text
Protocol = rules for communication
~~~

## 1.3 Host

A **host** is a device or system that participates in network communication.

Examples:

- Laptop
- Server
- Smartphone
- Virtual machine

## 1.4 Client and server

A **client** requests a service.

A **server** provides a service.

~~~text
Client -----------------> Server
       request

Client <----------------- Server
       response
~~~

One physical machine can provide multiple services.

## 1.5 Port

A port is a logical transport-layer endpoint associated with a service.

Example:

~~~text
192.168.1.10:22 -> SSH
192.168.1.10:80 -> HTTP
~~~

Think:

~~~text
IP address -> network-layer host/address
Port       -> transport-layer service endpoint
~~~

---

# 2. OSI Model

The **OSI model** is a conceptual seven-layer model.

| Layer | Name | Common examples |
|---:|---|---|
| 7 | Application | HTTP, DNS, SMTP, FTP |
| 6 | Presentation | Data representation, encryption concepts |
| 5 | Session | Session management |
| 4 | Transport | TCP, UDP, ports |
| 3 | Network | IP, routing |
| 2 | Data Link | Ethernet, Wi-Fi, MAC |
| 1 | Physical | Cable, radio, electrical/optical signaling |

For practical beginner networking:

~~~text
L7 -> Application -> DNS / HTTP / SMTP
L4 -> Transport  -> TCP / UDP / ports
L3 -> Network    -> IP / routing
L2 -> Data Link  -> Ethernet / Wi-Fi / MAC
L1 -> Physical   -> cable / radio / signal
~~~

## Key device relationship

~~~text
Switch -> primarily Layer 2 -> MAC -> Ethernet frames
Router -> primarily Layer 3 -> IP  -> routing
~~~

This is a learning shortcut, not a rule that real equipment can operate at only one layer.

---

# 3. Network Types

## 3.1 PAN — Personal Area Network

Small personal network.

Example:

~~~text
Phone <-> Bluetooth earbuds
~~~

## 3.2 LAN — Local Area Network

A network covering a relatively small local area such as:

- Home
- Office
- Room
- Building

## 3.3 WLAN — Wireless LAN

A LAN using wireless networking, commonly Wi-Fi.

~~~text
WLAN is a type of LAN
~~~

## 3.4 CAN — Campus Area Network

Connects several local networks across a campus.

Example:

~~~text
University
|- Library
|- Hostel
|- Labs
|- Administration
~~~

## 3.5 MAN — Metropolitan Area Network

Covers a city or metropolitan region.

## 3.6 WAN — Wide Area Network

Connects networks over large geographic areas.

The Internet is a huge interconnected system of networks.

## 3.7 VPN — Virtual Private Network

A VPN creates a logical/private connection or tunnel over another network.

~~~text
Laptop ===== VPN tunnel =====> Company network
~~~

A VPN is not primarily a geographic category like LAN or WAN.

### Mnemonic

~~~text
PAN -> Person
LAN -> Local
CAN -> Campus
MAN -> Metropolitan
WAN -> Wide
~~~

---

# 4. Networking Devices

## 4.1 Hub

A hub is a Layer 1 device.

It repeats incoming signals to other ports.

~~~text
PC1 --\
PC2 --- HUB --- PC3
PC4 --/
~~~

It does not intelligently forward traffic using MAC addresses.

Hubs are largely obsolete in modern switched networks.

## 4.2 Switch

A switch is primarily a Layer 2 device.

It:

- Receives Ethernet frames
- Examines destination MAC addresses
- Learns source MAC addresses
- Forwards frames through appropriate ports

~~~text
PC1 --\
PC2 --- Switch --- Server
PC3 --/
~~~

Memory:

~~~text
Switch -> MAC -> Ethernet frame
~~~

A Layer 3 switch can also perform routing.

## 4.3 Router

A router is primarily a Layer 3 device.

It connects different IP networks and uses routing information to forward packets.

~~~text
LAN 192.168.1.0/24
        |
      Router
        |
   WAN / Internet
~~~

Memory:

~~~text
Router -> IP -> routing
~~~

## 4.4 Access Point

An access point provides wireless access to a LAN.

~~~text
Laptop ))))
       \
        AP ---- Switch ---- Router
       /
Phone ))))
~~~

## 4.5 Bridge

A bridge connects Layer 2 network segments.

Modern switches are essentially advanced multi-port bridges.

## 4.6 Repeater

A repeater regenerates/repeats a signal, primarily at the physical layer.

## 4.7 Modem

A modem terminates/provides the ISP access technology. Modern broadband equipment can combine modem and router functions.

## 4.8 ONT

An **Optical Network Terminal (ONT)** is commonly used with fiber Internet.

~~~text
Fiber -> ONT -> Ethernet -> Router
~~~

## 4.9 Gateway

A gateway is a device/function that provides a path from one network to another.

In a typical home network, the router's LAN IP is the client's default gateway.

## 4.10 Firewall

A firewall controls traffic according to rules and may:

- Allow
- Block
- Log
- Inspect

## 4.11 DHCP and DNS server

DHCP and DNS are **services**, not necessarily separate physical devices.

A home router often provides both.

---

# 5. Ethernet, Wi-Fi, and MAC Addresses

## 5.1 Ethernet

Ethernet is a family of networking technologies covering physical and data-link behavior.

Traditional Ethernet commonly uses cables.

An Ethernet frame contains information such as:

- Destination MAC
- Source MAC
- Payload
- Error-detection information

## 5.2 Wi-Fi

Wi-Fi provides wireless LAN connectivity using radio.

Both Ethernet and Wi-Fi can:

- Carry IP packets
- Use MAC addresses at Layer 2
- Connect devices to the same LAN

Main difference:

~~~text
Ethernet -> usually wired
Wi-Fi    -> wireless
~~~

## 5.3 MAC address

A MAC address is a Layer 2 address associated with a network interface.

Example:

~~~text
AA:BB:CC:11:22:33
~~~

Memory:

~~~text
MAC -> Layer 2
IP  -> Layer 3
~~~

One computer can have multiple interfaces and therefore multiple MAC addresses.

## 5.4 Ethernet broadcast MAC

The special MAC address:

~~~text
FF:FF:FF:FF:FF:FF
~~~

is the Ethernet **broadcast destination**.

It means:

~~~text
Deliver the frame to all devices in the local
Layer 2 broadcast domain.
~~~

Why all ones?

~~~text
FF = 11111111
~~~

All 48 bits of the MAC address are 1.

## 5.5 Broadcast MAC vs ARP

Do not confuse:

~~~text
FF:FF:FF:FF:FF:FF -> broadcast destination MAC
ARP                -> IPv4 address-to-MAC resolution protocol
~~~

ARP requests commonly use the broadcast MAC.

## 5.6 Important Windows detail

Windows may display a virtual network adapter with the name Ethernet.

For example, virtualization software can create:

~~~text
VirtualBox
   |
   +-> Virtual Ethernet adapter
~~~

Therefore:

~~~text
Windows interface name "Ethernet"
!= proof that a physical Ethernet cable is connected
~~~

---

# 6. IPv4 Addressing

## 6.1 What is an IP address?

An IP address is a Layer 3 logical address used for IP communication.

Example:

~~~text
192.168.1.10
~~~

IPv4 uses 32 bits and is written as four decimal octets.

## 6.2 Does a laptop have a permanent IP?

Not necessarily.

A laptop can receive its IP configuration through:

- DHCP
- Static/manual configuration
- Another network configuration service

The same laptop can have different IP addresses on different networks.

Example:

~~~text
Home Wi-Fi      -> 192.168.1.10
College network -> 10.20.4.57
Phone hotspot   -> 192.168.43.x  (example)
~~~

## 6.3 MAC vs IP

~~~text
MAC -> Layer 2 interface address
IP  -> Layer 3 logical network address
~~~

They solve different problems.

## 6.4 DHCP does not create the MAC address

The network interface already has a MAC address.

DHCP configures IP-layer information. It does not create the interface MAC address.

---

# 7. Private and Public IP Addresses

## 7.1 Private IPv4 ranges

The three major private IPv4 ranges are:

~~~text
10.0.0.0       - 10.255.255.255
172.16.0.0     - 172.31.255.255
192.168.0.0    - 192.168.255.255
~~~

CIDR form:

~~~text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
~~~

Private addresses are intended for internal/private networks and are not directly routed across the public Internet.

## 7.2 Public IP

A public IP is generally Internet-routable and is commonly assigned by an ISP, cloud provider, or other public network operator.

## 7.3 Private does not mean secret

~~~text
Private IP != secret
Public IP  != automatically exposed
~~~

Exposure depends on:

- Routing
- Firewall rules
- NAT
- Port forwarding
- VPN configuration
- Listening services
- Access-control rules

## 7.4 Same private IP in different networks

This is valid:

~~~text
Network A                  Network B
Router -> 192.168.1.1     Router -> 192.168.1.1
PC     -> 192.168.1.10    PC     -> 192.168.1.10
~~~

The networks are separate, so their private address spaces can overlap.

Important:

~~~text
NAT is NOT the reason separate private networks can reuse
192.168.1.10.
~~~

NAT matters when traffic crosses a translation boundary.

---

# 8. Subnet Mask and CIDR

A subnet mask/prefix determines which part of an IPv4 address represents the network.

Example:

~~~text
IP   = 192.168.1.10
Mask = 255.255.255.0
CIDR = /24
~~~

This represents:

~~~text
192.168.1.0/24
~~~

## 8.1 Local destination

Host:

~~~text
192.168.1.10/24
~~~

Destination:

~~~text
192.168.1.20
~~~

Both belong to:

~~~text
192.168.1.0/24
~~~

So the destination is local to the subnet, and local Layer 2 delivery can be used.

## 8.2 Remote destination

Host:

~~~text
192.168.1.10/24
~~~

Destination:

~~~text
8.8.8.8
~~~

The destination is outside the local subnet, so the host uses its default gateway.

## 8.3 Core purpose

The subnet mask helps answer:

~~~text
"Is this destination on my local network,
or should I send the packet to a router?"
~~~

---

# 9. Default Gateway and Routing

## 9.1 Default gateway

The **default gateway** is the next-hop device used for destinations outside the local subnet when no more specific route exists.

Example:

~~~text
Laptop IP      = 192.168.1.10/24
Default gateway = 192.168.1.1
~~~

## 9.2 Same-network traffic

~~~text
Laptop 192.168.1.10
       |
       | local delivery
       v
PC 192.168.1.20
~~~

The laptop can reach the destination directly through the local network.

## 9.3 Remote traffic

~~~text
Laptop 192.168.1.10
       |
       | next hop
       v
Router 192.168.1.1
       |
       v
Other networks / Internet
~~~

## 9.4 Critical Layer 2 vs Layer 3 distinction

Suppose:

~~~text
Laptop IP     = 192.168.1.10
Router IP     = 192.168.1.1
Remote target = 8.8.8.8
~~~

The outgoing data can be thought of as:

~~~text
Ethernet destination MAC = Router MAC
IP destination           = 8.8.8.8
~~~

The Ethernet frame is delivered to the **next-hop router**, while the IP packet is still addressed to the **final remote destination**.

Therefore:

~~~text
Layer 2 destination -> next-hop MAC
Layer 3 destination -> final IP destination
~~~

This is one of the most important networking concepts to understand.

## 9.5 One address can have several roles

For example:

~~~text
192.168.1.1
~~~

can simultaneously be:

- A private IP
- The router's LAN IP
- The default gateway

These are different properties/roles.

---

# 10. DHCP

## 10.1 What is DHCP?

**DHCP = Dynamic Host Configuration Protocol**

DHCP automatically provides network configuration to clients.

Typical information:

- IP address
- Subnet mask/prefix
- Default gateway
- DNS server
- Lease information

## 10.2 DORA

The common DHCP process is:

~~~text
D -> Discover
O -> Offer
R -> Request
A -> Acknowledge
~~~

Conceptually:

~~~text
Client                     DHCP Server
  |                             |
  |------ DHCP Discover ------->|
  |<------- DHCP Offer ---------|
  |------ DHCP Request -------->|
  |<------ DHCP ACK ------------|
~~~

## 10.3 Why DHCP is useful

Without automatic configuration, a device might need manual entry of:

~~~text
IP
Subnet mask
Default gateway
DNS
~~~

DHCP automates this process.

## 10.4 DHCP is a service

A home router commonly runs the DHCP server.

Therefore:

~~~text
"Router gave me an IP"
~~~

is shorthand for:

~~~text
The router's DHCP service provided my IP configuration.
~~~

## 10.5 DHCP and MAC

DHCP can use information such as a client's MAC address for identification/reservations.

But:

~~~text
DHCP does not assign the MAC address.
~~~

---

# 11. ARP

## 11.1 What is ARP?

**ARP = Address Resolution Protocol**

For IPv4 local networking, ARP resolves:

~~~text
IPv4 address -> MAC address
~~~

## 11.2 Example

The laptop knows:

~~~text
Router IP = 192.168.1.1
~~~

but does not know the router's MAC.

It sends an ARP request:

~~~text
Who has 192.168.1.1?
Tell 192.168.1.10.
~~~

The Ethernet destination is commonly:

~~~text
FF:FF:FF:FF:FF:FF
~~~

The router replies:

~~~text
192.168.1.1 is at AA:BB:CC:DD:EE:FF
~~~

Now the laptop can send the Ethernet frame to that MAC.

## 11.3 ARP cache

Windows:

~~~powershell
arp -a
~~~

Linux:

~~~bash
ip neigh
~~~

These can show recently learned local neighbor information.

## 11.4 ARP and remote destinations

If the final target is:

~~~text
8.8.8.8
~~~

the laptop normally does not ARP for 8.8.8.8 on the local LAN.

Instead it resolves the MAC of the next hop:

~~~text
Default gateway IP -> Gateway MAC
~~~

## 11.5 IPv6

IPv6 does not use ARP.

IPv6 uses **Neighbor Discovery** mechanisms instead.

---

# 12. ICMP and Ping

## 12.1 ICMP

**ICMP = Internet Control Message Protocol**

It is used for:

- Diagnostics
- Network control
- Error reporting

## 12.2 Ping

The common ping utility uses:

~~~text
ICMP Echo Request
ICMP Echo Reply
~~~

Example:

~~~bash
ping 8.8.8.8
~~~

Conceptually:

~~~text
Laptop -----------------> Target
        Echo Request

Laptop <----------------- Target
        Echo Reply
~~~

## 12.3 ARP + ICMP

When pinging a local router, a typical sequence can be:

~~~text
1. Need router MAC
       |
2. ARP request/reply
       |
3. Build Ethernet frame
       |
4. IP packet carries ICMP Echo Request
       |
5. Receive ICMP Echo Reply
~~~

## 12.4 Ping failure is not absolute proof

A firewall/network policy may block ICMP.

Therefore:

~~~text
Ping failure != guaranteed "Internet is down"
~~~

Ping is one diagnostic signal, not absolute proof of connectivity.

---

# 13. NAT, PAT, and Port Forwarding

## 13.1 NAT

**NAT = Network Address Translation**

NAT changes IP addressing as traffic crosses a translation boundary.

Typical home network:

~~~text
Laptop 192.168.1.10 \
Phone   192.168.1.11  \
TV      192.168.1.12   -> Router -> NAT -> Public IP -> Internet
~~~

## 13.2 PAT / NAPT

A common form of NAT also translates transport ports.

Example:

~~~text
192.168.1.10:50000 -> 49.x.x.x:40001
192.168.1.11:50001 -> 49.x.x.x:40002
192.168.1.12:50002 -> 49.x.x.x:40003
~~~

Many internal connections can therefore share one public IPv4 address.

The router keeps translation state so returning traffic can be mapped to the correct internal host/port.

## 13.3 NAT is not a firewall

~~~text
NAT      -> address/port translation
Firewall -> traffic control using rules
~~~

A home router commonly performs both.

## 13.4 Port forwarding

Port forwarding explicitly maps an external service port to an internal host.

Example:

~~~text
Public:
49.x.x.x:8080
      |
      v
Internal:
192.168.1.10:8080
~~~

Port forwarding can make a private service reachable externally, subject to firewall/routing settings.

---

# 14. Home Router

A home Wi-Fi router is usually a multifunction networking device.

It may combine:

~~~text
+----------------------------------+
| Home Wi-Fi Router                |
|                                  |
| Router / routing                 |
| Ethernet switch                  |
| Wi-Fi access point               |
| DHCP server                      |
| NAT/PAT                          |
| Firewall                         |
| DNS forwarding/resolver function |
+----------------------------------+
~~~

Typical topology:

~~~text
                    Internet
                       |
                 ISP / ONT / Modem
                       |
                Home Wi-Fi Router
                /       |       \
               /        |        \
            Laptop     Phone      TV
          192.168.1.10 .11       .12
~~~

So when we say:

~~~text
"The router gave the laptop an IP."
~~~

the more precise description is:

~~~text
The router's DHCP service provided the laptop's IP configuration.
~~~

---

# 15. Phone Hotspot

A smartphone hotspot can behave like a small gateway/router.

~~~text
Mobile carrier network
        |
        v
      Phone
   +-----------+
   | Wi-Fi AP  |
   | DHCP      |
   | NAT       |
   | Gateway   |
   +-----------+
        |
       Wi-Fi
        |
      Laptop
~~~

The phone commonly provides:

- Wireless access
- Private IP configuration
- Default gateway
- DNS information
- DHCP
- NAT toward the mobile network

Traffic path:

~~~text
Laptop -> Phone hotspot -> Mobile carrier -> Internet
~~~

The exact private IP range depends on the phone/software.

---

# 16. TCP and UDP

## 16.1 TCP

**TCP = Transmission Control Protocol**

Characteristics:

- Connection-oriented
- Reliable delivery
- Ordered byte stream
- Retransmission
- Flow/congestion control

Common examples:

- HTTP/HTTPS
- SSH
- FTP
- SMTP
- POP3
- IMAP

## 16.2 UDP

**UDP = User Datagram Protocol**

Characteristics:

- Connectionless
- Lower overhead
- No TCP-style guarantee of delivery/order

Common examples:

- Traditional DNS queries
- DHCP

Memory:

~~~text
TCP -> reliability and ordered byte stream
UDP -> lightweight datagrams
~~~

---

# 17. Ports and Sockets

A port is a logical service endpoint at the transport layer.

Example:

~~~text
192.168.1.10:443
~~~

means:

~~~text
IP  -> network-layer address
443 -> transport-layer service endpoint
~~~

A connection can be described using information such as:

~~~text
Source IP
Source port
Destination IP
Destination port
Transport protocol
~~~

Example:

~~~text
192.168.1.10:51500 -> 93.184.216.34:443
~~~

Here:

~~~text
51500 -> client-side ephemeral port
443   -> server-side HTTPS port
~~~

---

# 18. DNS

## 18.1 What is DNS?

**DNS = Domain Name System**

DNS resolves names and stores many types of DNS records.

Basic example:

~~~text
example.com
     |
     v
DNS
     |
     v
93.184.216.34
~~~

## 18.2 Important DNS record types

| Record | Meaning |
|---|---|
| A | IPv4 address |
| AAAA | IPv6 address |
| MX | Mail server |
| NS | Name server |
| CNAME | Alias |
| TXT | Text/policy information |
| PTR | Reverse DNS |

## 18.3 DNS and port 53

Traditional DNS commonly uses:

~~~text
UDP 53
TCP 53
~~~

UDP is commonly used for normal queries; TCP is also used for cases such as larger responses and zone transfers.

---

# 19. nslookup

nslookup means **Name Server Lookup**.

It is a command-line DNS query utility.

## 19.1 Basic lookup

~~~bash
nslookup example.com
~~~

Typical concepts in the output:

~~~text
Server:     192.168.1.1
Address:    192.168.1.1#53

Name:       example.com
Address:    93.184.216.34
~~~

Interpretation:

- Server = DNS resolver being queried
- #53 = DNS service port
- Name = requested domain
- Address = returned address

## 19.2 A record

~~~bash
nslookup -query=A example.com
~~~

## 19.3 AAAA record

~~~bash
nslookup -query=AAAA example.com
~~~

## 19.4 Reverse lookup

~~~bash
nslookup 8.8.8.8
~~~

This may perform a PTR lookup:

~~~text
IP -> hostname
~~~

## 19.5 MX

~~~bash
nslookup -type=MX example.com
~~~

## 19.6 NS

~~~bash
nslookup -type=NS example.com
~~~

## 19.7 TXT

~~~bash
nslookup -type=TXT example.com
~~~

## 19.8 CNAME

~~~bash
nslookup -type=CNAME www.example.com
~~~

## 19.9 Specify the DNS server

~~~bash
nslookup example.com 8.8.8.8
~~~

---

# 20. dig

dig means **Domain Information Groper**.

It is more detailed and flexible than nslookup for DNS troubleshooting and investigation.

## 20.1 Basic query

~~~bash
dig example.com
~~~

Important sections include:

~~~text
QUESTION SECTION
ANSWER SECTION
AUTHORITY SECTION
ADDITIONAL SECTION
~~~

Example:

~~~text
example.com. 300 IN A 93.184.216.34
~~~

Meaning:

- example.com = domain
- 300 = TTL in seconds
- IN = Internet class
- A = IPv4 record
- 93.184.216.34 = answer

## 20.2 Useful commands

Only the answer:

~~~bash
dig example.com +short
~~~

A record:

~~~bash
dig example.com A
~~~

AAAA:

~~~bash
dig example.com AAAA
~~~

MX:

~~~bash
dig example.com MX
~~~

NS:

~~~bash
dig example.com NS
~~~

TXT:

~~~bash
dig example.com TXT
~~~

CNAME:

~~~bash
dig www.example.com CNAME
~~~

Reverse DNS:

~~~bash
dig -x 8.8.8.8
~~~

Specific resolver:

~~~bash
dig @8.8.8.8 example.com
dig @1.1.1.1 example.com
~~~

Trace:

~~~bash
dig example.com +trace
~~~

Conceptual trace:

~~~text
Root DNS
   |
   v
TLD DNS (.com)
   |
   v
Authoritative DNS
   |
   v
Final answer
~~~

DNSSEC-related queries:

~~~bash
dig example.com +dnssec
dig example.com DNSKEY
~~~

## 20.3 nslookup vs dig

| Feature | nslookup | dig |
|---|---|---|
| Quick DNS lookup | Excellent | Excellent |
| Detailed response | Basic | Excellent |
| Simple record queries | Yes | Yes |
| Short output | Limited | Excellent |
| Trace | No | Yes |
| Troubleshooting | Good | Excellent |
| Investigation | Useful | Very useful |

Memory:

~~~text
nslookup -> quick lookup
dig      -> detailed investigation
~~~

---

# 21. WHOIS

whois can provide available **domain registration information** and, for IP addresses, information about the network/organization associated with an allocation.

## 21.1 Domain lookup

~~~bash
whois example.com
~~~

Possible information:

- Domain name
- Registrar
- Creation date
- Updated date
- Expiration date
- Name servers
- Domain status

## 21.2 IP lookup

~~~bash
whois 8.8.8.8
~~~

This can provide allocation/registration information associated with the address/range.

## 21.3 WHOIS vs DNS

~~~text
WHOIS
  -> registration / allocation information

DNS
  -> names and DNS records
~~~

A recently registered suspicious domain can be an investigation indicator, but:

~~~text
new domain != automatically malicious
old domain != automatically trustworthy
~~~

WHOIS information may be redacted or privacy-protected.

---

# 22. HTTP and HTTPS

## 22.1 HTTP

**HTTP = Hypertext Transfer Protocol**

Used for web communication.

Common/default port:

~~~text
TCP 80
~~~

Flow:

~~~text
Browser / Client
      |
      | HTTP request
      v
Web Server
      |
      | HTTP response
      v
Browser / Client
~~~

Example:

~~~bash
curl http://example.com
~~~

HTTP without TLS is generally cleartext at the application layer.

## 22.2 HTTPS

**HTTPS = HTTP over TLS**

~~~text
HTTPS = HTTP + TLS
~~~

Common/default port:

~~~text
TCP 443
~~~

Example:

~~~bash
curl https://example.com
~~~

HTTPS protects application data in transit using TLS.

Important:

~~~text
HTTPS != proof that a website is trustworthy
~~~

A malicious site can also use HTTPS.

---

# 23. TLS and SSL

## 23.1 SSL

**SSL = Secure Sockets Layer**

SSL is the older security protocol family.

SSL 2.0 and SSL 3.0 are obsolete.

## 23.2 TLS

**TLS = Transport Layer Security**

TLS replaced SSL and is the modern protocol family used by HTTPS and many other applications.

Historical map:

~~~text
SSL 2.0 -> obsolete
SSL 3.0 -> obsolete
TLS 1.0 -> obsolete
TLS 1.1 -> obsolete
TLS 1.2 -> widely supported
TLS 1.3 -> modern
~~~

## 23.3 What TLS provides

### Confidentiality

Protects application data in transit from simple passive observation.

~~~text
Readable data
    |
    v
Encryption
    |
    v
Ciphertext
~~~

### Integrity

Helps detect unauthorized modification of protected traffic.

### Authentication

Certificates help a client authenticate the server.

## 23.4 TLS certificate

A certificate may contain:

- Domain/identity information
- Public key
- Certificate authority information
- Validity period
- Digital signature
- Other extensions

Conceptually:

~~~text
Website
   |
   | presents certificate
   v
Browser
   |
   | verifies hostname / chain / validity
   v
TLS connection
~~~

Certificate authorities include organizations such as DigiCert, Let's Encrypt, and GlobalSign.

## 23.5 TLS handshake

Simplified:

~~~text
Client                         Server
  |                              |
  |------ ClientHello ---------->|
  |<----- ServerHello -----------|
  |<----- Certificate -----------|
  |------ Key establishment ---->|
  |                              |
  |==== Encrypted application ===|
~~~

Exact handshake details depend on the TLS version.

## 23.6 Public-key and symmetric cryptography

TLS combines different cryptographic mechanisms.

Conceptually:

~~~text
Authentication / key establishment
             |
             v
      Shared secret/key
             |
             v
   Symmetric encryption
             |
             v
     Application data
~~~

## 23.7 Inspect TLS

~~~bash
curl -v https://example.com
~~~

or:

~~~bash
openssl s_client -connect example.com:443
~~~

TLS 1.2:

~~~bash
openssl s_client -connect example.com:443 -tls1_2
~~~

TLS 1.3:

~~~bash
openssl s_client -connect example.com:443 -tls1_3
~~~

---

# 24. Telnet and SSH

## 24.1 Telnet

Telnet is an old remote-terminal protocol.

Common/default port:

~~~text
TCP 23
~~~

Example:

~~~bash
telnet 192.168.1.10 23
~~~

Telnet is generally unencrypted.

Therefore:

~~~text
Telnet -> cleartext remote administration
~~~

## 24.2 SSH

**SSH = Secure Shell**

Common/default port:

~~~text
TCP 22
~~~

SSH provides encrypted remote administration.

## 24.3 Telnet can also test TCP connectivity

Example:

~~~bash
telnet 192.168.1.10 80
~~~

This does **not** mean port 80 is a Telnet service.

It means:

~~~text
Telnet client -> attempted TCP connection -> port 80
~~~

Important distinction:

~~~text
Client/tool being used
        !=
Service actually running on the destination port
~~~

---

# 25. FTP, FTPS, and SFTP

## 25.1 FTP

**FTP = File Transfer Protocol**

Used to transfer files.

FTP normally uses TCP.

Traditional ports:

~~~text
TCP 21 -> control
TCP 20 -> data in traditional active mode
~~~

Most important port:

~~~text
FTP -> 21
~~~

## 25.2 FTP control connection

~~~text
Client ---- TCP 21 ----> FTP Server
~~~

Commands include:

~~~text
USER
PASS
LIST
RETR
STOR
QUIT
~~~

## 25.3 FTP data connection

Used for:

- Directory listings
- Uploads
- Downloads

The data ports depend on active/passive FTP.

## 25.4 FTP security

Traditional FTP does not provide built-in encryption for normal credentials and data.

## 25.5 FTPS

FTPS is FTP protected with TLS.

A commonly associated implicit-TLS port is:

~~~text
990
~~~

## 25.6 SFTP

**SFTP = SSH File Transfer Protocol**

SFTP is a separate protocol from FTP.

It runs over SSH.

Common port:

~~~text
22
~~~

Very important:

~~~text
22 = SSH
SFTP = file transfer over SSH
SFTP != FTP with TLS
~~~

## 25.7 FTP client

~~~bash
ftp 192.168.56.10
~~~

Common commands:

~~~text
ls
dir
cd <directory>
get <file>
put <file>
mget <pattern>
mput <pattern>
bye
quit
~~~

## 25.8 Anonymous FTP

Some servers intentionally allow:

~~~text
Username: anonymous
~~~

During an authorized assessment, anonymous access should be checked for accidental exposure of sensitive files.

## 25.9 Authorized Nmap examples

~~~bash
nmap -sV -p 21 192.168.56.10
nmap --script ftp-anon -p 21 192.168.56.10
~~~

---

# 26. SMTP

## 26.1 What is SMTP?

**SMTP = Simple Mail Transfer Protocol**

SMTP is primarily used to send/transfer outgoing email.

~~~text
Email client
      |
      | SMTP
      v
Sender mail server
      |
      | SMTP
      v
Recipient mail server
~~~

## 26.2 Common ports

| Port | Typical purpose |
|---:|---|
| 25 | SMTP server-to-server transfer |
| 587 | Message submission; STARTTLS commonly used |
| 465 | SMTP over implicit TLS |

## 26.3 Common commands

~~~text
EHLO
MAIL FROM
RCPT TO
DATA
QUIT
~~~

## 26.4 SMTP security

SMTP can be protected using TLS.

~~~text
587 -> submission / STARTTLS commonly used
465 -> implicit TLS
~~~

## 26.5 SPF

**SPF = Sender Policy Framework**

A domain can publish which mail systems are authorized to send mail for that domain.

Example:

~~~bash
dig example.com TXT
~~~

## 26.6 DKIM

**DKIM = DomainKeys Identified Mail**

Uses a cryptographic signature for email. The public key is published in DNS.

## 26.7 DMARC

**DMARC = Domain-based Message Authentication, Reporting & Conformance**

Defines policy/reporting behavior for messages that fail relevant authentication/alignment checks.

Example:

~~~bash
dig _dmarc.example.com TXT
~~~

Memory:

~~~text
SPF  -> authorized senders
DKIM -> cryptographic signature
DMARC -> authentication policy/reporting
~~~

---

# 27. POP3 and IMAP

Both are used to retrieve/access email from a mail server.

~~~text
SMTP      -> send/transfer
POP3/IMAP -> retrieve/access
~~~

## 27.1 POP3

**POP3 = Post Office Protocol version 3**

Main idea:

~~~text
Download mail from the server
~~~

Common ports:

~~~text
110 -> POP3
995 -> POP3 over TLS
~~~

Depending on client settings, downloaded messages may be removed from the server.

## 27.2 IMAP

**IMAP = Internet Message Access Protocol**

Main idea:

~~~text
Access and synchronize mailbox on the server
~~~

Common ports:

~~~text
143 -> IMAP
993 -> IMAP over TLS
~~~

IMAP is especially useful for multiple devices.

~~~text
             Mail Server
           /      |      \
        Laptop   Phone   Tablet
~~~

Folders and read/unread state can remain synchronized through the server.

## 27.3 POP3 vs IMAP

| Feature | POP3 | IMAP |
|---|---|---|
| Main idea | Download | Access/synchronize |
| Default port | 110 | 143 |
| TLS port | 995 | 993 |
| Multi-device use | Less suitable | Excellent |
| Folder synchronization | Limited | Yes |
| Server-side mailbox model | Limited | Strong |

Memory:

~~~text
SMTP -> Send
POP3 -> Pull/download
IMAP -> Mailbox synchronization
~~~

---

# 28. Cleartext vs Encrypted Protocols

## 28.1 Common cleartext protocols

~~~text
FTP    -> 21
Telnet -> 23
SMTP   -> 25
HTTP   -> 80
POP3   -> 110
IMAP   -> 143
~~~

## 28.2 Common secure counterparts

~~~text
SSH        -> 22
HTTPS      -> 443
SMTP/TLS   -> 465
SMTP/STARTTLS commonly -> 587
FTPS       -> 990
IMAPS      -> 993
POP3S      -> 995
~~~

## 28.3 Port number alone does not prove security

Security depends on:

- Protocol
- Service configuration
- TLS/SSH negotiation
- Protocol version
- Cipher suite
- Certificate validation where applicable

Therefore:

~~~text
Port number != complete security diagnosis
~~~

---

# 29. Sniffing

**Sniffing = capturing/observing network traffic.**

Common tools:

- Wireshark
- tcpdump
- tshark

Example:

~~~bash
sudo tcpdump -i eth0
~~~

A packet capture may reveal:

- Source IP
- Destination IP
- Protocol
- Ports
- Packet metadata
- Payload when visible and not encrypted

Useful Wireshark filters:

~~~text
arp
icmp
dns
tcp.port == 80
ip.addr == 192.168.1.10
~~~

Security idea:

~~~text
Cleartext traffic -> payload may be readable
Encrypted traffic -> payload is protected from simple passive inspection
~~~

Only capture traffic you are authorized to inspect.

---

# 30. Spoofing

**Spoofing = pretending to be another entity/address.**

## 30.1 IP spoofing

Making a packet appear to come from another source IP.

## 30.2 MAC spoofing

Changing a network interface's MAC address to another value.

## 30.3 Email spoofing

Making an email appear to originate from another sender.

Memory:

~~~text
Sniffing -> capture
Spoofing -> pretend / impersonate
~~~

---

# 31. Scanning and Enumeration

## 31.1 Scanning

**Scanning = discovering hosts, ports, or services.**

Example:

~~~bash
nmap 192.168.1.10
~~~

Possible result:

~~~text
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https
~~~

Memory:

~~~text
Scanning -> "What is there?"
~~~

## 31.2 Enumeration

**Enumeration = collecting more detailed information after discovery.**

Example:

~~~text
Scanning:
445/tcp open

Enumeration:
SMB version?
Shares?
Users?
Accessible resources?
~~~

Memory:

~~~text
Scanning    -> discover
Enumeration -> collect details
~~~

---

# 32. Eavesdropping and MITM

## 32.1 Eavesdropping

Eavesdropping means secretly listening to communication.

Network sniffing can be one technique used for eavesdropping.

## 32.2 Man-in-the-Middle

A MITM situation places an attacker between two communicating parties.

Normal:

~~~text
Client <----------------> Server
~~~

MITM:

~~~text
Client <------> Attacker <------> Server
~~~

Potential goals include:

- Observe traffic
- Modify traffic
- Redirect communication
- Attempt credential theft

Strong encryption and correct endpoint/certificate authentication help defend against MITM attacks.

---

# 33. Phishing and Pharming

## 33.1 Phishing

Phishing is social engineering that tricks a user into:

- Clicking
- Opening a file/link
- Entering credentials
- Sending information
- Performing another unsafe action

Example:

~~~text
Fake email
    |
    v
Urgent message
    |
    v
Fake login page
    |
    v
Victim enters credentials
~~~

Memory:

~~~text
Phishing -> deceive the user
~~~

## 33.2 Pharming

Pharming focuses on redirecting a victim to a fraudulent destination, often through DNS, host-file, or network manipulation.

Example:

~~~text
Legitimate domain entered
          |
          v
Traffic redirected
          |
          v
Fraudulent destination
~~~

Memory:

~~~text
Phishing -> deception/social engineering
Pharming -> redirection/manipulation
~~~

---

# 34. DoS, DDoS, and Credential Attacks

## 34.1 DoS

**Denial of Service**

Attempts to make a service unavailable by exhausting resources or disrupting availability.

## 34.2 DDoS

**Distributed Denial of Service**

Uses multiple systems to generate attack traffic.

~~~text
Host 1 --\
Host 2 ---\
Host 3 ----> Target
Host 4 ---/
~~~

## 34.3 Brute force

Repeatedly tries passwords/credentials until a valid value is found.

~~~text
password1 -> wrong
password2 -> wrong
password3 -> wrong
password4 -> correct
~~~

Defenses include:

- MFA
- Strong unique passwords
- Rate limiting
- Throttling/lockout
- Monitoring authentication failures

## 34.4 Credential stuffing

Uses previously leaked username/password combinations against another service.

~~~text
Leaked credentials
       |
       v
Try the same credentials elsewhere
~~~

Especially effective when users reuse passwords.

## 34.5 Password spraying

Uses one or a few common passwords against many accounts.

~~~text
user1 -> common password
user2 -> common password
user3 -> common password
user4 -> common password
~~~

### Comparison

| Technique | Core idea |
|---|---|
| Brute force | Many password guesses against one account/system |
| Credential stuffing | Reuse leaked credential pairs |
| Password spraying | Few common passwords across many accounts |

---

# 35. Complete End-to-End Example

This section connects the concepts.

Assume:

~~~text
Laptop IP       = 192.168.1.10/24
Default gateway = 192.168.1.1
DNS resolver    = 192.168.1.1
Website         = example.com
~~~

The user enters:

~~~text
https://example.com
~~~

## Step 1 — DHCP

When the laptop joins the network, DHCP may provide:

~~~text
IP       = 192.168.1.10
Mask     = 255.255.255.0
Gateway  = 192.168.1.1
DNS      = 192.168.1.1
~~~

## Step 2 — DNS

The laptop needs the site's IP:

~~~text
example.com -> DNS -> destination IP
~~~

## Step 3 — Local or remote decision

The laptop compares the destination IP with:

~~~text
192.168.1.0/24
~~~

If the destination is outside the local subnet, the laptop chooses its default gateway.

## Step 4 — ARP

If the gateway MAC is not already known:

~~~text
192.168.1.1 -> router MAC
~~~

ARP can obtain this mapping.

## Step 5 — Ethernet/Wi-Fi frame

The local frame can be represented as:

~~~text
Ethernet destination MAC = Router MAC
IP destination           = Website IP
~~~

This gives the key rule:

~~~text
Layer 2 -> next hop
Layer 3 -> final destination
~~~

## Step 6 — Router

The router:

1. Receives the frame
2. Processes the IP packet
3. Consults routing information
4. Performs NAT/PAT if applicable
5. Forwards the traffic

## Step 7 — TCP and HTTPS

For a normal HTTPS session:

~~~text
TCP -> transport
TLS -> encryption/authentication
HTTP -> application protocol
~~~

## Step 8 — Response

The server response returns through the network.

The router can use NAT/PAT state to map the traffic back to the laptop.

### Complete chain

~~~text
DHCP
  ->
DNS
  ->
Subnet decision
  ->
ARP
  ->
Ethernet/Wi-Fi
  ->
Router
  ->
NAT/PAT
  ->
Internet
  ->
TCP
  ->
TLS
  ->
HTTP
~~~

---

# 36. Troubleshooting Method

When Internet access fails, do not immediately assume DNS is broken.

Work from lower-level connectivity upward.

## 36.1 Interface/link

Check:

~~~text
Wi-Fi connected?
Ethernet connected?
Interface enabled?
Virtual adapter present?
~~~

## 36.2 IP configuration

Windows:

~~~powershell
ipconfig /all
~~~

Linux:

~~~bash
ip addr
ip route
~~~

Look for:

~~~text
IP address
Subnet mask/prefix
Default gateway
DNS server
~~~

## 36.3 Gateway

Try the local gateway where ICMP is permitted:

~~~bash
ping 192.168.1.1
~~~

Remember that ICMP may be blocked.

## 36.4 Routing

Windows:

~~~powershell
route print
~~~

Linux:

~~~bash
ip route
~~~

Check whether a default route exists.

## 36.5 IP connectivity

Try a known IP:

~~~bash
ping 8.8.8.8
~~~

But remember:

~~~text
Ping failure != guaranteed no Internet
~~~

## 36.6 DNS

Test:

~~~bash
nslookup example.com
~~~

or:

~~~bash
dig example.com
~~~

## 36.7 Diagnostic scenarios

### Scenario A

~~~text
ping 192.168.1.20 -> works
ping 8.8.8.8      -> fails
~~~

Do not start with DNS.

Reason:

~~~text
8.8.8.8 is already an IP address.
~~~

Investigate:

- Default gateway
- Route table
- Upstream connectivity
- Firewall/policy

### Scenario B

~~~text
ping 8.8.8.8         -> works
nslookup example.com -> fails
~~~

DNS becomes a strong suspect.

---

# 37. Practical Commands

## 37.1 Windows

~~~powershell
ipconfig
ipconfig /all
arp -a
route print
ping 8.8.8.8
nslookup example.com
~~~

## 37.2 Linux

~~~bash
ip addr
ip route
ip neigh
ping 8.8.8.8
nslookup example.com
dig example.com
~~~

## 37.3 DNS

~~~bash
nslookup example.com
nslookup -type=MX example.com
nslookup -type=NS example.com
nslookup -type=TXT example.com
~~~

~~~bash
dig example.com
dig example.com +short
dig example.com MX +short
dig example.com NS +short
dig example.com TXT +short
dig -x 8.8.8.8 +short
dig @8.8.8.8 example.com
dig @1.1.1.1 example.com
dig example.com +trace
~~~

## 37.4 WHOIS

~~~bash
whois example.com
whois 8.8.8.8
~~~

## 37.5 HTTP/HTTPS

~~~bash
curl http://example.com
curl https://example.com
curl -I https://example.com
curl -v https://example.com
curl -L https://example.com
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
~~~

Download:

~~~bash
curl -O https://example.com/file.zip
curl -o output.zip https://example.com/file.zip
~~~

Custom header:

~~~bash
curl -H "User-Agent: TestClient" https://example.com
~~~

POST:

~~~bash
curl -X POST -d "username=test" https://example.com/login
~~~

JSON POST:

~~~bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"test"}' \
  https://example.com/api
~~~

## 37.6 TLS

~~~bash
openssl s_client -connect example.com:443
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -connect example.com:443 -tls1_3
~~~

## 37.7 FTP

~~~bash
ftp 192.168.56.10
~~~

## 37.8 Telnet / TCP connectivity test

~~~bash
telnet 192.168.1.10 23
telnet 192.168.1.10 80
~~~

## 37.9 Nmap

Use only against authorized targets.

~~~bash
nmap -sV -p 21 192.168.56.10
~~~

## 37.10 Packet analysis

Wireshark filters:

~~~text
arp
icmp
dns
tcp.port == 80
ip.addr == 192.168.1.10
~~~

tcpdump example:

~~~bash
sudo tcpdump -i eth0
~~~

---

# 38. SOC L1 Takeaways

A SOC Level 1 analyst should recognize common network patterns quickly.

## Port 21

~~~text
21 -> FTP control
~~~

Ask whether plain FTP is exposing credentials/data.

## Port 22

~~~text
22 -> SSH
~~~

Encrypted remote administration.

SFTP also uses SSH/port 22.

## Port 23

~~~text
23 -> Telnet
~~~

Generally a security concern because Telnet is cleartext.

## Port 25

~~~text
25 -> SMTP
~~~

Commonly server-to-server mail transfer.

## Port 53

~~~text
53 -> DNS
~~~

Traditional DNS commonly uses UDP/TCP 53.

## Port 80

~~~text
80 -> HTTP
~~~

Normally cleartext without TLS.

## Port 443

~~~text
443 -> HTTPS
~~~

HTTP protected by TLS.

## Port 110

~~~text
110 -> POP3
~~~

Plain POP3 is not encrypted by default.

## Port 143

~~~text
143 -> IMAP
~~~

Plain IMAP is not encrypted by default.

## Port 465

~~~text
465 -> SMTP over implicit TLS
~~~

## Port 587

~~~text
587 -> SMTP submission
    -> STARTTLS commonly used
~~~

## Port 990

~~~text
990 -> FTPS, commonly implicit TLS
~~~

## Port 993

~~~text
993 -> IMAPS
~~~

## Port 995

~~~text
995 -> POP3S
~~~

## Network investigation questions

~~~text
WHO?
 -> source IP / MAC

WHERE?
 -> destination IP

WHAT?
 -> protocol

WHICH?
 -> port / service

HOW?
 -> TCP or UDP

ENCRYPTED?
 -> TLS / SSH or cleartext

LOCAL OR REMOTE?
 -> subnet / routing

EXPECTED?
 -> normal activity or suspicious
~~~

---

# 39. Port Cheat Sheet

| Port | Protocol / Service | Main idea |
|---:|---|---|
| 20 | FTP data | Traditional active-mode data |
| 21 | FTP | Control connection |
| 22 | SSH / SFTP | Encrypted SSH; SFTP is separate from FTP |
| 23 | Telnet | Cleartext remote terminal |
| 25 | SMTP | Mail transfer |
| 53 | DNS | Name resolution |
| 80 | HTTP | Cleartext web |
| 110 | POP3 | Mail retrieval |
| 143 | IMAP | Mailbox access |
| 443 | HTTPS | HTTP over TLS |
| 465 | SMTP over TLS | Implicit TLS SMTP |
| 587 | SMTP submission | STARTTLS commonly used |
| 990 | FTPS | Common implicit TLS FTP |
| 993 | IMAPS | TLS-protected IMAP |
| 995 | POP3S | TLS-protected POP3 |

### Fast memory

~~~text
21  -> FTP
22  -> SSH
23  -> Telnet
25  -> SMTP
53  -> DNS
80  -> HTTP
110 -> POP3
143 -> IMAP
443 -> HTTPS
465 -> SMTP over implicit TLS
587 -> SMTP submission / STARTTLS
990 -> FTPS
993 -> IMAPS
995 -> POP3S
~~~

---

# 40. Final Memory Map

~~~text
NETWORK BASICS
 |
 +-- Protocol -> communication rules
 +-- Host     -> networked system
 +-- Client   -> requests a service
 +-- Server   -> provides a service
 +-- Port     -> logical service endpoint

OSI
 |
 +-- L7 Application -> DNS / HTTP / SMTP / FTP
 +-- L4 Transport   -> TCP / UDP / ports
 +-- L3 Network     -> IP / routing
 +-- L2 Data Link   -> Ethernet / Wi-Fi / MAC
 +-- L1 Physical    -> cable / radio

DEVICES
 |
 +-- Hub       -> Layer 1 / repeat
 +-- Switch    -> Layer 2 / MAC
 +-- Router    -> Layer 3 / IP
 +-- AP        -> wireless access
 +-- Bridge    -> Layer 2 segment connection
 +-- Repeater  -> signal regeneration
 +-- Modem     -> ISP access technology
 +-- ONT       -> fiber termination
 +-- Gateway   -> path to another network
 +-- Firewall  -> traffic control

ADDRESSING
 |
 +-- MAC -> Layer 2
 +-- IP  -> Layer 3
 +-- Private IP
 |    +-- 10.0.0.0/8
 |    +-- 172.16.0.0/12
 |    +-- 192.168.0.0/16
 |
 +-- Public IP -> generally Internet-routable
 +-- Subnet    -> local vs remote decision
 +-- Gateway   -> next hop for remote traffic

LOCAL DELIVERY
 |
 +-- ARP
 |    -> IPv4 address -> MAC
 |
 +-- FF:FF:FF:FF:FF:FF
 |    -> Ethernet broadcast
 |
 +-- Ethernet/Wi-Fi
 |    -> local frame delivery

NETWORK SERVICES
 |
 +-- DHCP -> automatic IP configuration
 |    +-- Discover
 |    +-- Offer
 |    +-- Request
 |    +-- Acknowledge
 |
 +-- DNS  -> name resolution
 +-- ICMP -> control / diagnostics / ping
 +-- NAT  -> address translation
 +-- PAT  -> address + port translation

APPLICATION PROTOCOLS
 |
 +-- HTTP  -> 80
 +-- HTTPS -> 443 + TLS
 +-- FTP   -> 21
 +-- FTPS  -> 990 (common)
 +-- SFTP  -> 22 via SSH
 +-- Telnet -> 23
 +-- SSH    -> 22
 +-- SMTP -> 25 / 465 / 587
 +-- POP3 -> 110 / 995
 +-- IMAP -> 143 / 993

SECURITY
 |
 +-- Sniffing -> capture
 +-- Spoofing -> impersonate
 +-- Scanning -> discover
 +-- Enumeration -> gather details
 +-- Eavesdropping -> secretly listen
 +-- MITM -> intercept
 +-- Phishing -> deceive
 +-- Pharming -> redirect
 +-- DoS/DDoS -> disrupt availability
 +-- Brute force -> repeated guessing
 +-- Credential stuffing -> leaked credentials
 +-- Password spraying -> common password across accounts

END-TO-END
 |
 DHCP
  ->
 DNS
  ->
 Subnet decision
  ->
 ARP
  ->
 Ethernet/Wi-Fi
  ->
 Router
  ->
 NAT/PAT
  ->
 Internet
  ->
 TCP/UDP
  ->
 TLS when used
  ->
 Application protocol
~~~

---

# 41. Revision Questions

## Fundamentals

1. What is a computer network?
2. What is a protocol?
3. What is a host?
4. What is the difference between a client and a server?
5. What is a port?
6. What is the difference between a MAC address and an IP address?

## OSI and devices

7. What are the seven OSI layers?
8. Which layer is a switch primarily associated with?
9. Which layer is a router primarily associated with?
10. Why does a switch use MAC addresses?
11. Why does a router use IP addresses?
12. What is the difference between a hub and a switch?
13. What is an access point?
14. What is a bridge?
15. What is a repeater?
16. What is an ONT?

## Network types

17. What is PAN?
18. What is LAN?
19. What is WLAN?
20. What is CAN?
21. What is MAN?
22. What is WAN?
23. What is a VPN?

## Addressing and routing

24. What is an IPv4 address?
25. Does a laptop necessarily have a permanent IP?
26. What are the three private IPv4 ranges?
27. What is the difference between a private and public IP?
28. Why can two separate private networks both use 192.168.1.10?
29. What is a subnet mask?
30. What does /24 mean?
31. How does a host decide whether a destination is local?
32. What is a default gateway?
33. Why is the router's MAC used when sending to a remote IP?

## DHCP, ARP, ICMP, NAT

34. What does DHCP provide?
35. What does DORA stand for?
36. Does DHCP assign the MAC address?
37. What does ARP do?
38. Why does ARP commonly use FF:FF:FF:FF:FF:FF?
39. What does ICMP do?
40. What does ping use?
41. Why can ping fail even when Internet access works?
42. What is NAT?
43. What is PAT/NAPT?
44. How can multiple private devices share one public IPv4 address?
45. What is port forwarding?
46. What is the difference between NAT and a firewall?

## Protocols

47. What is TCP?
48. What is UDP?
49. What is DNS?
50. What is the difference between nslookup and dig?
51. What does WHOIS provide?
52. What is HTTP?
53. What is HTTPS?
54. Why is Telnet insecure?
55. What is SSH?
56. What is TLS?
57. What is the difference between SSL and TLS?
58. What does an HTTPS certificate help provide?
59. What are FTP's control and data connections?
60. What is the difference between FTP, FTPS, and SFTP?
61. Which protocol mainly sends email?
62. What is the difference between SMTP, POP3, and IMAP?
63. What are SPF, DKIM, and DMARC?

## Security concepts

64. What is sniffing?
65. What is spoofing?
66. What is scanning?
67. What is enumeration?
68. What is eavesdropping?
69. What is MITM?
70. What is phishing?
71. What is pharming?
72. What is the difference between DoS and DDoS?
73. What is brute force?
74. What is credential stuffing?
75. What is password spraying?

## Scenario questions

76. A client can reach another local PC but cannot reach 8.8.8.8. What should you investigate first?
77. A client can reach 8.8.8.8 but cannot resolve example.com. What is the likely area to investigate?
78. Why can the same 192.168.1.10 exist in two different private networks?
79. Why can Windows show an Ethernet adapter when no physical cable is attached?
80. When a laptop opens an HTTPS website, where do DHCP, DNS, subnetting, ARP, the default gateway, NAT, TCP, TLS, and HTTP fit in the sequence?

---

## Final Rules to Memorize

~~~text
1. Switch -> MAC
2. Router -> IP
3. ARP -> IPv4 address to MAC
4. DHCP -> automatic IP configuration
5. DNS -> name resolution
6. ICMP -> diagnostics/control, ping
7. NAT -> address translation
8. PAT/NAPT -> address + port translation
9. Default gateway -> next hop for remote destinations
10. FF:FF:FF:FF:FF:FF -> Ethernet broadcast
11. HTTP -> 80
12. HTTPS -> 443
13. Telnet -> 23
14. SSH -> 22
15. FTP -> 21
16. SMTP -> 25 / 465 / 587
17. POP3 -> 110 / 995
18. IMAP -> 143 / 993
19. SFTP -> 22 via SSH; separate from FTP
20. Port number alone does not prove security
~~~

---

## Safety Note

Use reconnaissance, packet capture, service probing, password testing, and other security techniques only against your own systems, CTF/TryHackMe labs, or systems where you have explicit authorization.
