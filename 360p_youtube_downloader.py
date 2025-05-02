# 유튜브 영상(mp4, 오디오 포함)을 ffmpeg 없이 다운로드하는 프로그램

import yt_dlp  # yt-dlp 라이브러리 import (유튜브 영상 다운로드용)

# 사용자로부터 유튜브 영상 링크를 입력받음
url = input("유튜브 영상 주소를 입력하세요: ")

# yt-dlp 다운로드 옵션 설정 (딕셔너리 형태)
ydl_opts = {
    # mp4 형식 중 오디오와 비디오가 모두 포함된 stream만 선택 (progressive stream)
    'format': 'mp4[acodec!=none][vcodec!=none]',

    # 저장될 파일 이름을 유튜브 영상 제목으로 지정
    'outtmpl': '%(title)s.%(ext)s',

    # 출력 파일 형식을 mp4로 지정 (병합 시 필요하지만 progressive stream은 병합 불필요)
    'merge_output_format': 'mp4',

    # 후처리(postprocessing) 없음 → ffmpeg 없이도 실행 가능하게 설정
    'postprocessors': []
}

# yt-dlp 다운로드 실행
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # 입력받은 URL의 유튜브 영상을 다운로드
    ydl.download([url])

