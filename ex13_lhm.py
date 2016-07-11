#파이썬을 실행할때 python ex13.py 한자리수 두자리수 세자리수 형식으로 쳐주셔야되요
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
