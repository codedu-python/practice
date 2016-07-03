print ("Mary had a little lamb.")
print ("Its fleece was white as {}.".format('snow'))
print ("And everywhere that Mary went.")
print("." * 18) # What'd that do? -> 온점이 8번 인쇄되었다.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens.
print (end1 + end2+ end3 + end4 + end5 + end6, end= ' ') #마지막 end는 띄어쓰기 기능 수행
print (end7 + end8 + end9 + end10 + end11 + end12)
