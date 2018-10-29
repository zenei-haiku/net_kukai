# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:25:30 2018

@author: Sugawara
"""

import pandas as pd
import codecs

if __name__ == "__main__":
    itime=1
    sout_senpyo_tex='senpyo.tex'
    sin_first="firstpart_senpyo.tex"
    sin_end="lastpart_senpyo.tex"
    with codecs.open(sin_first, 'r', 'utf-8') as f:
        slines_first_raw=f.read()
        slines_first=slines_first_raw.replace("\r","")
    with open(sin_end, mode='r') as f:
        slines_end=f.read()
    with open(sout_senpyo_tex, mode='w') as f:
        f.write(slines_first)
    sin_senpyo='senpyo.csv'
 #   with codecs.open(sin_senpyo, 'r', 'utf-8', 'ignore') as fraw:
    with codecs.open(sin_senpyo, 'r', 'sjis', 'ignore') as fraw:
        senpyo_raw=pd.read_table(fraw,delimiter=",")
    inp=senpyo_raw.shape[0]

    for ci in range(inp):
        name=senpyo_raw.at[ci,"俳号"]
        tokusen=senpyo_raw.at[ci,"特選句"]
        namisen1=senpyo_raw.at[ci,"並選句1"]
        namisen2=senpyo_raw.at[ci,"並選句2"]
        namisen3=senpyo_raw.at[ci,"並選句3"]
        gyakusen=senpyo_raw.at[ci,"逆選句"]
        hyo_raw=senpyo_raw.at[ci,"選評 (改行可能)"]
        hyo=hyo_raw.replace("\n","\n\n")
        kinkyo_raw=senpyo_raw.at[ci,"自己紹介・近況など(改行可能)"]
        kinkyo=kinkyo_raw.replace("\n","\n\n")
        sline="{\\Huge " +str(name)+ "} \n\n \\vspace{5mm} \n\n "
        with open(sout_senpyo_tex, mode='a') as f:
            f.write(sline)
        sline="{\\Large 特選句} \n \\begin{haiku}[500pt] \n {\\large "+tokusen +  "} &  \\cr \n \\end{haiku} \n {\\Large 並選句} \n \\begin{haiku}[500pt] \n{\\large "+namisen1 +  "} &  \\cr \n {\\large "+namisen2 +  "} &  \\cr \n {\\large "+namisen3 +  "} &  \\cr \n  \\end{haiku} \n {\\Large 逆選句} \n \\begin{haiku}[500pt] \n {\\large "+ gyakusen +  "} &  \\cr \n \\end{haiku} \n  \\vspace{5mm} \n\n "
        with open(sout_senpyo_tex, mode='a') as f:
            f.write(sline)
        sline="{\\Large 選評} \n \n" +hyo +  "\n\n  \\vspace{5mm} \n\n " 
        with open(sout_senpyo_tex, mode='a') as f:
            f.write(sline)
        sline="{\\Large 自己紹介・近況} \n\n " +kinkyo +  "\n\n \clearpage"
        with open(sout_senpyo_tex, mode='a') as f:
            f.write(sline)
    with open(sout_senpyo_tex, mode='a') as f:
        f.write(slines_end)
#点数入り清記
    sout_seiki_tex='seiki_withpoint.tex'
    sin_first="firstpart_seiki.tex"
    sin_end="lastpart_seiki.tex"
    with codecs.open(sin_first, 'r', 'utf-8') as f:
        slines_first_raw=f.read()        
        slines_first=slines_first_raw.replace("\r","")
    with open(sin_end, mode='r') as f:
        slines_end=f.read()
    with open(sout_seiki_tex, mode='w') as f:
        f.write(slines_first)
    sin_ku='seiki_withpoint.csv'
    with codecs.open(sin_ku, 'r', 'shift-jis', 'ignore') as fraw:
  #  with codecs.open(sin_ku, 'r', 'utf-8', 'ignore') as fraw:
        seiki_raw_withna=pd.read_table(fraw,delimiter=",")
    seiki_raw=seiki_raw_withna.fillna("")
    inku=seiki_raw.shape[0]

    for ci in range(inku):
        ku=seiki_raw.at[ci,"句"]
        name=seiki_raw.at[ci, "俳号"]
        ntoku=str(int(seiki_raw.at[ci, "特選数"]))
        nnami=str(int(seiki_raw.at[ci, "並選数"]))
        nplus=str(int(seiki_raw.at[ci, "特選数"]+seiki_raw.at[ci, "並選数"]))
        ngyaku=str(int(seiki_raw.at[ci, "逆選数"]))
#        sline="{\\Large " +ku +  "} &" + name + "特" + ntoku+ "並" + nnami + "逆" + ngyaku + "  \\cr \n  & \\cr \n  "
        sline="{"+ nplus+ "-" + ngyaku + "\\Large " +ku +  "} &" + name +  "  \\cr \n  & \\cr \n  "
 #       sline="{"+ "特" + ntoku+ "並" + nnami + "逆" + ngyaku + "\\Large " +ku +  "} &" + name +  "  \\cr \n  & \\cr \n  "
        with open(sout_seiki_tex, mode='a') as f:
            f.write(sline)
    with open(sout_seiki_tex, mode='a') as f:
        f.write(slines_end)
