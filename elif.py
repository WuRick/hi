bmi = input('請輸入ＢＭＩ值： ')
bmi = float(bmi)
if bmi <= 18:
	print('過瘦')
elif bmi >18 and bmi <= 22:
	print('標準身材')
else:
	print('過胖')