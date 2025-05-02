# gui_main.py
import tkinter as tk
from tkinter import filedialog
from downloader import get_available_resolutions, download_video, download_audio  # downloader.py에서 함수 불러옴

# 폴더 선택 함수
def choose_folder():
    selected_folder = filedialog.askdirectory()  # 사용자에게 폴더 선택 요청
    if selected_folder:
        folder_path.set(selected_folder)  # 선택한 경로를 변수에 저장
        status_label.config(text=f"📁 저장 폴더: {selected_folder}")  # 상태 표시 업데이트

# 화질 목록 불러오기 함수
def fetch_qualities():
    url = entry.get()  # 입력창에서 URL 가져오기
    try:
        res_list = get_available_resolutions(url)  # 유튜브 영상에서 화질 목록 분석
        if not res_list:
            status_label.config(text="❗ 화질을 불러올 수 없습니다.")
            return

        # 기존 메뉴 초기화 후 새 화질 목록 추가
        quality_menu['menu'].delete(0, 'end')
        for res in res_list:
            quality_menu['menu'].add_command(label=res, command=tk._setit(selected_quality, res))
        selected_quality.set(res_list[0])  # 가장 높은 화질 선택
        status_label.config(text="✅ 화질 목록 불러오기 완료!")
    except Exception as e:
        status_label.config(text=f"❌ 분석 실패: {e}")

# 다운로드 시작 함수
def start_download():
    url = entry.get()  # 유튜브 URL
    path = folder_path.get()  # 저장 경로
    quality = selected_quality.get()  # 선택한 화질

    # 유효성 검사
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
        # 선택된 화질로 영상 다운로드
        download_video(url, path, quality)
        # 고정 화질로 오디오 다운로드
        download_audio(url, path)
        status_label.config(text="✅ 다운로드 완료!")
    except Exception as e:
        status_label.config(text=f"❌ 오류 발생: {e}")

# GUI 창 설정
root = tk.Tk()
root.title("유튜브 다운로더")
root.geometry("500x350")

folder_path = tk.StringVar()       # 저장 폴더 경로
selected_quality = tk.StringVar()  # 선택된 화질

# 링크 입력 안내 라벨
label = tk.Label(root, text="유튜브 링크를 입력하세요:")
label.pack(pady=5)

# 링크 입력창
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

# 폴더 선택 버튼
folder_btn = tk.Button(root, text="📂 저장 폴더 선택", command=choose_folder)
folder_btn.pack(pady=5)

# 화질 목록 불러오기 버튼
fetch_btn = tk.Button(root, text="🔍 화질 불러오기", command=fetch_qualities)
fetch_btn.pack(pady=5)

# 화질 선택 드롭다운 메뉴
quality_label = tk.Label(root, text="화질 선택:")
quality_label.pack(pady=2)

quality_menu = tk.OptionMenu(root, selected_quality, "")
quality_menu.pack(pady=2)

# 다운로드 시작 버튼
btn = tk.Button(root, text="⬇️ 다운로드 시작", command=start_download)
btn.pack(pady=10)

# 상태 메시지를 표시할 라벨
status_label = tk.Label(root, text="")
status_label.pack()

# GUI 이벤트 루프 시작
root.mainloop()
