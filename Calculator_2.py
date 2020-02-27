num = 0
result = 0
Selmenu = 0
state = 0


def Smenu():
    global result
    print(f"""
===========================
    결과 : {result}     

    1. Add
    2. Mul
    3. Sub
    4. Div

    0. Reset
    00. Exit
===========================
    """)


def Select():
    print("메뉴를 골라주세요 : ", end="")
    return input()


def Ipnum():
    n = int(input('숫자를 입력하시오 : '))
    print(f'입력한 숫자 : {n}')
    return n


def Check_state():
    global state
    if state == 0:
        return 1
    else:
        return 0


def Add():
    global num
    global result
    cs = Check_state()
    if cs:
        print('처음', end=' ')
        result = Ipnum()
    print('더할', end=" ")
    num = Ipnum()
    result += num


def Mul():
    global num
    global result
    cs = Check_state()
    if cs:
        print('처음', end=' ')
        result = Ipnum()
    print('곱할', end=" ")
    num = Ipnum()
    result *= num


def Sub():
    global num
    global result
    cs = Check_state()
    if cs:
        print('처음', end=' ')
        result = Ipnum()
    print('뻴', end=" ")
    num = Ipnum()
    result -= num


def Div():
    global num
    global result
    cs = Check_state()
    if cs:
        print('처음', end=' ')
        result = Ipnum()
    print('나눌', end=" ")
    num = Ipnum()
    if num == 0:
        result = 0
    else:
        result /= num


while True:
    Smenu()
    Selmenu = Select()
    if Selmenu == '1':
        Add()
        state = 1
    elif Selmenu == '2':
        Mul()
        state = 1
    elif Selmenu == '3':
        Sub()
        state = 1
    elif Selmenu == '4':
        Div()
        state = 1
    elif Selmenu == '0':
        result = 0
        num = 0
        state = 0
        print("초기화")
    elif Selmenu == '00':
        print('=' * 27)
        print(f"{'안녕하 가세요': ^27}")
        print('=' * 27)
        break
    else:
        continue
