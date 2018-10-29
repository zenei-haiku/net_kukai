# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:25:30 2018

@author: Sugawara
"""

import pandas as pd
import codecs

if __name__ == "__main__":
    sout_seiki_tex='seiki.tex'
    sin_first="firstpart_seiki.tex"
    sin_end="lastpart_seiki.tex"
    with codecs.open(sin_first, 'r', 'utf-8') as f:
         slines_first_raw=f.read()
         slines_first=slines_first_raw.replace("\r","")
    with open(sin_end, mode='r') as f:
        slines_end=f.read()
    with open(sout_seiki_tex, mode='w') as f:
        f.write(slines_first)
    sin_ku='seiki_withname.csv'
#    with codecs.open(sin_ku, 'r', 'shift-jis', 'ignore') as fraw:
    with codecs.open(sin_ku, 'r', 'utf-8', 'ignore') as fraw:
        seiki_raw=pd.read_table(fraw,delimiter=",")
    inku=seiki_raw.shape[0]

    for ci in range(inku):
        number=seiki_raw.at[ci,"番号"]
        ku=seiki_raw.at[ci,"句"]
        sline="{\\Huge " +str(number)+ "  "+ku +  "} &  \\cr \n  & \\cr \n  "
        with open(sout_seiki_tex, mode='a') as f:
            f.write(sline)
    with open(sout_seiki_tex, mode='a') as f:
        f.write(slines_end)
    
