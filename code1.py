
import pandas as pd

def ocr(file,text):
    data=pd.read_csv(file)
    data= data.sort_values(['x0','y0'],ascending=[True,True])
    data.reset_index(inplace=True)
    data=data.drop('index',axis=1)
    text1=[]
    for index in data.index:
        if (data['x0'][index]>=text[0] and data['x0'][index]<=text[2]) and (data['y0'][index]>=text[1] and data['y0'][index]<=text[3]):
            text1.append(data['Text'][index])
    return " ".join([w for w in text1])

