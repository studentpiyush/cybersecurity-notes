# Nmap Learning Notes

> Beginner-to-intermediate notes based on hands-on Nmap practice.

## 1. What is Nmap?

**Nmap (Network Mapper)** is a network discovery and security auditing tool.

It can be used to:
- Discover hosts
- Scan TCP and UDP ports
- Identify services and versions
- Attempt OS fingerprinting
- Analyze firewall filtering
- Run NSE scripts
- Perform traceroute
- Save scan results for later analysis

---

# 2. Nmap Mental Model

A useful way to understand Nmap is:

```text
Target
  ↓
Host Discovery
  ↓
Port Scanning
  ↓
Port State
  ↓
Service / Version Detection
  ↓
OS Detection
  ↓
NSE / Additional Enumeration
  ↓
Output / Reporting
```

Important distinction:

```text
-Pn  → controls host discovery behavior
-sS  → controls TCP port-scanning technique
-sU  → controls UDP port-scanning technique
-sA  → performs TCP ACK/filtering analysis
```

---

# 3. Commands Studied

## 3.1 Basic Nmap

```bash
nmap example.com
```

Runs Nmap using its default scan behavior.

On Linux with sufficient privileges, the default TCP port scan is normally a SYN-based scan.

---

# 4. Target Specification

## 4.1 List Scan: `-sL`

```bash
nmap -sL example.com
```

### Purpose

Lists the target(s) and performs target/name resolution without performing a normal port scan.

Useful for seeing:
- Target address
- Reverse/forward DNS information
- What Nmap considers the target

Example:

```text
example.com → 172.66.147.243
```

### Important

`-sL` does **not** mean the host is up or down.

---

## 4.2 Input List: `-iL`

```bash
nmap -iL input.txt
```

Reads targets from a file.

Example `input.txt`:

```text
192.168.1.10
example.com
scanme.nmap.org
```

Then:

```bash
nmap -iL input.txt
```

scans the listed targets.

If you see:

```text
Failed to open input file input.txt
```

Nmap cannot find the file at the specified path.

---

# 5. Host Discovery

## 5.1 `-sn`

```bash
nmap -sn example.com
```

### Meaning

Host discovery only.

It asks:

> Is the host reachable?

It does not perform a normal port scan.

Example:

```text
Host is up
```

---

## 5.2 `-Pn`

```bash
sudo nmap -Pn -p 80,443 example.com
```

### Meaning

Skip host discovery and assume the target is up.

Flow:

```text
Normal:
Host discovery
    ↓
Port scan

-Pn:
Skip host discovery
    ↓
Port scan directly
```

### Important

`-Pn` does **not** define the port-scan technique.

For example:

```bash
nmap -Pn example.com
```

means:

```text
Assume host is up
+
Use Nmap's normal/default scan behavior
```

While:

```bash
nmap -Pn -sS example.com
```

means:

```text
Assume host is up
+
Use TCP SYN scanning
```

### `-sn` vs `-Pn`

```text
-sn → perform host discovery, then stop
-Pn → skip host discovery and continue scanning
```

---

# 6. TCP SYN Scan: `-sS`

```bash
sudo nmap -sS example.com
```

### Purpose

Find open TCP ports using SYN probes.

Simplified packet flow:

```text
Nmap ── SYN ─────→ Target

Open port:
Nmap ←─ SYN/ACK ── Target

Closed port:
Nmap ←─ RST ────── Target
```

Typical interpretation:

```text
SYN/ACK → open
RST     → closed
No useful response → usually filtered
```

### Important

`-sS` is the main TCP port-scanning technique you have learned.

---

# 7. TCP Connect Scan: `-sT`

```bash
nmap -sT example.com
```

### Purpose

Find TCP ports using the operating system's normal TCP `connect()` mechanism.

Unlike a SYN scan, it completes a normal TCP connection when the port is open.

Simplified:

```text
SYN
 ↓
SYN/ACK
 ↓
ACK
 ↓
Connection established
```

### `-sS` vs `-sT`

