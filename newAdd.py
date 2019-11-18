import os
import random
import time
#######分割总txt，每230个为一个txt
LiMit = 6800
file_count = 0
url_list = []

path = 'qqnumber'
if not os.path.exists(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
with open("/Users/apple/Desktop/文件/iphone/6000.txt") as f:  ##总txt路径 开始分割
    for line in f:
        url_list.append(line)
        if len(url_list) < LiMit:
            continue
        file_name = str(file_count) + ".txt"
        file_home = path + '/' + file_name
        with open(file_home, 'w')as file:
            for url in url_list[:-1]:
                file.write(url)
            file.write(url_list[-1].strip())
            url_list = []
            file_count += 1
if url_list:
    file_name = str(file_count) + ".txt"
    with open(file_name, 'w') as file:
        for url in url_list:
            file.write(url)
print("done")


## 向所有txt中，添加.vcf内容，并把后缀名改为.vcf
###生成随机数
def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(H)
    return salt


number = 1
DIR = '/Users/apple/Desktop/TestUtil/Pythonproject/qqnumber'
geshu = int(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
print(">>>>>>>>>>>>>>>>>>>>>>>>" + str(geshu))
f = ''
jishu = 0
for i in range(geshu):
    one = 0
    tow = 12
    f = open('/Users/apple/Desktop/TestUtil/Pythonproject/qqnumber/' + str(jishu) + '.txt', 'r+')

    jishu = + 1
    print('处理txt文件：' + '/Users/apple/Desktop/TestUtil/Pythonproject/qqnumber/' + str(jishu) + '.txt')
    mingming = ranstr(5)

    f2 = open('/Users/apple/Desktop/文件/shuchu/allvcf/' + mingming + '.txt', 'w')
    print('准备生成：' + '/Users/apple/Desktop/文件/shuchu/allvcf/' + mingming + '.txt')
    data = f.read()
    chang = len(data) / 12
    zhuan = int(chang) + 1
    print(zhuan)
    for i in range(zhuan):
        print('第' + str(i))
        ## 通过下标来获取txt中的每行号码
        Phonen = data[one:tow]
        ##添加vcf格式的内容，形成通讯录文件----------
        f2.write('BEGIN:VCARD\n')
        number = time.time()
        number = str(number)[11:] + '000000'
        number = number[:6]
        print(number)
        f2.write('FN:' +number  + '\n')

        print(Phonen)
        content = 'TEL;type=CELL;type=VOICE;type=pref:' + Phonen
        f2.write(content)
        print(content)
        f2.write('VERSION:3.0\n')
        f2.write('END:VCARD\n')
        one = one + 12
        tow = tow + 12
    f2.flush()
    f.close()
    f2.close()
    # 运行一次试试看看结果

####将以上代码生成的txt文本后缀名改为.vcf格式
files = os.listdir("/Users/apple/Desktop/文件/shuchu/allvcf/")
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == ".txt":
        newname = portion[0] + ".vcf"
        os.chdir("/Users/apple/Desktop/文件/shuchu/allvcf/")
        os.rename(filename, newname)
