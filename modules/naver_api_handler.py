import requests
from config.naver_config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET


def search_naver_blogs(keyword, display=100, sort_option="정확도순", start=1):
    url = "https://openapi.naver.com/v1/search/blog.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    sort = "sim" if sort_option == "정확도순" else "date"
    params = {
        "query": keyword,
        "display": display,
        "start": start,
        "sort": sort
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"❌ 네이버 API 오류: {response.status_code} {response.reason}")
        return []


def parse_blog_results(items):
    blog_list = []
    for item in items:
        bloggerlink = item.get("bloggerlink", "")
        email = ""
        if bloggerlink:
            email_id = bloggerlink.rstrip("/").split("/")[-1]
            email = f"{email_id}@naver.com"
        blog_info = {
            "title": item.get("title", ""),
            "desc": item.get("description", ""),
            "url": item.get("link", ""),
            "postdate": item.get("postdate", ""),
            "bloggername": item.get("bloggername", ""),
            "bloggerlink": bloggerlink,
            "email": email
        }
        blog_list.append(blog_info)
    return blog_list


def search_and_parse(keyword, total_count=100, sort_option="정확도순"):
    """
    최대 1000개까지 100개 단위로 반복 요청하여 누적 수집
    """
    all_items = []
    for start in range(1, total_count + 1, 100):
        display = min(100, total_count - len(all_items))
        if display <= 0:
            break
        items = search_naver_blogs(keyword, display=display, sort_option=sort_option, start=start)
        if not items:
            break
        all_items.extend(items)
        if len(items) < display:
            break
    return parse_blog_results(all_items[:total_count])

# import pymysql
# from config.db_config import DB_CONFIG

def get_connection():
    # return pymysql.connect(**DB_CONFIG)
    pass

def save_campaign(name, url):
    """
    캠페인 정보를 저장하고 ID 반환
    """
    # conn = get_connection()
    # try:
    #     with conn.cursor() as cursor:
    #         sql = "INSERT INTO campaigns (name, product_url) VALUES (%s, %s)"
    #         cursor.execute(sql, (name, url))
    #         conn.commit()
    #         return cursor.lastrowid
    # finally:
    #     conn.close()
    pass

def save_blogs_to_db(blog_list, campaign_id):
    """
    블로그 데이터를 blogs 테이블에 저장하며 campaign_id 연동
    """
    # conn = get_connection()
    # try:
    #     with conn.cursor() as cursor:
    #         sql = """
    #             INSERT INTO blogs
    #             (campaign_id, title, description, url, postdate, bloggername, bloggerlink, email)
    #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    #         """
    #         for blog in blog_list:
    #             cursor.execute(sql, (
    #                 campaign_id,
    #                 blog.get("title", ""),
    #                 blog.get("desc", ""),
    #                 blog.get("url", ""),
    #                 blog.get("postdate", ""),
    #                 blog.get("bloggername", ""),
    #                 blog.get("bloggerlink", ""),
    #                 blog.get("email", "")
    #             ))
    #         conn.commit()
    #         return len(blog_list)
    # finally:
    #     conn.close()
    pass
