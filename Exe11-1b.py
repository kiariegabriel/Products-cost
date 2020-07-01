status=''
d={}
while status!='done':
	product=input('Enter product name: ')
	d[product]=eval(input('Enter price of the product: '))
	status=input('Enter Done to close ')
print(d)
for i in range(2):
	product=input('Enter the product: ')
	if product in d:
		print(d[product])
	else:
		print('Not in the list.')
dollar=eval(input('Enter the money: '))
l=[x[0] for x in d.items() if x[1]<=dollar ]
print(l)