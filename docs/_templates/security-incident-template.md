---
title: "Security Incident Response Template"
description: "Standard format for documenting and responding to security incidents"
created: 2025-07-02
updated: 2025-07-02
type: "docs/reference"
security: "L1"
version: "1.0.0"
document_id: "TMP-REF-2025-003-L0"
tags: ["template", "security", "incident-response", "reference"]
draft: false
author: ["Comrade 47"]
---

# Security Incident Response Template

*For documenting security incidents. Create on secure branch, share only with security committee first.*

```markdown
# Security Incident Report: [Brief Description]

**Report ID**: SIR-[YYYY-MM-DD]-[NUMBER]
**Date of Incident**: [YYYY-MM-DD]
**Time Discovered**: [HH:MM timezone]
**Reported By**: [Pseudonym]
**Severity**: [Low/Medium/High/Critical]
**Status**: [Active/Contained/Resolved]

## Incident Classification

**Type** (check all that apply):
- [ ] Digital surveillance detected
- [ ] Physical surveillance observed
- [ ] Infiltration suspected
- [ ] Device compromised
- [ ] Account breach
- [ ] Information leak
- [ ] Doxxing attempt
- [ ] Legal threat (warrant, subpoena)
- [ ] Other: [Specify]

## Immediate Actions Taken
1. [First action - e.g., "Notified security committee"]
2. [Second action - e.g., "Isolated affected systems"]
3. [Continue chronologically]

## Incident Details

### What Happened
[Factual description. No speculation. Include timeline.]

### How Discovered
[What alerted us to this incident?]

### Affected Resources
- **People**: [Pseudonyms only, number affected]
- **Systems**: [Which tools/platforms/devices]
- **Information**: [What data might be compromised]
- **Operations**: [What organizing work is impacted]

## Threat Assessment

### Threat Actor
**Suspected Source**: [State/Corporate/Unknown/Internal]
**Capability Level**: [Low/Moderate/Advanced]
**Intent**: [Surveillance/Disruption/Arrest/Intelligence]

### Potential Impact
- **Immediate**: [What's at risk now]
- **Short-term**: [Next 72 hours]
- **Long-term**: [Ongoing risks]

## Response Plan

### Containment (First 24 Hours)
- [ ] [Specific containment action]
- [ ] [Notify affected comrades]
- [ ] [Secure compromised accounts]
- [ ] [Document everything]

### Investigation (48-72 Hours)
- [ ] [Determine scope]
- [ ] [Identify entry point]
- [ ] [Assess information accessed]
- [ ] [Check for persistence]

### Recovery (Ongoing)
- [ ] [Restore secure operations]
- [ ] [Implement additional safeguards]
- [ ] [Update security protocols]
- [ ] [Train comrades on prevention]

## Evidence Preservation
- **Screenshots**: [Stored location]
- **Logs**: [What was collected]
- **Physical Evidence**: [If applicable]
- **Witness Accounts**: [Recorded statements]

## Lessons Learned

### What Worked
- [Effective responses]
- [Good security practices that helped]

### What Failed
- [Security gaps exploited]
- [Process breakdowns]

### Recommendations
1. [Specific improvement]
2. [Protocol change needed]
3. [Training required]

## Communication Plan

### Internal Communications
- **Who Needs to Know**: [By role, not name]
- **What They Need to Know**: [Minimum necessary]
- **When to Inform**: [Timeline]

### External Communications
- **Public Statement**: [Yes/No, if yes, key points]
- **Legal Counsel**: [Contacted? When?]
- **Allied Organizations**: [Who to warn]

## Follow-Up Actions

| Action | Responsible | Deadline | Status |
|--------|-------------|----------|--------|
| [Task] | [Role] | [Date] | [Status] |

## Operational Security Notes
- DO NOT include real names
- DO NOT specify physical locations
- DO NOT detail our security measures
- DO NOT share outside security committee until cleared

---

## Report Metadata
- **Classification**: L1 Minimum (upgrade to L2 if needed)
- **Distribution**: Security Committee Only (initially)
- **Retention**: Permanent (historical record)
- **Last Updated**: [Timestamp]
```

## Using This Template

### Immediate Response Checklist

When incident detected:
1. **STOP** - Don't panic or act rashly
2. **SECURE** - Contain immediate threat
3. **DOCUMENT** - Start this report immediately
4. **NOTIFY** - Alert security committee
5. **ASSESS** - Determine actual vs perceived threat

### Security Levels for Incidents

**Low**: Minor policy violations, no immediate threat
- Example: Comrade posts meeting photo on social media
- Response: Education, reminder of protocols

**Medium**: Potential compromise, limited scope
- Example: Suspicious login attempt on shared account
- Response: Password reset, audit access logs

**High**: Active threat, multiple comrades affected
- Example: Confirmed device compromise at meeting
- Response: Full security audit, possible tactical pause

**Critical**: Immediate danger to comrades
- Example: Warrant service, active surveillance
- Response: Emergency protocols, legal support

### Git Workflow for Security Incidents

```bash
# Create secure branch
git checkout -b security/incident-2025-07-02

# Add report using template
cp templates/security-incident-template.md \
   security/incidents/SIR-2025-07-02-001.md

# Commit with vague message (details in report)
git commit -m "Add security incident report

- Type: [General category only]
- Severity: [Level]
- Status: Under investigation"

# Push to restricted access
git push origin security/incident-2025-07-02
```

### What NOT to Document

Never include:
- Real names or identifying information
- Specific security measures we use
- Vulnerabilities not yet patched
- Information that could aid adversaries

### Legal Considerations

- Assume all documentation may be subpoenaed
- Write factually, avoid speculation
- Preserve evidence but protect comrades
- Consult legal support before external communication

### Learning from Incidents

Every incident teaches us:
1. **Technical**: What tools/protocols failed?
2. **Human**: What behaviors enabled this?
3. **Systemic**: What structures need change?

### Post-Incident Review

After resolution:
1. Sanitized version for general membership
2. Update security protocols
3. Training based on lessons learned
4. Appreciation for good responses

### Remember

Security incidents aren't failures - they're learning opportunities. The failure is in not documenting, not learning, not improving.

State repression is constant. We respond with discipline, documentation, and collective care.

---

See also:
- [[security-audits-for-organizers|Security Audits for Organizers]]
- [[when-they-come-knocking|When They Come Knocking]]
<!-- - [[pseudonym-discipline|Pseudonym Discipline]] -->