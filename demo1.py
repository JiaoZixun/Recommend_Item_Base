import pandas as pd
import numpy as np
import math


#建立用户-评分矩阵
user_rating = np.zeros((944, 1683))#数据集共943个用户，1682部电影，0行0列不用
#print(user_rating)
def Create_User_rating_Table(data):
    for it in data:
        user_rating[it[0]][it[1]]=it[2]
    print(user_rating)
    #outfile = "F:\\协同过滤推荐算法\\基于物品\\user_rating.csv"
    #data1=pd.DataFrame(user_rating)
    #print(data1.shape)
    #data1.to_csv(outfile, index=False, header=False)

def Create_User_items(user_rating):
    user_item=[]
    for user in range(1,944):
        items=[]
        for item in  range(1,1683):
            if user_rating[user][item] != 0:
                items.append(item)
        user_item.append(items)
    print(user_item)
    outfile = "F:\\协同过滤推荐算法\\基于物品\\user_item.csv"
    data = pd.DataFrame(user_item)
    data.to_csv(outfile, index=False, header=False)
    return user_item

def Create_Item_Sim(user_item):
    Item_Sim = np.zeros((1683, 1683))  # 数据集共1682部电影，0行0列不用
    N=np.zeros(1683)
    for items in user_item:
        for it1 in items:
            N[it1] += 1
            for it2 in items:
                if it1 == it2:
                    continue
                Item_Sim[it1][it2] += 1
                Item_Sim[it2][it1] += 1
    print(Item_Sim)
    W = np.zeros((1683, 1683))
    for it1 in range(1,1683):
        for it2 in range(1,1683):
            if it1 == it2 :
                continue
            if math.sqrt(N[it1]*N[it2]) == 0:
                W[it1][it2] = 0.0
                continue
            W[it1][it2]=Item_Sim[it1][it2]/math.sqrt(N[it1]*N[it2])
    print(W)
    return W
file="F:\\协同过滤推荐算法\\ml-100k\\u1.base"
lieming=["用户id", "电影id", "评分", "时间"]
data = pd.read_table(file, names=lieming)
#print(data)
list_data = np.array(data)#转换数组
#print(list_data)
data=list_data.tolist()#转换list
#创建用户评分矩阵
Create_User_rating_Table(data)
#创建用户看过的电影id的列表
user_items=Create_User_items(user_rating)
#根据用户看过的电影id计算电影间的相似度
Item_sim = Create_Item_Sim(user_items)
#输出
outfile = "F:\\协同过滤推荐算法\\基于物品\\item_sim.csv"
data1 = pd.DataFrame(Item_sim)
data1.to_csv(outfile, index=False, header=False)