echo "Creating documentaion based on git commit history"

git log -p --all --pretty=format:'Author : %an %nDate/Time :  %aD%nCommit : %s' > ./documentaion.md