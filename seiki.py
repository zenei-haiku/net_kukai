# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:25:30 2018

@author: Sugawara
"""

import pandas as pd
import numpy as np
import codecs

if __name__ == "__main__":
    itime=1
    sin="touku.csv"
    with codecs.open(sin, 'r', 'shift-jis', 'ignore') as frawdata:
        rawdata=pd.read_table(frawdata,delimiter=",")
    inp=rawdata.shape[0]
    name=rawdata["俳号"]
    names=pd.concat([name,name,name],ignore_index=True)
    ku1=rawdata["句1"]
    ku2=rawdata["句2"]
    ku3=rawdata["句3"]
    ku_all=pd.concat([ku1,ku2,ku3],ignore_index=True)
    idrand=np.random.rand(3*inp)
    dfidrand=pd.DataFrame(idrand,columns=["乱数"])
    seiki_raw=pd.concat([dfidrand,names],axis=1) 
    seiki_raw["句"]=ku_all
    seiki_sorted=seiki_raw.sort_values(by="乱数")
    seiki_sorted=seiki_sorted.reset_index(drop=True)
    sorted_id=np.arange(1,3*inp+1,1)
    dfsorted_id=pd.DataFrame(sorted_id,columns=["番号"])
    seiki=pd.concat([dfsorted_id,seiki_sorted],axis=1)    
    seiki_all=seiki[["番号","句","俳号"]]
    sout_all='seiki_withname.csv'
    seiki_all.to_csv(sout_all,index=False)
    seiki_mail=seiki[["番号","句"]]
    sout_mail='seiki_noname.csv'
    seiki_mail.to_csv(sout_mail,index=False)
    
