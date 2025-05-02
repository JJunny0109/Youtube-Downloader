import yt_dlp  # 유튜브 및 기타 플랫폼에서 미디어를 다운로드할 수 있는 라이브러리
import os      # 경로 조작을 위한 표준 라이브러리

# 🎥 영상 다운로드 함수
def download_video(url, save_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]',  # mp4 확장자의 최고 화질 영상 선택
        'outtmpl': os.path.join(save_path, '%(title)s_video.%(ext)s'),  # 저장 경로 및 파일명 지정
        'noplaylist': True,     # 재생목록이 아닌 단일 영상만 다운로드
        'overwrites': True      # 기존 파일이 있으면 덮어쓰기
    }

    # yt_dlp 객체 생성 후 다운로드 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # 리스트 형식으로 URL 전달

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
