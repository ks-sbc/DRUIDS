---
title: "Security Audits for Revolutionary Organizations"
description: "Comprehensive security audit framework for organizing groups, with automated tools and remediation guides"
created: 2025-07-05
updated: 2025-07-05
type: "docs/how-to"
security: "L1"
version: "1.0.0"
document_id: "HTG-SEC-2025-192-L1"
tags: ["security", "audit", "tools", "vulnerabilities", "remediation"]
draft: false
author: ["KSBC Security Committee"]
---

# Security Audits for Revolutionary Organizations

## Quick Start Checklist (Do This First!)

### ☐ Physical Security (5 minutes)
- [ ] Devices locked when not in use
- [ ] Sensitive documents secured
- [ ] Meeting location swept for recording devices
- [ ] No photography of sensitive materials
- [ ] "Clean" devices for sensitive meetings

### ☐ Digital Security (10 minutes)
- [ ] Password manager being used
- [ ] 2FA enabled on critical accounts
- [ ] Software updates installed
- [ ] VPN active for organizing work
- [ ] Encrypted storage enabled

### ☐ Communication Security (5 minutes)
- [ ] Using Signal/encrypted messaging
- [ ] No sensitive info in emails
- [ ] Meeting links not public
- [ ] Phone numbers protected
- [ ] Metadata removed from files

## Common Vulnerabilities in Organizing Contexts

### 1. The Activist Phone Problem
**Vulnerability**: Using personal phones for organizing
**Risk**: Complete social graph exposure, location tracking, message interception
**Remediation**:
```bash
# Separate organizing identity
- Get dedicated organizing phone/number
- Use GrapheneOS or CalyxOS
- Never link to personal accounts
- Keep powered off when not organizing
```

### 2. The Meeting Link Leak
**Vulnerability**: Reusing Zoom/Jitsi links publicly
**Risk**: Infiltration, recording, disruption
**Remediation**:
```bash
# Secure meeting protocol
- Generate unique links per meeting
- Require passwords + waiting room
- Share links only via Signal
- Never post links publicly
- Have backup communication channel
```

### 3. The Git History Exposure
**Vulnerability**: Real names/locations in Git history
**Risk**: Complete member identification
**Remediation**:
```bash
# Clean Git history
git filter-branch --env-filter '
export GIT_AUTHOR_NAME="Comrade47"
export GIT_AUTHOR_EMAIL="comrade47@protonmail.com"
export GIT_COMMITTER_NAME="Comrade47"
export GIT_COMMITTER_EMAIL="comrade47@protonmail.com"
' --tag-name-filter cat -- --branches --tags

# Prevent future exposure
git config user.name "YourPseudonym"
git config user.email "pseudonym@protonmail.com"
```

### 4. The Cloud Storage Trap
**Vulnerability**: Using Google Drive/Dropbox for organizing docs
**Risk**: Corporate surveillance, sudden deletion, legal requests
**Remediation**:
```bash
# Migrate to secure alternatives
- Set up Nextcloud instance
- Use Cryptpad for collaboration
- Git for permanent records
- Local encrypted backups
```

### 5. The Social Media OPSEC Fail
**Vulnerability**: Organizing on Facebook/Twitter
**Risk**: Network mapping, predictive policing, infiltration
**Remediation**:
- Move organizing off corporate platforms
- Use purpose-specific accounts
- Never connect personal/organizing identities
- Assume all posts are monitored

## Automated Security Scanning Tools

### Git Repository Scanner
Save as `security-scan.sh`:

