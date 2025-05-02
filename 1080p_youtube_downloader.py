import yt_dlp

url = input("유튜브 영상 주소를 입력하세요: ")

# 병합 없이 video + audio 따로 다운로드 (ffmpeg 없이 실행 보장)
ydl_opts = {
    'format': 'bestvideo[ext=mp4]',           # 영상만 다운로드
    'outtmpl': '%(title)s_video.%(ext)s',     # 영상 저장 파일명

    'noplaylist': True,                        # 재생목록 방지
    'postprocessors': [],                      # 후처리 제거 (병합 안 함)
    'merge_output_format': None,               # 병합 비활성화
    'overwrites': True                         # 파일 덮어쓰기 허용
}

# 영상 다운로드
print("🎥 고화질 영상(mp4) 다운로드 중...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# 오디오만 따로 다운로드
audio_opts = {
    'format': 'bestaudio[ext=m4a]',            # 오디오만 다운로드
    'outtmpl': '%(title)s_audio.%(ext)s',      # 오디오 저장 파일명

    'noplaylist': True,
    'postprocessors': [],
    'merge_output_format': None,
    'overwrites': True
}

print("🎧 오디오(m4a) 다운로드 중...")
with yt_dlp.YoutubeDL(audio_opts) as ydl:
    ydl.download([url])
