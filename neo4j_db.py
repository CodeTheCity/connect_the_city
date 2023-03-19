from neo4j import GraphDatabase

class neo4j_db:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_current_user(self):
        with self.driver.session() as session:
            query_result = session.run("SHOW CURRENT USER")
            return [record.data() for record in query_result][0]
        
    def create_repo_node(self, name):
        with self.driver.session() as session:
            session.execute_write(self._write_repo_node, name)

    @staticmethod
    def _write_repo_node(tx, name):
        result = tx.run("""
            CREATE (n:Project {name: $name})
        """, name=name)

    def create_contributor_node(self, name, repo):
        with self.driver.session() as session:
            session.execute_write(self._write_contributor_node, name, repo)

    @staticmethod
    def _write_contributor_node(tx, name, repo):
        tx.run("""
            MERGE (n:Contributor {name: $name})
        """, name=name)

    def create_relation(self, name, repo):
            with self.driver.session() as session:
                session.execute_write(self._write_relation, name, repo)

    @staticmethod
    def _write_relation(tx, name, repo):
        tran = tx.run("""
            MERGE (n:Project {name: $repo})
            MERGE (m:Contributor {name: $name})
            MERGE (m)-[:worked_on]->(n);
        """, name=name, repo=repo)
