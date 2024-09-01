import pandas as pd
from openai import OpenAI


def summarize_text(row, output_file):
    client = OpenAI(
        api_key="your-api-key",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    text = row['truth']
    content = f"请对以下文本进行总结，注意总结的凝炼性，将总结字数控制在20个字以内:\n{text}"
    chat_completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
    )
    summarized_text = chat_completion.choices[0].message.content
    # 将结果写入到文件中
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(f"{row['truth']},{summarized_text}\n")
    return summarized_text


# 读取CSV文件
df = pd.read_csv('rumor_truth.csv')

# 定义输出文件名，并写入CSV文件的表头
output_file = 'truth_summary.csv'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("truth,summary\n")

# 指定从哪一行开始（以0为基准）
start_row = 0

# 过滤数据框，从指定行开始进行摘要生成
df[start_row:].apply(summarize_text, axis=1, output_file=output_file)
