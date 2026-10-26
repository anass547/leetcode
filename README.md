# LeetCode Solutions

My LeetCode solutions, synced automatically to this repo with GitHub Actions.

[![Sync LeetCode](https://github.com/<github-username>/leetcode-solutions/actions/workflows/leetcode-sync.yml/badge.svg)](https://github.com/<github-username>/leetcode-solutions/actions/workflows/leetcode-sync.yml)

## Profile

[leetcode.com/u/anasuss](https://leetcode.com/u/anasuss)

## Structure

```
.
├── .github/workflows/leetcode-sync.yml   # sync workflow
└── solutions/                            # one folder per problem
    └── <id>-<problem-name>/
        ├── README.md                     # problem statement
        └── <solution file>               # accepted submission
```

## How it works

The workflow uses [joshcai/leetcode-sync](https://github.com/joshcai/leetcode-sync). Every 6 hours (or on manual trigger) it:

1. Fetches my accepted submissions from LeetCode
2. Commits new ones to `solutions/`
3. Uses commit messages in the form `[LeetCode Sync] Runtime - ... , Memory - ...`

## Setup (to reuse for your own repo)

1. Create a repo and add `.github/workflows/leetcode-sync.yml` from this repo.
2. Add these repository secrets (Settings → Secrets and variables → Actions):
   - `LEETCODE_CSRF_TOKEN`: the `csrftoken` cookie from leetcode.com
   - `LEETCODE_SESSION`: the `LEETCODE_SESSION` cookie from leetcode.com
3. Settings → Actions → General → Workflow permissions → **Read and write**.
4. Run the workflow from the Actions tab.

`LEETCODE_SESSION` expires after a few weeks and must be refreshed in the secrets.

## Languages

<Python / Java / SQL / ...>
