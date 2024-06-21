#初始化变量
收盘价列表 = []     #新建收盘价列表
diff列表 = []      #新建diff列表
dea列表 = []       #新建dea列表
短周期 = 12        #用于计算短期指数移动平均的周期
长周期 = 26        #用于计算长期指数移动平均的周期
dea周期 = 9        #用于计算dea指数移动平均的周期
N = param(9)
M1 = param(3)
M2 = param(3)

gj=[]
gt=[]
A1=[]
list_low=[]
list_high=[]
list_rsv=[]
list_k=[]
list_d=[]
#获取数据
for i in range(0, total):
    收盘价 = get("收盘价", i)     #获取收盘价
    开盘价 = get("开盘价", i)     #获取收盘价
    收盘价列表.append(收盘价)     #将收盘价储存在"收盘价列表"中, 用于后续计算
    gj.append(max(收盘价,开盘价))
    low=get("LOW",i)
    high=get("HIGH",i)
    list_low.append(low)
    list_high.append(high)
#计算数据并储存用于画线的数据
for i in range(0, total):
    短期指数移动平均 = EMA(收盘价列表, 短周期, i)   #计算短期指数移动平均
    长期指数移动平均 = EMA(收盘价列表, 长周期, i)   #计算长期指数移动平均
    diff = (短期指数移动平均 - 长期指数移动平均)*100 #计算diff值
    diff列表.append(diff)                       #将diff值存在diff列表中
    dea = EMA(diff列表, dea周期, i)              #计算dea值
    dea列表.append(dea)                         #将dea值保存到dea列表中
    macd = 2 * (diff - dea)                     #计算macd值
    save("DIFF", diff, i)                       #将diff值储存在"DIFF"对象中并用于画线
    save("DEA", dea, i)                         #将dea值储存在"DEA"对象中并用于画线
    save("MACD", macd, i)                       #将macd值储存在"MACD"对象中并用于画线
    llv = LLV(list_low, N, i)
    hhv = HHV(list_high, N, i)
    if hhv - llv == 0:
        rsv = 0;
    else:
        rsv = (get("CLOSE",i) - llv) / (hhv - llv) * 100
    list_rsv.append(rsv)
for i in range(0, visble_count):
    add('l4', LLV(gj,4,i+begin))
    add('H4', HHV(gj,4,i+begin))
    dea=get("DEA",i)
    if (dea > REF("DEA",1,i)) and (REF("DEA",1,i) < REF("DEA",2,i)):
        gt.append(True)
    else:
        gt.append(False)
    A1.append(BARSLAST(gt, i))
for i in range(0, visble_count):
    if REF("l4",A1[i]+1,i)>get("CLOSE",i+begin) and get("DIFF",i)>REF("DIFF",A1[i]+1,i) and gt[i]:
        draw.line(dea列表[i+begin-A1[i]], i+begin, dea列表[i+begin-A1[i]], i+begin-A1[i], "#FF0000");
        draw.line(dea列表[i+begin-A1[i]], i+begin, dea列表[i+begin], i+begin, "#FF0000");
        text(dea列表[i+begin], i+begin, "底背离", 0);
result_dif_dea = CROSS(diff列表, dea列表)
result_dea_dif = CROSS(dea列表, diff列表)

for i in range(0, total):
    k = SMA(list_rsv, M1, 1, i)
    save("k", k, i);
    list_k.append(k)
for i in range(0, total):
    d = SMA(list_k, M2, 1, i)
    list_d.append(d)
    save("d", d, i);
    j=3*list_k[i]-2*d
    save("j", j, i);

result_kd = CROSS(list_k, list_d)
result_dk = CROSS(list_d, list_k)
for i in result_dif_dea:
    text(dea列表[i], i, "买", 15)
for i in result_dea_dif:
    text(dea列表[i], i, "卖", 15)
for i in result_kd:
    text(list_d[i], i, "买", 15)
for i in result_dk:
    text(list_d[i], i, "卖", 15)
#画出储存好数据的线
draw.curve("DIFF", 15)            #画出"DIFF"折线
draw.curve("DEA", 4)              #画出"DEA"折线
draw.color_stick("MACD")          #画出"MACD"红涨绿跌图


draw.curve("k", 9)
draw.curve("d", 5)
draw.curve("j", 19)