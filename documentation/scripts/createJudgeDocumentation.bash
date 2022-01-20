echo "Creating documentation based on GIT history..."
rm ./documentation/files/judgeDocumentation.md
git log -p --all --pretty=format:'Author : %an %nDate/Time :  %aD%nCommit : %s' > ./documentation/files/judgeDocumentation.md
echo "Process completed successfully. You may now close this window."
