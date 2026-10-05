
# Foundational Networking Concepts — Studied in Chat

> This section covers the core concepts we studied from first principles: Ethernet, MAC/IP addressing, LAN/WLAN, devices, DHCP, ARP, ICMP, NAT/PAT, default gateway, subnetting basics, home routers, and phone hotspots.

---

## 1. Network Basics

A **computer network** is a collection of connected devices that exchange data and share services/resources.

~~~text
                 Internet
                    |
                ISP / ONT
                    |
             Home Wi-Fi Router
              /      |       \
             /       |        \
          Laptop    Phone      TV
       192.168.1.10 .11       .12
~~~

Useful vocabulary:

- **Host** — a device/system participating in network communication.
- **Client** — requests a service.
- **Server** — provides a service.
- **Protocol** — rules that define communication.
- **Port** — logical transport-layer endpoint for a service.
- **MAC address** — Layer 2 address associated with a network interface.
- **IP address** — Layer 3 logical address.

Example:

~~~text
192.168.1.10:22 -> SSH service
192.168.1.10:80 -> HTTP service
~~~

---

## 2. OSI Model

The OSI model is a conceptual seven-layer model:

| Layer | Name | Common examples |
|---:|---|---|
| 7 | Application | HTTP, DNS, SMTP, FTP |
| 6 | Presentation | Data representation, encryption concepts |
| 5 | Session | Session management |
| 4 | Transport | TCP, UDP, ports |
| 3 | Network | IP, routing |
| 2 | Data Link | Ethernet, Wi-Fi, MAC |
| 1 | Physical | Cable, radio, optical/electrical signaling |

For beginner networking, the most useful mental map is:

~~~text
L7 -> Application -> DNS / HTTP / SMTP
L4 -> Transport  -> TCP / UDP / ports
L3 -> Network    -> IP / routing
L2 -> Data Link  -> Ethernet / Wi-Fi / MAC
L1 -> Physical   -> cable / radio / signal
~~~

Key memory:

~~~text
Switch -> primarily Layer 2 -> MAC
Router -> primarily Layer 3 -> IP
~~~

Real devices can provide functions at several layers; OSI is a conceptual model.

---

## 3. Network Types

### PAN — Personal Area Network

Small personal network.

~~~text
Phone <-> Bluetooth earbuds
~~~

### LAN — Local Area Network

A local network in a home, room, office, building, etc.

### WLAN — Wireless LAN

A LAN using wireless technology such as Wi-Fi.

~~~text
WLAN is a type of LAN
~~~

### CAN — Campus Area Network

Connects multiple nearby networks across a campus, such as a university.

### MAN — Metropolitan Area Network

Covers a city/metropolitan area.

### WAN — Wide Area Network

Connects networks across large geographic areas.

### VPN — Virtual Private Network

A VPN is a logical/private connection or tunnel over another network. It is not primarily a geographic category.

Mnemonic:

~~~text
PAN -> Person
LAN -> Local
CAN -> Campus
MAN -> Metropolitan
WAN -> Wide
~~~

---

## 4. Networking Devices

### Hub

- Layer 1
- Repeats incoming signals
- Does not make forwarding decisions using MAC addresses
- Mostly obsolete in modern switched LANs

~~~text
PC1 --\
PC2 --- HUB --- PC3
PC4 --/
~~~

### Switch

- Primarily Layer 2
- Uses MAC addresses
- Forwards Ethernet frames
- Learns which MAC addresses are reachable through which ports

~~~text
PC1 --\
PC2 --- Switch --- Server
PC3 --/
~~~

Memory:

~~~text
Switch -> MAC -> Ethernet frame
~~~

Some Layer 3 switches can also route IP traffic.

### Router

- Primarily Layer 3
- Connects different IP networks
- Uses routing information
- Commonly acts as the default gateway

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

### Access Point (AP)

Provides wireless access and normally bridges Wi-Fi clients into a LAN.

### Bridge

Connects Layer 2 network segments. A modern switch is essentially an advanced multi-port bridge.

### Repeater

Regenerates/repeats signals, primarily at the physical layer.

### Modem

Terminates/provides the ISP access technology. Modern broadband devices often combine modem/router functions.

### ONT

Optical Network Terminal, commonly used with fiber.

~~~text
Fiber -> ONT -> Ethernet -> Router
~~~

### Gateway

A gateway is a device/function that provides access from one network to another. In a typical LAN, the router's LAN IP can be the client's default gateway.

### DHCP/DNS server

DHCP and DNS are **services**, not necessarily separate physical devices. A home router commonly provides both.

### Firewall

Controls traffic according to rules and may allow, block, log, or inspect traffic depending on its type/configuration.

---

## 5. Ethernet and Wi-Fi

### Ethernet

Ethernet is a family of networking technologies covering physical and data-link behavior. Traditional Ethernet commonly uses network cables.

Ethernet frames include information such as:

- Source MAC
- Destination MAC
- Payload
- Frame error-detection information

### Wi-Fi

Wi-Fi provides wireless LAN connectivity using radio.

Both Ethernet and Wi-Fi can carry IP packets and use MAC addressing at Layer 2.

~~~text
Ethernet -> usually wired
Wi-Fi    -> wireless
~~~

### Important Windows detail

An operating system may call a virtual adapter **Ethernet** even when no physical cable is connected.

For example, virtualization software can create a virtual Ethernet adapter.

~~~text
VirtualBox
   |
   +-> Virtual Ethernet adapter
~~~

Therefore:

~~~text
"Ethernet" interface name != proof of a physical cable
~~~

---

## 6. MAC Address and Ethernet Broadcast

A MAC address is a Layer 2 address associated with a network interface.

Example:

~~~text
AA:BB:CC:11:22:33
~~~

The special Ethernet destination:

