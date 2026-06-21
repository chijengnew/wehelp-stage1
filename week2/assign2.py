# （註解語法）
# 字串："morning"
# print("morning")
# 布林值：True, False
# 有順序且可動的列表： [good, better, best]
# 有順序但不可動的列表： (good better, best)
# 集合： {1, 2, 3}
# 字典： {"apple":"蘋果", "data":"資料"}
# 變數：name = "Python"
# name = "Python"
# print(name)
# /n 換行
# 字串內 index 從 0 開始
# 交集：取兩個集合中，相同的資料。
# s1 = {0, 1, 2}
# s2 = {1, 2, 3}
# s3 = s1 & s2
# print(s3)
# 聯集：取兩個集合中的所有資料，但不重複。
# s3 = s1 | s2
# print(s3)
# 差集：從 s1 中，減去和 s2 重複的部分。
# s3 = s1 - s2
# print(s3)
# s3 = s2 - s1
# print(s3)
# 反交集：取兩個集合中，不重疊的部分。
# s3 = s1 ^ s2
# print(s3)
# 字典：{"apple":"蘋果", "data":"資料"} = key-value.
# dictionary = {"apple":"蘋果", "data":"資料"}
# print(dictionary ["apple"])
# del dictionary["apple"] # 刪除 key-value.
# print(dictionary)
# dictionary = {apple:apple*2 for apple in [3, 4, 5]}
# print(dictionary)
# 判斷式
# x=input("請輸入數字：") # 取得字串型態的使用者輸入
# x=int(x) # 將字串型態轉換成數字型態
# if x>200:
    # print("good morning")
# elif x>100:
    # print("good afternoon")
# else:
    # print("good evening")
# 四則運算
# n1 = int(input("請輸入數字一："))
# n2 = int(input("請輸入數字二："))
# apple = input("請輸入運算：+, -, *, /：")
# if apple =="+":
    # print(n1+n2)
# elif apple=="-":
    # print(n1-n2)
# elif apple=="*":
    # print(n1*n2)
# elif apple=="/":
    # print(n1/n2)
# else:
# print("error")
# while 迴圈
# apple = 1
# while apple<=10:
    # print("變數 Apple 的資料是：", apple)
    # apple=apple+1
# for in 迴圈
# for 變數名稱 in 列表或字串：
# for apple in [0, 1, 2]:
    # print(apple)
# for apple in range(1, 11):
    # print(apple)
# 迴圈 & 數字型態使用法輸入
# apple=input("請輸入：")
# apple=int(apple)
# for apple in range(apple):
    # print(apple)
# 函式基礎
# def 函式名稱(參數名稱)
# 函式內部的程式碼
# def apple():
    # print("Hello Apple")
# apple()
# def apple(elephant):
    # print(elephant)
# apple("大象")
# def apple(elephant):
    # print(elephant)
    # return "good morning"
# value=apple("Keanu Reeves")
# print(value)
# def add(dogs, cats):
    # result=dogs+cats
    # return result
# mouse=add(5,10)
# print(mouse)
# def add(dogs, cats):
    # print(dogs*cats)
# chicken=add(5,10)
# print(monkey)
# 函式名稱 (參數名稱=預設資料)：
# 函式內部的程式碼。
# def apple(hello="goodbye"):
    # print(hello)
# apple()
# apple()
# 名稱對應
# def apple(morning, evening):
    # result=morning/evening
    # print(result)
# apple(evening=5,morning=10)
# 無限參數
# def apple (*morning):
    # for evening in morning:
        # print (evening)
# apple(2, 4, 6, 8, 10)
# --- 函式、參數與變數皆獨立運作 ---
# def apple(*morning):
    # afternoon=0
    # for evening in morning:
        # afternoon=afternoon+evening
        # print(afternoon/len(morning))
# apple(2, 4, 6, 8, 10)

