---
title: "Merge Request (Pull Request) Process for Democratic Approval"
description: "Guide for implementing formal merge request processes for collaborative vault management and democratic approval."
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-234-L0"
version: "1.0.0"
tags: ["pull-requests", "merge-requests", "collaboration", "approval", "workflow"]
---

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

---

By following this Pull Request process, teams can ensure that changes are properly reviewed, discussed, and approved before being integrated into key branches, maintaining the integrity and security of the shared Obsidian vault. This democratic approach fosters collaboration and quality.