~~~text
FF:FF:FF:FF:FF:FF
~~~

is the **broadcast MAC address**.

It means:

~~~text
Send the Ethernet frame to all devices in the local
Layer 2 broadcast domain
~~~

Why?

~~~text
FF = 11111111
~~~

All 48 bits are 1.

Important distinction:

~~~text
FF:FF:FF:FF:FF:FF -> broadcast destination MAC
ARP                -> protocol used for IPv4 address-to-MAC resolution
~~~

ARP requests commonly use the broadcast MAC, but the broadcast MAC itself is not "the ARP protocol."

---

## 7. IP Addresses

An IP address is a logical Layer 3 address.

Example:

~~~text
192.168.1.10
~~~

IPv4 uses 32 bits and is written as four decimal octets.

A laptop does **not** inherently have a permanent IP.

Its address may be:

- DHCP-assigned
- Static/manual
- Assigned by another network service

The same laptop can have different IPs on different networks:

~~~text
Home Wi-Fi      -> 192.168.1.10
College network -> 10.20.4.57
Phone hotspot   -> 192.168.43.x  (example)
~~~

The network interface's MAC address is separate from its IP configuration.

---

## 8. Private and Public IPv4

Private IPv4 ranges:

~~~text
10.0.0.0       - 10.255.255.255
172.16.0.0     - 172.31.255.255
192.168.0.0    - 192.168.255.255
~~~

Private addresses are intended for internal networks and are not directly routed across the public Internet.

A public IP is generally Internet-routable.

Important:

~~~text
Private != secret
Public  != automatically exposed
~~~

Exposure also depends on routing, firewalls, NAT, service configuration, VPNs, port forwarding, etc.

### Same private IP in different networks

This is valid:

~~~text
Network A                  Network B
Router -> 192.168.1.1     Router -> 192.168.1.1
PC     -> 192.168.1.10     PC     -> 192.168.1.10
~~~

The networks are separate, so their private address spaces can overlap.

**NAT is not the reason this reuse is possible.**

---

## 9. Subnet Mask and Local vs Remote

A subnet mask/prefix tells the host which part of an address represents the network.

Example:

~~~text
IP   = 192.168.1.10
Mask = 255.255.255.0
CIDR = /24
~~~

This commonly represents:

~~~text
192.168.1.0/24
~~~

If the destination is:

~~~text
192.168.1.20
~~~

it is on the same /24 subnet, so local Layer 2 delivery can be used.

If the destination is:

~~~text
8.8.8.8
~~~

it is outside the local subnet, so the host sends the packet to its default gateway.

This local-vs-remote decision is fundamental to understanding routing.

---

## 10. Default Gateway

The **default gateway** is the next-hop device used for destinations outside the local subnet when no more specific route exists.

Example:

~~~text
Laptop:
IP      = 192.168.1.10/24
Gateway = 192.168.1.1
~~~

Same-network:

~~~text
Laptop 192.168.1.10
       |
       v
PC 192.168.1.20
~~~

Remote:

~~~text
Laptop 192.168.1.10
       |
       v
Gateway 192.168.1.1
       |
       v
Other networks / Internet
~~~

### Critical Layer 2 vs Layer 3 distinction

Suppose:

~~~text
Laptop IP     = 192.168.1.10
Router IP     = 192.168.1.1
Remote target = 8.8.8.8
~~~

The outgoing packet can be thought of as:

~~~text
Ethernet destination MAC = router MAC
IP destination           = 8.8.8.8
~~~

The local Ethernet frame is delivered to the **next hop** (the router), while the IP packet is addressed to the **final remote destination**.

Therefore:

~~~text
Layer 2 destination -> next-hop MAC
Layer 3 destination -> final IP
~~~

Also, 192.168.1.1 can simultaneously be:

~~~text
Private IP
Router LAN IP
Default gateway
~~~

These are different roles/properties.

---

## 11. DHCP

**DHCP = Dynamic Host Configuration Protocol**

DHCP automatically provides network configuration to clients.

Typical information:

- IP address
- Subnet mask/prefix
- Default gateway
- DNS server
- Lease information

### DORA

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

DHCP is a **service**, and a home router commonly runs the DHCP server.

Important:

~~~text
DHCP configures IP settings
DHCP does not create/assign the network interface's MAC address
~~~

DHCP can use information such as a client's MAC address for identification/reservations.

---

## 12. ARP

**ARP = Address Resolution Protocol**

For IPv4 local networking, ARP resolves:

~~~text
IPv4 address -> MAC address
~~~

Example:

The laptop knows:

~~~text
Router IP = 192.168.1.1
~~~

but needs the router's MAC.

It sends:

~~~text
ARP Request:
Who has 192.168.1.1?
Tell 192.168.1.10.
~~~

The request is commonly broadcast:

~~~text
Destination MAC = FF:FF:FF:FF:FF:FF
~~~

The router responds with its MAC:

~~~text
192.168.1.1 is at AA:BB:CC:DD:EE:FF
~~~

The laptop can then construct a frame for the router.

### ARP cache

Windows:

~~~powershell
arp -a
~~~

Linux:

~~~bash
ip neigh
~~~

### ARP and remote destinations

If the target is 8.8.8.8, the laptop normally does not ARP for 8.8.8.8 on the local LAN.

It resolves the MAC of the next hop:

~~~text
Default gateway IP -> gateway MAC
~~~

IPv6 does not use ARP; IPv6 uses Neighbor Discovery.

---

## 13. ICMP and Ping

**ICMP = Internet Control Message Protocol**

It is used for network control, diagnostics, and error reporting.

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

### ARP + ICMP

For pinging a local router, a typical sequence is:

~~~text
1. Need router MAC
       |
2. ARP request/reply
       |
3. Send Ethernet frame
       |
