import random
import webbrowser

def generate_random_coordinate():
    # 한국의 위도와 경도 범위
    min_latitude = 33.1000
    max_latitude = 38.6137
    min_longitude = 124.6231
    max_longitude = 131.8722

    # 위도와 경도를 랜덤하게 생성
    random_latitude = random.uniform(min_latitude, max_latitude)
    random_longitude = random.uniform(min_longitude, max_longitude)

    return random_latitude, random_longitude

# 랜덤 좌표 생성
lat, lon = generate_random_coordinate()

# 구글 맵 검색 URL 생성
google_maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"

# URL 출력
print("Google Maps URL:", google_maps_url)

# 웹 브라우저로 URL 열기
webbrowser.open(google_maps_url)
