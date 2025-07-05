---
title: "Obsidian-Git Workflow Guide"
description: "Comprehensive workflow guide for secure and collaborative vault management using Obsidian-Git plugin"
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-185-L0"
version: "1.0.0"
tags: ["obsidian", "git", "workflow", "collaboration", "security"]
---

# Obsidian-Git: Comprehensive Workflow Guide for Secure and Collaborative Vault Management

## Introduction

This guide provides a comprehensive overview of workflows and best practices for using the Obsidian-Git plugin. Its purpose is to help users leverage Obsidian-Git for robust version control, data backup, and effective collaboration, with a particular emphasis on maintaining security for sensitive notes and implementing democratic approval processes for shared vaults.

By understanding and implementing the strategies outlined here, you can enhance your productivity, safeguard your valuable information, and work more effectively with others in a shared Obsidian environment.

This guide covers key topics including:

* Setting up and configuring automatic commits and synchronization.
* Implementing a branch management strategy for different security tiers of notes.
* Following a structured Merge Request (Pull Request) process for democratic approvals.
* Handling and resolving merge conflicts.
* Advanced security practices like commit signing with GPG and hardware keys.

## Table of Contents

* [Configuring Automatic Commits](#configuring-automatic-commits-in-obsidian-git)
* [Automated Backup and Synchronization](#automated-backup-and-synchronization)
* [Branch Management Strategy for Security Tiers](#branch-management-strategy-for-security-tiers)
* [Merge Request (Pull Request) Process for Democratic Approval](#merge-request-pull-request-process-for-democratic-approval)
* [Handling Merge Conflicts](#handling-merge-conflicts)
* [Commit Signing with GPG (and Hardware Keys)](#commit-signing-with-gpg-and-hardware-keys)

## Configuring Automatic Commits in Obsidian-Git

Automating commits can be a great way to ensure your notes are regularly backed up to your remote repository. Obsidian-Git offers several options to configure automatic operations. Here's how to set it up:

### 1. Accessing Plugin Settings

To configure automatic commits, you first need to access the Obsidian-Git plugin settings:

1. Open Obsidian.
2. Go to **Settings** (usually a gear icon in the bottom-left).
3. In the sidebar of the Settings window, scroll down to **Community plugins**.
4. Find **Obsidian Git** in your list of installed plugins and click on its name. If you have many plugins, you can use the search bar at the top of the "Community plugins" section.

This will open the settings panel for Obsidian-Git.

### 2. Enabling Auto-Sync

Obsidian-Git allows you to schedule automatic operations at regular intervals.

* **Set Auto-Sync Interval:**
  * Look for the option labeled **Vault backup interval (minutes)** or a similar wording.
  * Enter a numerical value representing the time in minutes between automatic operations. For example, `15` would mean the plugin attempts to perform the selected operations every 15 minutes. Choose an interval that suits your workflow – frequent enough to capture changes, but not so frequent that it becomes disruptive.

* **Enable Automatic Operations:**
  * You'll typically find checkboxes or toggles for the following operations:
    * **Auto Backup on interval**: This is the master switch for enabling automatic operations. Ensure this is turned ON.
    * **Auto Pull on interval**: If you want your local vault to automatically fetch changes from your remote repository, enable this. This is useful if you edit your notes on multiple devices.
    * **Auto Push on interval**: If you want your local commits to be automatically pushed to your remote repository, enable this.

    *It's generally recommended to enable auto pull and auto push if you are enabling auto backup to keep your local and remote repositories synchronized.*

### 3. Configuring the Commit Message

A clear and descriptive commit message is crucial for understanding the history of your changes.

* **Setting the Automatic Commit Message:**
  * Find the setting labeled **Commit message for auto backup** or similar.
  * In this field, you can define the message that will be used for all automatic commits.

* **Strategies for Meaningful Automatic Commit Messages:**
  * **Limitations:** Currently, Obsidian-Git primarily supports static commit messages for automatic backups. This means the same message will be used for every automatic commit. While there might be community discussions or feature requests for more dynamic messages (e.g., including the names of changed files or a timestamp), it's best to assume this capability is limited unless explicitly stated in the plugin's current version.
  * **Good Static Message Examples:**
    * `"chore: automatic backup"`
    * `"docs: periodic vault sync"`
    * `"style: auto-save notes"`
    * `"feat: regular snapshot of notes"`
    * If you want to include a timestamp (though the commit itself is timestamped by Git), you could use a generic message like: `"chore: vault backup (auto)"` and rely on Git's commit history for the exact time.
  * **Recommendation for Critical Changes:** For significant or complex changes, it is highly recommended to perform a **manual commit**. This allows you to write a detailed and specific commit message that accurately describes the changes made, which is invaluable for future reference. Don't rely on automatic commits for changes that need careful documentation.

### 4. Prerequisite: Authentication for Auto-Push

For the **Auto Push on interval** feature to work, your system must be configured to authenticate with your Git remote (e.g., GitHub, GitLab) without requiring manual password entry each time. This typically involves:

* **HTTPS:** Using a Git credential manager (like Git Credential Manager Core) or caching credentials.
* **SSH:** Setting up SSH keys and adding the public key to your remote Git provider.

If authentication is not set up correctly, automatic pushes will likely fail. Refer to Git documentation and your remote provider's instructions for setting up non-interactive authentication.

### 5. Testing the Setup

After configuring automatic commits, it's important to test that it's working as expected:

1. **Make a Small Change:** Open a note in your Obsidian vault and make a minor, easily identifiable change.
2. **Wait for the Interval:** Wait for the specified auto-sync interval to pass. For example, if you set it to 5 minutes, wait at least that long.
3. **Check Git History:**
    * You can use the Obsidian-Git plugin's interface (if it offers a history view) or a dedicated Git client (like GitKraken, Sourcetree, or the command line `git log`) to inspect the commit history of your repository.
    * Look for a new commit with the automatic commit message you configured.
    * Verify that the commit includes the small change you made.
4. **Check Remote Repository (if auto-push is enabled):** If you enabled auto-push, navigate to your remote repository (e.g., on GitHub) and check if the new commit has been pushed.

If you don't see the expected commit, review your settings, ensure there are actual changes to commit, and check for any error messages within Obsidian (sometimes shown in the top-right corner or in the developer console).

### 6. Initial Setup for New Repositories

If you are setting up Obsidian-Git in a vault that is not yet a Git repository:

1. **Initialize the Repository:** You must first initialize a Git repository in your vault's root folder. You can usually do this via a command in the Obsidian-Git plugin settings (e.g., "Initialize repository") or manually using the `git init` command in your vault's directory via a terminal.
2. **First Commit:** Make an initial commit of your existing files. This can be done manually through the plugin or command line.
3. **Configure Remote (Optional but Recommended):** Add a remote repository URL (`git remote add origin <your-repo-url>`) and push your initial commit (`git push -u origin main` or `git push -u origin master`) if you want to back up to a remote service.

Once the repository is initialized and ideally connected to a remote, the automatic commit features will function as described above.

By following these steps, you can effectively configure automatic commits in Obsidian-Git, helping you maintain a consistent backup and version history of your valuable notes. Remember to balance automation with the need for clear, manual commit messages for significant changes.

## Automated Backup and Synchronization

Automating the backup and synchronization of your Obsidian vault with Obsidian-Git can significantly enhance your workflow, data safety, and collaboration capabilities. This section guides you through configuring and understanding these automated processes.

### 1. Purpose of Automation

Setting up automated backup and synchronization offers several key benefits:

* **Data Safety:** Regular, automatic commits and pushes ensure your notes are frequently backed up to a remote repository, protecting against local data loss (e.g., hardware failure).
* **Version History:** Consistent commits create a detailed version history, allowing you to revert to previous states of your notes if needed.
* **Seamless Collaboration:** For shared vaults, automation helps keep everyone's local version more aligned with the central repository, reducing merge conflicts when changes are pulled from others.
* **Cross-Device Synchronization:** If you use Obsidian on multiple devices, automated sync keeps your notes consistent across all of them.

### 2. Accessing Obsidian-Git Settings

As a reminder, you can access the Obsidian-Git plugin settings by:

1. Opening Obsidian.
2. Navigating to **Settings** (gear icon).
3. Selecting **Community plugins** from the sidebar.
4. Clicking on **Obsidian Git** from your list of installed plugins.

### 3. Core Configuration (Scheduled Sync)

The primary automation feature is the scheduled execution of Git operations.

* **Enabling and Setting the Interval:**
  * Look for an option like **Vault backup interval (minutes)** or **Auto-Sync Interval**.
  * Enable this feature (often a toggle switch).
  * Set a numerical value for the interval in minutes (e.g., `15` for every 15 minutes, `60` for every hour). Choose an interval that balances frequency with performance and potential disruption. For active note-takers, 15-30 minutes is common.

* **Recommended Operational Order: Pull, then Commit, then Push:**
  * To minimize merge conflicts and ensure you're working with the latest version of your notes, the ideal sequence of automated operations is:
        1. **Pull:** Fetch changes from the remote repository and merge them into your local current branch. This ensures you have others' latest work before committing your own.
        2. **Commit:** Commit any local changes you've made to your notes.
        3. **Push:** Push your local commits (including any new changes you just pulled and merged, and your own new commits) to the remote repository.
  * **Configuration:**
    * **Separate Options:** Some versions of Obsidian-Git might have separate toggles for "Auto Pull on interval," "Auto Backup on interval" (for commits), and "Auto Push on interval." If so, **enable all three** to achieve the full Pull -> Commit -> Push sequence. The plugin is generally designed to perform them in this logical order if all are enabled for the interval.
    * **Combined "Sync" Option:** Newer versions or other Git plugins might offer a single "Auto Sync on interval" or similar option. This typically implies the Pull -> Commit -> Push sequence. Check the plugin's documentation if unclear.
    * **If only "Auto Backup/Commit" and "Auto Push" are available:** Enabling these will commit your local changes and then push them. However, without an "Auto Pull" first, you risk pushing changes that might conflict with un-pulled remote changes. Prioritize plugins or configurations that allow for an automatic pull before commit and push if possible.

* **Commit Message Guidance:**
  * Refer to the "[Configuring Automatic Commits](#configuring-automatic-commits-in-obsidian-git)" section for detailed advice on setting a meaningful **Commit message for auto backup**. A good static message like `"chore: automatic vault sync"` or `"docs: periodic backup"` is usually sufficient for automated commits.

### 4. Additional Feature: Auto-Pull on Startup

* **What it is:** Many versions of Obsidian-Git offer an option like **Pull updates on startup** or **Auto-pull on Obsidian launch**.
* **Benefit:** When enabled, Obsidian-Git will automatically attempt to pull the latest changes from your remote repository every time you open your Obsidian vault.
* **Recommendation:** **It is highly recommended to enable this feature.** This helps ensure you start each Obsidian session with the most up-to-date version of your notes, especially important if you collaborate or use multiple devices.

### 5. Prerequisites for Successful Automation

For automated operations to work reliably, ensure the following are in place:

1. **Initialized Git Repository:** Your vault must be an initialized Git repository.
2. **Configured Remote:** A remote repository (e.g., on GitHub, GitLab) must be added to your local Git configuration (e.g., named `origin`). Automated push and pull need a destination/source.
3. **Correct Git Authentication:** Your system must be set up to authenticate with the remote repository without requiring manual password/passphrase entry each time. This usually involves SSH keys or a credential manager for HTTPS. (Refer to "[Configuring Automatic Commits](#configuring-automatic-commits-in-obsidian-git)" - Prerequisite: Authentication for Auto-Push).
4. **Absence of Unresolved Merge Conflicts:** If your repository has existing unresolved merge conflicts, automated operations (especially commit and push) will likely fail until the conflicts are resolved manually.

### 6. Monitoring and Verification

While automation is convenient, it's not "set it and forget it." Periodically check that it's working:

* **Plugin Status Indicators:**
  * Obsidian-Git may have icons or messages in Obsidian's status bar indicating its last sync time or current status (e.g., "synced X minutes ago," "syncing," "error"). Pay attention to these.
* **Manual History Checks:**
  * **Local:** Occasionally use "Obsidian Git: Open Source Control View" and check the commit history. You should see your automated commits with the message you configured.
  * **Remote:** Log into your Git hosting platform (e.g., GitHub) and verify that these commits are appearing on the remote repository.
* **Error Messages:**
  * If Obsidian-Git encounters an error during an automated operation, it might display a notification. Don't ignore these. Investigate them promptly.

### 7. Troubleshooting Basic Automation Failures

If you notice automated operations are not working:

1. **Check Authentication:** This is the most common culprit. Test if you can manually push/pull from a terminal or using Obsidian-Git's manual commands. If prompted for credentials, your authentication isn't set up for non-interactive use.
2. **Check for Merge Conflicts:** Manually run "Obsidian Git: Pull." If it reports conflicts, resolve them. (See "[Handling Merge Conflicts](#handling-merge-conflicts)" section).
3. **Internet Connection:** Ensure you have a stable internet connection.
4. **Plugin Settings:** Double-check that the auto-sync interval is enabled and the desired operations (pull, commit, push) are selected.
5. **Try Manual Operations:** Attempt a manual "Obsidian Git: Pull," then "Obsidian Git: Commit all changes," then "Obsidian Git: Push." This can often give more specific error messages that help diagnose the problem.
6. **Obsidian Developer Console:** For more cryptic issues, you can open the Obsidian Developer Console (usually Ctrl+Shift+I or Cmd+Option+I, then go to the "Console" tab) to look for error messages from the plugin.

### 8. Branch Considerations for Sync

* **Sync Operates on the Current Branch:** Automated sync operations (pull, commit, push) will always apply to the Git branch that is currently checked out in your Obsidian vault.
* **Cautions for L1/L2 Sensitive Branches (Reiteration):**
  * As mentioned in "[Branch Management Strategy for Security Tiers](#branch-management-strategy-for-security-tiers)," if you have globally enabled "Auto Push on interval," this will attempt to push *any* branch you are currently on, including potentially sensitive branches like `L1-internal` or `L2-secure`.
  * For these sensitive branches, you might prefer:
    * **Manual Push:** Disable global auto-push and use "Obsidian Git: Push" manually after reviewing changes on these branches.
    * **Temporarily Disable Auto-Push:** If practical, disable the "Auto Push on interval" setting before switching to a sensitive branch and re-enable it when switching back to a less sensitive one (e.g., `main`). This is more error-prone.
  * Always be mindful of which branch you are on when relying on automated push operations.

By carefully configuring and monitoring automated backup and synchronization, you can leverage Obsidian-Git to maintain a robust and reliable system for your notes, ensuring they are safe, versioned, and accessible.

## Branch Management Strategy for Security Tiers

When managing notes with varying levels of sensitivity within a single Obsidian vault, a robust branch management strategy is crucial. This strategy helps prevent accidental exposure of sensitive information and allows for controlled collaboration. This guide outlines a tier-based branching model using Obsidian-Git.

### 1. Core Principles

This strategy revolves around the following core principles:

1. **Branch per Tier:** Each distinct security or sensitivity level will have its own dedicated Git branch.
2. **Default to Lowest Tier:** The vault should typically default to the lowest sensitivity tier branch (e.g., `main` for public/unclassified information). This minimizes the risk of accidentally committing sensitive information to a less secure branch.
3. **Conscious Switching:** Moving to a higher sensitivity tier branch requires a deliberate, conscious action by the user.
4. **No Direct Merge Down of Sensitive Information:** Information from a higher sensitivity branch (e.g., `L2-secure`) should *never* be directly merged into a lower sensitivity branch (e.g., `L1-internal` or `main`). If information needs to be declassified, it must be done manually by copying and pasting, ensuring no sensitive remnants remain.
5. **Optional Feature Branches:** For complex changes within a specific tier, users can create temporary feature branches off their current tier branch (e.g., `L1-internal-feature-x`). These should be merged back into their parent tier branch upon completion.

### 2. Tier Branch Details

Here's a breakdown of the recommended branches:

#### `main` (L0 - Public/Unclassified)

* **Purpose:** This branch is for notes and information that are considered public, unclassified, or safe for general sharing. It's the default branch your vault should be on most of the time.
* **Typical Obsidian-Git Workflow:**
  * Automatic commits and pushes can be safely enabled for this branch.
  * Regular synchronization with the remote `main` branch.
* **Collaboration Notes:**
  * Suitable for open collaboration.
  * Changes made here can be freely shared.
  * If collaborating, ensure all collaborators understand this is the public tier.

#### `L1-internal` (L1 - Internal Use Only)

* **Purpose:** This branch is for notes containing information that is not for public release but is suitable for internal team members or personal private use. This might include internal project details, meeting notes not meant for external eyes, or drafts of documents before they are sanitized for public release.
* **Explicit Switching Workflow with Obsidian-Git:**
    1. **Before Switching:**
        * Ensure all changes on your current branch (e.g., `main`) are committed or stashed. Use the Obsidian-Git "Commit all changes" or "Commit staged changes" command.
        * Verify your current branch status using the Obsidian-Git status bar or `git status` command.
    2. **Switch Branch:** Use the Obsidian-Git command palette (Ctrl/Cmd+P) to search for and select "Obsidian Git: Checkout branch" and choose `L1-internal`.
    3. **After Switching:**
        * Verify you are on the `L1-internal` branch.
        * Pull the latest changes for `L1-internal` from the remote to ensure your local branch is up-to-date before making new commits: "Obsidian Git: Pull".
* **Crucial Pre/Post Switching Commit Discipline:**
  * **ALWAYS commit or stash pending changes on your current branch BEFORE switching to `L1-internal`**. Failure to do so can result in unclassified changes being accidentally brought into the `L1-internal` branch or vice-versa.
  * **ALWAYS commit your `L1-internal` changes BEFORE switching back to `main` (or any other branch)**.
* **Auto-Commit/Push Considerations:**
  * **Auto-Commit:** Can be useful, but ensure the commit message for auto-backups is generic enough (e.g., `"chore: L1 internal sync"`).
  * **Auto-Push:** Exercise caution. If you frequently switch branches, you might prefer to manually push changes on `L1-internal` to have more control and avoid accidentally pushing incomplete or sensitive work prematurely. If auto-push is enabled globally, consider temporarily disabling it when working on `L1-internal` if this is a concern (see "Plugin Limitations" below).
* **Collaboration Notes:**
  * Suitable for collaboration with trusted internal team members.
  * Ensure collaborators are aware they are on the `L1-internal` branch and understand its sensitivity level.
  * The remote repository for `L1-internal` should have access controls limiting it to authorized personnel.

#### `L2-secure` (L2 - Highly Sensitive)

* **Purpose:** This branch is for notes containing highly sensitive, confidential, or restricted information. Access should be strictly controlled. This could include personal identifiable information (PII), trade secrets, critical security information, etc.
* **Explicit Switching Workflow:**
  * Follow the same rigorous pre/post switching commit discipline as with `L1-internal`.
  * The commands are the same: "Obsidian Git: Checkout branch" to `L2-secure`, and "Obsidian Git: Pull" after switching.
* **Extreme Care Notes (Commit Discipline):**
  * **Meticulous attention to detail is paramount.** Double-check the current branch before every commit.
  * Ensure no uncommitted changes from lower tiers are accidentally carried over.
  * Before pushing, review the changes staged for commit very carefully.
* **Recommendations for Auto-Push:**
  * **Strongly Recommended: Disable global auto-push** if you use this tier.
  * **Always use manual push** for the `L2-secure` branch. This provides a final checkpoint to ensure only intended information is transmitted.
  * Automatic commits can still be used locally, but the push to the remote should be a deliberate manual action.
* **Collaboration Notes:**
  * Collaboration on this tier should be minimal and only with individuals who absolutely require access.
  * All collaborators must be thoroughly trained on the handling procedures for this level of data.
* **Stricter Remote Repository Access Controls:**
  * The remote repository hosting the `L2-secure` branch (if pushed at all) MUST have highly restrictive access controls. This might involve separate private repositories, branch protection rules, and multi-factor authentication for all users with access. Consider if this tier should even have a remote, or if it should remain local-only or pushed to a highly secured, air-gapped, or end-to-end encrypted storage.

### 3. Implementation Notes & Considerations

* **Potential Plugin Limitations (Global Auto-Sync):**
  * Obsidian-Git's auto-sync settings (backup interval, auto-pull, auto-push) are typically global. This means if auto-push is enabled, it will attempt to push *any* branch you are currently on after a commit.
  * **Mitigation for L1/L2:**
    * **Manual Push:** The simplest approach is to disable global auto-push in Obsidian-Git settings and manually push changes for `L1-internal` and `L2-secure` using the "Obsidian Git: Push" command.
    * **Temporary Disable:** If you prefer to keep auto-push for `main`, you could temporarily disable the "Auto Push on interval" setting before switching to `L1-internal` or `L2-secure`, and re-enable it when switching back to `main`. This is more cumbersome and error-prone.
* **Importance of User Training:**
  * All users of the vault must be trained on this branching strategy.
  * Key training points:
    * Always commit (or stash) changes before switching branches.
    * Always verify the current active branch before committing sensitive information (Obsidian's status bar usually shows the current Git branch if the plugin is active).
    * Understand the sensitivity level of each branch.
* **The Role of `.gitignore`:**
  * Utilize a comprehensive `.gitignore` file to prevent common Obsidian files (cache, workspace settings if not shared, etc.) and any OS-specific files (e.g., `.DS_Store`, `thumbs.db`) from being committed to any branch.
  * You might also consider `.gitignore` for specific large files or temporary files that don't need to be versioned within any security tier.
* **Handling Accidental Commits:**
  * Mistakes can happen. If sensitive information is accidentally committed to the wrong branch (e.g., L1 data to `main`):
    * **Do NOT push the change if it hasn't been pushed yet!**
    * A detailed procedure for remediating such incidents (e.g., using `git reset`, `git rebase -i`, or filtering branch history) should be documented and understood by users. This is a more advanced Git topic and will be covered in a separate "Incident Response" section (placeholder). For now, the immediate action is to avoid pushing and seek help if unsure.
* **Future Security Enhancements (Forward Reference):**
  * For `L1-internal` and especially `L2-secure` branches, consider implementing additional security measures:
    * **Signed Commits:** Use GPG keys to sign commits, verifying the author's identity. Obsidian-Git may have settings to enable this if your Git environment is configured for it. (See "[Commit Signing with GPG (and Hardware Keys)](#commit-signing-with-gpg-and-hardware-keys))"
    * **Hardware Keys:** For ultimate security on `L2-secure` pushes, consider requiring hardware security keys (like YubiKey) for signing commits or authenticating to the remote repository. (See "[Commit Signing with GPG (and Hardware Keys)](#commit-signing-with-gpg-and-hardware-keys))"

This branch management strategy provides a framework for handling notes of varying sensitivity. Its effectiveness relies on user diligence, proper configuration, and awareness of the potential risks and mitigation techniques. Always prioritize the security of sensitive information.

## Merge Request (Pull Request) Process for Democratic Approval

For collaborative vaults, especially those employing the security tier branching strategy, a formal process for proposing, reviewing, and integrating changes is essential. This is typically achieved through Merge Requests (MRs) or Pull Requests (PRs). This guide focuses on using GitHub's Pull Request system, but the principles apply to other Git hosting platforms like GitLab or Bitbucket.

### 1. Clarifying Roles: Obsidian-Git vs. Git Hosting Platform

It's important to understand the distinct roles of Obsidian-Git and your Git hosting platform (e.g., GitHub):

* **Obsidian-Git (Local Operations):**
  * Used for all local Git operations within your Obsidian vault.
  * Creating new branches (e.g., feature branches off a security tier branch like `L1-internal`).
  * Making and committing changes to your notes.
  * Pushing your local branches (especially feature branches) to the remote repository.
  * Pulling changes from the remote repository to update your local branches.

* **Git Hosting Platform (e.g., GitHub - Remote Operations & Collaboration):**
  * Hosts the central/remote Git repository.
  * Manages user access and permissions.
  * **Facilitates the Pull Request (PR) creation, review, discussion, and approval process.**
  * Handles the merging of approved feature branches into the target (e.g., security tier) branches.
  * Can enforce branch protection rules (e.g., requiring reviews before merging).

You will use Obsidian-Git to prepare your changes and then switch to your web browser to interact with GitHub for the collaborative review and merge process.

### 2. Local Workflow (Obsidian & Obsidian-Git)

Before a Pull Request can be created, you need to prepare your changes locally:

1. **Ensure your Target Branch is Up-to-Date:**
    * Before creating a feature branch, switch to the base branch you intend to eventually merge into (e.g., `main`, `L1-internal`).
    * Use "Obsidian Git: Pull" to ensure this local branch has the latest changes from the remote.
2. **Create/Checkout a Feature Branch:**
    * Open the command palette (Ctrl/Cmd+P) in Obsidian.
    * Type "Obsidian Git: Create new branch".
    * Name your branch descriptively, often prefixed with `feature/`, `fix/`, or your initials, and indicating its purpose and parent branch if complex (e.g., `feature/L1-internal-user-authentication-docs` or `johndoe/L1-update-contact-list`).
    * This new branch will be based on your currently active branch.
3. **Make and Commit Changes Locally:**
    * Work on your notes, creating new content or modifying existing files.
    * Use "Obsidian Git: Stage all" or stage individual files.
    * Use "Obsidian Git: Commit staged changes." Write clear, concise commit messages for each logical change. It's good practice to make several small commits rather than one massive one.
4. **Push the Feature Branch to the Remote Repository:**
    * Once your changes are committed locally and you're ready for review, push your feature branch to the remote repository.
    * Open the command palette and run "Obsidian Git: Push". If it's the first time pushing this new branch, Git might require you to set an upstream: `git push --set-upstream origin your-feature-branch-name`. Obsidian-Git may handle this for you, or you might need to run this from a terminal if you encounter issues.

### 3. Creating the Pull Request (on GitHub)

With your feature branch pushed to the remote, you can now create a Pull Request:

1. **Navigate to GitHub:** Open your repository in your web browser. GitHub usually detects a newly pushed branch and displays a prompt to create a Pull Request. If not:
    * Go to the "Pull requests" tab.
    * Click "New pull request".
2. **Select Branches:**
    * **Base Branch:** Choose the branch you want your changes to be merged *into*. This will typically be one of your security tier branches (e.g., `main`, `L1-internal`, `L2-secure`).
    * **Compare Branch:** Choose your feature branch that contains the changes.
3. **PR Description - Crucial for Review:**
    * **Title:** Write a clear, concise title that summarizes the purpose of the PR.
    * **Description:** This is very important.
        * Clearly explain the **purpose** of the changes.
        * Summarize the key **modifications** made.
        * Explain how these changes align with the vault's **principles or goals**.
        * If it addresses a specific issue, link to it.
        * Provide any context reviewers might need (e.g., screenshots, links to discussions).
        * A good PR description helps reviewers understand the changes quickly and speeds up the approval process.
4. **Create Pull Request:** Click the "Create pull request" button.

### 4. Review and Democratic Approval Process (on GitHub)

This is where the collaborative "democratic" aspect comes into play:

1. **Assign Reviewers (or Request Reviews):**
    * Depending on repository settings or team norms, you might assign specific reviewers from the right-hand sidebar on the PR page.
    * Alternatively, team members may proactively pick up PRs for review.
2. **Discussion and Feedback:**
    * Reviewers will examine the "Files changed" tab in the PR.
    * They can leave comments on specific lines of code/text, ask questions, or request modifications.
    * Use GitHub's commenting features to discuss the changes. Keep discussions professional and constructive.
3. **Signifying Approval:**
    * **GitHub's "Approve" Feature:** Reviewers can formally approve the changes by clicking "Review changes" and selecting "Approve."
    * **Comment Conventions:** Some teams also use comment conventions like `+1`, `LGTM` (Looks Good To Me), or specific emojis to signify approval, though GitHub's formal approval feature is generally preferred for clarity.
4. **Branch Protection Rules (Recommended):**
    * Repository administrators can set up branch protection rules on GitHub (e.g., for `main`, `L1-internal`, `L2-secure`).
    * These rules can enforce that a certain number of approvals are required before a PR can be merged. They can also require that status checks (like automated tests) pass.
5. **Iterative Review:**
    * The PR author should monitor feedback.
    * If changes are requested, the author makes further commits to their local feature branch (in Obsidian, using Obsidian-Git).
    * After committing, the author pushes these new commits to the *same feature branch* on the remote. The Pull Request on GitHub will automatically update to show the new commits.
    * This review-update cycle continues until all reviewers are satisfied and have approved the changes.

### 5. Merging the Pull Request (on GitHub)

Once the PR has received the necessary approvals and any required checks have passed:

1. **Who Merges:** Typically, the PR author (if they have merge permissions), a designated maintainer, or anyone with appropriate permissions can merge the PR. This depends on your team's workflow and branch protection rules.
2. **When to Merge:** Only merge after all discussions are resolved and the required approvals are obtained.
3. **Merge Strategies (Brief Note):** GitHub offers several ways to merge:
    * **Create a merge commit:** Keeps all commits from the feature branch and adds a merge commit. This preserves detailed history but can make the main branch history look complex.
    * **Squash and merge:** Combines all commits from the feature branch into a single commit on the base branch. This creates a cleaner, linear history on the main branch. Often preferred for feature branches.
    * **Rebase and merge:** Re-applies commits from the feature branch onto the base branch. Use with caution, especially in shared branches.
    * Choose a strategy that suits your team's preference for history readability. "Squash and merge" is often a good default for feature branches.
4. **Deleting the Feature Branch Post-Merge:**
    * GitHub usually offers an option to automatically delete the feature branch after the PR is merged. This is good practice to keep the repository clean. The branch still exists in the commit history if needed but is removed from the list of active branches.

### 6. Post-Merge: Updating Local Repositories

Once the PR is merged into the target branch on GitHub (e.g., `L1-internal`):

1. **All Collaborators (including the PR author) Must Update Their Local Clones:**
    * Switch to the corresponding local branch (e.g., `L1-internal`) in Obsidian using "Obsidian Git: Checkout branch".
    * Run "Obsidian Git: Pull" to fetch the newly merged changes from the remote repository.
    * This ensures everyone's local version of the tier branch is up-to-date.

### 7. Forward Reference to Automation

Manual PR processes can be enhanced with automation:

* **GitHub Actions** (to be detailed in a later section) can be configured to:
  * Send notifications about new PRs or review requests.
  * Run automated checks (e.g., markdown linting, spell checking) on the changes in a PR.
  * Potentially automate merging if certain conditions are met (use with caution).

By following this Pull Request process, teams can ensure that changes are properly reviewed, discussed, and approved before being integrated into key branches, maintaining the integrity and security of the shared Obsidian vault. This democratic approach fosters collaboration and quality.

## Handling Merge Conflicts

Merge conflicts are a common occurrence in collaborative projects using Git. They happen when Git is unable to automatically reconcile differences between your local changes and changes from the remote repository (or another branch). While they can seem intimidating at first, understanding how to handle them is a key skill for smooth collaboration.

### 1. What are Merge Conflicts and Why Do They Occur?

A merge conflict arises when:

* You try to **pull** changes from a remote repository, and the incoming changes modify the same lines of a file that you have also modified locally (and haven't pushed yet).
* You try to **merge** one branch into another (e.g., a feature branch back into `main`), and both branches have made changes to the same part of the same file since they diverged.
* You try to **rebase** your work onto an updated branch, and similar overlapping changes exist.

Git is excellent at merging changes automatically when they occur in different parts of a file or in different files. However, when the *same lines* are edited in conflicting ways, Git doesn't know which version is correct. It then flags the file as conflicted and asks you to resolve it manually.

### 2. Conflict Detection

Here's how you'll typically know you have a merge conflict:

* **Obsidian-Git Notifications/Errors:**
  * When you perform an operation like "Obsidian Git: Pull" or "Obsidian Git: Sync Unsynced Changes," the plugin may show an error message or notification indicating that a merge conflict has occurred and the merge has failed or needs attention.
  * The Obsidian status bar might also display messages related to a merge conflict.
* **Git Conflict Markers in Files:**
  * Git directly modifies the conflicted file(s) to show you where the conflicts are. It inserts special markers:

        ```
        <<<<<<< HEAD
        This is your local version of the text.
        (Content from your current branch)
        =======
        This is the incoming version of the text from the remote or other branch.
        (Content from the branch you are trying to merge/pull)
        >>>>>>> [commit hash or branch name]
        ```

  * `<<<<<<< HEAD`: Indicates the start of the conflicting lines from your current local branch (often referred to as "ours" or "yours").
  * `=======`: Separates your changes from the incoming changes.
  * `>>>>>>> [commit hash/branch name]`: Indicates the end of the conflicting lines from the branch being merged (often referred to as "theirs" or "incoming").
* **Identifying Conflicted Files:**
  * **Obsidian-Git Source Control View:** The Obsidian-Git plugin usually has a dedicated "Source Control" view in the left sidebar. Conflicted files will often be highlighted here, typically under a "Merge Changes" or "Conflicts" section.
  * **`git status` (Terminal):** If you are comfortable with the command line, opening a terminal in your vault's root directory and running `git status` will clearly list any files that are "unmerged" or have conflicts.

### 3. Conflict Resolution Steps (File by File)

You need to resolve conflicts in each affected file one by one:

1. **Open the Conflicted File in Obsidian:**
    * Navigate to the conflicted file (identified via Obsidian-Git's UI or `git status`) and open it in the Obsidian editor.
2. **Interpret the Conflict Markers:**
    * Locate the `<<<<<<< HEAD`, `=======`, and `>>>>>>>` markers.
    * The content between `<<<<<<< HEAD` and `=======` is *your* version (what was on your branch before the pull/merge).
    * The content between `=======` and `>>>>>>> ...` is the *incoming* version (what Git is trying to bring in from the remote or another branch).
3. **Manually Edit to Resolve:**
    * Your task is to edit this section of the file to reflect the final desired state. You have several choices for each conflict block:
        * **Keep Your Changes:** Delete the incoming changes and the conflict markers, leaving only your version.
        * **Keep Their Changes:** Delete your changes and the conflict markers, leaving only the incoming version.
        * **Combine/Rewrite:** Manually edit the text, possibly taking parts from both versions, or rewriting the section entirely to integrate both ideas or create a new correct version. This is common for more complex conflicts.
    * **Example:**
        * Before Resolution:

            ```markdown
            <<<<<<< HEAD
            My preferred title for this section is "Advanced Techniques".
            =======
            The team decided the title should be "Expert Methods".
            >>>>>>> feature-branch-title-update
            ```

        * After Resolution (choosing "Expert Methods" and adding a note):

            ```markdown
            The team decided the title should be "Expert Methods".
            (Note: Previously considered "Advanced Techniques" but updated for consistency.)
            ```

4. **Crucially: Delete ALL Conflict Markers:**
    * Once you have edited the content to your satisfaction, you **must delete all the conflict marker lines** (`<<<<<<< HEAD`, `=======`, `>>>>>>> ...`).
    * The file should look like normal content again, with no Git-specific markers left. If you forget this step, the markers will be committed as actual text in your file.
5. **Save the File:** Save your changes in Obsidian.
6. **Communicate for Complex Conflicts:**
    * If you're unsure how to resolve a conflict, especially if the changes are complex or involve someone else's work, **communicate with your collaborators**. Discuss the conflicting changes to decide on the best resolution together. It's better to ask than to make a mistake that overwrites important work.

### 4. Staging and Committing the Resolution

Once you have resolved the conflicts in a file and saved it:

1. **Stage the Resolved File:**
    * In Obsidian-Git's Source Control view, the resolved file should now appear as "modified" rather than "conflicted."
    * Use the "Stage current file" option (often a "+" icon next to the file) or "Stage all changes" if you've resolved all conflicts.
    * Alternatively, from the command palette: "Obsidian Git: Stage current file" or "Obsidian Git: Stage all changes".
2. **Commit the Merge:**
    * After all conflicted files have been resolved and staged, you need to make a commit to finalize the merge.
    * Use the "Obsidian Git: Commit staged changes" command.
    * Git usually provides a default merge commit message (e.g., "Merge branch 'feature-xyz'" or "Merge remote-tracking branch 'origin/main'"). You can often keep this default message, or add more details if necessary.
    * If you were in the middle of a `pull` that caused conflicts, this commit finalizes the pull operation.

### 5. Pushing the Resolved Merge

After successfully committing the merge resolution:

* If the conflicts occurred during a `pull` or `sync`, your local branch is now up-to-date and includes both your previous local changes and the incoming changes, properly merged.
* You may need to push your changes (including the merge commit) back to the remote if you had local commits that were part of the conflict:
  * Use "Obsidian Git: Push".

### 6. Option: Aborting a Merge

If you encounter conflicts and feel overwhelmed, or if you realize you've made a mistake during resolution *before* committing the merge, you can often abort the merge process:

* **How to Abort:**
  * **Terminal:** The most reliable way is often via the terminal. Open a terminal in your vault's root directory and run:

        ```bash
        git merge --abort
        ```

        (If the conflict arose from a `git pull`, which is a fetch then a merge, `git merge --abort` is still the command to use. If it was from a `git rebase`, you'd use `git rebase --abort`.)
  * **Obsidian-Git Command:** Check if your version of Obsidian-Git offers a command like "Abort merge" or "Reset merge." This is less common.
* **Caution and Why:**
  * Aborting will revert your working directory back to the state it was in before you attempted the merge/pull. Any manual resolutions you made will be lost.
  * Use this if you want a clean slate to re-attempt the merge, or if you want to set aside your local changes to get a clean version of the remote branch first.

### 7. Tips for Prevention & Complex Conflicts

* **Pull/Sync Frequently:** The more often you pull changes from the remote (especially before starting new work or when working on shared files), the smaller and less frequent merge conflicts are likely to be.
* **Communicate:** When working on the same files as others, communicate about what you're planning to change to avoid overlapping work.
* **Feature Branches:** Using feature branches for new work isolates changes and means conflicts are usually handled when merging the feature branch, rather than directly in main shared branches.
* **External Merge Tools:** For very complex conflicts involving many lines or intricate code/text, dedicated external Git merge tools (e.g., VS Code's built-in merge editor, Sourcetree, Meld, KDiff3) can provide a more visual and powerful way to resolve differences. You would typically configure Git to use one of these tools.
* **Seek Help:** If you're stuck on a particularly nasty conflict, don't hesitate to ask a more experienced Git user on your team for assistance.

Resolving merge conflicts is a normal part of using Git in a team. With practice, you'll become more comfortable identifying and resolving them. Always take your time, understand the changes, and communicate when needed.

## Commit Signing with GPG (and Hardware Keys)

Commit signing is an important security practice that adds a layer of trust and accountability to your Git history. It cryptographically verifies that commits and tags were made by a specific user and that they haven't been tampered with since they were made. This is typically achieved using GnuPG (GPG).

### 1. Introduction to Commit Signing

* **What are GPG Signed Commits?**
    When you sign a commit, you use your private GPG key to create a unique digital signature for that commit. This signature is then attached to the commit.
* **Why are they Important?**
  * **Authenticity:** Signed commits help prove that you are the one who made the commit. Anyone can configure their Git `user.name` and `user.email` to impersonate someone else, but they cannot fake a GPG signature without access to the private key.
  * **Integrity:** The signature ensures that the commit (including its content, author, and timestamp) has not been altered since it was signed. If any part of the commit changes, the signature will no longer be valid.
  * **Trust:** In collaborative or sensitive environments, signed commits provide a higher degree of confidence in the source and integrity of changes.

### 2. Obsidian-Git's Role

* **Respects System Configuration:** Obsidian-Git itself does not directly manage GPG keys or signing configurations. Instead, it invokes your system's Git installation. Therefore, **Obsidian-Git will respect the global or repository-specific Git configuration for commit signing.**
* **No Specific UI for GPG Keys:** You will generally **not** find settings within the Obsidian-Git plugin UI to input GPG keys or directly enable signing. This setup is done at the Git and GPG level on your operating system.

### 3. Setting Up Your System for GPG Signed Commits (General Steps)

Configuring your system to sign Git commits with GPG involves several steps. The following is a general outline; refer to detailed GPG and Git documentation for platform-specific instructions.

1. **Prerequisite: Install GPG:**
    * Ensure GnuPG is installed on your system. (e.g., `gpg --version` in your terminal). If not, download and install it from [gnupg.org](https://gnupg.org/download/).
2. **Generate or Import a GPG Key:**
    * If you don't have a GPG key, you'll need to generate one: `gpg --full-generate-key`. Follow the prompts.
    * If you already have a GPG key, you can import it.
    * List your keys with `gpg --list-secret-keys --keyid-format LONG`. Copy the GPG key ID (the long string of characters) of the key you want to use for signing.
3. **Configure Git:**
    * Tell Git which key to use for signing:

        ```bash
        git config --global user.signingkey YOUR_GPG_KEY_ID
        ```

        (Replace `YOUR_GPG_KEY_ID` with your actual GPG key ID).
    * Optionally, tell Git to sign all commits by default:

        ```bash
        git config --global commit.gpgsign true
        ```

        If you don't set this, you'd have to use `git commit -S` for every commit, which isn't practical for Obsidian-Git automation.
    * Optionally, sign tags as well (recommended if you create annotated tags):

        ```bash
        git config --global tag.gpgsign true
        ```

    * These settings can be applied globally (`--global`) or per-repository (by omitting `--global` when inside a repository). For Obsidian vaults, global configuration is usually easiest.
4. **`GPG_TTY` (Shell Environment - If Needed):**
    * In some terminal environments, GPG might need to know which TTY (teletypewriter or terminal) to use for passphrase prompts. You might need to set this in your shell profile (e.g., `.bashrc`, `.zshrc`):

        ```bash
        export GPG_TTY=$(tty)
        ```

    * This is more relevant if you are signing from the command line and your GPG agent isn't configured.

### 4. Using Hardware Keys (Conceptual Overview)

Using a hardware security key (like a YubiKey or Nitrokey) to store your GPG private key significantly enhances security, as the private key never leaves the hardware device.

* **Advanced GPG Setup:** This involves generating your GPG private key (or a subkey) directly on the hardware device or transferring it securely.
* **Obsidian-Git Interaction:** Obsidian-Git (via Git, via GPG) will interact with the hardware key when a signature is required. You'll typically be prompted by the hardware key (e.g., to touch it) to authorize the signing operation.
* **Complexity:**
  * **Detailed setup of GPG with hardware keys is complex and highly specific to your operating system, GPG version, and the hardware key model.**
  * **Users MUST refer to the official documentation provided by their hardware key manufacturer and the GnuPG project.** (This level of detail is beyond the scope of this Obsidian-Git user guide; the focus here is that Obsidian-Git *can* work with it once your system is configured).

### 5. How Obsidian-Git Makes Signed Commits

* If your Git environment is correctly configured with `commit.gpgsign true` and a valid `user.signingkey`, then **any commits made through Obsidian-Git's interface (manual or automatic backups) should automatically be GPG signed.**
* Obsidian-Git simply calls `git commit`, and Git handles the signing process as per its configuration.

### 6. Verification

You can verify that your commits are being signed:

* **Terminal:**
  * Navigate to your vault's directory in a terminal.
  * Run `git log --show-signature`. You'll see details about the GPG signature for each signed commit, including the key ID and whether the signature is good.
* **Git Hosting Platforms (e.g., GitHub, GitLab):**
  * Platforms like GitHub will display a "Verified" badge next to commits that are signed with a GPG key they can link to a user's uploaded public GPG key. Unsigned or unverified commits will not have this badge or may show as "Unverified."

### 7. Limitations and Important Considerations

* **Mobile Platforms:**
  * Commit signing is **highly unlikely to work** with Obsidian-Git on mobile devices (iOS, Android). The `isomorphic-git` library used by Obsidian-Git on mobile typically does not have the capability to interact with system GPG tools or hardware keys. Assume commits made from mobile will be unsigned.
* **Passphrase Prompts & GPG Agent:**
  * When GPG signs a commit, it may need the passphrase for your private key. If Git is invoked by a background process (like Obsidian-Git's automatic backups), there might be no interactive terminal to enter the passphrase.
  * **Solution:** Configure a **GPG agent** (e.g., `gpg-agent` on Linux/macOS, Kleopatra on Windows as part of Gpg4win). A GPG agent can cache your passphrase for a session or a set period, allowing Git to use the key without a prompt each time. This is crucial for automated signed commits.
* **Initial Setup Complexity:**
  * Setting up GPG, generating keys, and configuring Git and a GPG agent can be challenging, especially for users less familiar with command-line tools and cryptographic concepts. This is generally considered an advanced user feature.
* **Recommendation for Security Tiers:**
  * For enhanced security and integrity, **GPG signing is strongly recommended for any commits made to sensitive branches** like `L1-internal` and especially `L2-secure` (as outlined in the "[Branch Management Strategy for Security Tiers](#branch-management-strategy-for-security-tiers)" section).

### 8. Troubleshooting

If your commits are not being signed as expected:

1. **Verify Git Configuration:**
    * Check `git config user.signingkey` and `git config commit.gpgsign` (globally and in the local repository).
2. **Verify GPG Setup:**
    * Ensure your GPG key is listed in `gpg --list-secret-keys`.
    * Check that the key is not expired or revoked.
3. **GPG Agent:**
    * Ensure your GPG agent is running and has your passphrase cached if you expect passphrase-less signing.
    * Try signing a commit manually from the terminal (`git commit -S -m "Test signing"`) to see if GPG prompts or errors appear there.
4. **Key Validity/Trust:** For verification on platforms like GitHub, ensure your public GPG key has been uploaded to your GitHub account and that the email address associated with the GPG key is a verified email on your GitHub account.

While setting up GPG commit signing requires some initial effort, it provides significant security benefits by ensuring the authenticity and integrity of your commit history. For vaults with sensitive information or collaborative projects, it's a worthwhile investment.