```bash
#!/bin/bash
# Automated security scanner for organizing repositories

echo "=== DRUIDS Security Scanner v1.0 ==="
echo "Starting scan at $(date)"
echo ""

# Check for exposed secrets
echo "[*] Scanning for exposed secrets..."
git grep -E "(password|api_key|secret|token|private_key)" || echo "✓ No obvious secrets found"

# Check for personal information
echo -e "\n[*] Scanning for personal information..."
git grep -E "([0-9]{3}-[0-9]{2}-[0-9]{4}|[0-9]{3}\.[0-9]{3}\.[0-9]{4})" || echo "✓ No SSNs found"
git grep -E "\b[A-Z][a-z]+ [A-Z][a-z]+\b" | grep -v -E "(Comrade|Worker|Organizer)" | head -20 || echo "✓ No obvious real names"

# Check commit authors
echo -e "\n[*] Checking commit authors..."
git log --format='%aN <%aE>' | sort -u | grep -E "(@gmail|@yahoo|@hotmail|real.*name)" || echo "✓ No personal emails found"

# Check for dangerous files
echo -e "\n[*] Checking for dangerous files..."
find . -name "*.env" -o -name "*password*" -o -name "*secret*" -o -name "*.key" | grep -v ".git" || echo "✓ No dangerous files found"

# Check file permissions
echo -e "\n[*] Checking file permissions..."
find . -type f -perm /077 -ls 2>/dev/null | grep -v ".git" || echo "✓ No world-writable files"

# Repository statistics
echo -e "\n[*] Repository statistics:"
echo "Total commits: $(git rev-list --all --count)"
echo "Contributors: $(git log --format='%aN' | sort -u | wc -l)"
echo "Branches: $(git branch -a | wc -l)"
echo "Tags: $(git tag | wc -l)"

echo -e "\n[✓] Scan complete at $(date)"
```

### Network Security Scanner
Save as `network-scan.py`:

```python
#!/usr/bin/env python3
"""Network security scanner for organizing infrastructure"""

import subprocess
import socket
import ssl
import sys

def scan_domain(domain):
    """Basic security scan of organizing domain"""
    print(f"\n[*] Scanning {domain}...")
    
    # Check DNS
    try:
        ip = socket.gethostbyname(domain)
        print(f"✓ Resolves to: {ip}")
    except:
        print(f"✗ DNS resolution failed")
        return
    
    # Check common ports
    ports = {
        80: "HTTP",
        443: "HTTPS", 
        22: "SSH",
        25: "SMTP",
        3306: "MySQL",
        5432: "PostgreSQL"
    }
    
    print("\n[*] Port scan:")
    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"  - Port {port} ({service}): OPEN")
        sock.close()
    
    # Check SSL certificate
    if check_port_open(domain, 443):
        print("\n[*] SSL Certificate check:")
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    print(f"  ✓ Valid until: {cert['notAfter']}")
        except Exception as e:
            print(f"  ✗ SSL Error: {e}")

def check_port_open(host, port):
    """Check if port is open"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 network-scan.py domain.com")
        sys.exit(1)
    
    scan_domain(sys.argv[1])
```

### Device Security Checker
Save as `device-check.sh`:

```bash
#!/bin/bash
# Device security checker for organizers

echo "=== Device Security Audit ==="
echo ""

# Check disk encryption
echo "[*] Disk Encryption Status:"
if command -v dmsetup &> /dev/null; then
    sudo dmsetup status | grep -q crypt && echo "✓ Disk encryption enabled" || echo "✗ Disk encryption NOT enabled"
else
    echo "⚠ Cannot verify disk encryption"
fi

# Check firewall
echo -e "\n[*] Firewall Status:"
if command -v ufw &> /dev/null; then
    sudo ufw status | grep -q "Status: active" && echo "✓ Firewall active" || echo "✗ Firewall inactive"
elif command -v iptables &> /dev/null; then
    sudo iptables -L | grep -q "Chain" && echo "✓ iptables rules present" || echo "✗ No iptables rules"
fi

# Check updates
echo -e "\n[*] System Updates:"
if command -v apt &> /dev/null; then
    updates=$(apt list --upgradable 2>/dev/null | grep -c upgradable)
    [ $updates -eq 0 ] && echo "✓ System up to date" || echo "✗ $updates updates available"
fi

# Check for suspicious processes
echo -e "\n[*] Suspicious Processes:"
ps aux | grep -E "(keylog|capture|sniff)" | grep -v grep || echo "✓ No obvious keyloggers"

# Check SSH configuration
echo -e "\n[*] SSH Security:"
if [ -f /etc/ssh/sshd_config ]; then
    grep -q "PasswordAuthentication no" /etc/ssh/sshd_config && echo "✓ Password auth disabled" || echo "⚠ Password auth enabled"
    grep -q "PermitRootLogin no" /etc/ssh/sshd_config && echo "✓ Root login disabled" || echo "⚠ Root login allowed"
fi

echo -e "\n[✓] Device check complete"
```

