import pandas as pd
from openai import OpenAI


def classify(row, output_file):
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    text = row['truth']
    content = f"请将文本分为以下几类中的一类：时事政治、党史国史、食药卫生、公共政策、公共安全、突发事件、科学常识、社会热点、其它。" \
              f"要求只输出分类结果即可，不要输出原因、解释等其它无关信息，注意输出结果只能是以上几个类别名词，不要包含其他词语: \n{text} "
    chat_completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
    )
    category = chat_completion.choices[0].message.content
    # 将结果写入到文件中
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(f"{row['truth']},{category}\n")
    return category


# 读取CSV文件
df = pd.read_csv('rumor_truth.csv')

# 定义输出文件名，并写入CSV文件的表头
output_file = 'truth_category.csv'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("truth,category\n")

# 指定从哪一行开始（以0为基准）
start_row = 0

# 过滤数据框，从指定行开始进行摘要生成
df[start_row:].apply(classify, axis=1, output_file=output_file)
