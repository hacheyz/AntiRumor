import pandas as pd
import spacy

# 加载spaCy的中文预训练模型
nlp = spacy.load('zh_core_web_sm')

# 读取CSV文件
file_path = 'rumor_truth.csv'
df = pd.read_csv(file_path)

# 创建新的列来存储地名
df['rumor_place'] = ''

# 识别地名并填充到新的列中
for index, row in df.iterrows():
    doc = nlp(row['rumor'])
    places = [ent.text for ent in doc.ents if ent.label_ == 'GPE']  # GPE表示地名
    df.at[index, 'rumor_place'] = ', '.join(places) if places else '无'

# 保存结果到新的CSV文件
output_path = 'rumor_place.csv'
df.to_csv(output_path, index=False)
