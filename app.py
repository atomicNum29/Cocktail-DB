from flask import Flask, render_template, redirect, url_for, request
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

# 칵테일 삭제 기능
@app.route('/delete/<int:cocktail_id>', methods=['POST'])
def delete_cocktail(cocktail_id):
    # 데이터베이스 연결
    conn = get_db_connection()
    
    # 삭제 작업
    try:
        conn.execute("DELETE FROM Cocktail WHERE id = ?", (cocktail_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error deleting cocktail: {e}")
    finally:
        conn.close()

    # 메인 페이지로 리다이렉션
    return redirect(url_for('index'))

# 칵테일 수정 기능
@app.route('/edit/<int:cocktail_id>', methods=['GET', 'POST'])
def edit_cocktail(cocktail_id):
    conn = get_db_connection()

    if request.method == 'POST':
        # 사용자가 입력한 데이터를 가져옴
        name = request.form['name']
        glass = request.form['glass']
        recipe = request.form['recipe']
        image = request.form['image']

        # 데이터베이스 업데이트
        try:
            conn.execute("""
                UPDATE Cocktail
                SET name = ?, glass = ?, recipe = ?, image = ?
                WHERE id = ?
            """, (name, glass, recipe, image, cocktail_id))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Error updating cocktail: {e}")
        finally:
            conn.close()

        # 수정 완료 후 상세 페이지로 리다이렉션
        return redirect(url_for('cocktail_detail', cocktail_id=cocktail_id))

    # GET 요청: 현재 데이터를 가져옴
    cocktail = conn.execute("SELECT * FROM Cocktail WHERE id = ?", (cocktail_id,)).fetchone()
    conn.close()

    if cocktail is None:
        return "Cocktail not found", 404

    return render_template('edit_cocktail.html', cocktail=cocktail)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)