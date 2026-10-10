# Cyber Incidents — Major Historical Cases for Cybersecurity Learners

> **Purpose:** A study reference for ethical hacking, networking, vulnerability assessment, SOC analysis, incident response, malware analysis, threat intelligence, and cyber law.
>
> **Scope:** A curated selection of major publicly documented incidents, from early Internet malware through 2024-era cases. It includes Indian examples and practical defensive takeaways. This is not an exhaustive list of all cyber incidents.
>
> **Attribution warning:** Cyber attribution is often probabilistic. A victim's infection does not by itself prove who operated the malware. This note distinguishes official public attribution, criminal allegations, security-research assessments, and cases where the actor remains unknown. An allegation or indictment is not the same as a conviction.

## Contents

1. [How to study an incident](#how-to-study-an-incident)
2. [Timeline at a glance](#timeline-at-a-glance)
3. [Major incidents in detail](#major-incidents-in-detail)
4. [People and groups worth knowing](#people-and-groups-worth-knowing)
5. [Attack patterns and defensive lessons](#attack-patterns-and-defensive-lessons)
6. [Incident-response workflow for a SOC analyst](#incident-response-workflow-for-a-soc-analyst)
7. [Practical study exercises](#practical-study-exercises)
8. [Glossary](#glossary)
9. [Recommended source library](#recommended-source-library)

---

## How to study an incident

For each case, be able to explain these seven things in your own words:

1. **Initial access:** How did the attacker first get in, if this is known? Examples include phishing, a vulnerable public-facing server, stolen credentials, or a compromised software update.
2. **Execution and persistence:** What ran, and how did the attacker maintain access?
3. **Privilege and lateral movement:** Did the attacker obtain more permissions or move between systems?
4. **Objective:** Was the goal espionage, theft, extortion, destruction, disruption, or ideological messaging?
5. **Impact:** What data, systems, people, or services were affected?
6. **Detection and response:** What evidence was available, and which containment and recovery actions mattered?
7. **Prevention:** Which controls could have reduced the likelihood, scope, or duration of the incident?

Do not assume all seven stages occurred in every case. A DDoS campaign may never involve access to a victim's internal systems. A vulnerability can be exploited without the operator being identified. A supply-chain compromise can originate with a trusted vendor rather than the final victim.

## Timeline at a glance

| Year | Incident | Main topic | Person, group, or attribution |
|---|---|---|---|
| 1988 | Morris Worm | Self-replicating malware, Internet resilience | Robert Tappan Morris |
| 2000 | Mafiaboy DDoS attacks | Availability and DDoS | Michael Calce, known as Mafiaboy |
| 2007 | Estonia cyberattacks | DDoS, national resilience | Several actors; attribution varies by incident |
| 2010 | Stuxnet | Industrial control systems | Commonly attributed by researchers to a US–Israeli operation; full details not officially confirmed by both governments |
| 2011 | HBGary Federal | Hacktivism, account compromise | Anonymous-associated participants |
| 2013 | Target payment-card breach | Third-party access, payment security | Criminal intruders; do not automatically connect Albert Gonzalez to this incident |
| 2013–2016 | Yahoo breaches | Credential theft, account data, espionage | Russian intelligence officers were charged in one related intrusion |
| 2014 | Sony Pictures attack | Destructive malware, data theft | US government attributed the incident to North Korea |
| 2015 | OPM breach | Sensitive identity and background data | Public reporting discussed state-linked attribution; sensitive-data protection is the core lesson |
| 2015–2016 | Ukraine power-grid attacks | OT/ICS disruption | Publicly attributed by several governments to Russian state-linked actors |
| 2016 | Bangladesh Bank heist | Spear-phishing, financial-message fraud | US DOJ connected the conspiracy to North Korean regime-backed operators |
| 2016 | Mirai botnet and Dyn DDoS | IoT botnet, DDoS | Paras Jha, Josiah White, and Dalton Norman pleaded guilty to Mirai-related offenses |
| 2017 | WannaCry | Ransomware, unpatched systems | Publicly attributed by several governments to North Korean actors associated with Lazarus |
| 2017 | NotPetya | Destructive malware, supply chain | UK government attributed the attack to the Russian military |
| 2017 | Equifax breach | Unpatched public-facing application | Four Chinese military members were indicted by the US; this is an allegation |
| 2018 | Cosmos Bank, Pune | Banking malware, ATM cash-outs, payment fraud | Criminal investigation; avoid naming an actor without a reliable case record |
| 2019 | Kudankulam network infection | IT/OT separation | Indian government confirmed an administrative-network infection; plant-control systems were reported unaffected |
| 2020 | SolarWinds | Trusted software update, espionage | US government attributed the campaign to Russia's SVR |
| 2021 | Colonial Pipeline | Ransomware and critical services | DarkSide ransomware operation |
| 2021 | Microsoft Exchange exploitation | Public-facing vulnerabilities, web shells | Microsoft and government reporting linked early activity to HAFNIUM, assessed as China-based; other actors also exploited it |
| 2021 | Kaseya VSA | MSP supply-chain ransomware | REvil/Sodinokibi operation |
| 2021 | Log4Shell | Critical Java library RCE | Exploited by multiple actors; not one single attacker |
| 2022 | AIIMS Delhi incident | Healthcare disruption | Public reporting did not establish a definitive named operator |
| 2023 | MOVEit Transfer mass exploitation | Zero-day SQL injection, data theft | FBI/CISA linked exploitation to CL0P |
| 2023 | MGM Resorts incident | Social engineering, identity abuse | Public reporting associated the incident with Scattered Spider; MGM's SEC disclosure did not independently establish attribution |
| 2024 | Change Healthcare ransomware | Healthcare ecosystem and ransomware | ALPHV/BlackCat claimed responsibility; describe attribution carefully |
| 2024 | Snowflake customer-data theft campaign | Stolen credentials, cloud data | Mandiant tracked the campaign as UNC5537 |
| 2024 | CrowdStrike update outage | Software quality and resilience | Faulty security-content update; not a malicious cyberattack |

---

# Major incidents in detail

## 1. 1988 — Morris Worm

**Main topic:** Early Internet worm, insecure services, unintended propagation  
**Person:** Robert Tappan Morris

### What happened
In November 1988, a self-replicating program spread across a substantial portion of the then-small Internet. It exploited weaknesses and trust relationships in Unix systems and services. Its replication logic could cause repeated copies to run on the same machine, consuming computing resources and making systems unusable. Morris later became the first person convicted under the US federal Computer Fraud and Abuse Act.

### Why it matters
The case showed that malware can cause major disruption without stealing files or demanding money. An experimenter's stated intent does not eliminate the harm caused by uncontrolled propagation.

### Defensive lessons
- Disable unnecessary services and restrict network exposure.
- Use least privilege and secure defaults.
- Monitor unexpected process creation, resource spikes, and unusual outbound connections.
- Design testing and release processes to prevent uncontrolled spread.
- Maintain a coordinated incident-response process for rapidly spreading malware.

### Study connection
Distinguish a **virus** (often attaches to a host file), a **worm** (self-propagates across systems), and a **trojan** (disguises its purpose). These behaviors can overlap in modern malware.

**Source:** [FBI — Morris Worm](https://www.fbi.gov/history/cases-and-criminals/morris-worm)

## 2. 2000 — Mafiaboy DDoS attacks

**Main topic:** Distributed denial of service (DDoS), availability  
**Person:** Michael Calce, known as Mafiaboy

### What happened
In February 2000, a teenage attacker launched denial-of-service attacks against prominent websites, including Yahoo!, eBay, CNN, and Amazon. The attacks flooded targets with traffic and disrupted access for legitimate users. Calce was later prosecuted in Canada.

### Technical significance
A DDoS attack targets **availability**. It does not necessarily mean the attacker accessed a database or took control of a server. Traffic can come from many compromised devices or other distributed sources, making it difficult to distinguish malicious traffic from legitimate demand.

### Defensive lessons
- Use upstream DDoS mitigation, traffic filtering, rate limiting, and resilient architecture.
- Monitor traffic volume, connection rates, source distribution, and application error rates.
- Keep DNS and network dependencies resilient; failure at a shared provider can affect many unrelated websites.
- Establish provider escalation paths and communication plans before an attack.

### Study connection
Explain the difference between DoS and DDoS. During triage, assess whether the symptom is network saturation, application exhaustion, DNS failure, or another outage.

**Sources:** [FBI — cases and criminals](https://www.fbi.gov/history/cases-and-criminals); [CISA — understanding DDoS attacks](https://www.cisa.gov/news-events/news/understanding-and-responding-distributed-denial-service-attacks)

## 3. 2007 — Estonia cyberattacks

**Main topic:** DDoS, dependence on online services, geopolitical context  
**Attribution:** Distributed activity; attribution and responsibility differ across accounts and individual incidents.

### What happened
In April and May 2007, Estonia experienced waves of cyberattacks amid political tensions surrounding the relocation of a Soviet-era war memorial. Government, media, banking, and other online services were disrupted by denial-of-service activity and related interference.

### Why it matters
Estonia had a highly digitized public and commercial environment. The incident became an influential case study in national cyber resilience and international cooperation. It also illustrates the difficulty of attribution when infrastructure, intermediaries, and participants cross borders.

### Defensive lessons
- Build resilient service architecture, including DDoS protection and recovery arrangements.
- Maintain communications channels that remain usable during online outages.
- Coordinate public agencies, ISPs, financial institutions, and incident responders.
- Separate verified technical evidence from political assumptions about responsibility.

### Study connection
Research national CERTs, cyber crisis management, DDoS traffic analysis, and the difference between technical attribution and legal attribution.

**Source:** [Council on Foreign Relations — 2007 Estonia cyberattacks](https://www.cfr.org/cyber-operations/2007-cyber-attacks-estonia)

## 4. 2010 — Stuxnet

**Main topic:** Industrial control systems (ICS), operational technology (OT), targeted malware  
**Attribution:** Commonly attributed by researchers to a US–Israeli operation; full details have not been officially confirmed by both governments.

### What happened
Stuxnet was a sophisticated worm discovered in 2010. Unlike malware aimed only at office computers, it targeted particular Siemens industrial control environments and manipulated programmable logic controller (PLC) operations while attempting to conceal changes from operators. It became widely known for its connection to Iran's Natanz nuclear enrichment program.

### Why it matters
Stuxnet showed that cyber operations can affect physical processes. OT environments prioritize safety, availability, and reliable operation; security techniques must be applied with industrial safety and uptime in mind.

### Defensive lessons
- Segment enterprise IT from OT and tightly control connections between them.
- Inventory PLCs, engineering workstations, firmware, and removable media.
- Restrict who can change control logic and independently review and record those changes.
- Use application allowlisting and controlled maintenance windows where appropriate.
- Test controls with OT engineers to avoid unsafe process changes.

### Study connection
Understand the differences between IT and OT, what a PLC does, how industrial processes are monitored, and why passive monitoring may be preferred in some operational environments.

**Sources:** [CISA — Industrial Control Systems advisories](https://www.cisa.gov/news-events/ics-advisories); [Symantec's technical history of Stuxnet](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)

## 5. 2011 — HBGary Federal and Anonymous

**Main topic:** Hacktivism, compromised accounts, email disclosure  
**Group:** People operating under the Anonymous name

### What happened
After security firm HBGary Federal publicly discussed efforts to identify members associated with Anonymous, attackers operating under the Anonymous name compromised the firm's systems. Public reporting described access to email and internal information, publication of correspondence, and defacement or disruption of company web properties.

### Why it matters
Security companies are not automatically secure. Public claims about adversaries can trigger retaliation, and a breach can expose internal security practices, client relationships, and communications.

### Defensive lessons
- Enforce MFA, especially for administrators and remote access.
- Protect email accounts, password-reset workflows, and privileged accounts.
- Avoid password reuse and restrict access to sensitive internal systems.
- Separate public-facing infrastructure from corporate assets.
- Have a plan for evidence preservation, account resets, and communication after a breach.

### Attribution caveat
Anonymous is a loose, decentralized label, not a single organization with stable membership. Do not describe every action claimed under that name as the action of a unified group.

**Source:** [WIRED — Anonymous hacks HBGary](https://www.wired.com/2011/02/anonymous-hacks-hbgary/)

## 6. 2013 — Target payment-card breach

**Main topic:** Third-party access, network segmentation, payment-card security  
**Victim:** Target Corporation

### What happened
During the 2013 holiday shopping period, attackers obtained access to Target's environment through credentials associated with a third-party vendor, according to public investigations and reporting. The intruders reached parts of the retail network where payment-card information was processed and deployed malware to collect card data. Target disclosed theft involving tens of millions of payment-card accounts and personal information relating to tens of millions of people.

### What made the incident important
The attacker did not have to begin with a direct exploit of the retailer's central payment systems. Vendor access became a route into a much larger organization. The incident became a classic lesson in third-party risk and segmentation.

### Defensive lessons
- Give vendors only the network access necessary for their work.
- Isolate payment environments from general corporate and vendor networks.
- Monitor vendor remote access and access to systems outside a vendor's normal role.
- Deploy endpoint detection and alert on unexpected processes or outbound traffic.
- Ensure security alerts are monitored and acted upon; a tool that generates alerts without response is not an effective control.

### Study connection
Draw a simple network diagram showing the vendor access route, point of entry, payment environment, and data-exfiltration path. Mark where segmentation, MFA, endpoint detection, or alert triage might interrupt the attack chain.

**Source:** [US Senate Permanent Subcommittee on Investigations — Target breach report (PDF)](https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/PSI%20REPORT%20-%20Target%20Corporation%20Breach%20(7-7-14).pdf)

## 7. 2013–2016 — Yahoo account breaches

**Main topic:** Credential theft, large-scale account data, espionage  
**People/group:** US authorities charged Russian intelligence officers and a criminal associate in connection with a 2014 Yahoo intrusion.

### What happened
Yahoo disclosed major breaches affecting hundreds of millions of accounts. In a criminal case announced in 2017, US prosecutors alleged that two officers of Russia's Federal Security Service (FSB), along with criminal hackers, were involved in a 2014 intrusion affecting at least 500 million Yahoo accounts. The stolen information included account data and was used for several purposes, including targeted access to selected accounts.

### Why it matters
A large account database is valuable even when passwords are not all immediately usable. Personal information can support spear-phishing, account-recovery abuse, impersonation, and attacks against people who reused credentials elsewhere.

### Defensive lessons
- Store passwords using modern salted password hashing, not reversible encryption or plaintext.
- Protect session cookies and recovery workflows; password security is only one part of account security.
- Force credential resets where warranted, revoke active sessions, and investigate suspicious access.
- Notify users transparently and provide practical advice about credential reuse.
- Use unique passwords and MFA, particularly for email accounts used to reset other accounts.

### Attribution caveat
The US DOJ announcement describes charges and allegations. Write “prosecutors alleged” or “the indictment charged” rather than presenting every allegation as a final judicial finding.

**Source:** [US Department of Justice — Yahoo intrusions case documents](https://www.justice.gov/archives/opa/press-release/file/948201/dl)

## 8. 2014 — Sony Pictures Entertainment attack

**Main topic:** Destructive malware, data theft, intimidation, geopolitical attribution  
**Group attribution:** The US government attributed the attack to North Korea; a group calling itself Guardians of Peace publicly claimed responsibility.

### What happened
In late November 2014, Sony Pictures Entertainment disclosed an intrusion in which destructive malware rendered thousands of computers inoperable and large quantities of company data were stolen and leaked. The attackers threatened the company and used stolen information to create pressure around the release of the film *The Interview*. The FBI publicly described its investigation and attributed the intrusion to North Korea.

### Why it matters
This was not merely a conventional ransomware event. Destruction, data theft, leaks, threats, and business disruption occurred together. Rebuilding systems cannot undo a confidentiality loss after information has been copied out.

### Defensive lessons
- Maintain offline or immutable backups and test restoration.
- Restrict privileged access, monitor administrative actions, and segment critical assets.
- Prepare for simultaneous system destruction and data disclosure.
- Preserve forensic images and logs before rebuilding, when feasible.
- Plan legal, employee, public-relations, and law-enforcement coordination in advance.

**Sources:** [US DOJ — update on the Sony investigation](https://www.justice.gov/archives/opa/pr/update-sony-investigation); [US DOJ — North Korean programmer case and Sony attack](https://www.justice.gov/archives/opa/pr/north-korean-regime-backed-programmer-charged-conspiracy-conduct-multiple-cyber-attacks-and)

## 9. 2015 — US Office of Personnel Management (OPM) breach

**Main topic:** Sensitive personal information, identity risk, long-term espionage value

### What happened
The US Office of Personnel Management disclosed in 2015 that intrusions had affected personnel records for about 4.2 million current and former federal employees and background-investigation records relating to about 21.5 million people. The latter included highly sensitive data collected during security-clearance processes.

### Why it matters
A breach of background-investigation data is different from theft of a regular customer database. Such records may contain personal history, relationships, and identifying details useful for long-term targeting, impersonation, or counterintelligence.

### Defensive lessons
- Classify information according to sensitivity and the harm if exposed.
- Minimize collection and retention of highly sensitive personal data.
- Enforce least privilege, strong identity controls, and monitoring of bulk data access.
- Monitor unusual database queries, exports, and access from compromised accounts.
- Have a long-term victim-support plan when exposed information cannot simply be changed, such as a date of birth or past history.

**Source:** [US Government Accountability Office — OPM security reviews](https://www.gao.gov/products/gao-19-143r)

## 10. 2015–2016 — Ukraine power-grid attacks

**Main topic:** OT/ICS security, critical infrastructure, destructive operations  
**Attribution:** Publicly attributed by the US and UK governments to Russian state-linked actors.

### What happened
In December 2015, cyber operations against Ukrainian electricity distribution companies contributed to power outages. Public investigations described attackers using remote access, credential theft, and destructive capabilities against IT systems supporting electricity operations. A further incident in December 2016 involved Industroyer/CrashOverride malware, designed to interact with electricity-grid industrial protocols.

### Why it matters
Critical-infrastructure attacks can affect public safety and essential services. The path to disruption may involve compromising corporate IT first, then crossing into operational networks or abusing legitimate remote management systems.

### Defensive lessons
- Segment IT from OT with monitored, tightly controlled conduits.
- Remove default credentials and unnecessary remote-access paths.
- Monitor changes to control systems and operator workstations.
- Keep tested manual operating and recovery procedures.
- Back up engineering configurations and test recovery without risking real-world safety.
- Coordinate with vendors and sector-response organizations.

**Sources:** [CISA — Russian state-sponsored threats to critical infrastructure](https://www.cisa.gov/news-events/alerts/2022/01/11/understanding-and-mitigating-russian-state-sponsored-cyber-threats-us-critical-infrastructure); [UK government — GRU cyber operations profile](https://www.gov.uk/government/publications/profile-gru-cyber-and-hybrid-threat-operations/profile-gru-cyber-and-hybrid-threat-operations)

## 11. 2016 — Bangladesh Bank heist

**Main topic:** Spear-phishing, financial networks, SWIFT fraud  
**Attribution:** US DOJ connected the conspiracy to North Korean regime-backed operators.

### What happened
In February 2016, attackers who had compromised Bangladesh Bank's environment sent fraudulent payment instructions through systems connected to SWIFT, the interbank financial messaging network. The instructions sought to move funds from the bank's account at the Federal Reserve Bank of New York to accounts overseas. About US$81 million was successfully transferred, although other attempted transfers were stopped.

### What to learn technically
SWIFT is a financial messaging network; it does not itself hold every bank's money. The attack involved compromising the environment used to prepare and authenticate payment messages and abusing trusted procedures.

### Defensive lessons
- Separate payment initiation, approval, and release responsibilities.
- Monitor unusual payment patterns, beneficiary changes, and out-of-hours activity.
- Restrict access to payment workstations and isolate them from general office systems.
- Use multi-person approval, transaction limits, and out-of-band confirmation for anomalous transfers.
- Retain detailed, tamper-resistant logs and reconcile transaction records promptly.
- Treat malware detection and financial fraud monitoring as complementary defenses.

**Sources:** [US DOJ — North Korean programmer case](https://www.justice.gov/archives/opa/pr/north-korean-regime-backed-programmer-charged-conspiracy-conduct-multiple-cyber-attacks-and); [US DOJ complaint describing the Bangladesh Bank transfers (PDF)](https://www.justice.gov/d9/press-releases/attachments/2018/09/06/2018_09_06_park_complaint_unsealed_0.pdf)

## 12. 2016 — Mirai botnet and the Dyn DDoS attack

**Main topic:** Internet of Things (IoT), botnets, DDoS  
**People:** Paras Jha, Josiah White, and Dalton Norman pleaded guilty to Mirai-related offenses.

### What happened
Mirai malware searched for internet-connected devices, particularly routers and cameras, that could be accessed using weak or default credentials. It enrolled compromised devices into a botnet that could be directed to generate high-volume traffic. On 21 October 2016, a Mirai-related DDoS attack against DNS provider Dyn made popular websites and services unreachable or intermittent for users.

### Why it matters
Owners of compromised devices were often not the direct targets. Their devices were used as unwilling participants in attacks against a third party. A weakness in a connected camera or router can therefore contribute to outages across the wider Internet.

### Defensive lessons
- Change default passwords and disable unnecessary remote administration.
- Keep IoT firmware updated and replace devices that no longer receive security updates.
- Prevent devices from exposing management interfaces directly to the public Internet.
- Monitor unusual connections from IoT network segments and restrict outbound traffic.
- Coordinate with upstream providers for DDoS mitigation and build resilient DNS dependencies.

### Study connection
Learn how a botnet differs from a single attacking host, how DNS resolution works, and why failure of a shared DNS provider can affect many unrelated services.

**Sources:** [US DOJ — Mirai charges and guilty pleas](https://www.justice.gov/archives/opa/pr/justice-department-announces-charges-and-guilty-pleas-three-computer-crime-cases-involving); [US DOJ — Dyn attack description](https://www.justice.gov/usao-nh/pr/individual-pleads-guilty-participating-internet-things-cyberattack-2016)

## 13. 2017 — WannaCry ransomware

**Main topic:** Ransomware, worm-like propagation, missing patches  
**Attribution:** Publicly attributed by multiple governments to North Korean actors associated with Lazarus.

### What happened
WannaCry began spreading globally on 12 May 2017. It encrypted files and demanded payment, while also spreading to vulnerable Windows systems by exploiting SMB-related weaknesses. The campaign disrupted organizations in many countries, including parts of the UK's National Health Service. Some NHS trusts diverted patients or cancelled appointments and procedures.

### Why it matters
WannaCry showed how one unpatched system can help turn a local compromise into a large network incident. Healthcare organizations faced both IT disruption and risks to patient care. Payment does not guarantee complete recovery or restore system integrity.

### Defensive lessons
- Patch internet-connected and internally reachable systems rapidly when active exploitation is reported.
- Disable obsolete protocols where possible and segment networks to restrict propagation.
- Keep verified offline or immutable backups and rehearse restoration.
- Maintain an accurate asset inventory, including unsupported systems.
- Use endpoint detection and centralized logging to find affected hosts quickly.
- Have a downtime plan for clinical or operational services.

**Sources:** [US DOJ — North Korean programmer case, including WannaCry](https://www.justice.gov/archives/opa/pr/north-korean-regime-backed-programmer-charged-conspiracy-conduct-multiple-cyber-attacks-and); [UK Parliament report on the NHS and WannaCry](https://assets.publishing.service.gov.uk/media/5c9cbb02ed915d07a7e613d4/TM_Progress_Report_20_March_final.pdf)

## 14. 2017 — NotPetya destructive malware

**Main topic:** Software supply-chain compromise, worm-like spread, destructive malware  
**Attribution:** The UK government attributed the attack to the Russian military.

### What happened
On 27 June 2017, malware known as NotPetya spread widely, initially targeting Ukraine. Investigations reported that a compromised update mechanism for Ukrainian tax/accounting software M.E.Doc was involved in the initial spread. The malware then spread through affected networks and caused destructive damage. Although it displayed a ransom demand, its behavior made recovery through payment unreliable; it is commonly characterized as a destructive wiper disguised as ransomware.

### Impact
International companies with operations connected to Ukraine were affected, including major logistics and pharmaceutical businesses. Maersk later reported very substantial losses and had to rebuild much of its IT environment.

### Defensive lessons
- Treat software vendors and update mechanisms as part of the attack surface.
- Use segmentation and restrict administrative credentials to prevent rapid lateral movement.
- Maintain independent backups of critical systems and configurations.
- Test the ability to rebuild identity infrastructure, directory services, and endpoints after a destructive incident.
- Plan for attacks that destroy systems rather than merely encrypt files.

### Study connection
Compare WannaCry with NotPetya: both spread widely and disrupted systems, but their objectives and recovery implications differed. Do not classify malware solely from the ransom note it displays.

**Sources:** [UK government attribution of NotPetya](https://www.gov.uk/government/news/foreign-office-minister-condemns-russia-for-notpetya-attacks); [UK National Crime Agency — NotPetya background](https://www.nationalcrimeagency.gov.uk/who-we-are/publications/178-the-cyber-threat-to-uk-business-2017-18/)

## 15. 2017 — Equifax data breach

**Main topic:** Vulnerability management, data theft, patching governance  
**Attribution:** US prosecutors indicted four members of China's People's Liberation Army; this is a criminal allegation by the US government.

### What happened
Equifax, a major credit-reporting agency, disclosed that attackers had exploited a vulnerability in an internet-facing application. The breach affected personal information associated with approximately 145 million Americans, including names, birth dates, Social Security numbers, and other identifying information.

### Why it matters
The incident is a textbook example of how a known vulnerability, a failure in patch management, and high-value data concentration can combine into a major breach. Personal identifiers are hard to replace and can enable identity fraud long after the incident.

### Defensive lessons
- Track internet-facing software and ownership, not just installed endpoint software.
- Prioritize patches based on exploit activity, exposure, asset criticality, and data sensitivity.
- Verify patches were applied successfully instead of treating a change ticket as proof.
- Use vulnerability scanning alongside asset inventories, log review, and external exposure monitoring.
- Reduce data retention and restrict access to large stores of sensitive data.
- Prepare clear disclosure and identity-protection support plans.

**Source:** [US DOJ — Equifax indictment announcement](https://www.justice.gov/archives/opa/pr/chinese-military-personnel-charged-computer-fraud-economic-espionage-and-wire-fraud-hacking)

## 16. 2018 — Cosmos Bank, Pune cyber fraud

**Main topic:** Banking malware, ATM cash-outs, financial-message fraud  
**Location:** Pune, India

### What happened
Cosmos Cooperative Bank reported a major cyber fraud in August 2018 involving unauthorized ATM withdrawals across multiple locations and a fraudulent international banking transfer. Public reporting put the total exposure at roughly ₹94 crore. Investigations described compromise of the bank's ATM switch environment and fraudulent SWIFT-related transfers. Different public accounts may use different totals and categories, so consult primary bank and police records when citing an exact figure.

### Why it matters
This was a significant Indian case showing that cybercrime can target payment infrastructure and financial transaction processes, not only consumer websites. International cash-outs can occur quickly, making monitoring and inter-bank coordination important.

### Defensive lessons
- Segment ATM switch systems and payment environments.
- Alert on unusual transaction velocity, geographic patterns, repeated withdrawals, and deviations from normal activity.
- Use independent controls for high-value transfers and verify anomalies through a second channel.
- Maintain reliable logs across ATMs, payment switches, endpoints, and banking systems.
- Establish rapid coordination among fraud teams, bank security, payment networks, and law enforcement.

### Study connection
Draw the ATM transaction path and a separate SWIFT payment workflow. Mark the controls that validate transaction authenticity and detect mismatches between normal behavior and fraud.

**Sources:** [Cosmos Bank Annual Report 2018–19 (PDF)](https://cosmos.bank.in/auth/writereaddata/files/110521193370101_Cosmos-Bank-AR-2018-19_web.pdf); [CERT-In — national incident-response role](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBWEL01)

## 17. 2019 — Kudankulam Nuclear Power Plant network infection

**Main topic:** Indian critical infrastructure, malware, IT/OT segmentation  
**Location:** Tamil Nadu, India

### What happened
In November 2019, India's Department of Atomic Energy confirmed a malware infection on the administrative network associated with Kudankulam Nuclear Power Plant. The government stated that the affected network handled administrative activities and that plant control and instrumentation systems were isolated from external and administrative networks and were not affected by the infection.

Some private threat-intelligence reporting associated the malware with DTrack and discussed links to Lazarus-related activity. The Indian government's public statement about the incident did not itself establish a named actor, so the government confirmation and outside attribution claims must be kept separate.

### Why it matters
A network can contain sensitive information without being the same network that directly controls a physical process. Segmentation helped limit the reported scope, but an infection on an administrative network still requires investigation.

### Defensive lessons
- Maintain strict, monitored separation between administrative IT and control networks.
- Inventory and investigate removable media, remote access, and connections crossing the IT/OT boundary.
- Build and retain evidence before removing malware.
- Verify which systems were affected rather than relying only on a network diagram.
- Communicate the scope clearly: malware on an administrative network does not automatically mean a plant was controlled by attackers.

**Sources:** [Press Information Bureau — cyber attack on KKNPP](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1592498&lang=2&reg=48); [CERT-In — national incident-response role](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBWEL01)

## 18. 2020 — SolarWinds supply-chain compromise

**Main topic:** Trusted software updates, espionage, persistence, threat hunting  
**Attribution:** US government publicly attributed the campaign to Russia's Foreign Intelligence Service (SVR).

### What happened
Attackers compromised the build or distribution process associated with SolarWinds Orion and inserted a backdoor into software updates. Customers that installed affected updates could become initial footholds for the attackers. The campaign affected government agencies and private organizations, but not every customer who installed an affected version experienced the same follow-on activity.

### Why it matters
The attack undermined trust in software victims had deliberately installed and allowed in their environments. Conventional controls that trust signed vendor software may not catch a malicious change introduced within a legitimate software pipeline.

### Defensive lessons
- Protect build systems, release credentials, source repositories, and signing processes.
- Inventory software dependencies and monitor vendor security advisories.
- Investigate unexpected authentication, identity-provider changes, unusual cloud access, and suspicious service activity.
- Use layered trust: code signing is valuable, but cannot independently guarantee a build is benign.
- Prepare a targeted hunt for follow-on activity; uninstalling or patching the initial product is not enough if another access path remains.
- Apply least privilege and separate administrative identities.

### Study connection
Learn the difference between initial access, a backdoor, persistence, and post-compromise activity. Incident response may require rotating secrets and investigating identity systems, not only removing one executable.

**Source:** [CISA — active exploitation of SolarWinds software](https://www.cisa.gov/news-events/alerts/2020/12/13/active-exploitation-solarwinds-software)

## 19. 2021 — Colonial Pipeline ransomware

**Main topic:** Ransomware, critical services, business continuity  
**Group:** DarkSide

### What happened
Colonial Pipeline, a major US fuel pipeline operator, was affected by a ransomware incident in May 2021. The company temporarily halted pipeline operations while responding. The disruption led to fuel-supply concerns across parts of the eastern United States. The US Department of Justice later announced seizure of part of the cryptocurrency ransom payment.

The operational shutdown was a business-continuity decision. Do not simplify it to a claim that the attacker directly controlled pipeline equipment; public accounts distinguished the IT incident and the decision to stop operations as a precaution.

### Why it matters
A compromise of IT systems can create operational and safety concerns even when industrial controls are not proven to have been directly compromised. Critical infrastructure plans must account for this dependency.

### Defensive lessons
- Separate business IT from OT and define safe shutdown criteria in advance.
- Secure remote access, enforce MFA, and disable stale accounts.
- Maintain offline backups, recovery procedures, and tested alternative operating processes.
- Establish clear incident-command and communications roles.
- Rehearse ransomware scenarios involving suppliers, regulators, law enforcement, customers, and the public.

**Sources:** [US DOJ — seizure of funds paid to DarkSide](https://www.justice.gov/archives/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside); [CISA — StopRansomware](https://www.cisa.gov/stopransomware)

## 20. 2021 — Microsoft Exchange Server exploitation

**Main topic:** Public-facing application vulnerabilities, web shells, mass exploitation  
**Attribution:** Microsoft and US government statements associated major early exploitation with HAFNIUM, assessed as China-based; other actors also exploited the vulnerabilities.

### What happened
In early 2021, attackers exploited multiple vulnerabilities in on-premises Microsoft Exchange Server. Depending on the vulnerability and environment, attackers could gain access, execute code, and install web shells to maintain remote access. After exploitation became public, additional groups scanned for and compromised vulnerable servers.

### Why it matters
A single internet-facing service can expose a large number of organizations. Once a vulnerability is widely known and exploitation tools circulate, patching must be rapid. Defenders cannot assume a patched server was never compromised.

### Defensive lessons
- Patch internet-facing systems urgently when active exploitation is reported.
- Check for web shells and other persistence mechanisms.
- Search historical logs and endpoint telemetry for exploitation, suspicious process creation, and outbound connections.
- Rotate credentials and investigate lateral movement after suspected compromise.
- Maintain an authoritative inventory of exposed services and owners.

### Study connection
Practice reading a vulnerability advisory, mapping a CVE to affected product versions, and writing a vulnerability-management ticket with exposure, risk, remediation, and verification steps.

**Sources:** [CISA — government release on Chinese cyber-threat activity and Exchange exploitation](https://www.cisa.gov/news-events/alerts/2021/07/19/us-government-releases-indictment-and-several-advisories-detailing); [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)

## 21. 2021 — Kaseya VSA supply-chain ransomware

**Main topic:** Managed service providers (MSPs), remote management tools, cascading compromise  
**Group:** REvil/Sodinokibi ransomware operators were associated with the campaign.

### What happened
In July 2021, attackers exploited Kaseya VSA, a remote monitoring and management product used by service providers. The incident enabled malicious activity to spread through MSP relationships to multiple downstream customers. This made it a service-provider and supply-chain incident, not simply a compromise of one company's endpoints.

### Why it matters
IT management tools often have extensive privileges across customer systems. A compromise of a trusted management plane can create a multiplier effect across many organizations.

### Defensive lessons
- Place management infrastructure behind strict access controls and MFA.
- Limit and monitor privileged management agents and administrative actions.
- Segment customer environments and prevent one tenant's compromise from freely spreading to others.
- Maintain independent backup and recovery channels outside the compromised management plane.
- Have coordinated communications and containment plans for affected customers and vendors.

**Source:** [CISA — Kaseya VSA supply-chain ransomware attack](https://www.cisa.gov/news-events/alerts/2021/07/02/kaseya-vsa-supply-chain-ransomware-attack)

## 22. 2021 — Log4Shell

**Main topic:** Java library vulnerability, remote code execution, software inventory  
**Identifier:** CVE-2021-44228; multiple actors exploited the weakness.

### What happened
In December 2021, a critical vulnerability in Apache Log4j 2 became public. In affected configurations, specially crafted input could trigger JNDI-related lookups and potentially lead to remote code execution. Log4j was embedded in many applications and products, making it difficult for organizations to identify every affected asset.

### Why it matters
The vulnerable component might be a dependency inside another application rather than a product that appears directly in the asset inventory. Patching only obvious servers may miss software bundles, cloud workloads, appliances, and third-party products.

### Defensive lessons
- Build a software and dependency inventory; use a software bill of materials (SBOM) where available.
- Identify affected versions in applications and vendor products, then apply vendor-supported fixes.
- Scan exposed assets and investigate signs of exploitation.
- Verify remediation; patching the Java runtime alone is not the same as patching the vulnerable Log4j library.
- Continue monitoring after the initial emergency because exploitation and secondary access can persist after patching.

### Study connection
Learn CVE identifiers, CVSS severity, dependency management, RCE, JNDI, and the difference between vulnerability scanning and compromise hunting.

**Source:** [CISA and partner agencies — Log4Shell mitigation advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-356a)

## 23. 2022 — AIIMS Delhi cyber incident

**Main topic:** Healthcare continuity, ransomware response, data confidentiality  
**Location:** New Delhi, India  
**Attribution:** Public reporting did not establish a definitive named individual or group.

### What happened
In November 2022, the All India Institute of Medical Sciences (AIIMS), New Delhi, suffered a major cyber incident that disrupted IT-dependent hospital services. Reports described systems being taken offline and digital services affected while investigators examined a suspected ransomware event. Public reporting included claims about data volume and ransom demands, but those claims should not be treated as verified facts unless corroborated by an official source.

### Why it matters
Healthcare downtime can affect patient registration, appointments, diagnostics, and administrative workflows. Recovery has to balance forensic preservation, data protection, clinical safety, and restoration of essential services.

### Defensive lessons
- Establish downtime procedures that allow patient care to continue safely.
- Separate clinical systems, administrative IT, and guest networks.
- Keep tested backups and validate that restoration will not reintroduce malware.
- Preserve logs and forensic evidence before rebuilding systems where possible.
- Use least privilege, MFA, patching, and network monitoring for sensitive healthcare environments.
- Communicate confirmed facts clearly and avoid amplifying unverified ransom or breach claims.

### Study connection
Compare this case with WannaCry. Both affected health services, but do not assume the same malware, initial-access vector, or responsible group without evidence.

**Sources:** [CERT-In — annual reports and incident trends](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBANULREPRT); [Government of India — cybersecurity response overview](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2116341&lang=2&reg=48)

## 24. 2023 — MOVEit Transfer mass exploitation

**Main topic:** Zero-day exploitation, SQL injection, web shells, data theft and extortion  
**Group:** FBI/CISA linked the campaign to the CL0P ransomware group and related actors.

### What happened
In May 2023, attackers exploited a previously unknown SQL injection vulnerability in Progress MOVEit Transfer, a managed file-transfer application. The FBI and CISA reported that the CL0P group exploited the vulnerability to place a web shell, access data, and exfiltrate files from vulnerable systems. Organizations using MOVEit to exchange files with employees, customers, or suppliers faced potential data theft.

### Why it matters
This was a mass-exploitation campaign centered on one product and vulnerability. In many cases, the main objective was stealing information and extorting affected organizations rather than deploying traditional file-encrypting ransomware across each victim environment.

### Defensive lessons
- Track internet-facing file-transfer products and apply vendor patches immediately.
- Check for compromise indicators and web shells, not just the current version number.
- Identify which files and external parties may have been exposed.
- Review vendor notifications, downstream data-processing obligations, and regulatory reporting.
- For high-value transfer services, minimize retained data and limit the sensitivity of files stored on the server.

**Sources:** [FBI/CISA joint advisory on CL0P and MOVEit (PDF)](https://www.cisa.gov/sites/default/files/2023-06/aa23-158a-stopransomware-cl0p-ransomware-gang-exploits-moveit-vulnerability_5_0.pdf); [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## 25. 2023 — MGM Resorts incident

**Main topic:** Social engineering, identity systems, business disruption  
**Attribution caveat:** Public reporting associated the incident with Scattered Spider, but MGM's SEC disclosure described the incident without independently establishing that group's responsibility.

### What happened
MGM Resorts International disclosed a cybersecurity incident in September 2023. The company took systems offline to contain risk, disrupting parts of hotel and casino operations and guest-facing services. MGM estimated a negative impact of approximately US$100 million on adjusted property earnings before interest, taxes, depreciation, amortization, and rent for the affected quarter, alongside incident-response expenses.

Public reporting described social engineering as a technique associated with the incident. Social engineering exploits people and organizational processes rather than relying only on software defects.

### Why it matters
Identity systems, help desks, and account-recovery workflows can be high-value attack targets. An attacker who convinces support staff to reset or transfer access can sometimes bypass otherwise strong technical controls.

### Defensive lessons
- Use phishing-resistant MFA for administrators and high-risk accounts.
- Verify help-desk identity requests with a documented, independent process.
- Monitor identity-provider changes, new MFA-device enrollment, suspicious session activity, and unusual privilege grants.
- Prepare fail-safe procedures for shutting down systems without losing incident coordination.
- Train staff using realistic social-engineering scenarios, then improve the process rather than simply blaming employees.

**Sources:** [MGM Resorts filing with the US Securities and Exchange Commission](https://www.sec.gov/Archives/edgar/data/789570/000119312523251667/d461062d8k.htm); [CISA — recognize and report phishing](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing)

## 26. 2024 — Change Healthcare ransomware

**Main topic:** Ransomware, healthcare ecosystem dependencies, third-party concentration  
**Group claim:** ALPHV/BlackCat claimed responsibility; describe attribution and stolen-data claims in line with the relevant evidence.

### What happened
Change Healthcare, a major healthcare claims and payment-processing provider owned by UnitedHealth Group, experienced a ransomware incident in February 2024. The company disconnected systems during response, causing disruption to pharmacy claims, provider payments, eligibility checks, and other healthcare workflows. UnitedHealth later said its investigation had found files containing protected health information or personally identifiable information that could affect a substantial proportion of people in the United States.

### Why it matters
A provider that sits between many insurers, pharmacies, clinics, and hospitals can become a single point of operational concentration. An incident at one intermediary can affect many organizations that are not directly breached themselves.

### Defensive lessons
- Apply MFA to remote and privileged access and monitor identity-policy exceptions.
- Map business dependencies and establish fallback processes for critical suppliers.
- Keep tested recovery procedures and alternatives for claims, payments, and pharmacy workflows.
- Minimize retained data and regularly review third-party access.
- Integrate incident response with business continuity, privacy, legal, and clinical operations.
- Treat ransom payment as no guarantee that data will be deleted or services restored safely.

**Sources:** [UnitedHealth Group — Change Healthcare incident update](https://www.unitedhealthgroup.com/newsroom/2024/2024-04-22-uhg-updates-on-change-healthcare-cyberattack.html); [US Senate Finance Committee — hearing on the Change Healthcare attack](https://www.finance.senate.gov/hearings/hacking-americas-health-care-assessing-the-change-healthcare-cyber-attack-and-whats-next)

## 27. 2024 — Snowflake customer-data theft campaign

**Main topic:** Stolen credentials, cloud data platforms, MFA, third-party access  
**Threat-intelligence tracking:** Mandiant tracked the campaign as UNC5537.

### What happened
In 2024, attackers used stolen credentials to access certain customer instances in Snowflake's cloud data platform and steal data for extortion. Public investigations reported that credentials had often been taken from infected customer computers by information-stealing malware. The campaign was not described as a compromise of Snowflake's underlying platform software; the focus was on customer credentials, account protection, and the configuration of individual environments.

### Why it matters
A cloud service can operate as designed while a customer account is compromised. Security responsibilities are shared: the provider secures its platform, while customers must protect identity credentials, access policies, data permissions, and monitoring.

### Defensive lessons
- Require MFA, preferably phishing-resistant MFA, for sensitive cloud accounts.
- Rotate credentials exposed on infected endpoints and investigate the endpoint that leaked them.
- Remove unused accounts and credentials and restrict access by role and network where appropriate.
- Review unusual data-download volume, unfamiliar sessions, and access from anomalous locations.
- Keep sensitive datasets access-controlled and minimize unnecessary data retention.
- Do not assume that buying a cloud service automatically makes its configuration secure.

**Source:** [Google Cloud/Mandiant — UNC5537 Snowflake customer-data theft and extortion](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion)

## 28. 2024 — CrowdStrike update outage (not a cyberattack)

**Main topic:** Change management, software quality, resilience, recovery at scale  
**Classification:** An operational outage caused by a faulty security-content update, not a malicious intrusion.

### What happened
On 19 July 2024, a faulty CrowdStrike Falcon content update caused Windows systems running affected software to crash. The outage disrupted organizations across sectors, including travel, healthcare, and business services. CrowdStrike published post-incident material describing the technical failure and remediation.

### Why it belongs in a cyber incident notebook
Cybersecurity teams must reduce both malicious risk and operational risk introduced by security tools. A security product with deep operating-system privileges can have a large blast radius if an update fails.

### Defensive lessons
- Roll out updates in staged rings instead of deploying all changes everywhere at once.
- Test updates against representative systems and preserve rollback procedures.
- Avoid single points of failure in critical business processes.
- Maintain break-glass access and recovery media for systems that fail to boot.
- Ensure third-party security controls have accountable change management, monitoring, and communication plans.

**Source:** [CrowdStrike — Falcon content-update remediation and guidance hub](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/)

---

# People and groups worth knowing

Names can be useful for historical study, but do not assume an actor's identity from a nickname or malware similarity alone.

| Person/group | Known for | Study point |
|---|---|---|
| **Robert Tappan Morris** | The 1988 Morris Worm | Intent and actual impact can differ; self-propagating code can destabilize systems. |
| **Michael Calce (Mafiaboy)** | 2000 DDoS attacks | Availability attacks can disrupt large services without stealing data. |
| **Albert Gonzalez** | Retail payment-card theft cases | Criminal use of intrusions for payment-card data theft. Do not casually label him the operator of the 2013 Target breach. |
| **Khalil Shreateh** | Unauthorized Facebook vulnerability demonstration in 2013 | Often cited as a grey-hat example; good intentions do not replace authorization. |
| **Paras Jha, Josiah White, Dalton Norman** | Mirai-related cases | Insecure IoT devices can be converted into DDoS infrastructure. |
| **Lazarus Group** | Threat cluster associated by governments and researchers with North Korean cyber operations | Study the distinction between technical clustering, public attribution, and legal allegations. |
| **APT28 / Fancy Bear** | Activity publicly attributed by several governments to Russia's GRU | State-linked espionage, credential theft, and influence-related operations. |
| **Sandworm / GRU Unit 74455** | Destructive campaigns including public attribution for NotPetya and activity against Ukrainian infrastructure | Cyber operations can target availability and physical services, not only data. |
| **DarkSide** | Colonial Pipeline ransomware operation | Ransomware can create consequences beyond the direct victim. |
| **REvil / Sodinokibi** | Kaseya VSA ransomware campaign | Compromised service providers can extend impact across downstream customers. |
| **CL0P** | MOVEit Transfer mass data theft/extortion campaign | Exploiting one widely used product can affect many organizations. |
| **Scattered Spider** | Social-engineering-focused intrusions described in security reporting | Identity verification and support processes are part of the security perimeter. |
| **UNC5537** | Mandiant's tracking name for the Snowflake customer-data theft campaign | A tracking label is not necessarily a verified legal identity. |
| **Santiago López** | Ethical hacker known for authorized bug bounty work | Legitimate scope and responsible disclosure distinguish ethical testing from unauthorized intrusion. |

## Hacker categories: apply them carefully

- **White hat:** Works with explicit authorization and a defined scope; reports findings through an agreed process.
- **Black hat:** Uses unauthorized access or other prohibited techniques for theft, extortion, sabotage, or other malicious goals.
- **Grey hat:** Finds or tests weaknesses without authorization and may later disclose them. A helpful motive does not make unapproved access lawful.
- **Script kiddie:** Informal label for someone who relies heavily on existing tools or scripts with limited understanding; not a precise legal category.
- **Hacktivist:** Uses cyber activity to advance a political or ideological cause. Actions may still be illegal and harmful.
- **State-sponsored/state-linked actor:** Activity is attributed to, supported by, or aligned with a state. State the exact relationship and confidence level where possible.
- **Cyberterrorism:** A contested term. Do not label every defacement, hacktivist act, or political DDoS attack cyberterrorism without explaining the definition and evidence.

**Core rule:** Authorization, intent, methods, impact, and applicable law matter more than the tool used. Test only systems you own or are explicitly permitted to assess.

---

# Attack patterns and defensive lessons

| Pattern | Cases illustrating it | Defensive priority |
|---|---|---|
| Unpatched vulnerable service | WannaCry, Equifax, Exchange Server, Log4Shell, MOVEit | Asset inventory, exploit-aware patching, verification |
| Credential theft or social engineering | Yahoo, MGM, Snowflake campaign | MFA, phishing resistance, session monitoring, help-desk controls |
| Third-party or software supply chain | Target, SolarWinds, Kaseya, NotPetya | Vendor access restrictions, build protection, segmentation, dependency inventory |
| Ransomware and destructive malware | WannaCry, NotPetya, Colonial Pipeline, Change Healthcare | Tested backups, containment, identity protection, business continuity |
| Data theft and extortion | Equifax, MOVEit, Snowflake, Yahoo | Data minimization, access controls, egress monitoring, privacy response |
| DDoS and botnets | Mafiaboy, Estonia, Mirai/Dyn | Upstream mitigation, traffic baselines, resilient DNS |
| OT/critical infrastructure | Stuxnet, Ukraine grid, KKNPP, Colonial Pipeline | IT/OT segmentation, safe recovery procedures, asset visibility |
| Malware/endpoint investigation | Morris Worm, Sony, WannaCry, SolarWinds | EDR, centralized logs, isolation, evidence preservation |
| Identity and privilege abuse | SolarWinds follow-on activity, MGM, Snowflake | Least privilege, MFA, alerting on role and session changes |
| Concentration and resilience risk | Dyn, Change Healthcare, CrowdStrike outage | Redundancy, alternatives, tested rollback and downtime procedures |

## Incident-response workflow for a SOC analyst

Use this as a learning checklist. Follow your organization's approved playbooks and authority limits.

1. **Triage:** Confirm the alert source, affected asset, timestamp, user, severity, and business context. Determine whether this is suspected activity or a confirmed incident.
2. **Scope:** Identify related hosts, accounts, network connections, cloud resources, and data. Build a timeline.
3. **Preserve evidence:** Retain relevant logs, alerts, endpoint telemetry, email artifacts, memory/disk evidence where authorized, and hashes of collected files. Follow legal and organizational evidence-handling requirements.
4. **Contain:** Coordinate isolation of affected endpoints or accounts, revoke compromised sessions, disable malicious access, or block confirmed indicators. Consider business and safety impacts before changing critical systems.
5. **Eradicate:** Remove persistence and malware, close the abused access path, patch the root cause, reset exposed credentials, and check for secondary access.
6. **Recover:** Restore clean systems from trusted backups, validate critical functions, monitor closely, and return services gradually.
7. **Communicate:** Inform incident leadership, legal/privacy teams, service owners, and relevant authorities according to policy and law.
8. **Learn:** Document root cause, control gaps, what worked, detection delays, corrective actions, owners, and deadlines.

### Useful SOC evidence sources
- Authentication and identity-provider logs
- Endpoint Detection and Response alerts
- Windows Event Logs and Linux authentication/system logs
- DNS, firewall, proxy, VPN, and network-flow telemetry
- Email gateway, mail-audit, and phishing-report data
- Cloud audit logs and storage/data-access logs
- Vulnerability scanner output and software inventory
- Backup, EDR, and security-appliance administrative logs

### Questions to ask during triage
- What is the first known suspicious event?
- Was the account expected to access this asset at that time?
- Is the source internal, external, or a service provider?
- Was data read, changed, deleted, encrypted, or transferred out?
- What evidence supports the suspected root cause?
- Is the activity still continuing?
- What would be the impact of isolating this system?
- How will we confirm that recovery is safe?

---

# Practical study exercises

Complete these using public reports or your own isolated lab. Do not test against real organizations without written authorization.

### Exercise 1 — Build an incident timeline
Choose SolarWinds, WannaCry, MOVEit, or the Snowflake campaign. Record five to ten events with timestamp, evidence source, action, and confidence level. Separate facts from analyst hypotheses.

### Exercise 2 — Map the attack chain
Create a table with columns: Stage, Evidence, Possible MITRE ATT&CK technique, Detection source, Mitigation. Use [MITRE ATT&CK](https://attack.mitre.org/) for technique names, but only map techniques supported by the source.

### Exercise 3 — Write a SOC alert
Write a short alert for unusual PowerShell execution, repeated failed logins followed by success, suspicious bulk downloads, or an unexpected new admin account. Include severity, host/user, timestamps, evidence, and next steps. Mark unconfirmed conclusions as suspected.

### Exercise 4 — Patch-management review
Use Equifax, Exchange, Log4Shell, and MOVEit to compare:
- How exposed assets were identified.
- Whether the vulnerability was known or a zero-day at exploitation time.
- What patch verification should look like.
- How you would hunt for prior exploitation.

### Exercise 5 — Incident report
Write one page with these headings: Executive Summary, Scope, Timeline, Initial Access, Impact, Containment, Recovery, Root Cause, Lessons Learned, and Open Questions. Do not claim certainty where evidence is incomplete.

### Exercise 6 — Small defensive lab
In a local lab you control, collect normal DNS and HTTP traffic with Wireshark, read authentication logs, test a harmless local web application, and produce a short baseline of normal behavior. Then use a prebuilt safe training scenario to practice triage. Do not reproduce ransomware, launch public DDoS, or access third-party systems.

---

# Glossary

- **APT (Advanced Persistent Threat):** A term often used for a capable, persistent threat actor or campaign. It does not automatically prove state sponsorship.
- **Attribution:** Assessment of who was responsible. It may be technical, intelligence-based, legal, or public/political, and confidence varies.
- **Botnet:** A collection of compromised devices controlled together.
- **C2 (Command and Control):** Infrastructure or methods used by an attacker to direct compromised systems.
- **CVE:** Common Vulnerabilities and Exposures identifier for a publicly catalogued vulnerability.
- **DDoS:** Distributed denial of service; an attempt to overwhelm a target or its dependencies with traffic or requests.
- **EDR:** Endpoint Detection and Response; endpoint telemetry and tools for investigating and responding to suspicious behavior.
- **Exfiltration:** Unauthorized removal or transfer of data from an environment.
- **IOC (Indicator of Compromise):** An observable artifact associated with suspected or known malicious activity, such as a hash, domain, IP address, or filename. IOCs can be stale or shared with legitimate infrastructure, so add context.
- **Lateral movement:** Movement from one compromised host or account to others in a target environment.
- **MFA:** Multi-factor authentication; authentication requiring evidence from multiple factor categories.
- **Ransomware:** Malware or an intrusion operation used to extort victims, commonly by encrypting systems, stealing data, or both.
- **RCE:** Remote code execution; a vulnerability or condition allowing code to execute on another system remotely.
- **SOC:** Security Operations Center; a team or function that monitors, investigates, and responds to security events.
- **Supply-chain attack:** An attack that abuses a vendor, software build/update, service provider, or dependency to affect downstream targets.
- **TTPs:** Tactics, Techniques, and Procedures used to describe how an adversary operates.
- **Wiper:** Malware designed to destroy or render data/systems unusable rather than primarily to restore them after ransom payment.
- **Zero-day:** A vulnerability exploited before an appropriate patch is available to affected defenders. Usage varies, so explain the timeline when precision matters.

---

# Recommended source library

Prefer primary or high-quality sources for incident research. These sources are useful for follow-up reading and should be checked for updates.

## Government and law-enforcement sources
- [CISA — Cybersecurity Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)
- [CISA — Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [CISA — StopRansomware](https://www.cisa.gov/stopransomware)
- [CISA — Industrial Control Systems advisories](https://www.cisa.gov/news-events/ics-advisories)
- [US Department of Justice — Computer crime and cybercrime news](https://www.justice.gov/news)
- [FBI — Cases and criminals](https://www.fbi.gov/history/cases-and-criminals)
- [UK National Cyber Security Centre](https://www.ncsc.gov.uk/)
- [CERT-In — Annual reports](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBANULREPRT)
- [CERT-In — Advisories](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBADVLIST)
- [India Press Information Bureau — government cyber-security releases](https://pib.gov.in/)

## Technical and research sources
- [MITRE ATT&CK](https://attack.mitre.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [NIST National Vulnerability Database](https://nvd.nist.gov/)
- [Google Cloud / Mandiant threat intelligence](https://cloud.google.com/blog/topics/threat-intelligence)
- [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/)
- [CrowdStrike — incident update hub for the July 2024 outage](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/)

## India-specific incident context
- [CERT-In](https://www.cert-in.org.in/) is India's national incident-response agency.
- [Kudankulam network infection — PIB, Government of India](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1592498&lang=2&reg=48)
- [Cosmos Bank Annual Report 2018–19](https://cosmos.bank.in/auth/writereaddata/files/110521193370101_Cosmos-Bank-AR-2018-19_web.pdf)

---

## Final revision checklist

Before calling an incident analysis complete, confirm that you can explain:

- [ ] The incident date and affected organization.
- [ ] The target's business or operational role.
- [ ] Initial access and the confirmed attack path, if known.
- [ ] The malware, vulnerability, account, or process involved.
- [ ] The impact on confidentiality, integrity, and availability.
- [ ] The evidence supporting actor attribution and how certain it is.
- [ ] The containment and recovery actions.
- [ ] Three realistic controls that could prevent or limit a similar incident.
- [ ] One lesson for a penetration tester and one lesson for a SOC analyst.
- [ ] At least two credible sources, including a primary source where available.

*Last reviewed for this study note: October 2026. Historical incident summaries are static, but source links, attribution assessments, and remediation guidance may evolve. This file is educational and does not authorize testing of third-party systems.*
