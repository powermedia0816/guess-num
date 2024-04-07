import random

start_num = int(input('請輸入隨機數字範圍起始值:'))
end_num = int(input('請輸入隨機數字範圍結束值:'))

r = random.randint(start_num,end_num)
count = 0
while True:
	count = count + 1
	num = int(input('請輸入數字'))
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count,'次')

