# 基于物品的协同过滤算法

## 1. 数据

使用movielens-100k数据集中的u1.base文件作为实验集

## 2.实验

### 1）demo1

在demo1中建立用户-评分矩阵和用户看过的电影id列表，根据用户看过的电影计算电影间相似度，根据项亮的《推荐系统实践》中方法计算用户相似度。

item_sim.csv：

![1](https://github.com/JiaoZixun/Recommend_Item_Base/blob/master/img/1.jpg)

### 2）demo2

在demo2中利用电影间的相似度，计算用户u对电影i的感兴趣值。

根据用户u看过的电影列表，找到看过电影的K个最近邻，计算用户u对这K个最近邻的感兴趣值，最后根据感兴趣值排序得到推荐列表。

用户1的推荐列表（第一列为电影id，第二列为感兴趣值）：

![2](https://github.com/JiaoZixun/Recommend_Item_Base/blob/master/img/2.jpg)
