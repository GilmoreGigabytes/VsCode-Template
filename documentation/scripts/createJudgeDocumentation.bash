echo "Creating documentation based on GIT history..."
> ../files/judgeDocumentation.md
git log -p --all --pretty=format:'Author : %an %nDate/Time :  %aD%nCommit : %s' > ../files/judgeDocumentation.md
echo "Process completed successfully. You may now close this window."