4. IP packet carries ICMP Echo Request
       |
5. Receive ICMP Echo Reply
~~~

### Important diagnostic rule

~~~text
Ping failure != guaranteed "no Internet"
~~~

ICMP can be blocked by a firewall or network policy.

---

## 14. NAT and PAT

### NAT

**NAT = Network Address Translation**

NAT translates network addressing at a boundary.

Typical home flow:

~~~text
Private LAN
192.168.1.10
192.168.1.11
192.168.1.12
       |
       v
     Router
       |
      NAT
       |
       v
Public IPv4 address
       |
       v
   Internet
~~~

### PAT / NAPT

A common form translates ports as well as addresses, allowing many internal connections to share one public IPv4 address.

Example:

~~~text
192.168.1.10:50000 -> 49.x.x.x:40001
192.168.1.11:50001 -> 49.x.x.x:40002
192.168.1.12:50002 -> 49.x.x.x:40003
~~~

The router tracks these mappings so response traffic can return to the correct internal host/port.

### NAT is not the same as firewall

~~~text
NAT      -> translates address/port information
Firewall -> controls traffic according to rules
~~~

Home routers commonly use both.

### Port forwarding

Port forwarding can map a public service port to an internal host:

~~~text
Public:   49.x.x.x:8080
             |
             v
Internal: 192.168.1.10:8080
~~~

---

## 15. Home Router

A typical home "Wi-Fi router" is a **multifunction device** rather than only a router.

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

Typical network:

~~~text
Internet
   |
ISP / ONT / Modem
   |
Home Wi-Fi Router
  /        |        \
Laptop    Phone      TV
~~~

So when we say "the router gave the laptop an IP," more precisely the router's **DHCP service** provided the IP configuration.

---

## 16. Phone Hotspot

A smartphone hotspot behaves like a small gateway/router.

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

- Private IP
- Subnet configuration
- Default gateway
- DNS information
- Wi-Fi access
- NAT toward the mobile network

Traffic path:

~~~text
Laptop -> Phone hotspot -> Mobile carrier -> Internet
~~~

The exact private IP range depends on the device/software.

---

## 17. End-to-End: Opening an HTTPS Website

Assume:

~~~text
Laptop       = 192.168.1.10/24
Gateway      = 192.168.1.1
DNS resolver = 192.168.1.1
Site         = example.com
~~~

### Step 1 — DHCP

The laptop receives IP, subnet, gateway, DNS and lease information.

### Step 2 — DNS

~~~text
example.com -> DNS -> destination IP
~~~

### Step 3 — Local/remote decision

The site IP is outside the laptop's local subnet.

### Step 4 — ARP

~~~text
192.168.1.1 -> router MAC
~~~

### Step 5 — Local frame

~~~text
Ethernet/Wi-Fi destination MAC = router MAC
IP destination                  = website IP
~~~

### Step 6 — Router

The router routes the packet and may perform NAT/PAT.

### Step 7 — Transport and security

For a normal HTTPS connection:

~~~text
TCP -> transport
TLS -> encryption/authentication
HTTP -> application protocol
~~~

### Step 8 — Response

The response returns through the network; the router can reverse NAT/PAT state and deliver it to the laptop.

### One-line memory

~~~text
DHCP -> DNS -> subnet decision -> ARP -> frame -> router -> NAT -> Internet
~~~

---

## 18. Troubleshooting Model

When Internet access fails, do not immediately assume DNS is the problem.

Work through the layers:

### 1. Link/interface

Check Wi-Fi, Ethernet, virtual adapters, and interface state.

### 2. IP configuration

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

### 3. Gateway

~~~bash
ping 192.168.1.1
~~~

Interpret carefully because ICMP may be blocked.

### 4. Routing

Windows:

~~~powershell
route print
~~~

Linux:

~~~bash
ip route
~~~

### 5. IP connectivity

~~~bash
ping 8.8.8.8
~~~

Again, ping is not absolute proof.

### 6. DNS

~~~bash
nslookup example.com
~~~

or:

~~~bash
dig example.com
~~~

### Important scenario

If:

~~~text
ping 192.168.1.20 -> works
ping 8.8.8.8      -> fails
~~~

Do not start with DNS. 8.8.8.8 is already an IP.

Investigate:

- Default gateway
- Routing
- Upstream connectivity
- Firewall/policy

If:

~~~text
ping 8.8.8.8          -> works
nslookup example.com  -> fails
~~~

DNS becomes a strong suspect.

---

## 19. High-Value Confusions to Avoid

### DHCP vs MAC

Wrong:

~~~text
DHCP gives the laptop its MAC address
~~~

Correct:

~~~text
MAC -> identifies the network interface
DHCP -> configures IP-layer network settings
~~~

### Switch vs Router

~~~text
Switch -> primarily MAC / Layer 2
Router -> primarily IP / Layer 3
~~~

### IP vs MAC

~~~text
IP  -> Layer 3 logical address
MAC -> Layer 2 interface address
~~~

### Broadcast MAC vs ARP

~~~text
FF:FF:FF:FF:FF:FF -> Ethernet broadcast destination
ARP -> IPv4-to-MAC resolution
~~~

### NAT vs private-IP reuse

Separate private networks can both use 192.168.1.10.

NAT is not what makes that possible.

### Default Gateway vs DNS

~~~text
Default gateway -> next hop for remote destinations
DNS             -> name resolution / DNS records
~~~

### Ping vs Internet

~~~text
Ping -> commonly ICMP Echo
Ping failure -> not always "Internet is down"
~~~

### Ethernet vs physical cable

~~~text
Ethernet interface name -> can be virtual
~~~

### Port vs protocol

Using a Telnet client to connect to port 80 does not mean port 80 is a Telnet service. It only means Telnet is being used as a TCP client.

