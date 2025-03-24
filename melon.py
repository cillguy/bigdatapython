pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# 1️⃣ 멜론 차트 URL
url = "https://www.melon.com/chart/index.htm"

# 2️⃣ 웹 페이지 요청 (User-Agent 추가)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
html = response.text

# 3️⃣ BeautifulSoup 객체 생성
soup = BeautifulSoup(html, "html.parser")

# 4️⃣ 노래 제목, 가수 정보 가져오기
songs = soup.select("tr")  # 차트에서 노래 정보를 포함하는 태그 선택

for song in songs:
    rank = song.select_one(".rank")  # 순위
    title = song.select_one(".rank01 a")  # 노래 제목
    artist = song.select_one(".rank02 span")  # 가수

    if rank and title and artist:  # 유효한 데이터만 출력
        print(f"{rank.text.strip()}위: {title.text.strip()} - {artist.text.strip()}")
