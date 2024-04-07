import random
r = random.randint(1,100)
while True:
	num = int(input('請輸入數字'))
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')