---

## 20. Quick Mental Map

~~~text
MAC
 -> Layer 2
 -> local interface addressing

IP
 -> Layer 3
 -> logical network addressing

Switch
 -> MAC
 -> Ethernet frames

Router
 -> IP
 -> routing

Subnet mask
 -> local vs remote decision

Default gateway
 -> next hop for remote networks

DHCP
 -> automatic IP configuration

ARP
 -> IPv4 address -> MAC

FF:FF:FF:FF:FF:FF
 -> Layer 2 broadcast

ICMP
 -> control / diagnostics / ping

NAT
 -> address translation

PAT/NAPT
 -> address + port translation

Home router
 -> router + switch + AP + DHCP + NAT + firewall (commonly)

Phone hotspot
 -> AP + DHCP + gateway + NAT (commonly)
~~~

---

## 21. Core Commands for Basic Networking

### Windows

~~~powershell
ipconfig /all
arp -a
route print
ping 8.8.8.8
nslookup example.com
~~~

### Linux

~~~bash
ip addr
ip route
ip neigh
ping 8.8.8.8
nslookup example.com
dig example.com
~~~

### Wireshark filters

~~~text
arp
icmp
dns
tcp.port == 80
ip.addr == 192.168.1.10
~~~

---

# Networking & Cybersecurity Fundamentals - Study Notes

> **Topic covered:** DNS, WHOIS, HTTP/HTTPS, Telnet, TLS/SSL, FTP, SMTP, POP3, IMAP, cleartext vs secure ports, and common cybersecurity terms.
>
> These notes are structured for GitHub and quick revision. Commands should be used only on systems you own or are authorized to test.

---

## Table of Contents