def func1(name):
    characters = {
        "悟空": {"x": 0, "y": 0, "side": 0},
        "辛巴": {"x": -3, "y": 3, "side": 0},
        "丁滿": {"x": -1, "y": 4, "side": 1},
        "貝吉塔": {"x": -4, "y": -1, "side": 0},
        "特南克斯": {"x": 1, "y": -2, "side": 0},
        "弗利沙": {"x": 4, "y": -1, "side": 1}
        }
    
    target = characters[name]
    distances = {}
    
    for char_name in characters:
        if char_name == name:
            continue    
        char_data = characters[char_name]
        dist_x = abs(target["x"] - char_data["x"])
        dist_y = abs(target["y"] - char_data["y"])
        total_dist = dist_x + dist_y
        
        if target["side"] != char_data["side"]:
            total_dist = total_dist + 2    
        distances[char_name] = total_dist

    max_dist = max(distances.values())
    min_dist = min(distances.values())

    farthest = []
    closest = []

    for char_name in distances:
        if distances[char_name] == max_dist:
            farthest.append(char_name)
        if distances[char_name] == min_dist:
            closest.append(char_name)

    print("最遠" + "、".join(farthest) + "；最近" + "、".join(closest))

func1("辛巴") # print 最遠弗利沙；最近丁滿、貝吉塔
func1("悟空") # print 遠丁滿、弗利沙；最近特南克斯
func1("弗利沙") # print 最遠辛巴；最近特南克斯
func1("特南克斯") # print 最遠丁滿；最近悟空

record = []

def func2(ss, start, end, criteria):
    op = ""
    if ">=" in criteria:
        op = ">="
    elif "<=" in criteria:
        op = "<="
    elif "=" in criteria:
        op = "="

    parts = criteria.split(op)
    field = parts[0]
    value = parts[1]

    if op != "=":
        value = float(value)

    best = {}

    for s in ss:
        name = s["name"]
        
        conflict = False
        for r in record:
            if r[0] == name:
                if start < r[2]:
                    if end > r[1]:
                        conflict = True
        
        if conflict == False:
            val = s[field]
            match = False

            if op == ">=":
                if val >= value:
                    match = True
            elif op == "<=":
                if val <= value:
                    match = True
            elif op == "=":
                if str(val) == str(value):
                    match = True

            if match == True:
                if best == {}:
                    best = s
                else:
                    if op == ">=":
                        if val < best[field]:
                            best = s
                    elif op == "<=":
                        if val > best[field]:
                            best = s

    if best != {}:
        record.append([best["name"], start, end])
        print(best["name"])
    else:
        print("Sorry")

services=[
    {"name":"S1", "r":4.5, "c":1000},
    {"name":"S2", "r":3, "c":1200},
    {"name":"S3", "r":3.8, "c":800}
    ]

func2(services, 15, 17, "c>=800") # S3
func2(services, 11, 13, "r<=4") # S3
func2(services, 10, 12, "name=S3") # Sorry
func2(services, 15, 18, "r>=4.5") # S1
func2(services, 16, 18, "r>=4") # Sorry
func2(services, 13, 17, "name=S1") # Sorry
func2(services, 8, 9, "c<=1500") # S2

def func3(index):
    value = 25
    step = 0
    
    for i in range(index):
        if step == 0:
            value = value - 2
        elif step == 1:
            value = value - 3
        elif step == 2:
            value = value + 1
        elif step == 3:
            value = value + 2
            
        step = step + 1
        if step == 4:
            step = 0
            
    print(value)

func3(1) # print 23
func3(5) # print 21
func3(10) # print 16
func3(30) # print 6

def func4(sp, stat, n):
    best_index = -1
    min_leftover = 9999
    
    for i in range(len(sp)):
        if stat[i] == "0":
            if sp[i] >= n:
                leftover = sp[i] - n
                if leftover < min_leftover:
                    min_leftover = leftover
                    best_index = i
                    
    if best_index == -1:
        max_space = -1
        for i in range(len(sp)):
            if stat[i] == "0":
                if sp[i] > max_space:
                    max_space = sp[i]
                    best_index = i
                    
    print(best_index)

func4([3, 1, 5, 4, 3, 2], "101000", 2) # print 5
func4([1, 0, 5, 1, 3], "10100", 4) # print 4
func4([4, 6, 5, 8], "1000", 4) # print 2