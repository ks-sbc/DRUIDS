---
title: Mermaid Test Page
description: Test page for verifying mermaid diagram rendering
---

# Mermaid Diagram Test Page

This page tests various Mermaid diagram types to ensure they render correctly with the Mandalorian theme.

## Flowchart Example

```mermaid
flowchart TD
    A[Start] --> B{Is it working?}
    B -->|Yes| C[Great!]
    B -->|No| D[Debug]
    D --> A
    C --> E[End]
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Server

    User->>Browser: Click button
    Browser->>Server: HTTP Request
    Server-->>Browser: Response
    Browser-->>User: Display result
```

## Class Diagram

```mermaid
classDiagram
    class DRUIDS {
        +String name
        +SecurityLevel level
        +encrypt()
        +decrypt()
    }

    class SecurityLevel {
        <<enumeration>>
        L0_PUBLIC
        L1_MEMBER
        L2_CADRE
    }

    DRUIDS --> SecurityLevel
```

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review: Submit PR
    Review --> Approved: Pass Review
    Review --> Draft: Request Changes
    Approved --> Merged: Merge
    Merged --> [*]
```

## Git Graph

```mermaid
gitGraph
    commit
    branch proposal/new-feature
    checkout proposal/new-feature
    commit
    commit
    checkout main
    merge proposal/new-feature
    commit
```

## Pie Chart

```mermaid
pie title DRUIDS Security Distribution
    "L0 Public" : 45
    "L1 Member" : 35
    "L2 Cadre" : 20
```
