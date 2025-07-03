---
title: Analytics & Privacy Setup Guide
description: Complete guide to setting up analytics with privacy controls
tags:
  - analytics
  - privacy
  - gdpr
  - configuration
  - google-analytics
comments: true
---

# Analytics & Privacy Setup Guide

Learn how to implement analytics while respecting user privacy and complying with GDPR and other privacy regulations.

## Overview

This guide covers:
- 🔍 **Google Analytics 4** setup with privacy controls
- 🛡️ **Privacy plugin** configuration for GDPR compliance
- 🍪 **Cookie consent** management
- 📊 **Feedback collection** with user consent
- 🔒 **External asset** privacy protection

## Google Analytics 4 Setup

### 1. Basic Configuration

```yaml
# mkdocs.yml
extra:
  analytics:
    provider: google
    property: !ENV [GOOGLE_ANALYTICS_KEY, '']
    feedback:
      title: Was this page helpful?
      ratings:
        - icon: material/emoticon-happy-outline
          name: This page was helpful
          data: 1
          note: Thanks for your feedback!
        - icon: material/emoticon-sad-outline
          name: This page could be improved
          data: 0
          note: >-
            Thanks for your feedback! Help us improve by
            <a href="https://github.com/yourusername/repo/issues/new" target="_blank">
            opening an issue</a>.
```

### 2. Environment Variables

Set your Google Analytics property ID:

```bash
# .envrc
export GOOGLE_ANALYTICS_KEY="G-XXXXXXXXXX"
```

### 3. Privacy-Enhanced Analytics

```javascript
// Custom analytics with privacy controls
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

// Initialize with privacy settings
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX', {
  // Privacy-enhanced settings
  'anonymize_ip': true,
  'allow_google_signals': false,
  'allow_ad_personalization_signals': false,
  'cookie_expires': 63072000, // 2 years
  'cookie_update': true,
  'cookie_flags': 'SameSite=None;Secure'
});

// Respect user consent
document.addEventListener('DOMContentLoaded', function() {
  const consent = __md_get("__consent");
  if (consent && consent.analytics) {
    gtag('consent', 'update', {
      'analytics_storage': 'granted'
    });
  } else {
    gtag('consent', 'default', {
      'analytics_storage': 'denied'
    });
  }
});
```

## Privacy Plugin Configuration

### 1. Basic Privacy Setup

```yaml
# mkdocs.yml
plugins:
  - material/privacy:
      enabled: !ENV [CI, false]
      external_assets: report
      external_assets_dir: assets/external
      external_links: true
      external_links_attr_map:
        target: _blank
        rel: noopener
      external_links_noopener: true
```

### 2. External Assets Management

The privacy plugin automatically:
- 📥 **Downloads external assets** (fonts, stylesheets, scripts)
- 🔒 **Self-hosts them** to prevent tracking
- 📊 **Reports external dependencies** for audit
- 🚫 **Blocks unauthorized requests** to external services

### 3. External Links Protection

```yaml
plugins:
  - material/privacy:
      external_links: true
      external_links_attr_map:
        target: _blank
        rel: noopener nofollow
        class: external-link
      external_links_noopener: true
```

This automatically adds security attributes to external links:
- `target="_blank"` - Opens in new tab
- `rel="noopener"` - Prevents window.opener access
- `rel="nofollow"` - Prevents SEO link juice transfer

## Cookie Consent Management

### 1. GDPR-Compliant Consent

```yaml
extra:
  consent:
    title: Cookie consent
    description: >-
      We use cookies to recognize your repeated visits and preferences, as well
      as to measure the effectiveness of our documentation and whether users
      find what they're searching for. With your consent, you're helping us to
      make our documentation better.
    actions:
      - accept
      - manage  
      - reject
    cookies:
      analytics:
        name: Google Analytics
        checked: false
        description: >-
          Google Analytics helps us understand how visitors interact with our site.
          This data is anonymized and helps us improve the user experience.
      github:
        name: GitHub
        checked: true
        description: >-
          GitHub integration enables features like edit links, issue reporting,
          and discussions. This is essential for site functionality.
      comments:
        name: Comments (Giscus)
        checked: false
        description: >-
          Giscus enables commenting functionality through GitHub Discussions.
          This requires GitHub authentication and stores your comments publicly.
```

### 2. Consent Categories

#### Essential Cookies (Always Enabled)
- **GitHub integration** - Required for edit links and issue reporting
- **Site functionality** - Navigation, search, theme preferences
- **Security** - CSRF protection, session management

#### Optional Cookies (User Choice)
- **Analytics** - Google Analytics for usage statistics
- **Comments** - Giscus for discussion functionality
- **Social features** - Social sharing and embeds

### 3. Custom Consent Handling

```javascript
// Custom consent management
document.addEventListener('DOMContentLoaded', function() {
  // Listen for consent changes
  document.addEventListener('consent', function(e) {
    const consent = e.detail;
    
    // Handle analytics consent
    if (consent.analytics) {
      enableAnalytics();
    } else {
      disableAnalytics();
    }
    
    // Handle comments consent
    if (consent.comments) {
      enableComments();
    } else {
      disableComments();
    }
  });
});

function enableAnalytics() {
  gtag('consent', 'update', {
    'analytics_storage': 'granted'
  });
}

function disableAnalytics() {
  gtag('consent', 'update', {
    'analytics_storage': 'denied'
  });
}
```

## Feedback Collection

### 1. Privacy-Aware Feedback

```yaml
extra:
  analytics:
    feedback:
      title: Was this page helpful?
      ratings:
        - icon: material/emoticon-happy-outline
          name: This page was helpful
          data: 1
          note: >-
            Thanks for your feedback! This helps us improve our documentation.
        - icon: material/emoticon-sad-outline
          name: This page could be improved
          data: 0
          note: >-
            Thanks for your feedback! Help us improve this page by
            <a href="https://github.com/yourusername/repo/issues/new" target="_blank">
            opening an issue</a> or leaving a comment below.
```

