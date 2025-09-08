import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Đọc tín hiệu đã lọc từ file CSV
cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
file_path = os.path.join(cwd, "data", "pcg", "c32.csv")

data = pd.read_csv(file_path, header=None)

# Lấy tín hiệu từ cột đầu tiên (giả sử dữ liệu là một cột)
signal = data[0].values

# Tính toán FFT của tín hiệu
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), d=1/4000)  # Giả sử sample rate là 4000Hz

# Lọc phần thực và phần ảo của FFT
fft_magnitude = np.abs(fft_signal)

# Vẽ đồ thị FFT
plt.plot(frequencies[:len(frequencies)//2], fft_magnitude[:len(frequencies)//2])  # Lấy nửa đầu của tần số
plt.title("FFT of Filtered Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Bien do")
plt.grid(True)
plt.show()
