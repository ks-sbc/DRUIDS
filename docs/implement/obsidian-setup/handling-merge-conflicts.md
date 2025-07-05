---
title: "Handling Merge Conflicts"
description: "Guide for understanding and resolving merge conflicts in Git collaborative workflows."
type: "how-to"
security: "L0"
document_id: "INT-HTG-2025-233-L0"
version: "1.0.0"
tags: ["git", "merge-conflicts", "collaboration", "resolution", "workflow"]
---

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

---

Resolving merge conflicts is a normal part of using Git in a team. With practice, you'll become more comfortable identifying and resolving them. Always take your time, understand the changes, and communicate when needed.
