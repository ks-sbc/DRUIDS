---
title: "Configuring Automatic Commits in Obsidian-Git"
description: "Step-by-step guide for setting up automatic commits in Obsidian-Git to ensure regular backup of notes."
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-232-L0"
version: "1.0.0"
tags: ["obsidian", "git", "automatic-commits", "configuration", "backup"]
---

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

---

By following these steps, you can effectively configure automatic commits in Obsidian-Git, helping you maintain a consistent backup and version history of your valuable notes. Remember to balance automation with the need for clear, manual commit messages for significant changes.
