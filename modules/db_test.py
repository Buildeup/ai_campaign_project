import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pymysql
from config.db_config import DB_CONFIG

def test_connection():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        print("✅ DB 연결 성공!")
        
        with conn.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("📦 현재 DB 테이블 목록:")
            for table in tables:
                print(table)
                
    except Exception as e:
        print("❌ DB 연결 실패:", e)
    finally:
        conn.close()
        print("🔒 연결 종료.")

if __name__ == "__main__":
    test_connection()
