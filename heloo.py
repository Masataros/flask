from flask import Flask, render_template #追加
import pymysql #追加

app = Flask(__name__)

@app.route('/')
def hello():

    #db setting
    db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='test',
            cursorclass=pymysql.cursors.DictCursor,
        )

    cur = db.cursor()
    sql = "select * from lost"
    cur.execute(sql)
    lost = cur.fetchall()

    cur.close()
    db.close()

    #return name
    return render_template('heloo.html', title='flask test', lost=lost) #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)

