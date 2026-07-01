# Development Process

## Git Workflow

We use a feature-branch workflow with pull requests.

```mermaid
gitGraph
    commit
    branch feature/week5-docs
    checkout feature/week5-docs
    commit
    commit
    checkout main
    merge feature/week5-docs
    commit
    branch feature/mvp-v2
    checkout feature/mvp-v2
    commit
    commit
    checkout main
    merge feature/mvp-v2
