formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) #False 와 True를 문자열로 취급하지 않아도 잘 인쇄가 되었네요. 그 이유가 궁금합니다.
print(formatter.format(formatter, formatter, formatter, formatter)) #각 formatter 하나에 {}가 네 개 들어있으므로 {}가 16개 인쇄되었습니다.
print(formatter.format(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
