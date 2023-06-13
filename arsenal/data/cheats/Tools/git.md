# git

#platform/multiple #target/local #cat/UTILS 

## Set global git user name
```
git config --global user.name <name>
```

## Set global git user email
```
git config --global user.email <email>
```

## Initializes a git repository
```
git init
```

## Clone a git repository
```
git clone -b <branch_name> <repository> <clone_directory>
```

## View all available remote for a git repository
```
git remote --verbose
```

## Adds a remote for a git repository
```
git remote add <remote_name> <remote_url>
```

## Renames a remote for a git repository
```
git remote rename <old_remote_name> <new_remote_name>
```

## Remove a remote for a git repository
```
git remote remove <remote_name>
```

## Checkout to branch
```
git checkout <branch>
```

## Displays the current status of a git repository
```
git status
```

## Displays unstaged changes for file
```
git diff <unstaged_files>
```

## Stage single or multiple files
```
git add <changed_files>;
```

## Stage all files in project
```
git add -A
```

## Saves the changes to a file in a commit
```
git commit -m <message>
```

## Pushes committed changes to remote repository
```
git push -u <remote_name> <branch_name>
```

## Pushes changes to a remote repository overwriting another branch
```
git push <remote_name> <branch>:<branch_to_overwrite>
```

## Overwrites remote branch with local branch changes
```
git push <remote_name> <branch_name> -f
```

## Pulls changes to a remote repo to the local repo
```
git pull --ff-only
```

## Merges changes on one branch into current branch
```
git merge <branch_name>
```

## Abort the current conflict resolution process, and try to reconstruct the pre-merge state.
```
git merge --abort
```

## Displays log of commits for a repo
```
git log
```

## Displays formatted log of commits for a repo
```
git log --all --decorate --oneline --graph
```

## Clear everything
```
git clean -dxf
```

## Sign all commits in a branch based on master
```
git rebase master -S -f
```

## Checkout a branch from a fork
```
git fetch origin pull/<pr_number>/head:pr/<pr_number> && git checkout pr/<pr_number>
```

## Add a new module
```
git submodule add <repository> <path>
```

## Update module
```
git submodule update --init
```

## Update module without init
```
git submodule update
```

## Pull all submodules
```
git submodule foreach git pull origin master
```

## Update all submodules
```
git submodule update --init --recursive
```

## Skip git hooks
```
git commit --no-verify
```

## Create new branch from current HEAD
```
git checkout -b <new_branch_name>
```

## pull remote branch and switch to it
```
git checkout -b <new_branch_name> <remote>/<branch_name>
```

## git dump
```
gitdumper <url>/.git/ <destination_dir>
```

= remote: origin
