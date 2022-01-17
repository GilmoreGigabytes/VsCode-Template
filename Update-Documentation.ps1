Clear-Content ".\Documentation.md"

echo "Updating documentaion based on git commit history"

git log -p --all > documentation.md
