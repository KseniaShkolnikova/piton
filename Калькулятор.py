import math
print('Запустить программу?')
red=input()
if red=='да' or red== 'нет':
    while red=='да':
        try:
            pervoeznachenie = float (input('Введите первое значение: '))
        except ValueError:
            print ('Нужно вводить число. Конец программы.')
            exit()
        else:
            result=0 
            deistvie=input("Выберите операцию: +, -, *, /,**,sqrt,!, sin, cos, tg: ")
            if deistvie =='+' or deistvie=='-' or deistvie=="*" or deistvie=='/' or deistvie=='**' or deistvie=='sqrt' or deistvie=='!'or deistvie=='sin' or deistvie=="cos" or deistvie=='tg':
                if deistvie=="sqrt":
                    if pervoeznachenie>=0:
                        result = math.sqrt (pervoeznachenie)
                    else: 
                        print ('Корень не может быть отрицательным. Конец программы.')
                        exit()
                elif deistvie=='!':
                    pervoeznachenie= int(pervoeznachenie)
                    if pervoeznachenie>0:
                        result=math.factorial (pervoeznachenie)
                    else: 
                        print ('Факториал не может быть отрицательным. Конец программы.')
                        exit()
                elif deistvie== 'sin':
                    result= math.sin (pervoeznachenie)
                elif deistvie== 'cos':
                    result= math.cos (pervoeznachenie)
                elif deistvie=='tg':
                    result= math.tan (pervoeznachenie)
                else :
                    try:
                        vtoroeznachenie= float (input("Введите второе число: "))
                    except ValueError:
                        print('Нужно вводить число. Конец пргораммы.')
                        exit()
                    else:
                        if deistvie== "+":
                            result= pervoeznachenie + vtoroeznachenie
                        elif deistvie=='-':
                            result= pervoeznachenie-vtoroeznachenie
                        elif deistvie=='*':
                            result= pervoeznachenie * vtoroeznachenie
                        elif deistvie == '/':
                            if vtoroeznachenie==0:
                                print ('Делить на ноль нельзя. Конец программы.')
                                exit()
                            else:
                                result=pervoeznachenie/vtoroeznachenie
                        elif deistvie=='**':
                            result=pervoeznachenie**vtoroeznachenie
                print (result)
                print ('Хотите продолжть?')
                red=input()
                if red!= 'нет' and red!='да':
                    print('Нужно вводить да или нет. Конец пргораммы.')
                    exit()  
            else: 
                print ('Выберите опперацию из списка. Конец программы.')  
                exit()  
else:
    print ('Нужно вводить да или нет. Конец программы.')
    exit()
if red=='нет' or red !="да":
    print ('Конец программы.')
    exit()

    
       


