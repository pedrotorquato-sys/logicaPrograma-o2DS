num1 = input ("Digite o primeiro numero:")
num2 = input ("Digite o segundo numero:")
num3 = input ("Digite o terceiro numero:")
if num1 > num2 or num1 > num3:
    print (num3,' e o maior')
elif num2 > num3:
    print (num2,' e o maior')
else:
    print (num3,' e o maior')