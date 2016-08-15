#이번 단원은 오류고치기 단원인데됴... 화내지마시구 차근차근 해보세요.

import ex25_lsy #요로코롬 임포트시켜서 ex25의 함수들을 사용합니다.

print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print("----------")
print(poem)
print("----------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." %(beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

words = ex25_lsy.break_words(sentence) #ex25에서 break_words란 함수를 가져와 사용한다는 의미
print(words)
sorted_words = ex25_lsy.sort_words(words)
print(sorted_words)

ex25_lsy.print_first_word(words)
ex25_lsy.print_last_word(words)
ex25_lsy.print_first_word(sorted_words)
ex25_lsy.print_last_word(sorted_words)
sorted_words = ex25_lsy.sort_sentence(sentence)
print(sorted_words)

ex25_lsy.print_first_and_last(sentence)

ex25_lsy.print_first_and_last_sorted(sentence)
