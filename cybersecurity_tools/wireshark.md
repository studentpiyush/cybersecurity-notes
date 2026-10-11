# Wireshark

Wireshark is a network protocol analyzer used to capture and inspect packets. It helps explain how hosts communicate and is useful for troubleshooting, security monitoring, and validating what network tools such as Nmap send and receive.

## 1. Capture Setup

For the example VirtualBox lab:

- Kali host-only interface: `eth1`, address `192.168.56.102`
- Metasploitable 2: `192.168.56.101`

1. Start Wireshark in Kali.
2. Select the interface connected to the host-only network (for this example, `eth1`).
3. Start capture before generating traffic.
4. Run a ping or Nmap scan in a terminal.
5. Stop the capture and apply a display filter.

A display filter only changes which captured packets are shown; it does not change what is captured.

## 2. Display Filters

| Purpose | Filter |
|---|---|
| Show traffic to or from the lab target | `ip.addr == 192.168.56.101` |
| Show TCP traffic to or from target | `ip.addr == 192.168.56.101 && tcp` |
| Show SSH traffic | `tcp.port == 22` |
| Show FTP traffic | `tcp.port == 21` |
| Show HTTP traffic | `http` |
| Show DNS packets | `dns` |
| Show ICMP packets | `icmp` |
| Show TCP packets with SYN set | `tcp.flags.syn == 1` |
| Show TCP reset packets | `tcp.flags.reset == 1` |
| Show SYN packets without ACK | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| Show retransmissions (when detected by Wireshark) | `tcp.analysis.retransmission` |
| Show ARP packets | `arp` |

Combine filters to narrow the view, for example:

```text
ip.addr == 192.168.56.101 && tcp.port == 22
```

## 3. TCP Three-Way Handshake

A normal TCP connection begins with:

1. **SYN** — client requests a connection.
2. **SYN, ACK** — server acknowledges the request and offers its side of the connection.
3. **ACK** — client acknowledges the server's response; the handshake is complete.

In Wireshark, inspect the Source, Destination, source/destination ports, and Info column. Use **Follow → TCP Stream** when you need to inspect the application data in a TCP conversation. Do not assume application data will be readable if it is encrypted.

## 4. Why RST Can Appear When Nmap Reports an Open Port

A TCP SYN scan (`nmap -sS`) often uses this sequence for an open port:

1. Kali sends `SYN` to the target.
2. The target replies with `SYN, ACK`, indicating the port is open.
3. Kali sends `RST` or `RST, ACK` to abort the half-open connection rather than complete the handshake.

The direction matters. A target reset in response to an initial SYN commonly indicates a closed port. A Kali-originated reset after a target SYN/ACK is consistent with Nmap's SYN scan behavior.

To inspect SSH in the example lab:

```text
ip.addr == 192.168.56.101 && tcp.port == 22
```

Compare the packet source and destination addresses and ports before interpreting a reset.

## 5. Compare Nmap Scan Types

Run each command against the isolated lab target while capturing on the correct interface.

### SYN scan

```bash
sudo nmap -sS -p 21,22 192.168.56.101
```

For open ports, expect SYN, SYN/ACK, and often a client-side RST. The TCP handshake is normally not completed.

### TCP connect scan

```bash
nmap -sT -p 21,22 192.168.56.101
```

For open ports, expect SYN, SYN/ACK, ACK, followed by connection teardown. Exact FIN/RST behavior can vary.

## 6. Other Protocols to Practice

### ICMP (ping)

Command:

```bash
ping -c 4 192.168.56.101
```

Filter:

```text
icmp
```

Look for Echo Request and Echo Reply packets.

### ARP

Filter:

```text
arp
```

ARP maps an IPv4 address to a link-layer address on a local network. ARP traffic is especially useful when troubleshooting communication between VMs on the same host-only network.

### DNS

Filter:

```text
dns
```

Inspect query names, record types, and replies. DNS over HTTPS or other encrypted DNS mechanisms will not appear as ordinary readable DNS queries.

### HTTP

Filter:

```text
http
```

In a controlled lab using unencrypted HTTP, inspect request methods, paths, response codes, and headers. HTTPS encrypts application data, so packet captures usually reveal connection metadata rather than the plaintext request and response.

## 7. Troubleshooting

- **No packets appear:** Verify the selected interface and confirm capture started before the traffic.
- **Ping works but scan packets are missing:** Capture on the host-only interface used to reach the target.
- **A filter shows no results:** Clear the display filter to check whether the packets were captured at all.
- **Traffic is encrypted:** Use the relevant application logs or authorized TLS decryption setup if available; do not expect plaintext from an ordinary encrypted capture.
- **Packets appear duplicated or unusual:** Consider retransmissions, capture points, offloading, and the packet direction before drawing conclusions.

## 8. Practice Checklist

- [ ] Capture four ping requests and replies.
- [ ] Capture an Nmap SYN scan and identify the SYN/ACK and client-side RST.
- [ ] Capture an Nmap connect scan and identify the completed handshake.
- [ ] Filter for ARP and explain an address-resolution exchange.
- [ ] Inspect a DNS query and response in a lab.
- [ ] Inspect an HTTP request and response in a controlled, unencrypted lab.
- [ ] Save a `.pcapng` capture and document what it demonstrates.

## References

- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures)
