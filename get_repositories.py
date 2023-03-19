from github import Github
import yaml
from neo4j_db import neo4j_db

# Set up config
print("======================")
print("Setting up config from config.yml...")
print("======================\n")
config = yaml.safe_load(open("config.yml"))
token = config["github"]["token"]

# Connect to neo4j
print("======================")
print("Connecting to Neo4j...")
print("======================\n")
neo4j_config = config["neo4j"]
neo4j_database = neo4j_db(neo4j_config["uri"],neo4j_config["username"],neo4j_config["password"])

current_user = neo4j_database.get_current_user()

print("======================")
print("Currently logged in as " + current_user["user"] + " at " + neo4j_config["uri"])
print("======================\n")


# Connect to GitHub and get repos for CTC
g = Github(token)
my_repos = g.get_organization("codethecity").get_repos()

contributor_list = []

for repo in my_repos:
    print(repo.name)
    print("Adding to Neo4j database...")
    #neo4j_database.create_repo_node(repo.name)
    contributors = repo.get_contributors()
    print("\t" + str(contributors.totalCount) + " total contributors:")
    for contributor in contributors:
        print("\t\t" + contributor.login)
        contributor_list.append(contributor.login)
        #neo4j_database.create_contributor_node(contributor.login, repo.name)
        neo4j_database.create_relation(contributor.login, repo.name)
    

# Get a list of unique contributors
distinct_list = set(contributor_list)

print('=====')
print(str(len(contributor_list)) + " instances of users contributing to a project")
print(str(len(distinct_list)) + " distinct contributors found across " + str(my_repos.totalCount) + " total repos")
print('=====')