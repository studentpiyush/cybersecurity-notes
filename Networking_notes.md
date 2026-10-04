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
