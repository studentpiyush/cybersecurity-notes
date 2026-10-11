# Cybersecurity Tools

Practical notes, commands, lab exercises, and troubleshooting references for tools used in network reconnaissance, packet analysis, and web application security testing.

## Tools

- [Nmap](nmap.md) — host discovery, port scanning, service detection, and scan-result interpretation.
- [Wireshark](wireshark.md) — packet capture, display filters, TCP analysis, and protocol troubleshooting.
- [Burp Suite](burpsuite.md) — intercepting and inspecting HTTP traffic and testing web applications in authorized labs.

## Lab Safety

Use active scanning and security-testing tools only on systems you own or have explicit permission to test. The examples in these notes are intended for isolated practice environments such as Kali Linux and Metasploitable 2.

## Suggested Practice Order

1. Discover a lab host and scan selected ports with Nmap.
2. Capture the scan in Wireshark and explain the packets you observe.
3. Use Burp Suite against an intentionally vulnerable web application to inspect requests and responses.

## Learning Notes

For each exercise, record the target, command or filter, observed output, interpretation, and any troubleshooting steps. Never store credentials, tokens, cookies, or other secrets in public notes.
