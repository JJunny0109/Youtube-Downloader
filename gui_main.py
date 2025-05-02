import tkinter as tk
from tkinter import filedialog
import threading  # ❗ 다운로드 중 응답 없음 방지를 위한 쓰레딩
from downloader import get_available_resolutions, download_video, download_audio
from merger import merge_video_audio  # ✅ 병합 모듈 추가 import

# ✅ 진행률 텍스트를 상태 라벨에 실시간 표시하는 함수
def update_status_text(text):
    status_label.config(text=text)
    root.update_idletasks()

# 폴더 선택 함수
def choose_folder():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        folder_path.set(selected_folder)
        status_label.config(text=f"📁 저장 폴더: {selected_folder}")

# 화질 목록 불러오기 함수
def fetch_qualities():
    url = entry.get()
    try:
        res_list = get_available_resolutions(url)
        if not res_list:
            status_label.config(text="❗ 화질을 불러올 수 없습니다.")
            return

        quality_menu['menu'].delete(0, 'end')
        for res in res_list:
            quality_menu['menu'].add_command(label=res, command=tk._setit(selected_quality, res))
        selected_quality.set(res_list[0])
        status_label.config(text="✅ 화질 목록 불러오기 완료!")
    except Exception as e:
        status_label.config(text=f"❌ 분석 실패: {e}")

# ❗ 실제 다운로드 동작은 별도의 쓰레드에서 수행
def _do_download():
    url = entry.get()
    path = folder_path.get()
    quality = selected_quality.get()

    if not url:
        status_label.config(text="❗ URL을 입력하세요.")
        return
    if not path:
        status_label.config(text="❗ 저장 폴더를 선택하세요.")
        return
    if not quality:
        status_label.config(text="❗ 화질을 선택하세요.")
        return

    status_label.config(text="⬇️ 다운로드 중...")
    root.update()

    try:
        # ✅ 다운로드 수행
        download_video(url, path, quality, progress_callback=update_status_text)
        download_audio(url, path, progress_callback=update_status_text)

        # ✅ 병합 수행
        status_label.config(text="🔧 영상과 오디오 병합 중...")
        root.update()
        merge_video_audio(path)

        # ✅ 완료
        status_label.config(text="✅ 다운로드 및 병합 완료!")
    except Exception as e:
        status_label.config(text=f"❌ 오류 발생: {e}")

# 쓰레드로 다운로드 함수 실행
def start_download():
    threading.Thread(target=_do_download).start()

# 🔽 GUI 설정
root = tk.Tk()
root.title("유튜브 다운로더")
root.geometry("500x350")

folder_path = tk.StringVar()
selected_quality = tk.StringVar()

# 링크 입력
label = tk.Label(root, text="유튜브 링크를 입력하세요:")
label.pack(pady=5)

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

# 폴더 선택
folder_btn = tk.Button(root, text="📂 저장 폴더 선택", command=choose_folder)
folder_btn.pack(pady=5)

# 화질 불러오기
fetch_btn = tk.Button(root, text="🔍 화질 불러오기", command=fetch_qualities)
fetch_btn.pack(pady=5)

# 화질 드롭다운
quality_label = tk.Label(root, text="화질 선택:")
quality_label.pack(pady=2)

quality_menu = tk.OptionMenu(root, selected_quality, "")
quality_menu.pack(pady=2)

# 다운로드 버튼
btn = tk.Button(root, text="⬇️ 다운로드 시작", command=start_download)
btn.pack(pady=10)

# 상태 출력
status_label = tk.Label(root, text="", wraplength=450, justify="left")
status_label.pack()

# 메인 루프 시작
root.mainloop()
