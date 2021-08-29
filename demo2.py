import pandas as pd
import numpy as np
import xlwt

def Create_User_items(user_rating):
    user_item=[]
    for user in range(1,944):
        items=[]
        for item in  range(1,1683):
            if user_rating[user][item] != 0:
                items.append(item)
        user_item.append(items)
    #print(user_item)
    return user_item
#计算电影u相关的所有电影
def Count_User_Interest(Sim_W,K,user_item,user_rating):
    userid = 0
    Recommend = {}
    for items in user_item:
        userid += 1
        cur_recommend = []
        for item in items:
            cur = []
            cur_rating=user_rating[userid][item]
            cur_item_sim = Sim_W[item]
            for it1 in range(1,1683):
                if cur_item_sim[it1] != 0:
                    cur.append([it1,cur_item_sim[it1]])
            cur.sort(key=(lambda x:x[1]), reverse=True)
            cur_sort=cur[0:K]
            for item2 in cur_sort:
                if item2 in items:
                    continue
                item2[1]*=cur_rating
                #去重
                flag = 0
                for cur_re in cur_recommend:
                    if item2[0] == cur_re[0]:
                        flag = 1
                        if item2[1]>cur_re[1]:
                            cur_re[1] = item2[1]
                if flag == 0:
                    cur_recommend.append(item2)
        for cur_item in cur_recommend:#将每一个二元组放入推荐字典中
            Recommend.setdefault(userid,[]).append(cur_item)

    #输出
    for userid in range(1,944):
        outfile = "F:\\协同过滤推荐算法\\基于物品\\推荐结果集合\\Recommend{}.csv".format(userid)
        Recommend[userid].sort(key=(lambda x:x[1]), reverse=True)
        data = pd.DataFrame(Recommend[userid])
        data.to_csv(outfile, index=False, header=False)
        print(Recommend[userid],len(Recommend[userid]))
    return Recommend

file1="F:\\协同过滤推荐算法\\基于物品\\user_rating.csv"
data1=pd.read_csv(file1, header=None)#header取消列名
user_rating=np.array(data1)
#print(user_rating)

file2="F:\\协同过滤推荐算法\\基于物品\\item_sim.csv"
data1=pd.read_csv(file2,header=None)
item_sim=np.array(data1)

#得到用户喜欢物品的列表
user_item = Create_User_items(user_rating)

#得到推荐列表
Count_User_Interest(item_sim,30,user_item,user_rating)
