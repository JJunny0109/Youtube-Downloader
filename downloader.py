import yt_dlp  # 유튜브 영상 다운로드를 위한 라이브러리
import os      # 경로 조작을 위한 표준 라이브러리
import re      # ANSI 이스케이프 코드 제거용
import time    # 시간 체크용

# 🔍 영상에서 사용 가능한 해상도 목록 가져오기
def get_available_resolutions(url):
    """
    영상의 사용 가능한 화질 목록 반환 (예: ['2160p', '1440p', '1080p', ...])
    """
    ydl_opts = {'quiet': True}  # 로그 출력 최소화
    resolutions = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # 다운로드 없이 정보만 추출
        formats = info.get("formats", [])

        for f in formats:
            height = f.get("height")  # 영상 해상도 정보
            ext = f.get("ext")        # 파일 형식 (mp4 등)
            if height and ext == 'mp4':  # mp4 영상만 필터링
                res_label = f"{height}p"
                if res_label not in resolutions:
                    resolutions.append(res_label)

    # 높은 해상도부터 정렬
    resolutions = sorted(resolutions, key=lambda x: int(x.replace("p", "")), reverse=True)
    return resolutions

# ✅ ANSI 색상 코드 제거 함수
def strip_ansi(text):
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

# 🎥 영상 다운로드 함수
def download_video(url, save_path, quality='1080p', progress_callback=None):  # ✅ 진행률 콜백 추가
    # 선택된 화질(예: 1080p → 1080)로 필터 조건 생성
    height = quality.replace("p", "")
    format_string = f"bestvideo[height={height}][ext=mp4]"

    # ✅ 다운로드 중일 때 진행률을 콜백으로 전달
    def hook(d):
        if d['status'] == 'downloading' and progress_callback:
            percent = d.get('_percent_str', '0.0%').strip()
            clean_percent = strip_ansi(percent)
            progress_callback(f"📥 영상 다운로드 중... {clean_percent}")

    ydl_opts = {
        'format': format_string,  # 사용자가 선택한 화질
        'outtmpl': os.path.join(save_path, '%(title)s_video.%(ext)s'),  # 저장 경로 및 파일명 지정
        'noplaylist': True,     # 재생목록이 아닌 단일 영상만 다운로드
        'overwrites': True,     # 기존 파일이 있으면 덮어쓰기
        'merge_output_format': 'mp4',  # 오디오와 병합 시 사용할 형식
        'progress_hooks': [hook],  # ✅ 진행률 hook 등록
        'quiet': True
    }

    # yt_dlp 객체 생성 후 다운로드 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # 리스트 형식으로 URL 전달

# 🎵 오디오 다운로드 함수
def download_audio(url, save_path, progress_callback=None):  # ✅ 진행률 콜백 추가
    # ✅ 다운로드 중일 때 진행률을 콜백으로 전달
    def hook(d):
        if d['status'] == 'downloading' and progress_callback:
            percent = d.get('_percent_str', '0.0%').strip()
            clean_percent = strip_ansi(percent)
            progress_callback(f"🎵 오디오 다운로드 중... {clean_percent}")

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',  # m4a 확장자의 최고 음질 오디오 선택
        'outtmpl': os.path.join(save_path, '%(title)s_audio.%(ext)s'),  # 저장 경로 및 파일명 지정
        'noplaylist': True,     # 재생목록 방지
        'overwrites': True,     # 파일 덮어쓰기
        'progress_hooks': [hook],  # ✅ 진행률 hook 등록
        'quiet': True
    }

    # yt_dlp 객체 생성 후 다운로드 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # 리스트로 감싸서 전달
