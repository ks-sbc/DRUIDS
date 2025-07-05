---
title: "Offline Obsidian Vault Synchronization with Git"
description: "Guide for synchronizing Obsidian vaults between air-gapped systems using Git and removable storage media."
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-235-L0"
version: "1.0.0"
tags: ["obsidian", "git", "offline", "air-gapped", "synchronization", "sneakernet"]
---

# Guide: Offline Obsidian Vault Synchronization with Git (Air-Gapped/"Sneakernet")

## 1. Introduction

### Purpose of This Guide

This guide provides detailed procedures for synchronizing an Obsidian vault between two or more computers that are not directly networked, such as an air-gapped system (like a well-configured Tails OS) and an internet-connected machine, using Git and a removable storage medium (e.g., a USB flash drive). This is often referred to as a "sneakernet" workflow.

### Benefits Over Basic File Sync

Using Git for offline synchronization offers significant advantages over basic file copying methods (like `rsync`):

* **Version History:** Git tracks every change, allowing you to revert to previous versions of notes or your entire vault.
* **Branching:** You can work on different features or drafts in isolated branches and merge them later.
* **Conflict Resolution:** Git provides mechanisms to identify and help resolve conflicts when changes are made to the same file on different machines.
* **Data Integrity:** Git's hashing mechanisms help ensure data integrity during transfers.

### When to Use This Workflow

* When one or more machines are intentionally air-gapped for security.
* When direct network connections between machines are unavailable, unreliable, or untrusted.
* When using Tails OS and wanting to synchronize vault changes with a non-Tails machine.

### Assumed Basic Git Knowledge

This guide assumes you have a basic understanding of Git concepts and commands, including:

* `git add`, `git commit`
* `git branch`, `git checkout`
* `git merge`, `git fetch`, `git pull`, `git push`
* Understanding what a "remote" repository is (even if it's on a USB drive).

## 2. Prerequisites

* **Obsidian Vault as a Git Repository:** Your Obsidian vault must be initialized as a Git repository on **both** machines you intend to sync between.
  * To do this: In your vault's root directory, run `git init` (if not already a Git repository).
* **Git Installed on Both Machines:**
  * **Machine A (e.g., Tails OS):** Git is usually pre-installed. Verify with `git --version`.
  * **Machine B (e.g., your main desktop/laptop):** Install Git if it's not already present (see [official Git downloads](https://git-scm.com/downloads)).
* **`obsidian-git` Plugin (Recommended, Optional):**
  * While not strictly necessary for this manual workflow, having the `obsidian-git` plugin installed in Obsidian on both machines can make committing changes and managing local branches more convenient from within Obsidian. This guide focuses on terminal commands for the sync process itself.
* **Secure USB Flash Drive:** This will be your "sneakernet" transfer medium.
  * **Security Note: Encryption of Transfer Medium.**
        > **[!IMPORTANT]
        > Git bundles and bare repositories are NOT encrypted at rest by Git itself. If your vault's content or commit history is sensitive and the USB drive could be lost or stolen, it is **strongly recommended to encrypt the USB drive itself.**
        > ***Operator Action:** Use tools like VeraCrypt (cross-platform) or LUKS (Linux) to create a full-disk encrypted USB drive. This encryption/decryption occurs outside of Git. Perform this one-time setup on a trusted system.
        >* When using Tails OS, you might need to install `veracrypt` via "Additional Software" persistence to use VeraCrypt volumes. Tails can typically unlock LUKS volumes if the drive was formatted with LUKS on another Linux system.
* **(Optional but Recommended) GPG Signing Setup:** If you sign your Git commits, ensure GPG is configured on both machines, and your GPG key (ideally hardware-backed, like a Feitian K9D) is accessible.

## 3. Core Concepts for Offline Git Sync

* **"Sneakernet":** Manually transferring data between computers using removable media (like a USB drive).
* **USB as Transport:** The USB drive acts as a temporary transport mechanism for Git data (bundles or as a portable bare repository).
* **Importance of Regular Commits:** Commit your changes frequently on each machine with meaningful messages. This makes synchronization smoother and version history more useful.
* **Synchronization Discipline:** Establish a regular routine for syncing. If you make changes on both machines without syncing, you *will* encounter merge conflicts (which Git can help resolve). Aim to sync before switching machines if possible.

## 4. Method 1: Using `git bundle` (Recommended for Flexibility)

The `git bundle` command creates a single file that archives Git objects and references. This method is flexible and doesn't require the USB drive to be formatted as a Git repository itself.

### A. Understanding `git bundle`

A bundle file (`.bundle`) is like a portable, read-only Git repository snapshot. It contains all necessary Git objects and references (like branches and tags) to update another repository or to clone from.

* `git bundle create <file> <refs>`: Creates a bundle file.
  * Using specific refs like `HEAD main develop` bundles only those branches and the objects reachable from them. This is efficient for routine synchronization of active branches.
  * Using `--all` bundles all references in the repository, including all local branches and tags. This is useful for creating a full backup for cloning or archival purposes but results in a larger file.

### B. Initial Synchronization (Cloning a Vault via Bundle - Optional)

If setting up a vault on a new machine (Machine T) from an existing one (Machine S):

1. **On Machine S (Existing Vault):**
    * `cd /path/to/your/vault_on_S`
    * `git add . && git commit -m "Prepare for initial bundle"`
    * Create a full bundle: (**Operator Variable:** Replace `<usb_path_on_S>` with your USB mount point and `<bundle_name.bundle>` with your chosen filename.)

        ```bash
        git bundle create <usb_path_on_S>/<bundle_name.bundle> --all
        ```

2. **Transfer USB** to Machine T.
3. **On Machine T (New Vault Location):**
    * `mkdir /path/to/new_vault_location_on_T && cd /path/to/new_vault_location_on_T`
    * Clone from the bundle: (**Operator Variable:** Adjust `<usb_path_on_T>`, `<bundle_name.bundle>`, and `<main_branch_name>`.)

        ```bash
        git clone -b <main_branch_name> <usb_path_on_T>/<bundle_name.bundle> .
        ```

        (The `.` clones into the current directory. `-b <main_branch_name>` checks out that specific branch.)

### C. Routine Synchronization Workflow (e.g., Machine S → Machine T)

Sync changes from Machine S (e.g., Tails) to Machine T (e.g., main desktop).

1. **On Machine S (Source - e.g., Tails OS):**
    * `cd ~/Persistent/MyVaults/YourVaultName/` (**Operator Variable**: Path to your vault)
    * Commit changes: `git add . && git commit -m "Sync from Tails - $(date +%Y-%m-%d)"`
    * Create a bundle of relevant branches:
        * **Operator Variables:**
            * `<usb_mount_point_tails>`: e.g., `/media/amnesia/YOUR_USB_LABEL/`
            * `<bundle_filename.bundle>`: e.g., `vault_update.bundle`
            * `main`: Branch(es) to sync (e.g., `HEAD main develop`)

        ```bash
        git bundle create <usb_mount_point_tails>/<bundle_filename.bundle> HEAD main
        ```

2. **Securely Transfer USB** to Machine T.
3. **On Machine T (Destination - e.g., Main Desktop):**
    * `cd /path/to/your/vault_on_T` (**Operator Variable**: Path to your vault)
    * **(Optional) Inspect bundle:** (**Operator Variable:** Adjust `<usb_path_on_T>` and `<bundle_filename.bundle>`)

        ```bash
        git ls-remote <usb_path_on_T>/<bundle_filename.bundle>
        ```

    * **Fetch changes into a temporary local branch (Recommended Practice):**
        * This fetches `main` from the bundle into a new local branch `main_from_S`.
        * **Operator Variables:**
            * `<usb_path_on_T>/<bundle_filename.bundle>`
            * `main:main_from_S`: Fetches `main` ref from bundle into local `main_from_S`.

        ```bash
        git fetch <usb_path_on_T>/<bundle_filename.bundle> main:main_from_S
        ```

    * **Review Changes (Crucial):**

        ```bash
        git log main..main_from_S  # Commits in main_from_S not yet in local main
        git diff main..main_from_S # File changes
        ```

    * **Merge the Changes:**

        ```bash
        git checkout main
        git merge main_from_S
        ```

        Resolve conflicts if any (Section 6).
    * **(Optional) Delete temporary branch:** `git branch -d main_from_S`

### D. Syncing Back (Machine T → Machine S)

Reverse the process, creating a bundle on Machine T and fetching/merging on Machine S, using a differently named temporary branch (e.g., `main_from_T`).

### E. Branch Management with Bundles

* When creating: `git bundle create <file> HEAD main develop featureX`
* When fetching: `git fetch <file> main:temp_main develop:temp_develop featureX:temp_featureX`

## 5. Method 2: Using a Bare Repository on USB Drive (Alternative "Portable Remote")

This treats the USB drive as a Git remote. Requires a one-time setup of a bare repository on the USB.

### A. Understanding Bare Repositories

A bare repository (`--bare`) contains only the Git history and references (contents of a typical `.git` folder), with no working copy of files. It's used as a central point for `push` and `fetch`.

> **[!CAUTION]
> Do not run `git add` or `git commit` commands directly within the bare repository folder (e.g., `MyVault.git`) on the USB drive, as it has no working files. All commits should be made in your actual Obsidian vault repositories on Machine S or Machine T.

### B. One-Time Setup on USB Drive

1. Insert USB. **Operator Variable:** Identify `<usb_mount_point>` (e.g., `/media/amnesia/YOUR_USB_LABEL/` on Tails, `/Volumes/YOUR_USB_LABEL/` on macOS, `/mnt/usb/` on other Linux).
2. **Operator Variable:** Choose a name like `MyVault.git` for the bare repo folder.

    ```bash
    # On either Machine S or T, once:
    mkdir -p <usb_mount_point>/MyVault.git 
    cd <usb_mount_point>/MyVault.git
    git init --bare
    ```

### C. Connecting Existing Vaults to the USB Bare Repository (Initial Setup)

* **On Machine S (e.g., Tails - connecting to this new USB remote):**
    1. `cd ~/Persistent/MyVaults/YourVaultName/` (**Operator Variable**)
    2. Add remote: (**Operator Variables:** `usb_sneakernet_remote` is your chosen name for the remote; `<usb_mount_point_tails>/MyVault.git` is the path.)

        ```bash
        git remote add usb_sneakernet_remote <usb_mount_point_tails>/MyVault.git
        ```

    3. Push existing branches:

        ```bash
        git push -u usb_sneakernet_remote main # And any other branches
        ```

* **On Machine T (e.g., Main Desktop):**
  * **If cloning from USB for the first time:**

        ```bash
        # Operator Variables: <usb_path_on_T>, YourLocalVaultName
        git clone <usb_path_on_T>/MyVault.git YourLocalVaultName 
        cd YourLocalVaultName
        git remote rename origin usb_sneakernet_remote # Optional: for clarity
        ```

  * **If vault exists, add USB as remote:**
        `cd /path/to/your/vault_on_T` (**Operator Variable**)
        `git remote add usb_sneakernet_remote <usb_path_on_T>/MyVault.git`
        `git fetch usb_sneakernet_remote`
        `git merge usb_sneakernet_remote/main` (or rebase, onto your local `main`)

### D. Routine Synchronization Workflow (Bare Repo Method)

1. **On Machine with New Changes (e.g., Machine S - Tails):**
    * `cd ~/Persistent/MyVaults/YourVaultName/` (**Operator Variable**)
    * `git add . && git commit -m "Sync from Tails"`
    * Push to USB: (**Operator Variable:** `usb_sneakernet_remote` and `main`)

        ```bash
        git push usb_sneakernet_remote main
        ```

2. **Transfer USB.**
3. **On Other Machine (e.g., Machine T - Main Desktop):**
    * `cd /path/to/your/vault_on_T` (**Operator Variable**)
    * Fetch from USB: (**Operator Variable:** `usb_sneakernet_remote` and `main`)

        ```bash
        git fetch usb_sneakernet_remote main
        ```

    * Review: `git log main..usb_sneakernet_remote/main`, `git diff main..usb_sneakernet_remote/main`
    * Merge:

        ```bash
        git checkout main
        git merge usb_sneakernet_remote/main
        ```

        (Or `git pull usb_sneakernet_remote main` which does fetch + merge). Resolve conflicts.

### E. Pros & Cons of Bare Repo on USB vs. Bundle

* **Bare Repo Pros:** Familiar `push`/`fetch`/`pull` workflow. Simpler for routine syncs once remotes configured.
* **Bare Repo Cons:** USB is "live" Git data; corruption is more impactful. USB needs a folder acting as a Git repo.
* **Bundle Pros:** Single file is easy to copy/archive. USB needs no special Git formatting. Bundles are generally read-only sources for fetching, which can feel safer.
* **Bundle Cons:** More verbose fetch commands (mapping refs to temporary branches).

## 6. Handling Merge Conflicts (General Advice)

If changes on the same lines in the same file occurred on both machines since the last sync, Git will pause the merge and require manual resolution.

1. **Identify Conflicts:** `git status` shows unmerged paths.
2. **Edit Files:** Open conflicted files. Git adds conflict markers:

    ```markdown
    Here is some content without conflict.
    <<<<<<< HEAD
    This is content from your current branch (e.g., local main).
    =======
    This is the conflicting content from the branch you are trying to merge (e.g., main_from_S or usb_sneakernet_remote/main).
    >>>>>>> main_from_S 
    And here is more content without conflict.
    ```

3. **Resolve:** Manually edit the file to keep desired changes and remove the `<<<<<<<`, `=======`, `>>>>>>>` markers.
4. **Stage Resolved Files:** `git add <resolved_file_name>`
5. **Complete Merge:** `git commit` (Git usually pre-fills a merge commit message) or `git merge --continue`.

Consult official Git documentation for advanced conflict resolution.

## 7. Security and Best Practices for Offline Git Sync

* **USB Drive Security:** Use dedicated, trusted USBs. Avoid untrusted computers. Store securely.
* **Encryption of USB Drive (Re-emphasize):**
    > **[!IMPORTANT] Operator Action: Encrypt your USB drive.**
    > If your vault's history or content is sensitive, **encrypt the USB drive itself** (VeraCrypt/LUKS). Git does not encrypt data on the USB.
* **GPG Commit Signing:** Signatures persist, verifying authenticity across systems.
* **Regular Syncs:** Minimize divergence and conflict complexity.
* **Consistent Branch Names:** (e.g., `main`) simplifies workflows.
* **Sync vs. Backup:** This is for synchronization. Maintain separate, dedicated backups.
  * **Cross-Reference:** See "Guide: Air-Gapped Backup and Synchronization for Obsidian on Tails OS."

This Git-based offline workflow provides a robust method for maintaining version control and synchronizing your Obsidian vault in air-gapped or "sneakernet" scenarios.
