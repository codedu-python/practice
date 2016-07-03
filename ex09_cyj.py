#Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #c언어와 마찬가지로 \n을 입력하면 줄이 바뀝니다.

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6
""")
#큰따옴표를 양쪽에 세 개씩 찍으면 그 안에 있는 내용이 줄바뀜까지 그대로 표시됩니다.
#큰따옴표를 한 세트 벗겨내니 오류로 실행이 불가능하다 나옵니다.
#대부분의 경우 줄이 바뀌면 이전 줄에서의 설명이 적용되지 않습니다.
#print가 대표적이고, 위에 days= "Mon Tue..."할 때에도 한 줄이내에서 해결해야 합니다.
#설명을 하고 줄을 바꿀 때마다 앞에 샾을 붙이는 것도 같은 이유에서입니다.