## Monthly Security Audit

### Personnel Security (L1)
1. **Access Review**
   - [ ] Review who has access to repositories
   - [ ] Check for inactive members still in systems
   - [ ] Verify emergency contacts updated
   - [ ] Run automated scan: `./security-scan.sh`
   
   ```bash
   # Automated access audit
   git log --format='%aN' --since="6 months ago" | sort -u > active-users.txt
   git log --format='%aN' | sort -u > all-users.txt
   comm -13 active-users.txt all-users.txt > inactive-users.txt
   echo "Inactive users to review:"
   cat inactive-users.txt
   ```

2. **Password Audit**
   - [ ] All passwords unique and strong
   - [ ] Shared passwords rotated
   - [ ] Recovery codes backed up securely
   - [ ] Check password manager health:
   
   ```bash
   # Password audit checklist
   echo "=== Password Audit ==="
   echo "1. Open password manager"
   echo "2. Run security audit/watchtower"
   echo "3. Fix any weak/duplicate passwords"
   echo "4. Update shared vault passwords"
   echo "5. Verify 2FA on all critical accounts"
   ```

3. **Device Security**
   - [ ] Full disk encryption enabled
   - [ ] Auto-lock configured (5 minutes)
   - [ ] Find My Device/remote wipe ready
   - [ ] Backups encrypted and tested
   - [ ] Run device checker: `./device-check.sh`

### Operational Security (L1)
1. **Meeting Security**
   - [ ] Using secure video platforms
   - [ ] Recording policies followed
   - [ ] Minutes properly classified (L0/L1/L2)
   - [ ] No phones during sensitive discussions

2. **Communication Audit**
   - [ ] Signal disappearing messages enabled
   - [ ] Email signatures don't leak info
   - [ ] Social media OPSEC maintained
   - [ ] Metadata stripped from shared files

3. **Git Security**
   - [ ] No secrets in commit history
   - [ ] Proper .gitignore configured
   - [ ] Commits use pseudonyms consistently
   - Action: `git secrets --scan`

### Infrastructure Security (L2)
1. **Repository Audit**
   - [ ] Access logs reviewed
   - [ ] Unusual activity investigated
   - [ ] Backups tested and verified
   - [ ] Encryption keys rotated quarterly

2. **Emergency Procedures**
   - [ ] Panic button procedures known
   - [ ] Legal contacts accessible
   - [ ] Raid response plan current
   - [ ] Data destruction ready if needed

## Quarterly Deep Audit

### Comprehensive Security Review

#### Phase 1: Threat Assessment (Week 1)

**Current Threat Landscape Analysis**:
```bash
# Document current threats
cat > audits/Q4-2024-threats.md << EOF
# Q4 2024 Threat Assessment

## State Surveillance
- Local police capabilities: [assess]
- Federal interest level: [low/medium/high]
- Recent operations in area: [document]

## Corporate Threats  
- Platform deplatforming risk: [assess]
- Employment retaliation risk: [assess]
- Financial service denial: [assess]

## Fascist/Right-wing Threats
- Local group activity: [document]
- Doxxing attempts: [number]
- Physical threat level: [assess]

## Infiltration Indicators
- Suspicious new members: [list]
- Unusual questions/interest: [note]
- Technical anomalies: [describe]
EOF
```

**Adversary Capability Matrix**:
| Adversary | Technical | Physical | Legal | Financial |
|-----------|-----------|----------|--------|-----------|
| Local Police | Medium | High | High | Low |
| Federal Agencies | High | High | High | Medium |
| Corporations | High | Low | Medium | High |
| Fascist Groups | Low | Medium | Low | Low |

#### Phase 2: Technical Audit (Week 2)

