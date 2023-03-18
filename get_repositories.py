from github import Github
import os

token = os.getenv('github_token')

g = Github(token)

my_repos = g.get_organization("codethecity").get_repos()

for repo in my_repos:
    print(repo.name)
    contributors = repo.get_contributors()
    print("\t" + str(contributors.totalCount) + " total contributors:")
    for contributor in contributors:
        print("\t" + contributor.name)
