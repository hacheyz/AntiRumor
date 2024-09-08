import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

# 加载CSV文件
file_path = 'province_category.csv'
df = pd.read_csv(file_path)

# 定义类别的顺序
category_order = ["时事政治", "党史国史", "食药卫生", "公共政策", "公共安全", "突发事件", "科学常识", "其它"]

# 创建数据透视表以汇总数据
pivot_table = df.pivot_table(index='rumor_province', columns='category', aggfunc='size', fill_value=0)

# 按照指定的类别顺序重新排列列的顺序
pivot_table = pivot_table[category_order]

# 设置matplotlib图形
plt.figure(figsize=(10, 8))

# 使用数据透视表数据绘制热图
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", cbar=True)

# 设置标签和标题
plt.xlabel('类别', fontsize=16)
plt.ylabel('省份', fontsize=16)
plt.title('省份 vs 类别', fontsize=16)

# 保存图表
plt.savefig('省份_类别.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()
