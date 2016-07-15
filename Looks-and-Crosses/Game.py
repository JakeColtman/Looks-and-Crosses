
class Game:

    def __init__(self, conn, schema, table):
        self.conn = conn
        self.schema = schema
        self.table = table
        self.marks = ['x', 'o']
        self.turn = 1
        self.reset()

    def reset(self):
        query = """
            DROP TABLE {0}.{1};
            CREATE TABLE {0}.{1} (
              r_id char(1),
              l char(2),
              m char(2),
              r char(2)
            )
            """
        print(query.format(self.schema, self.table))
        self.conn.run_query(query.format(self.schema, self.table))

        self.conn.run_query("""

        INSERT INTO {0}.{1} (r_id, l,m,r)
        VALUES
        ('t', 'tl','tm','tr'),
        ('m', 'ml','mm','mr'),
        ('b', 'bl','bm','br')
        """.format(self.schema, self.table))

    def update_position(self, r, c):
        query = """
           UPDATE {0}.{1} set {2} = '{4}' where r_id = '{3}'
        """.format(self.schema, self.table, c, r, self.marks[self.turn])
        print(query)
        self.conn.run_query(query)
        self.turn += 1
        if self.turn > 1:
            self.turn = 0