echo "Creating documentation based on git history "

git log -p --all --pretty=format:'Author : %an %nDate/Time :  %aD%nCommit : %s' > ./documentaion.md
