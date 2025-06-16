import pymysql
from config.db_config import DB_CONFIG

def get_connection():
    return pymysql.connect(**DB_CONFIG)


def save_campaign(name, url):
    """
    캠페인 정보를 저장하고 ID 반환
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO campaigns (name, product_url) VALUES (%s, %s)"
            cursor.execute(sql, (name, url))
            conn.commit()
            return cursor.lastrowid
    finally:
        conn.close()


def save_blogs_to_db(blog_list, campaign_id):
    """
    블로그 데이터를 blogs 테이블에 저장하며 campaign_id 연동
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO blogs
                (campaign_id, title, description, url, postdate, bloggername, bloggerlink, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            for blog in blog_list:
                cursor.execute(sql, (
                    campaign_id,
                    blog.get("title", ""),
                    blog.get("desc", ""),
                    blog.get("url", ""),
                    blog.get("postdate", ""),
                    blog.get("bloggername", ""),
                    blog.get("bloggerlink", ""),
                    blog.get("email", "")
                ))
            conn.commit()
            return len(blog_list)
    finally:
        conn.close()
