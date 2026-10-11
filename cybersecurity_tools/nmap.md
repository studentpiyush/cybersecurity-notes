# Nmap

Nmap (Network Mapper) is a network discovery and security-auditing tool. It can identify reachable hosts, probe TCP and UDP ports, detect services and versions, and perform selected checks using the Nmap Scripting Engine (NSE).

## 1. Installation and Help

Kali Linux usually includes Nmap. Verify it with:

```bash
nmap --version
nmap --help
```

On Debian-based systems, install it with:

```bash
sudo apt update
sudo apt install nmap
```

## 2. Lab Target

Example isolated lab:

- Kali interface on the host-only network: `192.168.56.102`
- Metasploitable 2 target: `192.168.56.101`

Replace these addresses with the values in your own lab. Scan only systems you own or are authorized to assess.

Check reachability:

```bash
ping -c 4 192.168.56.101
```

## 3. Common Scans

### Default TCP port scan

```bash
nmap 192.168.56.101
```

Scans Nmap's default set of 1,000 most common TCP ports.

### Scan selected ports

```bash
nmap -p 21,22,80,445,3306 192.168.56.101
```

### Scan all TCP ports

```bash
nmap -p- 192.168.56.101
```

This checks TCP ports 1–65535 and can take longer than a default scan.

### TCP SYN scan

```bash
sudo nmap -sS -p 21,22,80 192.168.56.101
```

A SYN scan sends TCP SYN probes. A SYN/ACK response usually indicates an open port; a reset response usually indicates a closed port. Nmap commonly resets the half-open connection after identifying an open port.

### TCP connect scan

```bash
nmap -sT -p 21,22,80 192.168.56.101
```

A connect scan uses the operating system's TCP connect function and completes the TCP handshake when a port is open. It is useful when raw-packet privileges are unavailable.

### Service and version detection

```bash
nmap -sV 192.168.56.101
```

Nmap probes discovered ports to help identify the service and version. Results are estimates and should be validated.

### OS detection

```bash
sudo nmap -O 192.168.56.101
```

OS detection uses network-response characteristics and may be inconclusive, especially when responses are filtered or the target is unusual.

### Default scripts and version detection

```bash
nmap -sC -sV 192.168.56.101
```

This runs Nmap's default script set and version detection. Use it only where scanning and script checks are authorized.

### UDP scan

```bash
sudo nmap -sU --top-ports 20 192.168.56.101
```

UDP scans can be slow and ambiguous. An open UDP service may not reply to a probe, and ICMP errors can indicate closed or filtered ports.

### Save results

```bash
nmap -sV -oN nmap-results.txt 192.168.56.101
nmap -sV -oX nmap-results.xml 192.168.56.101
```

## 4. Interpreting Port States

- **open** — an application is accepting connections or responding as an open service.
- **closed** — the host is reachable, but no service is listening on that port.
- **filtered** — Nmap cannot determine whether the port is open because filtering or another network condition prevents a clear answer.
- **open|filtered** — Nmap cannot distinguish between an open port and a filtered port for that probe.

A port state describes what the scan could infer at that time; it is not a complete security verdict.

## 5. SYN Scan vs. Connect Scan in Wireshark

Capture on Kali's host-only interface (in the example lab, `eth1`) while running a scan.

Useful display filter:

```text
ip.addr == 192.168.56.101 && tcp
```

For SSH only:

```text
ip.addr == 192.168.56.101 && tcp.port == 22
```

Typical SYN scan sequence for an open port:

1. Kali → target: `SYN`
2. Target → Kali: `SYN, ACK`
3. Kali → target: often `RST` or `RST, ACK`, aborting the half-open connection

Typical connect scan sequence for an open port:

1. Kali → target: `SYN`
2. Target → Kali: `SYN, ACK`
3. Kali → target: `ACK`, completing the handshake
4. The connection is then closed; teardown packets vary.

**Important:** An RST packet does not automatically mean a port is closed. Check the packet direction and the preceding exchange. A target RST in response to a SYN commonly indicates a closed port; a client-side RST after a target SYN/ACK is consistent with a SYN scan of an open port.

## 6. Practice Exercises

Use only the Metasploitable lab target.

- [ ] Run a default scan and record the open ports.
- [ ] Compare `-sS` and `-sT` against ports 21 and 22.
- [ ] Run `-sV` and explain what each detected service does.
- [ ] Capture both scans in Wireshark and identify SYN, SYN/ACK, ACK, FIN, and RST packets.
- [ ] Scan all TCP ports with `-p-` and compare the results with the default scan.
- [ ] Save a scan to a text file and write a short summary of the findings.

## 7. Troubleshooting

- **No response to ping:** ICMP may be blocked; verify VM network adapters and the target IP before drawing conclusions.
- **Host appears down:** In an authorized lab, try `-Pn` to skip host discovery: `nmap -Pn -p 22 192.168.56.101`.
- **Wireshark shows no scan packets:** Confirm capture is running on the interface connected to the target network.
- **Different results between scans:** SYN and connect scans use different connection behavior; firewalls, service changes, packet loss, and timing can affect results.

## References

- [Official Nmap Reference Guide](https://nmap.org/book/man.html)
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Nmap Service and Version Detection](https://nmap.org/book/man-version-detection.html)
