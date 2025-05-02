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
    url = entry.get()
    path = folder_path.get()
    quality = selected_quality.get()  # 🔹 선택된 화질을 가져옴

    if not path:
        status_label.config(text="❗ 저장 폴더를 먼저 선택하세요.")
        return

    status_label.config(text="🎥 다운로드 중...")
    root.update()

    try:
        download_video(url, path, quality)  # 🔹 선택한 화질 전달
        download_audio(url, path)
        status_label.config(text="✅ 다운로드 완료!")
    except Exception as e:
        status_label.config(text=f"❌ 오류 발생: {e}")

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

# 🔽 화질 선택 드롭다운 구성 (버튼 위에 추가)
quality_options = ["1080p", "720p", "480p", "360p"]
selected_quality = tk.StringVar(value=quality_options[0])  # 기본 선택값은 1080p

quality_label = tk.Label(root, text="화질 선택:")
quality_label.pack()

quality_menu = tk.OptionMenu(root, selected_quality, *quality_options)
quality_menu.pack()

# 다운로드 시작 버튼
btn = tk.Button(root, text="⬇️ 다운로드 시작", command=start_download)
btn.pack(pady=10)

# 상태 메시지를 표시할 라벨
status_label = tk.Label(root, text="")
status_label.pack()

# GUI 이벤트 루프 시작
root.mainloop()
