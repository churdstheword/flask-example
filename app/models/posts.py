class Posts:

    def __init__(self, conn):
        self.conn = conn

    def getPosts(self):
        return self.conn.execute('SELECT * FROM posts').fetchall()

    def getPost(self, post_id):
        return self.conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()    

    def insertPost(self, title, content):
        self.conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        self.conn.commit()
        return

    def updatePost(self, title, content, id):
        self.conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
        self.conn.commit()
        return

    def deletePost(self, id):
        self.conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        return