1. [Core Network Concepts](#1-core-network-concepts)
2. [DNS: nslookup](#2-dns-nslookup)
3. [DNS: dig](#3-dns-dig)
4. [WHOIS](#4-whois)
5. [HTTP, HTTPS, and Telnet](#5-http-https-and-telnet)
6. [TLS and SSL](#6-tls-and-ssl)
7. [FTP](#7-ftp)
8. [SMTP](#8-smtp)
9. [POP3 and IMAP](#9-pop3-and-imap)
10. [Cleartext vs Secure Ports](#10-cleartext-vs-secure-ports)
11. [Sniffing, Spoofing, Scanning, and More](#11-sniffing-spoofing-scanning-and-more)
12. [Port Cheat Sheet](#12-port-cheat-sheet)
13. [Practical Command Cheat Sheet](#13-practical-command-cheat-sheet)
14. [Big Picture](#14-big-picture)
15. [SOC Level 1 Takeaways](#15-soc-level-1-takeaways)

---

# 1. Core Network Concepts

A **protocol** is a set of rules that devices use to communicate.

A **port** identifies a network service/application endpoint on a host.

A simplified model is:

```text
Application
    |
    |  HTTP / DNS / SMTP / FTP / SSH
    v
Transport
    |
    |  TCP / UDP
    v
Internet
    |
    |  IP
    v
Network Access
    |
    |  Ethernet / Wi-Fi
    v
Physical network
```

### TCP vs UDP

**TCP**
- Connection-oriented
- Reliable
- Ordered delivery
- Used by many common services such as HTTP/HTTPS, SSH, FTP, SMTP, IMAP, and POP3.

**UDP**
- Connectionless
- Lower overhead
- Does not provide TCP-style delivery guarantees
- Commonly used by services such as DNS.

---

# 2. DNS: `nslookup`

## What is DNS?

**DNS (Domain Name System)** translates human-readable domain names into IP addresses and can also store other DNS records.

```text
example.com
     |
     v
DNS
     |
     v
93.184.216.34
```

## What is `nslookup`?

`nslookup` = **Name Server Lookup**.

It is a command-line utility used to query DNS.

### Basic lookup

```bash
nslookup example.com
```

Typical concepts in the output:

```text
Server:     192.168.1.1
Address:    192.168.1.1#53

Name:       example.com
Address:    93.184.216.34
```

- **Server** = DNS resolver queried by your system.
- **#53** = DNS service port.
- **Name** = domain requested.
- **Address** = IP returned.

### IPv4 / A record

```bash
nslookup -query=A example.com
```

### IPv6 / AAAA record

```bash
nslookup -query=AAAA example.com
```

### Reverse DNS

```bash
nslookup 8.8.8.8
```

This may perform a PTR lookup:

```text
IP -> hostname
```

### Mail servers / MX

```bash
nslookup -type=MX example.com
```

### Name servers / NS

```bash
nslookup -type=NS example.com
```

### TXT records

```bash
nslookup -type=TXT example.com
```

### CNAME

```bash
nslookup -type=CNAME www.example.com
```

### Use a particular DNS server

```bash
nslookup example.com 8.8.8.8
```

---

# 3. DNS: `dig`

## What is `dig`?

`dig` = **Domain Information Groper**.

It is a more detailed and flexible DNS troubleshooting/investigation tool than `nslookup`.

### Basic query

```bash
dig example.com
```

Important sections:

```text
QUESTION SECTION
ANSWER SECTION
AUTHORITY SECTION
ADDITIONAL SECTION
```

A typical A record answer looks like:

```text
example.com.  300  IN  A  93.184.216.34
```

Meaning:

- `example.com` = domain
- `300` = TTL in seconds
- `IN` = Internet class
- `A` = IPv4 record
- `93.184.216.34` = answer

## Useful `dig` commands

### Only return the answer

```bash
dig example.com +short
```

### A record

```bash
dig example.com A
```

### AAAA record

```bash
dig example.com AAAA
```

### MX

```bash
dig example.com MX
```

### NS

```bash
dig example.com NS
```

### TXT

```bash
dig example.com TXT
```

### CNAME

```bash
dig www.example.com CNAME
```

### Reverse DNS

```bash
dig -x 8.8.8.8
```

### Use a specific DNS resolver

```bash
dig @8.8.8.8 example.com
```

Cloudflare DNS:

```bash
dig @1.1.1.1 example.com
```

### Trace the DNS resolution path

```bash
dig example.com +trace
```

Conceptually:

```text
Root DNS
   |
   v
TLD DNS (.com)
   |
   v
Authoritative DNS
   |
   v
Final DNS answer
```

### DNSSEC-related query

```bash
dig example.com +dnssec
dig example.com DNSKEY
```

## `nslookup` vs `dig`

| Feature | `nslookup` | `dig` |
|---|---|---|
| Simple DNS lookup | Yes | Yes |
| Detailed response | Basic | Excellent |
| `+short` | No | Yes |
| `+trace` | No | Yes |
| Troubleshooting | Good | Excellent |
| Security investigations | Good | Very useful |

**Memory:**

```text
nslookup -> quick DNS lookup
dig      -> detailed DNS investigation
```

---

# 4. WHOIS

## What is WHOIS?

`whois` is used to retrieve available **domain registration information** and, for IP addresses, information about the network/organization associated with an allocation.

### Domain lookup

```bash
whois example.com
```

Fields may include:

- Domain name
- Registrar
- Creation date
- Updated date
- Expiration date
- Name servers
- Domain status

### IP lookup

```bash
whois 8.8.8.8
```

This can provide network/registration information associated with the IP allocation.

## WHOIS vs DNS

```text
WHOIS
  |
  v
Registration / allocation information

DNS
  |
  v
Domain -> IP, mail servers, name servers, TXT, etc.
```

### Domain age

A useful investigation field is:

```text
Creation Date
```

A recently registered suspicious domain can be a useful indicator, but:

```text
new domain != malicious
old domain != trustworthy
```

WHOIS data may be redacted or privacy-protected.

---

# 5. HTTP, HTTPS, and Telnet

# HTTP

**HTTP = Hypertext Transfer Protocol**

Used for web communication.

Default port:

```text
TCP 80
```

Simplified flow:

```text
Browser / Client
      |
      | HTTP request
      v
Web Server
      |
      | HTTP response
      v
Browser / Client
```

Example:

```bash
curl http://example.com
```

HTTP traffic is generally **cleartext** at the application layer when no encryption is used.

---

# HTTPS

**HTTPS = HTTP over TLS**

```text
HTTPS = HTTP + TLS
```

Default port:

```text
TCP 443
```

Example:

```bash
curl https://example.com
```

HTTPS protects data in transit using TLS.

Important:

```text
HTTPS != "the website is trustworthy"
```

HTTPS protects the connection; it does not make a malicious website legitimate.

---

# Telnet

**Telnet** is an old protocol for remote terminal access.

Default port:

```text
TCP 23
```

Example:

```bash
telnet 192.168.1.10 23
```

Telnet is **unencrypted/cleartext** and is therefore unsuitable for secure remote administration.

The secure modern alternative is:

```text
SSH -> TCP 22
```

### Telnet as a port test

Telnet can also be used to test whether a TCP service is reachable:

```bash
telnet 192.168.1.10 80
```

This does not mean the service on port 80 is Telnet; it only means Telnet is being used as a TCP client.

---

# 6. TLS and SSL

## SSL

**SSL = Secure Sockets Layer**

SSL is the older protocol family. Modern SSL versions are obsolete and insecure.

Do not use:

- SSL 2.0
- SSL 3.0

## TLS

**TLS = Transport Layer Security**

TLS replaced SSL and is the modern security protocol used by HTTPS and many other applications.

Important versions:

```text
SSL 2.0  -> obsolete
SSL 3.0  -> obsolete
TLS 1.0  -> obsolete
TLS 1.1  -> obsolete
TLS 1.2  -> widely supported
TLS 1.3  -> modern
```

## What TLS provides

### 1. Confidentiality

Encrypts data in transit.

```text
Readable data
    |
    v
TLS encryption
    |
    v
Ciphertext
```

### 2. Integrity

Helps detect unauthorized modification of protected data in transit.

### 3. Authentication

Certificates help the client authenticate the server.

---

## TLS certificates

A digital certificate can contain:

- Domain name
- Public key
- Certificate authority
- Validity period
- Digital signature

Simplified:

```text
Website
   |
   | presents certificate
   v
Browser
   |
   | verifies chain / hostname / validity
   v
TLS connection
```

## Certificate Authorities

Examples include:

- DigiCert
- Let's Encrypt
- GlobalSign

Browsers and operating systems maintain trusted CA roots.

---

## TLS handshake

A simplified concept:

```text
Client                         Server
  |                              |
  |------ ClientHello ---------->|
  |<----- ServerHello -----------|
  |<----- Certificate -----------|
  |------ Key exchange --------->|
  |                              |
  |==== Encrypted traffic =======|
```

Modern TLS 1.3 has a more efficient handshake than older versions.

## Public-key vs symmetric cryptography

TLS uses cryptographic mechanisms with different jobs:

```text
Authentication / key establishment
             |
             v
      Shared secret/key
             |
             v
Fast symmetric encryption
             |
             v
   Application data
```

## Inspect TLS from Kali

```bash
curl -v https://example.com
```

Or:

```bash
openssl s_client -connect example.com:443
```

TLS 1.2:

```bash
openssl s_client -connect example.com:443 -tls1_2
```

TLS 1.3:

```bash
openssl s_client -connect example.com:443 -tls1_3
```

---

# 7. FTP

## What is FTP?

**FTP = File Transfer Protocol**

Used to transfer files between a client and server.

```text
Client
  |
  | upload / download
  v
FTP Server
```

FTP normally uses TCP.

Traditional FTP ports:

```text
TCP 21 -> control connection
TCP 20 -> data connection in traditional active mode
```

The most important port to remember:

```text
FTP -> 21
```

## Two FTP connections

### Control connection

```text
Client ---- TCP 21 ----> Server
```

Used for commands such as:

```text
USER
PASS
LIST
RETR
STOR
QUIT
```

### Data connection

Used for:

- Directory listings
- File uploads
- File downloads

The exact data-port behavior depends on active vs passive FTP.

## FTP security

Traditional FTP does **not provide encryption**.

Credentials and file contents can potentially be exposed to a network observer.

---

## FTP vs FTPS vs SFTP

```text
FTP
  -> traditional FTP
  -> no built-in encryption

FTPS
  -> FTP protected with TLS

SFTP
  -> SSH File Transfer Protocol
  -> runs over SSH
  -> not the same protocol as FTP
```

Common ports:

```text
FTP  -> 21
FTPS -> commonly 990 for implicit TLS FTP
SFTP -> 22 (via SSH)
```

## FTP client

```bash
ftp 192.168.56.10
```

Common FTP commands:

```text
ls
dir
cd <directory>
get <file>
put <file>
mget <pattern>
mput <pattern>
bye
quit
```

## Anonymous FTP

Some servers intentionally permit:

```text
Username: anonymous
```

Anonymous access should be reviewed during authorized security assessments because accidental exposure of files can create security risk.

## Nmap FTP checks in an authorized lab

```bash
nmap -sV -p 21 192.168.56.10
```

Anonymous FTP check:

```bash
nmap --script ftp-anon -p 21 192.168.56.10
```

---

# 8. SMTP

## What is SMTP?

**SMTP = Simple Mail Transfer Protocol**

SMTP is primarily used to **send/transfer outgoing email**.

```text
Email client
      |
      | SMTP
      v
Sender mail server
      |
      | SMTP
      v
Recipient mail server
```

## Common SMTP ports

| Port | Typical purpose |
|---:|---|
| 25 | SMTP server-to-server transfer |
| 587 | Message submission; STARTTLS commonly used |
| 465 | SMTP over implicit TLS |

## SMTP commands

You may see commands such as:

```text
EHLO
MAIL FROM
RCPT TO
DATA
QUIT
```

Simplified:

```text
Client -> EHLO
Server -> 250 ...

Client -> MAIL FROM:<sender@example.com>
Client -> RCPT TO:<recipient@example.com>
Client -> DATA
Client -> message body
Client -> .
```

## SMTP and TLS

SMTP can use TLS to protect connections.

```text
SMTP
  |
  +--> STARTTLS (commonly on 587)
  |
  +--> implicit TLS (commonly 465)
```

## Email security: SPF, DKIM, DMARC

### SPF

**Sender Policy Framework**

A domain can publish which mail systems are authorized to send for it.

Check TXT records:

```bash
dig example.com TXT
```

### DKIM

**DomainKeys Identified Mail**

Adds a cryptographic signature to email so the receiving system can verify the signature using a public key published in DNS.

### DMARC

**Domain-based Message Authentication, Reporting & Conformance**

Defines handling/reporting policies for email that fails authentication checks.

Typical DMARC record:

```bash
dig _dmarc.example.com TXT
```

---

# 9. POP3 and IMAP

Both are email protocols used to **retrieve/access email from a mail server**.

```text
SMTP -> send
POP3 / IMAP -> receive or access
```

# POP3

**POP3 = Post Office Protocol version 3**

POP3 is primarily designed to **download mail** from the server to the client.

Common ports:

```text
POP3       -> TCP 110
POP3 + TLS -> TCP 995
```

Traditional POP3 workflows may remove mail from the server after download, depending on client settings.

---

# IMAP

**IMAP = Internet Message Access Protocol**

IMAP is designed for **server-side mailbox access and synchronization**.

Common ports:

```text
IMAP       -> TCP 143
IMAP + TLS -> TCP 993
```

IMAP is especially useful when the same mailbox is accessed from several devices.

Example:

```text
             Mail Server
           /      |      \
        Laptop   Phone   Tablet
```

Read/unread state and folders can remain synchronized through the server.

---

## POP3 vs IMAP

| Feature | POP3 | IMAP |
|---|---|---|
| Full name | Post Office Protocol v3 | Internet Message Access Protocol |
| Default port | 110 | 143 |
| TLS port | 995 | 993 |
| Main idea | Download | Access/synchronize |
| Server-side mailbox model | Limited | Strong |
| Multiple devices | Less suitable | Excellent |
| Folder synchronization | Limited | Yes |
| Read/unread synchronization | Limited | Yes |

### Memory

```text
SMTP -> Send
POP3 -> Pull/download
IMAP -> Internet mailbox synchronization
```

---

# 10. Cleartext vs Secure Ports

## Cleartext

A cleartext application protocol does not provide encryption for the protocol data.

Common examples:

```text
FTP   -> 21
SMTP  -> 25
HTTP  -> 80
Telnet -> 23
POP3  -> 110
IMAP  -> 143
```

## Secure / encrypted counterparts

```text
FTPS       -> 990 (common implicit-TLS port)
SMTP/TLS   -> 465
Submission -> 587 (STARTTLS commonly used)
HTTPS      -> 443
POP3S      -> 995
IMAPS      -> 993
SSH        -> 22
```

### Important nuance

A port number alone does not guarantee encryption.

Security depends on:

- The protocol
- How the service is configured
- Whether TLS/SSH is actually negotiated
- Which version/cipher suite is used

---

## Cleartext / Secure matching used in the study quiz

```text
CLEAR
21  -> FTP
25  -> SMTP
80  -> HTTP
23  -> Telnet
110 -> POP3
143 -> IMAP

SECURE
990 -> FTPS
465 -> SMTP over TLS
587 -> SMTP submission / STARTTLS
443 -> HTTPS
995 -> POP3S
993 -> IMAPS
22  -> SSH
```

Quick mapping:

| Cleartext service | Secure counterpart |
|---|---|
| FTP (21) | FTPS (commonly 990) / SFTP (22, separate protocol) |
| SMTP (25) | TLS-protected SMTP (465/587, depending on mode) |
| HTTP (80) | HTTPS (443) |
| Telnet (23) | SSH (22) |
| POP3 (110) | POP3S (995) |
| IMAP (143) | IMAPS (993) |

---

# 11. Sniffing, Spoofing, Scanning, and More

These terms are easy to confuse.

# Sniffing

**Sniffing = capturing/observing network traffic.**

Tools include:

- Wireshark
- tcpdump
- tshark

Example:

```bash
sudo tcpdump -i eth0
```

A packet capture can show:

- Source IP
- Destination IP
- Protocol
- Ports
- Packet metadata
- Payload when it is visible / not encrypted

Important:

```text
Cleartext traffic -> contents may be readable
Encrypted traffic -> payload is protected from simple inspection
```

---

# Spoofing

**Spoofing = pretending to be another entity.**

Examples:

### IP spoofing

Making a packet appear to come from another source IP.

### MAC spoofing

Changing a device's MAC address to another value.

### Email spoofing

Making an email appear to come from a different sender.

Memory:

```text
Sniffing -> listen/capture
Spoofing -> pretend
```

---

# Scanning

**Scanning = discovering systems, ports, or services.**

Example:

```bash
nmap 192.168.1.10
```

A scan may find:

```text
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https
```

Memory:

```text
Scanning -> "What is there?"
```

---

# Enumeration

**Enumeration = gathering more detailed information from discovered services.**

Example:

```text
Scanning:
445/tcp open

Enumeration:
SMB version?
Shares?
Users?
Accessible resources?
```

Memory:

```text
Scanning   -> discover
Enumeration -> collect details
```

---

# Eavesdropping

**Eavesdropping = secretly listening to communication.**

It is a broad concept. Network sniffing can be one way to eavesdrop on network communications.

---

# Man-in-the-Middle (MITM)

A MITM situation places an attacker between two communicating parties.

Normal:

```text
Client <----------------> Server
```

MITM:

```text
Client <------> Attacker <------> Server
```

Potential goals include:

- Observe traffic
- Modify traffic
- Redirect communication
- Attempt credential theft

Strong encryption plus proper endpoint/certificate authentication helps defend against MITM attacks.

---

# Phishing

**Phishing = social engineering that tricks a user into clicking, opening, sending, or disclosing something.**

Example:

```text
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
```

---

# Pharming

**Pharming = redirecting a victim to a fraudulent destination, often through DNS/host/network manipulation.**

Conceptually:

```text
User enters legitimate domain
          |
          v
Traffic is redirected
          |
          v
Fraudulent site
```

Phishing primarily uses deception/social engineering; pharming focuses on redirection/manipulation.

---

# DoS and DDoS

### DoS

**Denial of Service**

Attempt to make a service unavailable by consuming or exhausting resources.

### DDoS

**Distributed Denial of Service**

Same general objective, but traffic comes from multiple systems.

```text
Host 1 --\
Host 2 ---\
Host 3 ----> Target
Host 4 ---/
```

---

# Brute Force

**Brute force = repeatedly trying credentials/passwords until a valid one is found.**

Conceptually:

```text
password1 -> wrong
password2 -> wrong
password3 -> wrong
password4 -> correct
```

Defenses include:

- MFA
- Strong passwords
- Rate limiting
- Account lockout / throttling
- Monitoring failed authentication

---

# Credential Stuffing

Uses **previously leaked username/password combinations** against another service.

```text
Leaked credentials
       |
       v
Try same username/password elsewhere
```

This works particularly well when users reuse passwords.

---

# Password Spraying

Instead of trying many passwords against one account, an attacker tries one or a few common passwords against many accounts.

```text
user1 -> Password123
user2 -> Password123
user3 -> Password123
user4 -> Password123
```

This may reduce account-lockout triggers compared with repeatedly attacking a single account.

---

## Comparison

| Term | Core idea |
|---|---|
| Sniffing | Capture traffic |
| Spoofing | Pretend to be another entity |
| Scanning | Discover hosts/ports/services |
| Enumeration | Gather detailed service information |
| Eavesdropping | Secretly listen to communication |
| MITM | Intercept communication between parties |
| Phishing | Trick the user |
| Pharming | Redirect to a fraudulent destination |
| DoS | Disrupt availability |
| DDoS | Distributed DoS |
| Brute force | Repeated credential guessing |
| Credential stuffing | Reuse leaked credentials |
| Password spraying | Few common passwords across many accounts |

---

# 12. Port Cheat Sheet

## Core ports from these topics

| Port | Protocol / Service | Typical security note |
|---:|---|---|
| 20 | FTP data (traditional active mode) | Cleartext FTP |
| 21 | FTP control | Cleartext FTP |
| 22 | SSH / SFTP | Encrypted |
| 23 | Telnet | Cleartext |
| 25 | SMTP | Usually server-to-server SMTP; TLS may be negotiated |
| 53 | DNS | Classic DNS is not encrypted by default |
| 80 | HTTP | Cleartext |
| 110 | POP3 | Cleartext |
| 143 | IMAP | Cleartext |
| 443 | HTTPS | TLS-protected HTTP |
| 465 | SMTP over implicit TLS | Encrypted |
| 587 | SMTP submission | STARTTLS commonly used |
| 990 | FTPS | Common implicit TLS FTP port |
| 993 | IMAPS | TLS-protected IMAP |
| 995 | POP3S | TLS-protected POP3 |

### Important distinction

```text
22 = SSH
SFTP = file transfer over SSH
```

Do not describe port 22 as "secure FTP". SFTP is a **separate protocol**.

---

# 13. Practical Command Cheat Sheet

## DNS

```bash
nslookup example.com
nslookup -type=MX example.com
nslookup -type=NS example.com
```

```bash
dig example.com
dig example.com +short
dig example.com MX +short
dig example.com NS +short
dig example.com TXT +short
dig -x 8.8.8.8 +short
dig @8.8.8.8 example.com
dig example.com +trace
```

## WHOIS

```bash
whois example.com
whois 8.8.8.8
```

## HTTP / HTTPS

```bash
curl http://example.com
curl https://example.com
curl -I https://example.com
curl -v https://example.com
curl -L https://example.com
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
```

### Download

```bash
curl -O https://example.com/file.zip
curl -o output.zip https://example.com/file.zip
```

### Custom header

```bash
curl -H "User-Agent: TestClient" https://example.com
```

### POST

```bash
curl -X POST -d "username=test" https://example.com/login
```

### JSON POST

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"test"}' \
  https://example.com/api
```

## TLS

```bash
openssl s_client -connect example.com:443
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -connect example.com:443 -tls1_3
```

## FTP

```bash
ftp 192.168.56.10
```

## Telnet / TCP connectivity test

```bash
telnet 192.168.1.10 23
telnet 192.168.1.10 80
```

---

# 14. Big Picture

The tools and protocols fit together like this:

```text
                         NETWORK INVESTIGATION
                                  |
         +------------------------+------------------------+
         |                        |                        |
         v                        v                        v
       DNS                    Registration               Web
         |                        |                        |
    nslookup / dig              whois                curl / browser
         |                        |                        |
         v                        v                        v
  IP / MX / NS / TXT       Domain/IP info         HTTP / HTTPS
         |
         v
   Network service
         |
         +-------------------+
         |                   |
         v                   v
       Cleartext            Encrypted
         |                   |
     HTTP / FTP /       HTTPS / SSH /
     Telnet / etc.      TLS-protected email
```

---

# 15. SOC Level 1 Takeaways

A SOC analyst should be able to recognize these patterns quickly.

## If you see port 80

```text
80 -> HTTP -> cleartext web
```

Investigate the request/response and whether sensitive information is being transmitted without encryption.

## If you see port 443

```text
443 -> HTTPS -> TLS-protected web
```

For deeper investigation, inspect TLS metadata, certificate details, destination reputation, and application behavior.

## If you see port 23

```text
23 -> Telnet -> cleartext remote terminal
```

This is generally a security concern on modern networks.

## If you see port 22

```text
22 -> SSH
```

Usually encrypted remote administration.

## If you see port 21

```text
21 -> FTP control
```

Check whether plain FTP is exposing credentials/data and whether secure alternatives are available.

## If you see ports 110 / 143

```text
110 -> POP3
143 -> IMAP
```

Investigate whether encrypted alternatives are being used:

```text
995 -> POP3S
993 -> IMAPS
```

## If you see SMTP ports

```text
25  -> SMTP
465 -> SMTP over TLS
587 -> submission / STARTTLS commonly
```

In a SOC, email security also means understanding:

```text
SPF + DKIM + DMARC
```

---

# Final Memory Map

```text
DNS
 |
 +-- nslookup -> simple DNS lookup
 +-- dig      -> detailed DNS lookup
 +-- 53       -> DNS

WHOIS
 |
 +-- domain registration information
 +-- IP/network allocation information

WEB
 |
 +-- HTTP  -> 80  -> cleartext
 +-- HTTPS -> 443 -> TLS

REMOTE TERMINAL
 |
 +-- Telnet -> 23 -> cleartext
 +-- SSH    -> 22 -> encrypted

FILE TRANSFER
 |
 +-- FTP  -> 21 -> cleartext
 +-- FTPS -> 990 (common) -> TLS
 +-- SFTP -> 22 -> SSH-based, separate protocol

EMAIL
 |
 +-- SMTP -> 25 / 465 / 587 -> send/submit
 +-- POP3 -> 110 / 995      -> download
 +-- IMAP -> 143 / 993      -> access/synchronize

SECURITY TERMS
 |
 +-- Sniffing       -> capture traffic
 +-- Spoofing       -> impersonate
 +-- Scanning       -> discover
 +-- Enumeration    -> gather details
 +-- MITM           -> intercept
 +-- Phishing       -> trick users
 +-- Pharming       -> redirect
 +-- DoS/DDoS       -> disrupt availability
 +-- Brute force    -> repeated guessing
 +-- Credential stuffing -> leaked credentials
 +-- Password spraying   -> common password across accounts
```

---

## Quick Revision Questions

1. What is the difference between `nslookup` and `dig`?
2. What does a WHOIS query tell you?
3. What is the difference between HTTP and HTTPS?
4. Why is Telnet insecure?
5. What does TLS provide?
6. What is the difference between SSL and TLS?
7. What are FTP's control and data connections?
8. What is the difference between FTP, FTPS, and SFTP?
9. Which protocol is mainly used to send email?
10. What is the difference between POP3 and IMAP?
11. What is the difference between cleartext and encrypted traffic?
12. What is sniffing?
13. What is spoofing?
14. What is scanning vs enumeration?
15. What is a MITM attack?
16. What is phishing vs pharming?
17. What is the difference between brute force, credential stuffing, and password spraying?
18. What do ports 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, and 990 represent?

---

> **Safety note:** Use reconnaissance, packet capture, service probing, and authentication testing only against your own systems, CTF/TryHackMe labs, or systems where you have explicit permission.
