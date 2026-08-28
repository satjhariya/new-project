---
name: commit-message-storyteller
description: "Analyzes git working tree, inspects diffs/staged changes, generates narrative commit messages that explain WHY a change was made, not just what changed — following Conventional Commits formats, and handles git staging and commit workflows. ALWAYS trigger this skill whenever the user mentions committing changes, running a commit, saving changes to git, or writing commit messages—including phrases like 'commit the changes', 'commit my changes', 'commit this', 'commit', 'make a commit', 'write a commit message', 'stage and commit', 'generate commit', or 'help me commit'."
---

# Commit Message Storyteller

Transforms working tree changes, git diffs, and change descriptions into clear, story-driven commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification, and guides or executes the staging and committing workflow.

## When to Use This Skill

ALWAYS use this skill when the user requests a commit or commit message, including:
- "commit the changes" or "commit my changes"
- "commit" or "make a commit"
- "stage and commit"
- "write a commit message" or "generate a commit"
- "what should I commit this as?" or "summarize my diff"
- User pastes a git diff or describes code changes to commit

## End-to-End Workflow

### Step 1: Inspect Working Tree Automatically

Do not wait for the user to paste diffs manually. Immediately run shell commands to inspect the repository state:

```bash
git status
git diff
git diff --staged
```

- If no changes exist in `git status`, notify the user that the working tree is clean.
- Identify which files are untracked, modified, or already staged.

### Step 2: Gather Change Context & Evaluate Commit Splitting

Extract the core story:
1. **What changed** — files, functions, and logic affected
2. **Why it changed** — problem solved, bug fixed, feature added, refactored
3. **Trigger / Reference** — issue numbers, user request, or task goal

**Check for split commits:**
If the diff contains logically distinct, unrelated concerns (e.g., updating docs + fixing a bug + refactoring an API), offer to split them into separate atomic commits:
- Separate files/modules with unrelated purposes -> separate commits.
- Feature work vs. independent bug fix -> separate commits.

### Step 3: Identify Commit Type & Scope

Map the change to a Conventional Commits type:

| Type | Use When |
|------|----------|
| `feat` | A new feature or capability is added |
| `fix` | A bug or incorrect behavior is corrected |
| `refactor` | Code restructured without changing behavior |
| `perf` | A change that improves performance |
| `docs` | Documentation only changes |
| `style` | Formatting, whitespace, missing semicolons (no logic change) |
| `test` | Adding or updating tests |
| `chore` | Build process, dependency updates, config changes |
| `ci` | CI/CD pipeline changes |
| `revert` | Reverting a previous commit |

See `references/conventional-commits-guide.md` for detailed examples.

### Step 4: Write the Narrative Commit Message

Follow this exact structure:

```
<type>(<optional scope>): <short imperative summary>

<body — the story: why this change was made, what problem it solves>

<footer — issue refs, breaking change notices>
```

#### Rules for Each Part

**Subject line (first line):**
- Use imperative mood: "add", "fix", "remove" (not "added" or "fixes")
- Max 72 characters
- No period at the end
- Lowercase after the colon

**Body (the story):**
- Explain the *why*, not the *what* (the diff already shows the what)
- Describe the problem that existed before this change
- Mention any alternatives considered if relevant
- Keep lines under 100 characters
- Separate from subject with a blank line

**Footer:**
- Reference issues: `Closes #123`, `Fixes #456`, `Refs #789`
- Mark breaking changes: `BREAKING CHANGE: <description>`

### Step 5: Present Message & Execute Commit

1. Display the proposed commit message in a copyable code block along with a one-sentence summary of the story told.
2. If files are unstaged, stage the relevant files (`git add <files>` or `git add .`).
3. Execute the commit (`git commit -m "..."`).
4. If permissions or unsandboxed command prompts arise during execution, guide the user cleanly or request appropriate execution approval.

## Example Output

```
fix(auth): prevent token refresh loop on expired sessions

When a user's session expired mid-request, the auth middleware was
triggering a token refresh, which itself failed validation and triggered
another refresh — causing an infinite retry loop that crashed the app.

This adds a recursion guard flag that aborts the refresh cycle if a
refresh is already in progress, returning a clean 401 instead.

Closes #312
```

> **Story told:** A silent infinite loop on session expiry was crashing the app; this stops the cycle early and returns a clean error.

---

## Multiple Commits from One Diff

If the diff contains **logically separate changes**, split them into multiple commit messages and tell the user. Use this heuristic:

- Different files with unrelated purposes → likely separate commits
- Same file but distinct concerns (e.g., bug fix + refactor) → suggest splitting
- Everything tightly coupled → one commit is fine

---

## Edge Cases

| Situation | How to Handle |
|-----------|---------------|
| User provides no context beyond a diff | Infer type and scope from file names and changed symbols |
| Working tree has untracked files | Check if untracked files belong to the change before staging |
| Breaking change detected | Add `BREAKING CHANGE:` footer automatically and append `!` to type |
| User says "keep it short" | Omit body, just write a strong subject line |
| User denies command permission | Present the full git command line for the user to run manually |

---

## Quick Reference Commands

```bash
# Check working tree status
git status

# Inspect unstaged and staged diffs
git diff
git diff --staged

# Stage and commit
git add .
git commit -m "<message>"
```

See `references/conventional-commits-guide.md` for type examples and scope guidelines.
