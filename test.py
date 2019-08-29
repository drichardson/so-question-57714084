import git

repo = git.Repo(path=".", search_parent_directories=True)

repo.config_reader()

print repo.untracked_files

_git = repo.git

print 'hi'
print _git.log("ce33f5aeee2f14de06bea795649b930d96a15aec..fe1b885ae9934f9e28ebe68c3633db2088e6f38e")
print '2'
print _git.log("fe1b885ae9934f9e28ebe68c3633db2088e6f38e..ce33f5aeee2f14de06bea795649b930d96a15aec", "--pretty=tformat:%h:%s:%cn")

print 'TESTING'
good="fe1b885ae9934f9e28ebe68c3633db2088e6f38e"
bad="ce33f5aeee2f14de06bea795649b930d96a15aec"
_git = git.Git(repo.working_tree_dir)
print(_git.log('{}..{} --pretty=tformat:%h:%s:%cn'.format(good, bad).split()))

print 'DONE'

