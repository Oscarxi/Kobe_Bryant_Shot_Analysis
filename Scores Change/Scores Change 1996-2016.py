import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
raw_data = pd.read_csv('Kobe Bryant Shot  Analysis/data.csv')

# 記錄分數類型
score_type = []
for i in raw_data['shot_type']:
    score_type.append(int(i.split('PT')[0]))

# 新增分數欄位
raw_data['scores'] = score_type * raw_data['shot_made_flag']

# 計算不同日期之總得分
scores_info = raw_data[['scores', 'season']]
scores_day = scores_info.groupby('season').sum().reset_index()

# 製作圖表：得分變化
data_time = scores_day['season']
data_change = scores_day['scores']

# 圖表設定
fix1, ax1 = plt.subplots()
ax1.plot(data_time, data_change, color = "navy")
ax1.set_title("Scores Change 1996-2016", size = 20)
fix1.set_size_inches(16,8)

# 輸出圖表
plt.show()