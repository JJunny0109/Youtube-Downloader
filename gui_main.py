# gui_main.py
import tkinter as tk
from downloader import download_video, download_audio  # downloader.py에서 함수 불러옴

def start_download():
    url = entry.get()
    status_label.config(text="🎥 영상 다운로드 중...")
    root.update()

    try:
        download_video(url)
        download_audio(url)
        status_label.config(text="✅ 다운로드 완료!")
    except Exception as e:
        status_label.config(text=f"❌ 오류 발생: {e}")

# GUI 창 설정
root = tk.Tk()
root.title("유튜브 다운로더")
root.geometry("400x200")

label = tk.Label(root, text="유튜브 링크를 입력하세요:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn = tk.Button(root, text="다운로드 시작", command=start_download)
btn.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
