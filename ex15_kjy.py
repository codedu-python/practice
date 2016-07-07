#파이썬을 실행할때 python 파일이름 형식으로 쳐주셔야되요 예를들어 python ex15.py ex13.py
from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {}:".format(filename))
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
