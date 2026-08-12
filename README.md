# Penetration-Testing Recruiter Project

A comprehensive penetration testing portfolio demonstrating **end-to-end security assessment capabilities** — from reconnaissance through exploitation to professional reporting. Built to showcase technical depth, methodology, and compliance-aware practices to potential security employers.

## Project Overview

| Phase | Focus | Tools |
|-------|-------|-------|
| 🔍 Reconnaissance | Public data collection, network discovery | LinkedIn OSINT scraper, TCP/IP fingerprinter |
| 🔎 Vulnerability Analysis | CVE mapping, risk prioritization | Custom vulnerability scanner |
| 🎯 Exploitation | Payload generation, attack simulation | Custom exploit framework |
| 🛡️ Post-Exploitation | Persistence, data exfiltration | Simulated post-exploitation modules |
| 📊 Reporting | Executive/technical reports | Markdown templates with sample data |

---

## Key Features

- **Ethical OSINT Collection** (`recon/linkedin_osint.py`): Demonstrates responsible reconnaissance that respects LinkedIn's Terms of Service, implements rate limiting, and follows GDPR/CCPA compliance principles.
- **Advanced TCP/IP Fingerprinting** (`recon/tcp_fingerprint.py`): Low-level packet crafting for OS detection, implementing techniques like TTL analysis, TCP option parsing, and window-size fingerprinting.
- **CVE-Based Vulnerability Scanning** (`analysis/vulnerability_scanner.py`): Maps service fingerprints to known CVEs with CVSS scoring and exploitability assessment using a local SQLite vulnerability database.
- **Sample Data Integration** (`analysis/vulnerability_scanner.csv`): Contains real-world findings from simulated assessments (CVE-2020-1472 Zerologon, CVE-2017-0144 EternalBlue, SQL injection examples).

---

## Repository Structure

```
penetration-testing-project/
├── recon/
│   ├── linkedin_osint.py              # Ethical LinkedIn OSINT scraper
│   ├── tcp_fingerprint.py             # TCP/IP stack fingerprinting tools
│   └── network_discovery.py           # Internal network scanner
├── analysis/
│   ├── vulnerability_scanner.py      # CVE correlation & risk scoring
│   └── vulnerability_scanner.csv     # Sample vulnerability findings
├── exploitation/
│   ├── payload_generator.py          # Custom payload creation
│   └── post_exploitation.py          # Persistence & lateral movement
├── reports/
│   ├── executive_summary.md          # Board-level findings report
│   ├── technical_report.md           # Detailed technical analysis
│   └── remediation.md                # Strategic mitigation roadmap
├── scripts/
│   ├── automated_recon.sh            # Recon automation script
│   ├── vuln_scan.sh                  # Automated vulnerability scan
│   └── exploitation_workflow.sh      # End-to-end exploitation pipeline
├── .github/workflows/
│   └── ci.yml                        # GitHub Actions CI pipeline
└── README.md                         # This file
```

---

## How to Use

### Prerequisites

```bash
# Python 3.11+
python --version

# Required packages
pip install -r requirements.txt  # or
pip install requests sqlite3 nmap

# Optional tools
# - nmap (for network scanning)
# - metasploit-framework (for exploitation)
```

### Quick Start

```bash
# Clone the repository
git clone https://github.com/sinethembakhumalo33/penetration-testing-project.git
cd penetration-testing-project

# Run the automated recon workflow
./scripts/automated_recon.sh <target_domain_or_ip>

# Perform a vulnerability scan
python analysis/vulnerability_scanner.py <target>

# Review sample findings
cat analysis/vulnerability_scanner.csv
```

### Running Individual Modules

```bash
# LinkedIn OSINT (ethical, rate-limited)
python recon/linkedin_osint.py

# TCP Fingerprinting
python recon/tcp_fingerprint.py <target_ip>

# Vulnerability Scanning
python analysis/vulnerability_scanner.py
```

---

## Methodology

This project follows the **OWASP Testing Guide** and **PTES (Penetration Testing Execution Standard)** methodology:

1. **Pre-assessment** — Scope definition, compliance review
2. **Intelligence Gathering** — Passive OSINT, public records search
3. **Active Testing** — Network scanning, service identification
4. **Vulnerability Detection** — CVE correlation, exploitability scoring
5. **Exploitation** — Demonstrated attack vectors (simulated)
6. **Post-Exploitation** — Impact analysis, persistence simulation
7. **Reporting** — Executive summaries, technical findings, remediation

---

## Sample Findings

The `reports/` directory contains completed templates with sample data demonstrating:

- **Critical Vulnerability**: CVE-2020-1472 (Zerologon) — CVSS 9.8
- **High Severity**: CVE-2017-0144 (EternalBlue) — CVSS 8.8
- **Medium Risk**: SQL Injection — CVSS 7.5
- **Low Risk**: Excessive Permissions — CVSS 4.3

Full technical details with attack narratives and remediation steps are in:
- [reports/executive_summary.md](reports/executive_summary.md)
- [reports/technical_report.md](reports/technical_report.md)
- [reports/remediation.md](reports/remediation.md)

---

## Portfolio Highlights

This repository demonstrates skills in:

- 🔐 **Security Testing**: Vulnerability assessment, penetration testing, risk analysis
- 🛠️ **Tool Development**: Custom Python tools for reconnaissance and scanning
- 📊 **Reporting**: Executive communication and technical documentation
- 🛡️ **Compliance**: Ethical data collection, privacy-by-design principles
- ⚙️ **Automation**: CI/CD integration, workflow scripting, reproducible assessments
- 🧠 **Problem Solving**: Advanced OSINT techniques, CVE research, exploit development

---

## License & Ethics

This project is for **educational and professional portfolio purposes only**. All techniques demonstrated:

- **Comply with platform TOS** (LinkedIn, GitHub, etc.)
- **Implement rate limiting** to avoid service disruption
- **Respect data privacy** (GDPR, CCPA compliance)
- **Require explicit authorization** for real-world use
- **Document consent** in all testing engagements

**Never deploy these tools against systems you do not own or lack written authorization to test.**

---

## Contact

- GitHub: [@sinethembakhumalo33](https://github.com/sinethembakhumalo33)
- Project: [penetration-testing-project](https://github.com/sinethembakhumalo33/penetration-testing-project)
- Security Research | Portfolio Project | Educational Use

---

⭐ **If you're a recruiter or hiring manager, feel free to explore the codebase, run the tools, or reach out with any questions about the methodology and findings.**
