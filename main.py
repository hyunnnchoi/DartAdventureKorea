import random
import folium
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

# 중심 좌표를 한국의 중앙쯤으로 설정
map_center = [36.5, 127.5]

# 지도 생성
m = folium.Map(location=map_center, zoom_start=7)

# 랜덤 좌표 생성 및 지도에 표시
for _ in range(1):
    lat, lon = generate_random_coordinate()
    folium.Marker([lat, lon], popup=f"위도: {lat:.6f}, 경도: {lon:.6f}").add_to(m)

# 지도를 HTML 파일로 저장
map_file = "random_coordinates_map.html"
m.save(map_file)

# 웹 브라우저로 HTML 파일 열기
webbrowser.open(map_file)
