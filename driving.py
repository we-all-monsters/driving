country = input('請問你是什麼地方的人：')
age = input('你的年齡是：')
age = int(age)
if country == '香港' or 'HK':
	if age >= 18:
		print('你可以考駕照')
	else :
		print('你還不可以考駕照')