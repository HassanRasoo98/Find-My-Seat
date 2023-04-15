import pandas as pd
from utilities import get_filename

def get_time(room = 'AI3002  Machine Learning         BAI-6J      Room No.C-402    4th Floor'):
#     print(room, type(room))
    code = room[:6] #.split()[0]
    filename = get_filename('.xlsx')
    df = pd.read_excel(filename)
    df.drop([0,1], axis=0, inplace=True)
    df.bfill(inplace=True)
    df.ffill(inplace=True)
    df.dropna(axis=1, inplace=True)
    df.columns = df.iloc[0]
    df.drop([2], axis=0, inplace=True)
    def encode(string):
        return string.split()[0]

    for i in range(len(df.columns)):
        if i==0:
            continue
        df[df.columns[i]] = df[df.columns[i]].apply(encode)

    temp = df[df.eq(code).any(axis=1)]

    return temp.columns[df.isin([code]).any()][0]    