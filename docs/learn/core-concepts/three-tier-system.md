---
title: "The Three-Tier Security Model"
description: "Understanding L0, L1, and L2 security tiers for revolutionary organizing"
created: 2025-07-05
updated: 2025-07-05
type: "docs/explanation"
security: "L0"
version: "1.0.0"
document_id: "EXPL-TIERS-2025-001-L0"
tags: ["security", "L0", "L1", "L2", "threat-model", "opsec"]
draft: false
author: ["KSBC Security Committee"]
---

# The Three-Tier Security Model

## Overview

The three-tier security model provides practical, threat-appropriate security for revolutionary organizations. Instead of paranoid "perfect security" that paralyzes action, we implement proportional security based on actual risk assessment.

## Core Principle: Security Serves Organizing

Security that prevents organizing is counterproductive. Our model balances:
- **Protection** of sensitive information
- **Accessibility** for legitimate users
- **Practicality** in daily operations
- **Scalability** as organizations grow

## The Three Tiers

### L0: Public Information
**What**: Information safe for public consumption
**Examples**:
- Published statements and demands
- Public event announcements
- Educational materials
- General meeting notes (no names)
- Propaganda and outreach content

**Security Measures**:
- Standard Git repositories
- Basic access controls
- Public or organization-wide sharing
- Focus on integrity over secrecy

**Use When**:
- Building public support
- Educational campaigns
- Media relations
- Recruitment materials

### L1: Organizational Information
**What**: Internal information requiring basic protection
**Examples**:
- Member contact lists
- Internal meeting minutes with names
- Campaign strategies
- Financial records
- Working documents

**Security Measures**:
- Encrypted repositories
- Access control lists
- Pseudonymous commits
- Regular security audits
- Encrypted device storage

**Use When**:
- Day-to-day organizing
- Internal coordination
- Strategic planning
- Resource management

### L2: Sensitive Operations
**What**: Information requiring maximum protection
**Examples**:
- Direct action plans
- Legal defense strategies
- Whistleblower identities
- Underground railroad routes
- Security protocols

**Security Measures**:
- Air-gapped systems
- Hardware encryption
- Need-to-know access
- Compartmentalization
- Physical security protocols
- Destruction procedures

**Use When**:
- High-risk operations
- Legal vulnerability
- State repression threats
- Protection of individuals

## Implementation Principles

### 1. Default to Lower Tiers
Start with L0 and only escalate when materially necessary. Over-classification kills organizing capacity.

### 2. Clear Boundaries
Everyone must understand what belongs in each tier. Ambiguity creates both security holes and accessibility barriers.

### 3. Proportional Response
Match security measures to actual threats, not imagined ones. A tenant union doesn't need NSA-level security.

### 4. Regular Review
Threat landscapes change. Review classifications quarterly and adjust based on material conditions.

### 5. Training Before Tools
The best encryption fails with poor practices. Prioritize security culture over security theater.

## Practical Examples

### Tenant Organizing
- **L0**: Demands to landlords, know-your-rights materials
- **L1**: Tenant contact lists, meeting minutes, rent strike plans
- **L2**: Rarely needed unless facing violent landlords

### Labor Organizing
- **L0**: Public campaigns, worker education
- **L1**: Organizing committee lists, strategy documents
- **L2**: Plans for workplace actions management might retaliate against

### Direct Action Groups
- **L0**: Public calls to action, educational content
- **L1**: Member lists, general planning
- **L2**: Specific action plans, security protocols

## Common Mistakes

### Over-Classification
Marking everything L2 makes L2 meaningless and kills organizing capacity.

### Under-Classification
Putting member lists in public repos endangers comrades.

### Inconsistent Application
Different standards in different contexts creates confusion and gaps.

### Security Theater
Complex procedures that don't address actual threats waste energy.

### Individual Solutions
Security is collective practice, not individual choice.

## Technical Implementation

### L0 Setup
```bash
# Standard Git repository
git init campaign-public
git remote add origin https://github.com/org/campaign-public
```

### L1 Setup
```bash
# Encrypted repository with access controls
git init campaign-internal
git-crypt init
git-crypt add-gpg-user YOUR_KEY_ID
```

### L2 Setup
```bash
# Air-gapped system with hardware encryption
# No network connectivity
# Physical security required
# Detailed procedures in security documentation
```

## Assessment Questions

To determine appropriate tier:

1. **What happens if this becomes public?**
   - No harm → L0
   - Organizational damage → L1
   - Individual harm → L2

2. **Who needs access?**
   - Everyone → L0
   - Members only → L1
   - Specific individuals → L2

3. **What's the threat?**
   - Public embarrassment → L0
   - Organizational disruption → L1
   - State repression → L2

## Security Culture, Not Security Theater

Remember:
- Perfect security is impossible
- Good enough security enables action
- Consistency matters more than complexity
- Training beats technology
- Collective practice beats individual paranoia

## Adapting to Your Context

This model is a framework, not dogma. Adjust based on:
- Your threat landscape
- Organizational capacity
- Technical resources
- Political context
- Material conditions

## Conclusion

The three-tier model provides practical security that enhances rather than hinders organizing. By matching security measures to actual threats, we protect what matters while maintaining the accessibility needed for mass organizing.

Security serves the revolution, not the other way around.

---

*Next Steps:*
- **Practice implementation**: [Security Protocols](../../implement/security/security-playbook.md)
- **Handle incidents**: [Help, I Committed Sensitive Data!](../../implement/security/help-committed-sensitive-data.md)
- **Build culture**: [Security as Revolutionary Practice](../../learn/core-concepts/druids-security-implementation.md)