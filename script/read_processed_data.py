import pandas as pd
import mysql.connector
from mysql.connector import Error

# 读取CSV文件
csv_file = "../data/rumor_truth_processed.csv"
df = pd.read_csv(csv_file)

# 连接到MySQL数据库
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abc123",
            database="antirumor"
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# 插入谣言数据到数据库
def insert_rumor_data(connection, rumor, truth, published_date, origin, url):
    cursor = connection.cursor()
    insert_rumor_query = """
    INSERT INTO rumor (rumor, truth, published_date, origin, url) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_rumor_query, (rumor, truth, published_date, origin, url))
    connection.commit()
    return cursor.lastrowid

# 插入标签数据到数据库，如果标签已存在则返回标签id
def insert_tag_data(connection, tag_name):
    cursor = connection.cursor()
    # 检查标签是否已存在
    cursor.execute("SELECT id FROM tag WHERE name = %s", (tag_name,))
    tag = cursor.fetchone()
    if tag is None:
        insert_tag_query = "INSERT INTO tag (name) VALUES (%s)"
        cursor.execute(insert_tag_query, (tag_name,))
        connection.commit()
        return cursor.lastrowid
    return tag[0]

# 插入谣言和标签的关联数据
def insert_rumor_tag_data(connection, rumor_id, tag_id):
    cursor = connection.cursor()
    insert_rumor_tag_query = "INSERT INTO rumor_tag (rumor_id, tag_id) VALUES (%s, %s)"
    cursor.execute(insert_rumor_tag_query, (rumor_id, tag_id))
    connection.commit()

# 处理CSV文件中的数据
def process_csv_data(df, connection):
    for _, row in df.iterrows():
        # 插入rumor表数据
        rumor_id = insert_rumor_data(
            connection,
            row['rumor'],
            row['truth'],
            row['published_date'],
            row['origin'],
            row['url']
        )
        
        # 处理rumor_province中的多个省份
        if row['rumor_province'] != "无":
            provinces = row['rumor_province'].split(',')
            for province in provinces:
                province_tag_id = insert_tag_data(connection, province.strip())
                insert_rumor_tag_data(connection, rumor_id, province_tag_id)

        # 处理category字段
        category_tag_id = insert_tag_data(connection, row['category'])
        insert_rumor_tag_data(connection, rumor_id, category_tag_id)

# 主函数
def main():
    connection = create_connection()
    if connection:
        process_csv_data(df, connection)
        connection.close()

if __name__ == "__main__":
    main()
