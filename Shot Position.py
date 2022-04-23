import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
raw_data = pd.read_csv('data.csv')

# 製作圖表：進攻位置分析
data_x = raw_data[raw_data['shot_made_flag'] == 1.0]['loc_x']
data_y = raw_data[raw_data['shot_made_flag'] == 1.0]['loc_y']

# 圖表設定
fig1, ax1 = plt.subplots()
ax1.scatter(data_x, data_y, c = "red", alpha = 0.08)
ax1.set_title("Shot Made Position", size = 20)
fig1.set_size_inches(8, 8)

# 輸出圖表
plt.show()