dohyeon = ["박도현", '27', '010-']
name = dohyeon[0]
age =dohyeon[1]
phone = dohyeon[2]
print(type(dohyeon))
print(name, age, phone)

names = [['박도현', 'ㅇㅇㅇ', 'ㅇㅇㅌ'], ['20','21','22'],['010','011','012']]
print(names[0])

numbers =[1,2,3,4,5]
result = numbers[2] +numbers[-1]
print(result)

print(len(names[0]))

#리스트에 요소 추가 및 제거하기
last =[1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)