### 2. Anonymous Feedback Collection

```javascript
// Collect feedback without personal data
function submitFeedback(rating, page) {
  // Only collect if analytics consent is given
  const consent = __md_get("__consent");
  if (consent && consent.analytics) {
    gtag('event', 'page_feedback', {
      'rating': rating,
      'page_path': page,
      'timestamp': Date.now()
    });
  }
  
  // Always show thank you message
  showFeedbackThankYou();
}
```

## Data Protection Measures

### 1. IP Anonymization

```javascript
// Google Analytics with IP anonymization
gtag('config', 'G-XXXXXXXXXX', {
  'anonymize_ip': true,
  'allow_google_signals': false,
  'allow_ad_personalization_signals': false
});
```

### 2. Data Retention

```yaml
# Set appropriate data retention periods
extra:
  analytics:
    # Configure in Google Analytics dashboard:
    # - User data retention: 14 months
    # - Event data retention: 14 months
    # - Reset on new activity: Yes
```

### 3. User Rights

Provide mechanisms for users to:
- **Access their data** - Link to Google Analytics data export
- **Delete their data** - Instructions for opting out
- **Correct their data** - Contact information for data issues
- **Port their data** - Data export capabilities

## Privacy Policy Integration

### 1. Required Disclosures

Your privacy policy should include:

```markdown
## Data Collection

We collect the following data to improve our documentation:

### Analytics Data (Optional)
- **What we collect**: Page views, session duration, referrer information
- **Why we collect it**: To understand how users interact with our documentation
- **How long we keep it**: 14 months, then automatically deleted
- **Your control**: You can opt out via cookie settings

### Comments Data (Optional)
- **What we collect**: GitHub username, comment content, timestamps
- **Why we collect it**: To enable community discussions
- **How long we keep it**: Until you delete your comments
- **Your control**: You can delete comments anytime via GitHub

### Essential Data (Required)
- **What we collect**: Theme preferences, navigation state
- **Why we collect it**: Essential site functionality
- **How long we keep it**: Until you clear browser data
- **Your control**: Clear browser data to remove
```

### 2. Contact Information

```markdown
## Data Protection Contact

For questions about data protection:
- **Email**: privacy@yoursite.com
- **Data Protection Officer**: dpo@yoursite.com
- **Postal Address**: [Your address for GDPR compliance]
```

## Compliance Checklist

### GDPR Compliance
- [ ] **Lawful basis** for processing clearly stated
- [ ] **Consent mechanism** implemented and documented
- [ ] **Data minimization** - only collect necessary data
- [ ] **Purpose limitation** - use data only for stated purposes
- [ ] **Storage limitation** - automatic data deletion after retention period
- [ ] **User rights** - access, rectification, erasure, portability
- [ ] **Privacy by design** - privacy controls built into the system
- [ ] **Data protection impact assessment** completed if required

### Technical Measures
- [ ] **IP anonymization** enabled in Google Analytics
- [ ] **External assets** self-hosted via privacy plugin
- [ ] **Secure cookies** with appropriate flags
- [ ] **External links** protected with noopener/nofollow
- [ ] **Consent management** properly implemented
- [ ] **Data encryption** in transit and at rest

### Documentation
- [ ] **Privacy policy** comprehensive and up-to-date
- [ ] **Cookie policy** explains all cookies used
- [ ] **Data processing records** maintained
- [ ] **User guides** for exercising data rights
- [ ] **Incident response plan** for data breaches

## Testing Privacy Controls

### 1. Consent Testing

```bash
# Test consent functionality
# 1. Visit site in incognito mode
# 2. Verify consent banner appears
# 3. Test "Accept All" functionality
# 4. Test "Reject All" functionality  
# 5. Test "Manage" individual preferences
# 6. Verify analytics only loads with consent
```

### 2. Privacy Plugin Testing

```bash
# Test external asset handling
mkdocs build --verbose

# Check for external assets report
cat site/assets/external/report.txt

# Verify no external requests in browser dev tools
```

### 3. Analytics Testing

```javascript
// Test analytics consent integration
console.log('Consent state:', __md_get("__consent"));

// Test feedback submission
// Should only send to GA if analytics consent given
```

## Troubleshooting

### Common Issues

**Consent banner not appearing:**
```yaml
# Ensure consent is properly configured
extra:
  consent:
    title: Cookie consent  # Required
    description: "..."     # Required
    actions: [accept, reject]  # At least these two
```

**Analytics not loading:**
```bash
# Check environment variable
echo $GOOGLE_ANALYTICS_KEY

# Verify consent state in browser console
__md_get("__consent")
```

**External assets not downloading:**
```yaml
# Check privacy plugin configuration
plugins:
  - material/privacy:
      enabled: true  # Must be enabled
      external_assets: report  # Must be set
```

## Best Practices

### 1. Privacy by Design
- **Minimize data collection** - only collect what you need
- **Default to privacy** - require opt-in for non-essential features
- **Transparent communication** - clearly explain data usage
- **User control** - provide easy opt-out mechanisms

### 2. Performance Considerations
- **Self-host assets** to reduce external dependencies
- **Lazy load** analytics scripts until consent is given
- **Optimize consent UI** for fast loading and interaction
- **Cache consent decisions** to avoid repeated prompts

### 3. Legal Compliance
- **Regular audits** of data collection practices
- **Update policies** when practices change
- **Monitor regulations** for changes in requirements
- **Document decisions** for compliance evidence

---

*Privacy and analytics setup requires careful balance between insights and user privacy. Always err on the side of protecting user privacy.*