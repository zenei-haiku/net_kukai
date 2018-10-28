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
    sin="seiki_withname.csv"
    with codecs.open(sin, 'r', 'utf-8', 'ignore') as frawdata:
        seiki_raw=pd.read_table(frawdata,delimiter=",")
    inku=seiki_raw.shape[0]
    inp=int(inku/3)
    sin2="senku.csv"
    with codecs.open(sin2, 'r', 'shift-jis', 'ignore') as frawdata:
        senku_raw=pd.read_table(frawdata,delimiter=",")
    dfsen_in=senku_raw[["特選句（番号、半角)","並選句1（番号、半角)","並選句2（番号、半角)","並選句3（番号、半角)","逆選句（番号、半角)"]]
    msen=np.array(dfsen_in)
    mpoint=np.zeros((inku,3))
    dfsen_out= pd.DataFrame(index=senku_raw.index, columns=["特選句","並選句1","並選句2","並選句3","逆選句"])
#選句ポイント数え上げ
    for ci in range(inku):
        for cj in range(inp):
            if msen[cj,0]==ci+1:
                mpoint[ci,0]=mpoint[ci,0]+1
                tokusen=seiki_raw.at[seiki_raw.index[ci],"句"]
                dfsen_out.at[dfsen_out.index[cj],"特選句"]=tokusen
            #並選*3
            if msen[cj,1]==ci+1:
                mpoint[ci,1]=int(mpoint[ci,1]+1)
                namisen=seiki_raw.at[seiki_raw.index[ci],"句"]
                dfsen_out.at[dfsen_out.index[cj],"並選句1"]=namisen
            if msen[cj,2]==ci+1:
                mpoint[ci,1]=int(mpoint[ci,1]+1)
                namisen=seiki_raw.at[seiki_raw.index[ci],"句"]
                dfsen_out.at[dfsen_out.index[cj],"並選句2"]=namisen
            if msen[cj,3]==ci+1:
                mpoint[ci,1]=int(mpoint[ci,1]+1)
                namisen=seiki_raw.at[seiki_raw.index[ci],"句"]
                dfsen_out.at[dfsen_out.index[cj],"並選句3"]=namisen
            if msen[cj,4]==ci+1:
                mpoint[ci,2]=int(mpoint[ci,2]+1)
                gyakusen=seiki_raw.at[seiki_raw.index[ci],"句"]
                dfsen_out.at[dfsen_out.index[cj],"逆選句"]=gyakusen
    dfpoint=pd.DataFrame(mpoint,columns=["特選数","並選数","逆選数"])
    seiki_done=pd.concat([seiki_raw,dfpoint],axis=1)
#0点句は無記名に
    for ci in range(inku):
        ipoint=mpoint[ci,0]+mpoint[ci,1]+mpoint[ci,2]
        if ipoint==0:
            seiki_done.at[seiki_done.index[ci],"俳号"]=""
    sout_seiki_done='seiki_withpoint.csv'
    seiki_done.to_csv(sout_seiki_done,index=False)
#選評
    asenku=np.random.rand(3*inp)
    name=senku_raw[["俳号"]]
    senpyo=senku_raw[["選評 (改行可能)","自己紹介・近況など(改行可能)"]]
    senpyo_all=pd.concat([name,dfsen_out,senpyo],axis=1)    
    sout_senpyo='senpyo.csv'
    senpyo_all.to_csv(sout_senpyo,index=False)
    
