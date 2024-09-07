import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Lorem ipsum odor amet, consectetuer adipiscing elit. Neque congue dignissim posuere blandit orci. Gravida dictumst auctor elit nam ad; mi sagittis. Eleifend eleifend dictumst tincidunt amet ullamcorper sed. Semper pulvinar dictumst iaculis neque torquent scelerisque pretium volutpat. Purus nisl sociosqu tempor vestibulum parturient suscipit vestibulum sagittis. Ultricies libero cursus fermentum quam augue habitant. Praesent scelerisque morbi dis mattis lectus non justo. Montes gravida sem eget dictum donec elementum torquent venenatis.Porttitor tincidunt natoque pretium ex feugiat amet velit mattis fames. Iaculis auctor accumsan magnis nisl purus duis eros. Aptent aenean ultrices ac efficitur; hac malesuada nostra. Aenean egestas erat aliquam blandit; parturient accumsan. Suspendisse mi sociosqu scelerisque sociosqu magna. Taciti libero sagittis lacus congue eleifend. Viverra eu ad vivamus morbi class tincidunt. Adipiscing integer maecenas suscipit magnis orci. Sapien cubilia senectus odio felis at blandit.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Third Post', 'Content for the pooopppp post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Fourth Post', 'Lorem ipsum odor amet, consectetuer adipiscing elit. Neque congue dignissim posuere blandit orci. Gravida dictumst auctor elit nam ad; mi sagittis. Eleifend eleifend dictumst tincidunt amet ullamcorper sed. Semper pulvinar dictumst iaculis neque torquent scelerisque pretium volutpat. Purus nisl sociosqu tempor vestibulum parturient suscipit vestibulum sagittis. Ultricies libero cursus fermentum quam augue habitant. Praesent scelerisque morbi dis mattis lectus non justo. Montes gravida sem eget dictum donec elementum torquent venenatis.Porttitor tincidunt natoque pretium ex feugiat amet velit mattis fames. Iaculis auctor accumsan magnis nisl purus duis eros. Aptent aenean ultrices ac efficitur; hac malesuada nostra. Aenean egestas erat aliquam blandit; parturient accumsan. Suspendisse mi sociosqu scelerisque sociosqu magna. Taciti libero sagittis lacus congue eleifend. Viverra eu ad vivamus morbi class tincidunt. Adipiscing integer maecenas suscipit magnis orci. Sapien cubilia senectus odio felis at blandit.')
            )

connection.commit()
connection.close()