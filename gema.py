list_low = []
for i in range(0, total):
    low = get("最低价", i)
    list_low.append(low)

for i in range(0, total):
    ema5 = EMA(list_low, 5, i)
    ema13 = EMA(list_low, 13, i)
    ema21 = EMA(list_low, 21, i)
    ema55 = EMA(list_low, 55, i)
    ema89 = EMA(list_low, 89, i)
    ema144 = EMA(list_low, 144, i)
    ema233 = EMA(list_low, 233, i)
    ema377 = EMA(list_low, 377, i)
    ema610 = EMA(list_low, 610, i)

    save("EMA5", ema5, i)
    save("EMA13", ema13, i)
    save("EMA21", ema21, i)
    save("EMA55", ema55, i)
    save("EMA89", ema89, i)
    save("EMA144", ema144, i)
    save("EMA233", ema233, i)
    save("EMA377", ema377, i)
    save("EMA610", ema610, i)

draw.curve("EMA5", "#FFFFFF", 1)
draw.curve("EMA13", "#FFFF00", 2)
draw.curve("EMA21", "#FF0000", 3)
draw.curve("EMA55", "#00FF00", 4)
draw.curve("EMA89", "#8500FFFF", 2)
draw.curve("EMA144", "#70808000", 1)
draw.curve("EMA233", "#55008080", 1)
draw.curve("EMA377", "#40FF0000", 1)
draw.curve("EMA610", "#25C0C0C0", 1)