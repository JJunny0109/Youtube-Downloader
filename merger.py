# merger.py
import subprocess
import os

# ✅ ffmpeg.exe가 현재 파이썬 파일과 같은 위치에 있을 때의 경로 지정
ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

# ✅ 영상과 오디오 파일을 병합하는 함수
def merge_video_audio(folder_path):
    """
    폴더 내에서 *_video.mp4 와 *_audio.m4a 를 찾아 병합하고
    최종 결과는 base_name.mp4 로 저장됩니다.
    원본 영상/오디오 파일은 병합 후 삭제됩니다.
    """
    files = os.listdir(folder_path)

    videos = [f for f in files if f.endswith("_video.mp4")]
    audios = [f for f in files if f.endswith("_audio.m4a")]

    for video_file in videos:
        base_name = video_file.replace("_video.mp4", "")
        audio_file = f"{base_name}_audio.m4a"
        output_file = f"{base_name}.mp4"  # ✅ "_merged" 없이 원래 이름으로 저장

        if audio_file in audios:
            video_path = os.path.join(folder_path, video_file)
            audio_path = os.path.join(folder_path, audio_file)
            output_path = os.path.join(folder_path, output_file)

            print(f"🎬 병합 중: {video_file} + {audio_file} → {output_file}")
            command = [
                ffmpeg_path, "-y",
                "-i", video_path,
                "-i", audio_path,
                "-c", "copy",
                output_path
            ]
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

            # ✅ 병합 후 원본 파일 삭제
            os.remove(video_path)
            os.remove(audio_path)
            print(f"🗑️ 원본 삭제: {video_file}, {audio_file}")

    print("✅ 모든 병합 완료")
