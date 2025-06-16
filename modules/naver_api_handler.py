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
