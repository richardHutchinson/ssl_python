#!/usr/bin/env python

import mysql.connector
import PostsClasses

class MySQLCursorDict(mysql.connector.cursor.MySQLCursor):
    def _row_to_python(self, rowdata, desc=None):
        row = super(MySQLCursorDict, self)._row_to_python(rowdata, desc)
        if row:
            return dict(zip(self.column_names, row))
        return None

cnx = mysql.connector.connect(user='root', database='ssl_todd')
cursor = cnx.cursor(cursor_class=MySQLCursorDict)

query = ("SELECT * FROM users")
cursor.execute(query)
row = cursor.fetchall()

postClasses = PostsClasses.PostsClasses()

print "Content-Type: text/html"
print
print """\
<html>
<body>
<p>""" + postClasses.returnPosts("a") + """</p>
</body>
</html>
"""