**Infrastructure Deep Scan**:
```bash
#!/bin/bash
# Quarterly infrastructure audit

echo "=== Quarterly Security Deep Scan ==="

# Scan all repositories
for repo in $(find ~/organizing -name ".git" -type d); do
    echo "Scanning: $repo"
    cd $(dirname $repo)
    ./security-scan.sh
    echo "---"
done

# Check all domains
for domain in $(cat infrastructure/domains.txt); do
    python3 network-scan.py $domain
done

# Audit all servers
ansible all -m shell -a "uname -a; uptime; df -h"
```

**Penetration Testing Checklist**:
- [ ] Password spray against services
- [ ] Check for default credentials
- [ ] Test backup restoration
- [ ] Verify encryption at rest
- [ ] Check network segmentation
- [ ] Test incident response

#### Phase 3: Personnel Security Review (Week 3)

**Member Security Practices Audit**:
```bash
# Create security survey
cat > audits/security-survey.md << EOF
# Member Security Self-Assessment

Name (pseudonym): ________________
Date: ________________

## Device Security
- [ ] Full disk encryption enabled
- [ ] Strong device passwords/biometrics
- [ ] Auto-lock configured
- [ ] Regular updates installed

## Account Security  
- [ ] Using password manager
- [ ] 2FA on all critical accounts
- [ ] No password reuse
- [ ] Recovery codes secured

## Operational Security
- [ ] Separate organizing identity
- [ ] Using Signal for sensitive comms
- [ ] Following meeting security protocols
- [ ] No sensitive data on personal devices

## Training Needs
What security topics need clarification?
_________________________________
EOF
```

#### Phase 4: Remediation Planning (Week 4)

**Risk Prioritization Matrix**:
```
         Impact →
    ↓    Low    Medium    High
Likely   🟡      🟠       🔴
Possible 🟢      🟡       🟠  
Unlikely 🟢      🟢       🟡

🔴 Critical - Fix immediately
🟠 High - Fix within 30 days
🟡 Medium - Fix within 90 days
🟢 Low - Track and monitor
```

### Security Audit by Threat Level

#### Threat Level: GREEN (Normal Operations)
Focus: Maintaining good practices

```bash
# Weekly tasks
- [ ] Review access logs
- [ ] Update software
- [ ] Backup verification
- [ ] Security news review

# Monthly tasks  
- [ ] Password rotation
- [ ] Access review
- [ ] Device audit
- [ ] Training refresher
```

#### Threat Level: YELLOW (Elevated Concern)
Trigger: Increased state attention, threats received

```bash
# Immediate actions
- [ ] Notify all members of elevation
- [ ] Review and update emergency contacts
- [ ] Ensure backups are current
- [ ] Brief legal support

# Enhanced monitoring
- [ ] Daily log reviews
- [ ] Increase meeting security
- [ ] Limit new member access
- [ ] Prepare grab bags
```

#### Threat Level: ORANGE (High Alert)
Trigger: Active surveillance confirmed, immediate threats

```bash
# Immediate lockdown
- [ ] Freeze new access
- [ ] Audit all accounts
- [ ] Move to high-security comms only
- [ ] Implement buddy system

# Operational changes
- [ ] In-person meetings only
- [ ] Rotate meeting locations  
- [ ] Use burner devices
- [ ] Legal team on standby
```

#### Threat Level: RED (Emergency)
Trigger: Raids, arrests, active targeting

See: [[when-they-come-knocking|When They Come Knocking]]

### Incident Response Procedures

#### Security Incident Playbook

**1. Identification** (0-1 hour)
```bash
# Document everything
echo "Incident detected: $(date)" > incident.log
echo "Type: [breach|exposure|infiltration|legal]" >> incident.log
echo "Severity: [low|medium|high|critical]" >> incident.log
echo "Affected systems: " >> incident.log
```

**2. Containment** (1-4 hours)
```bash
# Immediate actions by incident type

# Data exposure
git checkout main
git reset --hard [safe-commit]
git push --force

# Account compromise  
# Revoke all sessions
# Force password reset
# Review access logs

# Device compromise
# Isolate device
# Revoke all keys
# Wipe if necessary
```

