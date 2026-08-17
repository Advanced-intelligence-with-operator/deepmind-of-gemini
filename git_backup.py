import os
import pygit2

def auto_commit_changes(repo_path, commit_message="Automated local environment backup"):
    # 1. Open the repository (or initialize it if it doesn't exist)
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print(f"Initializing new Git repository at {repo_path}...")
        repo = pygit2.init_repository(repo_path)
    else:
        repo = pygit2.Repository(repo_path)

    # 2. Get the repository status to see if anything changed
    status = repo.status()
    if not status:
        print("No changes detected. Everything is up to date.")
        return

    # 3. Stage all changes (add everything to the index)
    index = repo.index
    index.add_all()
    index.write()

    # 4. Create the tree from the updated index
    tree_id = index.write_tree()
    tree = repo[tree_id]

    # 5. Set up signature details (using local profile details)
    author = pygit2.Signature('James Anthony Sovereign', 'james@geminiinclllc.local')
    committer = author

    # 6. Determine the parent commit (if any exists yet)
    parents = []
    if not repo.is_empty:
        # Get the current HEAD commit
        head_commit = repo[repo.head.target]
        parents.append(head_commit.id)

    # 7. Commit the changes
    commit_id = repo.create_commit(
        'HEAD',          # Update the HEAD reference
        author,          # Author signature
        committer,       # Committer signature
        commit_message,  # Commit message
        tree_id,         # The tree we just built
        parents          # Parent commit list
    )

    print(f"Successfully committed changes! Commit ID: {commit_id}")

# Example usage inside your Termux home directory:
# repo_dir = os.path.expanduser("~/my_local_workspace")
# auto_commit_changes(repo_dir)