```text
-sS → SYN scan; normally does not complete the normal TCP connection
-sT → TCP Connect scan; establishes the TCP connection
```

`-sT` is especially useful when raw-packet scanning is unavailable.

---

# 8. UDP Scan: `-sU`

```bash
sudo nmap -sU example.com
```

### Purpose

Scan UDP ports.

UDP does not have a TCP-style handshake.

Simplified:

```text
Nmap ── UDP probe ──→ Target
```

Possible results:

```text
UDP response       → open
ICMP unreachable   → closed
No response        → open|filtered
```

### Why `open|filtered`?

A UDP service may be open but simply not respond to an unexpected UDP packet.

Therefore:

```text
open|filtered
```

means Nmap cannot distinguish:

```text
OPEN
or
FILTERED
```

It does NOT mean both are confirmed.

---

# 9. TCP ACK Scan: `-sA`

```bash
sudo nmap -sA example.com
```

### Purpose

Analyze TCP filtering/firewall behavior.

Nmap sends an ACK probe:

```text
Nmap ── ACK ─────→ Target
```

Typical interpretation:

```text
RST response  → unfiltered
No response   → filtered
```

### Important

`unfiltered` does **not** mean `open`.

An ACK scan normally cannot determine whether an unfiltered port is open or closed.

---

# 10. `-sS` vs `-sA` vs `-sU`

```text
-sS
 ↓
Find open TCP ports

-sA
 ↓
Analyze TCP filtering/firewall behavior

-sU
 ↓
Find UDP services/ports
```

Easy memory:

```text
-sS → SYN → open TCP ports
-sA → ACK → filtering
-sU → UDP → UDP services
```

---

# 11. Port Selection: `-p`

## Single port

```bash
nmap -p 80 example.com
```

Scans only port 80.

## Multiple ports

```bash
nmap -p 21,80,443 example.com
```

Scans ports 21, 80, and 443.

## Range

```bash
nmap -p 1-1000 example.com
```

Scans ports 1 through 1000.

## All TCP ports

```bash
nmap -p- example.com
```

Scans TCP ports 1–65535.

### Common mistake

This is incorrect if you mean multiple ports:

```bash
nmap -p 80 443 21 example.com
```

Nmap interprets the arguments after `80` as separate targets.

Correct:

```bash
nmap -p 80,443,21 example.com
```

---

# 12. Port States

Nmap's port `STATE` describes what Nmap can determine from its probes.

## `open`

```text
80/tcp open http
```

A service is accepting connections.

---

## `closed`

```text
23/tcp closed telnet
```

The host is reachable, but no service is listening on that port.

A TCP RST commonly indicates this for a SYN scan.

---

## `filtered`

```text
21/tcp filtered ftp
```

Something is preventing Nmap from determining the port state.

Common reasons include:
- Firewall
- Packet filtering
- Silent packet dropping
- Network filtering

Important:

```text
filtered ≠ closed
```

---

## `unfiltered`

Commonly seen with `-sA`:

```text
unfiltered
```

Nmap can reach the port, but the scan technique cannot determine whether the port is open or closed.

Important:

```text
unfiltered ≠ open
```

---

## `open|filtered`

Commonly seen with UDP:

```text
open|filtered
```

Nmap cannot distinguish between an open port and a filtered port.

---

## `closed|filtered`

Nmap cannot distinguish between closed and filtered.

---

# 13. `no response`

Example:

```text
Not shown: 1000 filtered tcp ports (no-response)
```

This means Nmap sent probes but did not receive a useful response for those ports.

It does NOT automatically prove:
- The host is down
- The port is closed
- A firewall definitely exists

Possible causes include:
- Filtering
- Packet loss
- Rate limiting
- Unresponsive services
- Network conditions

---

# 14. Service and Version Detection: `-sV`

```bash
sudo nmap -sV -p 22,80,443 example.com
```

### Purpose

Attempts to identify:
- Service
- Software
- Version

Example:

```text
PORT    STATE SERVICE VERSION
80/tcp  open  http    ...
```

Important distinction:

```text
-sS → Is a TCP port open?
-sV → What service/software is running?
```

