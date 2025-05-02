import yt_dlp  # 유튜브 및 기타 플랫폼에서 미디어를 다운로드할 수 있는 라이브러리
import os      # 경로 조작을 위한 표준 라이브러리

# 🎥 영상 다운로드 함수
def download_video(url, save_path, quality='1080p'):
    # 화질에 따른 resolution filter 설정
    resolution_map = {
        "1080p": "bestvideo[height<=1080][ext=mp4]",
        "720p": "bestvideo[height<=720][ext=mp4]",
        "480p": "bestvideo[height<=480][ext=mp4]",
        "360p": "bestvideo[height<=360][ext=mp4]",
    }
    selected_format = resolution_map.get(quality, resolution_map["720p"])  # fallback

    ydl_opts = {
        'format': selected_format,
        'outtmpl': os.path.join(save_path, '%(title)s_video.%(ext)s'),
        'noplaylist': True,
        'overwrites': True,
        'merge_output_format': 'mp4',  # audio와 merge용
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# 🎵 오디오 다운로드 함수
def download_audio(url, save_path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',  # m4a 확장자의 최고 음질 오디오 선택
        'outtmpl': os.path.join(save_path, '%(title)s_audio.%(ext)s'),  # 저장 경로 및 파일명 지정
        'noplaylist': True,     # 재생목록 방지
        'overwrites': True      # 파일 덮어쓰기
    }

    # yt_dlp 객체 생성 후 다운로드 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # 리스트로 감싸서 전달
