# run_denoise.py
from pyrnnoise import RNNoise

# 1. 샘플레이트(Hz)
SR = 48000

# 2. RNNoise 객체 생성
denoiser = RNNoise(sample_rate=SR)

# 3. 파일 경로
in_path  = "input.wav"
out_path = "output.wav"

# 4. 노이즈 제거 실행
#    process_wav()가 출력 파일을 쓰고, 발화 확률을 반환합니다.
for speech_prob in denoiser.process_wav(in_path, out_path):
    pass

print(f"✅ 노이즈 제거 완료: {out_path}")
