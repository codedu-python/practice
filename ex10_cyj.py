tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spilt\non a line."
backslash_cat = "I'm \ a \ cat"
#슬래쉬(\)가 하나이건 둘이건 \그대로 인쇄되었다.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#큰따옴표 세개 안에 있는 내용이 그대로 인쇄, 컴퓨터로 tap을 누르는 것과 \t는 간격이 다름.
# \n과 엔터는 동일한 기능 수행
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
