---
title: "Commit Signing with GPG and Hardware Keys"
description: "Guide for implementing commit signing with GPG keys for enhanced security and trust in Git workflows."
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-231-L0"
version: "1.0.0"
tags: ["gpg", "commit-signing", "security", "hardware-keys", "git"]
---

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
  * For enhanced security and integrity, **GPG signing is strongly recommended for any commits made to sensitive branches** like `L1-internal` and especially `L2-secure` (as outlined in the "Branch Management Strategy for Security Tiers" section).

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

---

While setting up GPG commit signing requires some initial effort, it provides significant security benefits by ensuring the authenticity and integrity of your commit history. For vaults with sensitive information or collaborative projects, it's a worthwhile investment.