**3. Eradication** (4-24 hours)
- Remove malicious access
- Patch vulnerabilities
- Update security controls
- Reset compromised credentials

**4. Recovery** (1-7 days)
- Restore normal operations
- Verify security controls
- Monitor for recurrence
- Update documentation

**5. Lessons Learned** (Within 2 weeks)
```markdown
## Incident Post-Mortem

**What happened?**
[Factual timeline]

**Why did it happen?**
[Root cause analysis]

**What worked well?**
[Effective responses]

**What didn't work?**
[Gaps identified]

**Action items:**
- [ ] Update procedures
- [ ] Additional training
- [ ] New controls needed
```

### Incident Review
- [ ] All incidents documented
- [ ] Lessons learned captured
- [ ] Procedures updated
- [ ] Near-misses analyzed
- [ ] Training updated

## Security Findings Template

```yaml
date: YYYY-MM-DD
auditor: [pseudonym]
type: monthly|quarterly|incident
classification: L0|L1|L2

findings:
  - severity: critical|high|medium|low
    category: personnel|operational|infrastructure
    description: |
      Clear description of issue
    remediation: |
      Specific steps to fix
    assigned_to: [pseudonym]
    due_date: YYYY-MM-DD

completed_items:
  - Regular password rotation
  - Device encryption verified
  - [etc]

next_audit: YYYY-MM-DD
```

## Enhanced Remediation Tracking

### Remediation Management System

**1. Finding Classification**:
```bash
# Create structured finding report
cat > findings/2024-Q4-001.md << EOF
# Security Finding 2024-Q4-001

**Date**: $(date)
**Auditor**: SecurityWG
**Severity**: High
**Category**: Access Control

## Description
Inactive members still have repository access after 6 months of inactivity.

## Risk Assessment
- **Likelihood**: Medium
- **Impact**: High  
- **Risk Score**: 7/10

## Evidence
git log shows 5 users with no commits in 6+ months still have write access.

## Remediation Plan
1. Review all user access quarterly
2. Implement automatic access expiration
3. Create offboarding checklist

## Assigned To
- Technical: @ComradeTech
- Process: @ComradeOps
- Due Date: 2024-12-15
EOF

git add findings/
git commit -m "SECURITY[high]: Document inactive user access finding"
```

**2. Remediation Workflow**:
```bash
# Track remediation progress
git checkout -b remediation/2024-Q4-001

# Implement fixes
./scripts/audit-users.sh > inactive-users.txt
# Remove access for inactive users

# Document changes
cat >> findings/2024-Q4-001.md << EOF

## Remediation Progress
- [x] Identified 5 inactive users (2024-11-20)
- [x] Contacted users for confirmation (2024-11-22)
- [x] Removed access for 4 confirmed inactive (2024-11-25)
- [ ] Implement automated quarterly review
EOF

git add findings/2024-Q4-001.md
git commit -m "SECURITY[remediation]: Remove inactive user access"
```

**3. Verification Process**:
```bash
# Verify remediation effectiveness
cat > findings/2024-Q4-001-verify.sh << 'EOF'
#!/bin/bash
# Verify no inactive users have access

echo "=== Access Verification ==="
for user in $(git log --format='%aN' | sort -u); do
    last_commit=$(git log --author="$user" -1 --format="%ar")
    if [[ $last_commit == *"months"* ]] && [[ ${last_commit%% *} -gt 6 ]]; then
        echo "WARNING: $user last committed $last_commit"
    fi
done
EOF

chmod +x findings/2024-Q4-001-verify.sh
./findings/2024-Q4-001-verify.sh
```

### Remediation Metrics Dashboard

