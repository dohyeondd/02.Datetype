name1 =input('이름을입력하세요')
age1 = input('나이를입력하세요')
email1=input('이메일을 입력하세요')
number1=input('연락처를 입력하세요')

name2 =input('이름을입력하세요')
age2 = input('나이를입력하세요')
email2=input('이메일을 입력하세요')
number2=input('연락처를 입력하세요')

dic1 ={name1: [age1, email1, number1]}
dic2 ={name2: [age2, email2, number2]}

print(dic1)
print(dic2)


#2
exchange = {'달러': 1320, '엔화' :800, '위안':130}
chul= [13,200,13]

chul = [13,200,13]

total=exchange['달러']*chul[0]+exchange['엔화']*chul[1]
print('가지고 계신 돈은 '+ str(total) +'원 입니다.')


