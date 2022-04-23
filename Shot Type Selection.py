import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
raw_data = pd.read_csv('data.csv')

# 檢視是否成功得分的缺失值
# print(raw_data[raw_data['shot_made_flag'].isnull()])

# 檢視得分方式
shot_type = set(raw_data['combined_shot_type'])

# 計算得分方式之得分和失分次數
def counter(data):
    ball_in = len(data[data['shot_made_flag'] == 1.0])
    ball_out = len(data[data['shot_made_flag'] == 0.0])
    return ball_in, ball_out

# 建立新資料表
type1_in, type1_out = counter(raw_data[raw_data['combined_shot_type'] == 'Bank Shot'])
type2_in, type2_out = counter(raw_data[raw_data['combined_shot_type'] == 'Dunk'])
type3_in, type3_out = counter(raw_data[raw_data['combined_shot_type'] == 'Hook Shot'])
type4_in, type4_out = counter(raw_data[raw_data['combined_shot_type'] == 'Jump Shot'])
type5_in, type5_out = counter(raw_data[raw_data['combined_shot_type'] == 'Layup'])
type6_in, type6_out = counter(raw_data[raw_data['combined_shot_type'] == 'Tip Shot'])

datas = [[type1_in, type1_out],
        [type2_in, type2_out],
        [type3_in, type3_out],
        [type4_in, type4_out],
        [type5_in, type5_out],
        [type6_in, type6_out]]
shot_info = pd.DataFrame(data = datas, columns = ['Ball In', 'Ball Out'], index = ['Bank Shot', 'Dunk', 'Hook Shot', 'Jump Shot', 'Layup', 'Tip Shot'])

# 新增進球機率之欄位
shot_info['FG%'] = shot_info['Ball In'] / (shot_info['Ball In'] + shot_info['Ball Out']) * 100

# 製作圖表：進攻方式命中率
data = shot_info['FG%']
labels = list(shot_type)

# 圖表設定
fig1, ax1 = plt.subplots()
ax1.bar(labels, data, width = 0.3, color = 'navy')
ax1.set_title("Shot Type FG%", size = 20)
fig1.set_size_inches(12, 8)

# 輸出圖表
plt.show()