Nmap probes the service instead of simply assuming that a port number tells you the software.

---

# 15. OS Detection: `-O`

```bash
sudo nmap -O -p 22,80,443 scanme.nmap.org
```

### Purpose

Attempts to identify the target operating system from network behavior/fingerprints.

Example:

```text
OS details: Linux ...
```

### Important warning

OS detection is not guaranteed to be accurate.

You may see:

```text
Warning: OSScan results may be unreliable
```

when Nmap does not have enough information.

For example, Nmap may want at least:
- One known open port
- One known closed port

OS detection can also be affected by:
- Firewalls
- NAT
- Virtualization
- CDNs
- Proxies

---

# 16. Aggressive Scan: `-A`

```bash
sudo nmap -A example.com
```

### `-A` enables several detection features

Conceptually:

```text
-A
├── OS detection
├── Service/version detection
├── Default NSE scripts
└── Traceroute
```

It provides much more information than a basic scan and can take significantly longer.

### Important

`-A` does NOT mean:

> Scan every port.

It enables aggressive detection features; it does not automatically scan all 65,535 TCP ports.

---

# 17. NSE / Nmap Scripting Engine

NSE is Nmap's scripting system.

Important options:

```bash
nmap -sC target
```

```bash
nmap --script=<script> target
```

NSE can automate tasks such as:
- Service discovery
- Additional enumeration
- Version enhancement
- Vulnerability checks
- Other network tasks

NSE scripts are written in Lua.

These should be used only against systems you are authorized to test.

---

# 18. Output

## Grepable output: `-oG`

```bash
nmap -sS example.com -oG nmap_result
```

Saves results in grepable format.

View it:

```bash
cat nmap_result
```

Search it:

```bash
grep open nmap_result
```

Useful tools for processing results:

```text
grep
awk
sed
cut
sort
```

## Other output formats

```bash
-oN file     # normal output
-oG file     # grepable output
-oX file     # XML output
-oA name     # multiple standard formats
```

---

# 19. Traceroute

There are two related concepts.

## Linux traceroute

```bash
traceroute scanme.nmap.org
```

This is primarily a traceroute command.

It attempts to show the network hops between your machine and the destination.

Example:

```text
1  10.0.2.2
2  * * *
3  * * *
...
```

### Hop

A hop is a router/network device encountered along the route.

Conceptually:

```text
Your machine
    ↓
Router 1       ← Hop 1
    ↓
Router 2       ← Hop 2
    ↓
Router 3       ← Hop 3
    ↓
Destination
```

### `* * *`

Means no traceroute response was received for that probe.

It does not necessarily mean the route is broken.

Routers/firewalls may simply not respond to traceroute probes.

---

## Nmap `--traceroute`

```bash
nmap --traceroute example.com
```

Important:

```text
--traceroute
```

does not mean "run only traceroute".

Nmap still performs a normal scan and then includes traceroute information.

To reduce scan time while learning:

```bash
nmap -p 80 --traceroute example.com
```

---

# 20. `--trace` vs `--traceroute`

Incorrect:

```bash
nmap --trace example.com
```

Correct:

```bash
nmap --traceroute example.com
```

`--trace` should not be confused with Nmap's traceroute option.

---

# 21. Timing and Slow Scans

Timing templates:

```text
-T0 → very slow
-T1 → slow
-T2 → polite
-T3 → normal/default
-T4 → fast
-T5 → very aggressive
```

Example:

```bash
sudo nmap -sS -T4 example.com
```

Other performance options to learn later:

```bash
--max-retries
--host-timeout
--scan-delay
--max-scan-delay
--min-rate
--max-rate
```

### Retransmission warning

Example:

```text
Warning: 45.33.32.156 giving up on port because retransmission cap hit (10).
```

Meaning:

Nmap sent a probe, did not receive a useful response, retried it, and eventually stopped retrying that port.

This can be caused by:
- Packet loss
- Filtering
- Rate limiting
- High latency
- Network congestion
- Target behavior

It does NOT automatically mean the host is down.

