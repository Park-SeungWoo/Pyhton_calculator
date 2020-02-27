def print_bar():
    print('=' * 50)


class calculator:
    def __init__(self):
        self.val = 0
        self.num = 0

    def save(self, nn, sta):
        self.num = nn
        if sta == 0:
            self.val = nn

    def cal_menu(self, sta):
        print_bar()
        print('''
        previous enter number : %f
        result number : %f
        
        1. add
        2. multiply
        3. subtract
        4. divide
        5. clear
        6. exit
        
        ''' % (self.num, self.val))
        if sta != 0:
            print('Input menu : ', end='')

    def add(self):
        self.val += self.num
        return self.val

    def mul(self):
        self.val *= self.num
        return self.val

    def sub(self):
        self.val -= self.num
        return self.val

    def div(self):
        self.val /= self.num
        return self.val

    def pres(self):
        return self.val


beggining_menu = '''
    1.Calculate
    2.exit

    Input menu : '''
state = 0

CAL = calculator()

while True:
    print_bar()
    print(beggining_menu, end='')
    bn = input()
    if bn == '1':
        while True:
            CAL.cal_menu(state)
            if state == 0:
                n = int(input('Enter number : '))
                CAL.save(n, state)
            else:
                cmn = input()
                if cmn == '1':
                    CAL.num = int(input('Enter number : '))
                    print("result : ", CAL.add())
                elif cmn == '2':
                    CAL.num = int(input('Enter number : '))
                    print("result : ", CAL.mul())
                elif cmn == '3':
                    CAL.num = int(input('Enter number : '))
                    print("result : ", CAL.sub())
                elif cmn == '4':
                    CAL.num = int(input('Enter number : '))
                    print("result : ", CAL.div())
                elif cmn == '5':
                    CAL.val = 0
                    state = 0
                    CAL.num = 0
                    continue
                elif cmn == '6':
                    break
                else:
                    print('error')
                    continue
            state += 1
        break
    elif bn == '2':
        break
    else:
        continue

