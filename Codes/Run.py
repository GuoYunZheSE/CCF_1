import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import xgboost as xgb
from sklearn.cross_validation import train_test_split

if __name__ == '__main__':
    traindata=pd.read_csv('G:\\CCF_1\\Result\\Middle_2017-11-10_22.55.52.csv', encoding='gbk')
    testdata=pd.read_csv('G:\\CCF_1\\Result\\Big.csv',encoding='gbk')
    traindata['add_date'] = pd.to_datetime(traindata['TrueDate'])
    train,val=train_test_split(traindata, test_size=0.2, random_state=1)
    Big_Features=[
        'BigCount',
        'custid',
        'BigID',
        'SourceDate'
    ]
    Middle_Features=[
        'MiddleCount',
        'custid',
        'MiddleID',
        'SourceDate'
    ]
    num_round=2000
    params = {
        'booster': 'gbtree',
        'objective': 'reg:linear',
        'gamma': 0.1,  # 用于控制是否后剪枝的参数,越大越保守，一般0.1、0.2这样子。
        'max_depth': 3,  # 构建树的深度，越大越容易过拟合
        'lambda': 2,  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
        # ，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
        # 这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting。
        'silent': 0,  # 设置成1则没有运行信息输出，最好是设置为0.
        'eta': 0.007,  # 如同学习率
    }
    plst = list(params.items())
    Big_test=xgb.DMatrix(testdata[Big_Features[2:3]])
    Big_train = xgb.DMatrix(train[Big_Features[1:]], label=train[Big_Features[0]])
    Big_val=xgb.DMatrix(val[Big_Features[1:]],label=val[Big_Features[0]])
    # 训练模型并保存
    # early_stopping_rounds 当设置的迭代次数较大时，early_stopping_rounds 可在一定的迭代次数内准确率没有提升就停止训练
    watchlist=[(Big_train,'Train'),(Big_val,'Validation')]
    Big_BST = xgb.train(plst, Big_train, num_round,watchlist,early_stopping_rounds=100)
    S_Name = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())
    Big_BST.save_model('G:\\CCF_1\\Model\\Big_BST_'+S_Name+'.model')
    print('Best Best_ntree_limit',Big_BST.best_ntree_limit)

    preds = Big_BST.predict(Big_test, ntree_limit=Big_BST.best_ntree_limit)

