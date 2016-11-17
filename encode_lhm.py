password = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t',
 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n','z':'a', 'y':'b', 'x':'c', 'w':'d',
  'v':'e', 'u':'f', 't':'g',
  's':'h', 'r':'i', 'q':'j', 'p':'k', 'o':'l', 'n':'m'}

gg = ''

print('암호 입력하세요')

a = input('')

for b in a:
    gg = gg + password[b]

print(gg)
