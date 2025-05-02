import tkinter as tk
from tkinter import filedialog  # 폴더 선택 다이얼로그를 위한 모듈
from downloader import download_video, download_audio  # downloader.py에서 함수 불러오기

# 폴더 선택 함수
def choose_folder():
    selected_folder = filedialog.askdirectory()  # 사용자에게 폴더 선택 요청
    if selected_folder:
        folder_path.set(selected_folder)  # 선택한 경로를 변수에 저장
        status_label.config(text=f"📁 저장 폴더: {selected_folder}")  # 상태 표시 업데이트

# 다운로드 시작 함수
def start_download():
    url = entry.get()  # 입력창에서 URL 가져오기
    path = folder_path.get()  # 선택한 저장 경로 가져오기

    # 저장 경로가 비어 있으면 경고 메시지
    if not path:
        status_label.config(text="❗ 저장 폴더를 먼저 선택하세요.")
        return

    status_label.config(text="🎥 다운로드 중...")  # 상태 표시 업데이트
    root.update()  # GUI 업데이트

    try:
        # 영상과 오디오 다운로드 실행 (저장 경로 포함)
        download_video(url, path)
        download_audio(url, path)
        status_label.config(text="✅ 다운로드 완료!")  # 성공 메시지
    except Exception as e:
        status_label.config(text=f"❌ 오류 발생: {e}")  # 예외 발생 시 에러 메시지 출력

# 🔽 GUI 창 설정 시작 🔽

root = tk.Tk()  # tkinter 창 생성
root.title("유튜브 다운로더")  # 창 제목
root.geometry("450x250")  # 창 크기 설정

folder_path = tk.StringVar()  # 선택한 폴더 경로를 저장할 변수

# 링크 입력 안내 라벨
label = tk.Label(root, text="유튜브 링크를 입력하세요:")
label.pack(pady=5)

# 링크 입력창
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# 폴더 선택 버튼
folder_btn = tk.Button(root, text="📂 저장 폴더 선택", command=choose_folder)
folder_btn.pack(pady=5)

# 다운로드 시작 버튼
btn = tk.Button(root, text="⬇️ 다운로드 시작", command=start_download)
btn.pack(pady=10)

# 상태 메시지를 표시할 라벨
status_label = tk.Label(root, text="")
status_label.pack()

# GUI 이벤트 루프 시작
root.mainloop()
