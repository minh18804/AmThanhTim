import pandas as pd
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
file_path = os.path.join(cwd, "data", "pcg", "c32.csv")

data_fame = pd.read_csv(file_path)
x = range(len(data_fame))
plt.plot(x, data_fame, marker="x", linestyle='-')

plt.xlabel('Chỉ số dòng')
plt.ylabel('Biên độ')
plt.title('Biểu đồ dữ liệu từ file CSV')

plt.show()  