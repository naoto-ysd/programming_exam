y, m, d = input().split()

if len(m) == 1:
    temp_m = "0" + m
else:
    temp_m = m

if len(d) == 1:
    temp_d = "0" + d
else:
    temp_d = d

seireki = y + temp_m + temp_d
seireki = int(seireki)


if seireki <= 19120729:
    print('明治年' + m + '月' + d + '日' )
elif seireki <= 19261224:
    print('大正年' + m + '月' + d + '日' )
elif seireki <= 19890107:
    print('昭和年' + m + '月' + d + '日' )
elif seireki <= 20190430:
    print('平成年' + m + '月' + d + '日' )
else:
    print('令和年' + m + '月' + d + '日' )