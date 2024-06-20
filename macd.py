# BACKGROUNDSTYLE(2);
# DIFF:EMA(CLOSE,SHORT)-EMA(CLOSE,LONG),COLORWHITE,PRECIS3;
# DEA :EMA(DIFF,M),COLORYELLOW,PRECIS3;
# MACD:(DIFF-DEA)*2,COLORSTICK,PRECIS3;
#
# GJ:=MAX(C,O);
# L4:=LLV(GJ,4);
# JL:=(HHV(DIFF,55)-LLV(DIFF,55))/5;
# GT:=DEA>REF(DEA,1) AND REF(DEA,1)<REF(DEA,2);
# A1:=BARSLAST(REF(GT,1));
# 底背离:=REF(L4,A1+1)>CLOSE AND DIFF>REF(DIFF,A1+1) AND GT;
# DRAWTEXT(底背离,REF(DEA,A1)*1.18,' 底背离'),COLORRED;
# H4:=HHV(GJ,4);
# GT2:=DEA<REF(DEA,1) AND REF(DEA,1)>REF(DEA,2);
# A2:=BARSLAST(REF(GT2,1));
# 顶背离:= REF(H4,A2+1)<H4 AND  DIFF<REF(DIFF,A2+1) AND GT2;
#
# DRAWTEXT(顶背离,REF(DEA,A2)*1.18,' 顶背离'),COLORGREEN;
# SHORT 5, LONG 10, M 2

{13, 21, 9}
# DIF:EMA(LOW,SD)-EMA(LOW,LD),COLORWHITE;
# DEA:EMA(DIF,MD),COLORYELLOW;
# MACD:(DIF-DEA)*2,COLORSTICK,COLORE970DC;
# ZERO:0,COLORGRAY;
# STICKLINE(DIF<0 AND DIF<=0 AND (DIF+MACD)>0,DIF,(DIF+MACD),0,-1),COLORWHITE;
# STICKLINE(DEA<0 AND DIF<=0 AND (DEA+MACD)>0,DEA,(DEA+MACD),0,1),COLORYELLOW;


SHORT = 13
LONG = 21
M = 9
list_close = []
list_DIFF = []
list_DEA = []
list_MACD = []
# DIFF:EMA(CLOSE,SHORT)-EMA(CLOSE,LONG),COLORWHITE,PRECIS3;
# DEA :EMA(DIFF,M),COLORYELLOW,PRECIS3;
# MACD:(DIFF-DEA)*2,COLORSTICK,PRECIS3;

for i in range(0, total):
    close = get("收盘价", i)
    list_close.append(close)

for i in range(0, total):
    diff = EMA(list_close, SHORT, i) - EMA(list_close, LONG, i)
    list_DIFF.append(diff)
    dea = EMA(list_DIFF, M, i)
    list_DEA.append(dea)
    macd = (diff - dea) * 2
    list_MACD.append(macd)

    save("DIFF", diff, i)
    save("DEA", dea, i)
    save("MACD", macd, i)

    if i == total - 1:
        text(max(list_MACD), total - 3, "涨停", 0)

# 画线
draw.color_stick("MACD")
draw.curve("DIFF", 15)
draw.curve("DEA", 7)


