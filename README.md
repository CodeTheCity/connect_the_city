# connect_the_city

A project started at CTC28 looking to find who worked on which CTC projects

## Project participants

- Samuel Onekutu
- Jack Gilmore
- Angel Emmanuel

## Getting started

You will need to create a copy of `config_template.yml` and save it as `config.yml`, making sure to populate the GitHub token key with a GitHub personal access token with `public_repo` access.

You also need to set up the `neo4j` key with your connection details for your neo4j database.

## Repo metadata tagging
The following tags are picked up by the script when reading repos:
| Tag           | Purpose                                                                                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ctc##         | Tagging a project repo associated with a particular event. You can add multiple of these if the repo was used across multiple events. Sub out the hashes for the number |
| event-repo    | Tagging the main "hub" repo associated with an event. Usually named with a pattern of CTC## e.g. CTC28                                                                  |
| graph-exclude | Exclude repository from script. E.g. if it's a utility repository or something that's archived.                                                                         |

TODO: If a repo isn't excluded or have an event tag, assign it an Unknown event node!
