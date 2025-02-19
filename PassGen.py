import random
nums = int(input("Из скольки символов будет состоять ваш пароль? Число(1-100) :"))
print('*'*60)
colvo = int(input("Сколько паролей сгенерировать? (1-10) :"))
print('*'*40)
uper = input(" Нужны ли заглавные буквы? (Да/Нет) :").lower()
print('*'*40)
specsimvol = input(" Нужны ли спец символы? (Да/Нет) :").lower()
print('*'*40)

def generate(nums, uper, specsimvol):
    str_all = '1234567890qwertyuiopasdfghjklzxcvbnm'
    str_spec = '.,:;!_*-+()/#¤%&'
    str_up = str_all.upper()
    if uper == 'да' and specsimvol == 'да':
        str = str_all + str_spec + str_up
        ls = list(str)
        random.shuffle(ls)
    elif uper == 'да' and specsimvol != 'да':
        str = str_all + str_up
        ls = list(str)
        random.shuffle(ls)
    elif uper != 'да' and specsimvol == 'да':
        str = str_all + str_spec
        ls = list(str)
        random.shuffle(ls)
    else:
        str = str_all
        ls = list(str)
        random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(nums)])
    return psw
ex = 0
while ex < colvo:
    print(generate(nums, uper, specsimvol))
    ex += 1