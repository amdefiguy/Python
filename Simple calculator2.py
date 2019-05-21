print("PYTHON CALCULATOR")
while True:
	num1=input("")
	opera=input("")
	num2=input("")

	if opera=="+":
		print("=")
		print(num1+num2)
		print("answer is"+ result)

	elif opera=="-":
		print("=")
		print(num1-num2)
		print("answer is"+ result)

	elif opera=="*":
		print("=")
		print(num1*num2)
		print("answer is"+ result)

	elif opera=="/":
		print("=")
		print(num1/num2)
		print("answer is"+ result)

	else:
			print("SYNTAX ERROR")
			print("answer is"+ result)


