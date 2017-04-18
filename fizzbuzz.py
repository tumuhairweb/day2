def fizz_buzz(number):
	number Types =(int,float,long)
	if insinstance(number, numberTypes):
	   if(number % 3 == 0):
	      return 'fizz'
		elif(number % 5 == 0) and (number % 3 == 0):
			
			return 'fizzbuzz'
		elif(number% 5 == 0)
			return 'buzz'
		else:
		 return number
	else:
		raise TypeError