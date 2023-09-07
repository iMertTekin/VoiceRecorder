import time

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
freq = 44100
duration = 5
countdown_duration = 3

for geri_sayım in range(countdown_duration, 0, -1):
    print(f"{geri_sayım} saniye içinde kayıt başlayacak, hazır olun...")
    time.sleep(1)
print("Lütfen Konuşunuz")

recordin = sd.rec(int(duration * freq),
                  samplerate=freq, channels=2)
sd.wait()
write("recording0.wav", freq, recordin)
print("Ses kaydı tamamlandı")
