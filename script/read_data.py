import pandas as pd
import mysql.connector

# 读取CSV文件
csv_file = '../data/rumor_truth.csv'  # 替换为你的CSV文件路径
df = pd.read_csv(csv_file)

# 数据库连接信息
db_config = {
    'host': 'localhost',    # 数据库主机地址
    'user': 'root', # 替换为你的数据库用户名
    'password': 'abc123', # 替换为你的数据库密码
    'database': 'antirumor'   # 数据库名称
}

# 创建数据库连接
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 插入数据到rumor表
for _, row in df.iterrows():
    sql = """
    INSERT INTO rumor (rumor, truth, origin, published_date, url)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        row['rumor'],
        row['truth'],
        row['origin'],
        row['published_date'],
        row['url']
    ))

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()

print("数据导入成功！")