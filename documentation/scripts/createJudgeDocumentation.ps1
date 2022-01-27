echo "Creating documentaion based on GIT commit history."
rm ../files/judgeDocumentation.md
git log -p --all --pretty=format:'Author : %an %nDate/Time :  %aD%nCommit : %s' > ./documentation/files/judgeDocumentation.md
echo "Process completed successfully. You may now close this window."
