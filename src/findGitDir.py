import os
import subprocess

"""
This method will get all of the git repos listed under the given 
directory

param: directory path
retuns: list
"""
def find_git_repos(dir):
    repos = []
    for (path, dirs, files) in os.walk(dir):
        for directory in dirs:
            if directory == ".git":
                repos.append(path)
    return repos

"""
This will run git status for all the git repos
and compile a list of repo dirs that have
any staged commits

param: list
return: list
"""
def git_status(repos):
	for repo in repos:
		os.chdir(repo)
		status = subprocess.check_output(['git', 'status'])
		print status
		
				
def main():
	print "Enter the full directory you want to scan: "
	initial_directory = raw_input()
	repos = find_git_repos(initial_directory)
	print repos
	print "\n %s" % repos[0] 
	git_status([repos[0]])
	

	
if  __name__ =='__main__':main()