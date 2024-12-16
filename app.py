from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'DB/cocktail-DB.db'

# DB 연결 함수
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# 메인 페이지: 칵테일 리스트
@app.route('/')
def index():
    conn = get_db_connection()
    cocktails = conn.execute('SELECT * FROM Cocktail').fetchall()
    conn.close()
    return render_template('index.html', cocktails=cocktails)

# 특정 칵테일의 상세 정보
@app.route('/cocktail/<int:cocktail_id>')
def cocktail_detail(cocktail_id):
    conn = get_db_connection()
    cocktail = conn.execute('SELECT * FROM Cocktail WHERE id = ?', (cocktail_id,)).fetchone()
    ingredients = conn.execute("""
        SELECT i.name, ci.amount
        FROM Ingredient i
        JOIN Cocktail_Ingredient ci ON i.id = ci.ingredient_id
        WHERE ci.cocktail_id = ?
    """, (cocktail_id,)).fetchall()
    conn.close()
    return render_template('cocktail_detail.html', cocktail=cocktail, ingredients=ingredients)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)