import subprocess
import os

def run_cmd(cmd):
    """Run a shell command and return its output"""
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def commit_file(filename, message):
    """Stage and commit one file"""
    run_cmd(f'git add "{filename}"')
    run_cmd(f'git commit -m "{message}"')

def main():
    # Ensure inside a git repo
    try:
        run_cmd("git rev-parse --is-inside-work-tree")
    except subprocess.CalledProcessError:
        print("❌ Not inside a git repository. Exiting.")
        return

    # Get changed files from git status
    status_output = run_cmd("git status --porcelain").splitlines()
    changed_files = []
    for line in status_output:
        # Format: "XY filename"
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            filename = parts[1]
            if os.path.isfile(filename):  # skip folders
                changed_files.append(filename)

    if not changed_files:
        print("ℹ️ No modified or untracked files found.")
        return

    # Take only the first 3
    files_to_commit = changed_files[:3]

    print("📂 Files that will be committed (one per commit):")
    for f in files_to_commit:
        print(" -", f)

    confirm = input("\nDo you want to proceed with committing these files? (y/n): ").lower()
    if confirm != "y":
        print("🚫 Commit cancelled.")
        return

    # Commit each file separately
    for f in files_to_commit:
        commit_msg = f"Add/update {f}"
        commit_file(f, commit_msg)

    # Show summary
    print("\n✅ Commits created. Summary:\n")
    summary = run_cmd(f"git log -{len(files_to_commit)} --oneline")
    print(summary)

    # Ask before pushing
    confirm = input("\nDo you want to push these commits? (y/n): ").lower()
    if confirm == "y":
        try:
            branch = run_cmd("git branch --show-current")
            run_cmd(f"git push origin {branch}")
            print(f"🚀 Pushed to origin/{branch}")
        except subprocess.CalledProcessError as e:
            print("❌ Push failed:", e)
    else:
        print("🚫 Push cancelled.")

if __name__ == "__main__":
    main()
