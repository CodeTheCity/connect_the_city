from github import Github
import os

token = os.getenv('github_token')

g = Github(token)

my_repos = g.get_organization("codethecity").get_repos()

contributor_list = []

for repo in my_repos:
    print(repo.name)
    contributors = repo.get_contributors()
    print("\t" + str(contributors.totalCount) + " total contributors:")
    for contributor in contributors:
        print("\t\t" + contributor.login)
        contributor_list.append(contributor.login)



distinct_list = set(contributor_list)

print('=====')
print(str(len(contributor_list)) + " instances of users contributing to a project")
print(str(len(distinct_list)) + " distinct contributors found across " + str(my_repos.totalCount) + " total repos")
print('=====')