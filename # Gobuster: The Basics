## Objective
Learn how to use Gobuster to perform content discovery, subdomain enumeration, and virtual host enumeration.

---

## What is Gobuster?

Gobuster is an open-source directory, DNS, and virtual host brute-forcing tool written in Go.

It is commonly used during the reconnaissance phase of penetration testing.

---

# Modes

## 1. Directory Enumeration (dir)

Searches for hidden directories and files.

Example:

```bash
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt
```

Useful Flags

| Flag | Purpose |
|------|---------|
| -u | Target URL |
| -w | Wordlist |
| -x | Search file extensions |
| -k | Skip TLS verification |
| -r | Follow redirects |
| -t | Number of threads |

Example

```bash
gobuster dir \
-u https://example.com \
-w /usr/share/wordlists/dirb/common.txt \
-x php,html,txt \
-k
```

---

## 2. DNS Enumeration (dns)

Discovers subdomains.

Example

```bash
gobuster dns \
-d example.com \
-w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

Required flags

- -d → Domain
- -w → Wordlist

---

## 3. Virtual Host Enumeration (vhost)

Finds virtual hosts sharing the same IP.

Example

```bash
gobuster vhost \
-u http://example.com \
-w wordlist.txt
```

---

# HTTP Status Codes

200 → OK

301 → Redirect

302 → Temporary Redirect

403 → Forbidden

404 → Not Found

500 → Internal Server Error

---

# TLS Verification

TLS verification checks whether a website's certificate is valid.

Gobuster can skip certificate verification using

```bash
-k
```

Useful in labs using self-signed certificates.

---

# Wordlists Used

Directory:

```text
/usr/share/wordlists/dirb/common.txt
```

Subdomain:

```text
/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

---

# Key Learning

- Gobuster is a content discovery tool.
- Faster than Dirb because it is written in Go.
- Supports directory, DNS, and virtual host enumeration.
- Wordlists are the core of brute-force enumeration.
- Status codes help identify interesting resources.

---

# Skills Learned

- Directory Enumeration
- DNS Enumeration
- Virtual Host Enumeration
- HTTP Response Analysis
- Content Discovery
