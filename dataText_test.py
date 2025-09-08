import os
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
file_path = os.path.join(cwd, "data", "pcg", "c32.csv")

# Bước 1: Đọc dữ liệu từ file
with open(file_path, "r") as file:
    raw_data = file.read()

# Bước 2: Xử lý dữ liệu thô thành danh sách số nguyên
# Loại bỏ ký tự xuống dòng và khoảng trắng, sau đó chuyển thành số nguyên
data = [int(value) for value in raw_data.strip().split()]

# Bước 3: Vẽ tín hiệu âm thanh
plt.figure(figsize=(12, 6))
plt.plot(data, label="Audio Signal")
plt.title("Raw Audio Signal from INMP441")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()  
