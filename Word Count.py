import re

pattern = r'\b[a-zA-Z]+\b'
with open("1.txt", "r") as file:  # 打开文件
    data_1 = file.read()  # 读取文件
    res = re.findall(pattern,data_1)

#print(res)
dict_1 = {}
for key in res:
    dict_1[key] = dict_1.get(key, 0) + 1
#print (dict)


c = sorted(dict_1,key = lambda x:dict_1[x])
abc = []
#for key in c[-100:]:
for key in c:
    abc.append ([key,':',dict_1[key]])

print (abc)
with open("tags.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件

list2 = data.split(',')

print(type(list2))

dict = {}
for key in list2:
    dict[key] = dict.get(key, 0) + 1
#print (dict)


b = sorted(dict,key = lambda x:dict[x])
for key in b:
    print (key,':',dict[key])