```bash
# Generate remediation metrics
cat > reports/security-metrics.sh << 'EOF'
#!/bin/bash

echo "=== Security Remediation Metrics ==="
echo "Generated: $(date)"
echo ""

# Open findings
echo "Open Findings:"
grep -l "Status: Open" findings/*.md | wc -l

# By severity
echo -e "\nBy Severity:"
echo "Critical: $(grep -l "Severity: Critical" findings/*.md | grep -l "Status: Open" | wc -l)"
echo "High: $(grep -l "Severity: High" findings/*.md | grep -l "Status: Open" | wc -l)"
echo "Medium: $(grep -l "Severity: Medium" findings/*.md | grep -l "Status: Open" | wc -l)"
echo "Low: $(grep -l "Severity: Low" findings/*.md | grep -l "Status: Open" | wc -l)"

# Average remediation time
echo -e "\nAverage Remediation Time:"
# Calculate from git history
EOF

chmod +x reports/security-metrics.sh
```

## Red Flags Requiring Immediate Action

🚨 **STOP and get help if you find**:

### Technical Red Flags
- Active malware/spyware indicators
- Unauthorized access in logs
- Unexpected outbound connections
- Modified security tools
- Disabled logging/monitoring

### Physical Red Flags  
- Missing devices with org data
- Signs of physical tampering
- Unexpected "maintenance" visits
- New people asking questions
- Surveillance indicators

### Legal Red Flags
- Subpoenas or warrants
- Grand jury summons
- Asset freeze notices
- FOIA requests about your org
- Law enforcement contact

**Emergency Response**: See [[security-playbook|Security Emergency Response Plan]]

## Building Revolutionary Security Culture

### Make It Collective, Not Individual

**Transform security from burden to collective power**:

```bash
# Rotate security roles monthly
cat > security/rotation-schedule.md << EOF
# Security Role Rotation

## January: Team A
- Audit Lead: @Comrade1
- Tool Maintenance: @Comrade2
- Training: @Comrade3

## February: Team B
[continues...]
EOF

# Security skill sharing sessions
- Monthly security café
- Pair security audits
- "I got phished" storytelling
- Celebrate security wins
```

### Make It Material, Not Abstract

**Connect to real organizing conditions**:

```markdown
## Threat Scenarios We Train For

### Scenario 1: Employer Retaliation
"Your boss finds your organizing Twitter"
- Practice: Identity separation
- Tool: Compartmentalization
- Skill: OPSEC discipline

### Scenario 2: Police Raid
"They're at the door with a warrant"
- Practice: Device encryption
- Tool: Panic buttons
- Skill: Legal rights

### Scenario 3: Infiltrator Exposed
"The new enthusiastic member is a cop"
- Practice: Information silos
- Tool: Access controls
- Skill: Verification culture
```

### Make It Sustainable, Not Heroic

**Build systems, not heroes**:

```bash
# Automate security tasks
cat > cron/security-tasks << EOF
# Daily
0 9 * * * /opt/security/daily-scan.sh

# Weekly  
0 10 * * 1 /opt/security/backup-verify.sh

# Monthly
0 10 1 * * /opt/security/access-audit.sh

# Quarterly
0 10 1 */3 * /opt/security/full-audit.sh
EOF

# Create security habits
- Password manager in onboarding
- Security check before actions
- Verification as culture
- Learning from incidents
```

### Security as Revolutionary Practice

Remember: Our security isn't paranoia - it's preparation. Every security measure we take is an act of love for our comrades and our movement.

The state has resources, but we have each other. Their surveillance assumes we're individuals; our security builds collective power.

## Quick Reference Cards

### Daily Security Habit Card
```
Morning:
☐ Check device encryption active
☐ Verify VPN connected
☐ Review calendar for OPSEC

During Work:
☐ Lock screen when away
☐ Verify links before clicking  
☐ Check sender before replying

Evening:
☐ Review what was shared today
☐ Secure devices for night
☐ Check for security updates
```

### Monthly Audit Card
```
Week 1: Personnel
☐ Access review
☐ Password audit
☐ Device check

Week 2: Infrastructure  
☐ Run scans
☐ Check logs
☐ Verify backups

Week 3: Operations
☐ Meeting security
☐ Comms audit
☐ Training needs

Week 4: Planning
☐ Review findings
☐ Assign fixes
☐ Update docs
```

---

*Remember: The best security system is one that gets used. Start where you are, improve consistently, protect each other.*