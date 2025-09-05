import sqlite3

def test_user_status():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT username, status FROM users WHERE username='student'")
    result = cursor.fetchone()

    assert result[1] == "active"  # validation check

    conn.close()
