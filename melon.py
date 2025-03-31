
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
import random
import time

songs = ["a노래", "b노래", "c노래", "d노래"]
print(songs)
print(songs[0])
print(songs[1])
print(songs[2])
print(songs[3])

for song in songs:
    print(song)   

print("AI야 노래 한곡만 추천해줘") 
print("""
알겠습니다. 
제가 열심히 분석해서 
고객님께 노래를 한곡 
추천합니다
      """) 
# 여기서 AI가 돌아야죠
ai_song = random.choice(songs)
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)
    
print(f"제가 추천한곡은 {ai_song}입니다.") 

# 리스트를 쓰는 이유
song1 = "a노래"
song2 = "b노래"
song3 = "c노래"

# print(song1)
# print(song2)
# print(song3)
