## Objective

Understand what shells are, their purpose, and how attackers use shell access during penetration testing.

---

# What is a Shell?

A shell is a program that allows users to interact with the operating system by executing commands.

Examples

- Bash
- PowerShell
- CMD
- Zsh

---

# Why Attackers Want Shell Access

Once attackers obtain a shell they can:

- Execute commands
- Browse files
- Read sensitive information
- Install software
- Create users
- Move laterally
- Escalate privileges

---

# Types of Shells

## Bind Shell

Victim opens a port.

Attacker connects.

```
Victim ----open port----> Attacker connects
```

Pros

Simple

Cons

Blocked by firewalls.

---

## Reverse Shell

Victim connects back to attacker.

```
Victim --------> Attacker Listener
```

Pros

Works better through NAT and firewalls.

Most common in penetration testing.

---

# Common Post-Exploitation Activities

## Privilege Escalation

Gain administrator/root privileges.

---

## Persistence

Maintain access after reboot.

Examples

- Backdoor accounts
- Startup scripts
- Scheduled tasks

---

## Data Exfiltration

Steal sensitive files.

Examples

- Passwords
- Documents
- Databases

---

## Pivoting

Use one compromised machine to attack other systems inside the network.

Example

Internet

↓

Victim A (Compromised)

↓

Internal Server

---

## Remote System Control

Execute commands remotely.

---

## Covering Tracks

Delete logs

Hide malware

Clear command history

---

# Common Shell Commands

Linux

```bash
pwd
ls
cd
cat
whoami
id
hostname
```

Networking

```bash
ip addr
ss -tuln
netstat -tuln
ping
```

Windows

```powershell
whoami
hostname
ipconfig
dir
systeminfo
```

---

# Key Learning

- Shells provide command execution on a target system.
- Reverse shells are more common than bind shells.
- Shell access is often the beginning of an attack.
- Attackers usually perform privilege escalation after obtaining shell access.
- Pivoting allows movement to internal systems.

---

# Skills Learned

- Shell Fundamentals
- Reverse Shell Concepts
- Bind Shell Concepts
- Post Exploitation
- Privilege Escalation
- Pivoting
- Persistence
