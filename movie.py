import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 🔍 크롤링할 영화 코드 
movie_code = "221150"
base_url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false"

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_reviews = []

for page in range(1, 11): 
    url = f"{base_url}&page={page}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    review_boxes = soup.select("div.score_result > ul > li")

    if not review_boxes:
        print(f"{page}페이지: 리뷰 없음")
        break

    for box in review_boxes:
        try:
            score = box.select_one("div.star_score > em").text
            review = box.select_one("div.score_reple > p").text.strip()
            date = box.select_one("div.score_reple dt em:nth-of-type(2)").text.strip()
            all_reviews.append({
                "score": int(score),
                "review": review,
                "date": date
            })
        except Exception as e:
            print("리뷰 파싱 중 오류:", e)

    print(f"{page}페이지 완료")
    time.sleep(1)  # 서버에 부담 안 주기 위해 잠깐 쉬기

