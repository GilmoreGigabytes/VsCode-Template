echo "Creating documentaion based on GIT commit history."
rm ./judgeDocumentation.md
git log -p --all --pretty=format:'Author : %an %nDate/Time :  %aD%nCommit : %s' > ./documentation.md
echo "Process completed successfully. You may now close this window."
