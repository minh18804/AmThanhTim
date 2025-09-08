import os
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
# Đường dẫn đến file txt chứa dữ liệu thô
#parent_cwd = os.path.join(cwd, os.pardir)
file_path = os.path.join(cwd, "data", "pcg", "c32.csv")

with open(file_path, "r") as r:
    print(r.read())

print(file_path)