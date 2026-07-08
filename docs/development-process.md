# Development Process

## Git Workflow

We use a feature-branch workflow with pull requests.  

```mermaid
gitGraph
    commit id: "v1.0" tag: "release"
    branch feature/architecture
    checkout feature/architecture
    commit id: "architecture"
    commit id: "ADRs"
    checkout main
    merge feature/architecture id: "merge architecture" tag: "v0.3.0"
    commit id: "hotfix"
    branch feature/mavlink-backend
    checkout feature/mavlink-backend
    commit id: "add mavlink"
    commit id: "tests"
    checkout main
    merge feature/mavlink-backend id: "merge backend" tag: "v1.2"
```

**How we use it**
1. **Main branch** – protected. All changes go through PRs.
2. **Feature branches** – created from main for each issue (e.g., 40-write-tests).
3. **Pull requests** – required for all changes. At least one approval needed.
4. **CI** – runs on every PR and push to main (tests, linters, link checks).
5. **Merging** – after review and passing CI.

**Work Status**
We use GitHub issues with status labels:

- **To Do** – not started
- **In Progress** – currently working
- **Done** – merged and closed

**Definition of Done**  
See [Definition Of Done](definition-of-done.md).
