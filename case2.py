import random



ran = int(10*random.random())
sans = 2
print(ran)


while True:
    enter = int(input('1-10 arasinda bir reqem daxil edin. '))
    
    if(enter == ran ):
        print('Tebrikler duzgun cavabi tapdiniz!')
        break
    elif(sans == 0):
        print("Təəssüfki düzgün cavabl tapa bilmədiz. Yenidən oynamaq üçün proqramı təkrar işə salın" )
        break
    elif(enter != ran):
        sans -=1
        print("Bextinizi bir daha sinayin. Sizin "+ str(sans) +" sansiniz qalib")
    
