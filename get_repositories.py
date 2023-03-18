from github import Github

g = Github()

my_repos = g.get_organization("codethecity").get_repos()

for repo in my_repos:
    print(repo.name)

print(my_repos.totalCount)