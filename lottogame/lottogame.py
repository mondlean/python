import random 

while (True) :#계속 돌아감 
    lottonum=[]
    mylotlist = [] 
    numberList = 0
    Bonus=[]#보너스 숫자m
    
    rannum=0
    mylotnum = 0
    comlotnum=0
    while (mylotnum < 6):#로또 숫자 입력 함수
        mynum = int(input("1부터 45까지의 번호를 적어주세요 "))
        if mynum > 45 :
            print("45보다 큰 수입니다 다시 적어주세요")#큰 수 제거 코드
            continue
        if mynum in mylotlist:
             print("중복된 값이 있습니다 다시 적어주세요")#중복제거
             continue
        mylotlist.append(mynum)  #오름차순 정렬
        mylotnum +=1
        print(mylotnum)
    mylotlist.sort()
    print(mylotlist)
    while (comlotnum<6):# 로또번호 생성 코드
        
        rannum=random.randint(1,45)
        if rannum in lottonum:
            continue
        lottonum.append(rannum)
        comlotnum+=1
    comlotnum=0
    while (comlotnum<1):# 보너스번호 생성 코드
        rannum=random.randint(1,45)
        if rannum in lottonum:
            continue
        Bonus.append(rannum)
        comlotnum+=1
       
        
    lottonum.sort()
        
    print (lottonum,"+",Bonus)
        
    for i in range(6):
        for j in range(6):
            if mylotlist[i]==lottonum[j]:
                numberList+=1
        
    if numberList<3 :
        print ("꽝! ㅋㅋ 그래도 {0}개 맞췄네".format(numberList))    
    if numberList==3 :
        print ("5등 축하드립니다")
    if numberList==4 :
        print ("4등 축하드립니다")
    if numberList==5 :
        print ("3등 축하드립6니다")    
    if numberList==5 and lottonum in Bonus:
        print ("2등 축하드립니다")
    if numberList==6 :
        print ("1등 축하드립니다")
    
    connue= input("다시하시겠습니까? Y/N: ")
    if connue=="Y" or connue== "y":
        print("다시합니다")
    else:
        break
        