---

# 22. Useful Comparison Table

| Option | Main purpose |
|---|---|
| `-sL` | List targets / DNS information |
| `-sn` | Host discovery without normal port scanning |
| `-Pn` | Skip host discovery; assume host is up |
| `-sS` | TCP SYN scan |
| `-sT` | TCP Connect scan |
| `-sU` | UDP scan |
| `-sA` | TCP ACK/filtering scan |
| `-p` | Choose ports |
| `-iL` | Read targets from a file |
| `-sV` | Service/version detection |
| `-O` | OS detection |
| `-A` | Aggressive detection |
| `-sC` | Default NSE scripts |
| `--script` | Run selected NSE scripts |
| `-oG` | Grepable output |
| `-oN` | Normal output |
| `-oX` | XML output |
| `-oA` | Save multiple output formats |
| `--traceroute` | Nmap scan + traceroute |

---

# 23. The Most Important Mental Model

```text
HOST DISCOVERY
    │
    ├── -sn → discover hosts
    ├── -Pn → skip discovery
    ├── -PS → TCP SYN host-discovery probe
    ├── -PA → TCP ACK host-discovery probe
    ├── -PU → UDP host-discovery probe
    ├── -PE → ICMP Echo host discovery
    └── -PR → ARP discovery (local Ethernet)

PORT SCANNING
    │
    ├── -sS → TCP SYN
    ├── -sT → TCP Connect
    ├── -sA → TCP ACK/filtering
    └── -sU → UDP

PORT SELECTION
    │
    └── -p

DETECTION
    │
    ├── -sV → service/version
    ├── -O  → OS
    └── -A  → several detection features

SCRIPTING
    │
    ├── -sC
    └── --script

OUTPUT
    │
    ├── -oN
    ├── -oG
    ├── -oX
    └── -oA

NETWORK PATH
    │
    └── --traceroute
```

---

# 24. Recommended Learning Order

For practical cybersecurity learning:

```text
1. Target specification
2. Host discovery
3. TCP scanning
4. UDP scanning
5. Port states
6. Port selection
7. Service/version detection
8. OS detection
9. NSE
10. Output formats
11. Timing/performance
12. Traceroute
13. Firewall behavior
14. Advanced scan techniques
15. Nmap internals/source code
```

---

# 25. Important Commands to Remember

```bash
# List target
nmap -sL example.com

# Discover host
nmap -sn example.com

# Skip host discovery
nmap -Pn example.com

# TCP SYN scan
sudo nmap -sS example.com

# TCP Connect scan
nmap -sT example.com

# UDP scan
sudo nmap -sU example.com

# ACK/filtering scan
sudo nmap -sA example.com

# Specific ports
nmap -p 21,22,80,443 example.com

# Port range
nmap -p 1-1000 example.com

# All TCP ports
nmap -p- example.com

# Service/version detection
sudo nmap -sV example.com

# OS detection
sudo nmap -O example.com

# Aggressive scan
sudo nmap -A example.com

# Read targets from file
nmap -iL input.txt

# Save grepable results
nmap -sS example.com -oG nmap_result

# Nmap traceroute
nmap --traceroute example.com

# Linux traceroute
traceroute example.com
```

---

# 26. Safety / Authorization

Use Nmap scans only against:
- Systems you own
- Your own lab
- Intentionally provided training targets
- Systems for which you have explicit authorization

Good practice targets include intentionally provided security-training systems such as Nmap's `scanme.nmap.org`, subject to the target's current usage policy.

---

# 27. Current Progress

Studied so far:

```text
✓ -sL
✓ -sn
✓ -Pn
✓ -sS
✓ -sT
✓ -sU
✓ -sA
✓ -p
✓ -iL
✓ -oG
✓ -A
✓ --traceroute
✓ traceroute
✓ -sV
✓ -O
✓ -PS
```

Next topics:

```text
→ -PA
→ -PU
→ -PE
→ -PR
→ Other host-discovery methods
→ More TCP scan techniques
→ NSE
→ Advanced performance
→ Nmap internals
```
