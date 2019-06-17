import pandas as pd
import numpy as np
import jieba
import collections
import json




'''
list1=['1','1','2','2','3','3','3']
list2=['a1','a2','b1','b2','c1','c2','c3']
df=pd.DataFrame({'col1':list1,'col2':list2})

unq_list=['1','2','3']
results=[]
dic = {}

for i in unq_list:
    str = ''
    for mun,value in enumerate(df['col1']):
        if value == i:
            str += df['col2'][mun]

    results.append(str)
print(results)
'''

'''
pd.set_option('display.max_columns', None)

path = '../data/分轨文本_未合并str.xlsx'
data_one = pd.DataFrame(pd.read_excel(path , sheet_name=0))
data_two = data_one[['RECORD_ID' , 'SENTENCE']]
data_two['increase_index'] = pd.Series(np.arange(len(data_two['RECORD_ID'])))

dic1 = data_two.set_index('increase_index').T.to_dict('list')
print(dic1)
lis2 = []
for k , line in dict(dic1).items():
    dic2 = {line[0]:line[1]}
    lis2.append(dic2)
print(lis2)

dic3 = {}
for line in lis2:
    for k , content in dict(line).items():
        dic3.setdefault(k , []).append(content)
print(dic3)

dic4 = {}
for k , word in dic3.items():
    str1 = ''
    for content in word:
        str1 += str(content)
        dic4[k] = str1 + '\n'
print(dic4)

dic5 = pd.Series([v for k , v in dic4.items()])
print(dic5)

'''

'''
path = '../data/分轨文本_未合并str.xlsx'
data_one = pd.DataFrame(pd.read_excel(path , sheet_name=0))
data_two = data_one[['RECORD_ID' , 'SENTENCE']]

lis1 = list(data_two['RECORD_ID'].drop_duplicates())
lis2 = list(data_two['RECORD_ID'])
lis3 = list(data_two['SENTENCE'])
# print(lis3)
# def aa(content):
lis4 = []
for k in lis1:
    str1 = ''
    # dic4 = {}
    for i , v in enumerate(lis2):
        if v == k:
            str1 += str(lis3[i])
    # dic4[i] = str1 + '\n'
    lis4.append(str1)
print(lis4)
# for i in lis4:

'''

path = '../data/demo.txt'
path4 = '../data/hlt_stop_words.txt'
# 读取 新词发现 的 词表汇总
with open('wordlist1.txt' , 'r' ,encoding='utf-8') as file:
    n_gram_fenci = file.readlines()
with open(path4 , 'r' , encoding='utf-8') as file:
    stop_word = []
    for str in file:
        stop_word.append(str.replace('\n' , '').strip())

path2 = 'new 2.txt'
# 读取 坐席对话文本
with open(path2 , 'r' , encoding='utf-8') as file:
    str1 = ''
    for word in file:
        str1 += word.replace('/  ' , '').strip() + '\n'

# 分词
lis = ['清账' , '立刻','处理','到期','下午一点' , '11点' , '下午三点','尾号' , '金额','查账' , '罚息' , '切身利益' , '责任' , '困难' , '维护' , '财务']
for i in lis:
    jieba.add_word(i)
content = ' '.join(jieba.cut(str1))
content = content.strip().split(' ')
word_list = [word for word in content if word not in stop_word]
str2 = ''
for word in word_list:
    str2 += word + ' '
    str3 = str2.split('\n')
for i in str3:

# # 词频统计
lis_frequency = []
lis_frequency.extend(collections.Counter(word_list).most_common(len(word_list) - 1))
print(lis_frequency)
# jieba_dic = [{word[0]:word[1]} for word in lis_frequency]  # 词频字典列表
# jieba_word = [word[0] for word in lis_frequency]           # 词列表
#
# with open('jieba_dic.txt' , 'w' , encoding='utf-8') as writer:
#     for dic1 in jieba_dic:
#         writer.write(json.dumps(dic1 , ensure_ascii=False))
#         writer.write('\n')
# with open('jieba_word.txt' , 'w' , encoding='utf-8') as writer:
#     for dic1 in jieba_word:
#         writer.write(json.dumps(dic1 , ensure_ascii=False))
#         writer.write('\n')

# # create停用词表  1.挑选出use_word
# use_word = [word for content in n_gram_fenci for word in jieba_word if word in content]
# use_word1 = []
# use_word1.extend(collections.Counter(use_word).most_common(len(use_word) - 1))
# with open('use_word.txt' , 'w' , encoding='utf-8') as writer:
#     for word in use_word1:
#         if word[0] != '\n':
#             writer.write(str(word[0]).strip())
#             writer.write('\n')
# # 2.得到stop_word：jieba分词总词表 - use_word
# use_word2 = [word[0] for word in use_word1]
# stop_word = [word for word in jieba_word if str(word).replace('"' , '').replace('"' , '') not in use_word2]
# stop_word_one = [word for word in jieba_word if len(word) < 2]
# stop_word_one1 = [word for content in n_gram_fenci for word in stop_word_one if word in content]
# with open('stop_word1.txt' , 'w' , encoding='utf-8') as writer:
#     for word in stop_word_one:
#         if word != '\n':
#             writer.write(str(word).strip())
#             writer.write('\n')



