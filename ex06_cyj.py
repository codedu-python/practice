x = "There are {} types of people." .format (10)
binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}." .format (binary, do_not)

print(x)
print(y)

print ("I said : {}.".format(x))
print("I also said : {}." .format(y))

hilarious = False #False의 의미가 뭔지 모르겠습니다.
joke_evaluation = "Isn't that joke so funny?! {}"

print (joke_evaluaion. format(hilarious)) #Isnt't that joke so funny? 한후에 중괄호가 있어야 할 위치에 False가 들어가는 것 같았는데...
#False에 따옴표를 씌우는 것은 의도하신 바가 아니시겠죠?ㅠㅠ
w = "This is the left side of..."
e = "a string with a right side."

print (w + e)
