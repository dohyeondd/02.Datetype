dic = {'박도현' : 27, 'ㅇㅇㅇ' : 28}
print(type(dic), dic['박도현'])

#딕셔너리 데이터 업데이트
dic['박도현'] = 27
print(dic['박도현'])

dic_2 = {'박도현':[25,180,72,'010-0000-0000]'], '홍길동' : [20,]}
print(dic_2['박도현'][0])
dic_3 ={'박도현':{'나이':25, '키':180 ,'몸무게' :72, '연락처':010-0000-0000'}
               '홍길동': {...}
               }

print(dic_3['박도현']['연락처'])