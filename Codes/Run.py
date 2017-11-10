import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def ComputeBigCount(filepath):
    DataSet = pd.read_csv(filepath, encoding='gbk')
    DataSet.head()
    Cash = []
    tic = time.time()
    for i in range(DataSet.__len__()):
        tic1 = time.time()
        if DataSet['Mark'][i] != 1:
            for j in range(i + 1, DataSet.__len__()):
                tic2 = time.time()
                if DataSet['BigID'][i] == DataSet['BigID'][j] and DataSet['Date'][i] == DataSet['Date'][j]:
                    DataSet.iat[i, 17] = DataSet.iat[i, 17] + 1
                    DataSet.iat[j, 19] = 1
                    Cash.append(j)
                    print(('BigID {} equal BigID {} Time Used: {c:0.3f}ms').format(i, j, c=((time.time() - tic2) * 1000)))
            for n in Cash:
                DataSet.iat[n, 17] = DataSet.iat[i, 17]
            Cash = []

        print(('BigID {} complete Time Used: {c:0.3f}ms').format(i, c=((time.time() - tic1) * 1000)))
    S_Name = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())
    DataSet.to_csv('G:\\CCF_1\\Result\\' + 'Big_'+S_Name + '.csv', index=False)
    print(('Complete Time Used: {c:0.2f}s').format(c=(time.time() - tic)))


def ComputeMiddleCount(filepath):
    DataSet = pd.read_csv(filepath, encoding='gbk')
    DataSet.head()
    Cash = []
    tic = time.time()
    for i in range(DataSet.__len__()):
        tic1 = time.time()
        if DataSet['Mark'][i] != 2:
            for j in range(i + 1, DataSet.__len__()):
                tic2 = time.time()
                if DataSet['MiddleID'][i] == DataSet['MiddleID'][j] and DataSet['Date'][i] == DataSet['Date'][j]:
                    DataSet.iat[i, 18] = DataSet.iat[i, 18] + 1
                    DataSet.iat[j, 19] = 2
                    Cash.append(j)
                    print(('MiddleID {} equal MiddleID {} Time Used: {c:0.3f}ms').format(i, j,c=((time.time() - tic2) * 1000)))
            for n in Cash:
                DataSet.iat[n, 18] = DataSet.iat[i, 18]
            Cash = []

        print(('MiddleID {} complete Time Used: {c:0.3f}ms').format(i, c=((time.time() - tic1) * 1000)))
    S_Name = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())
    DataSet.to_csv('G:\\CCF_1\\Result\\' +'Middle_'+ S_Name + '.csv', index=False)
    print(('Complete Time Used: {c:0.2f}s').format(c=(time.time() - tic)))
if __name__ == '__main__':
    fp='G:\\CCF_1\\Result\\2017-11-10_17.38.26.csv'
    ComputeMiddleCount(fp)