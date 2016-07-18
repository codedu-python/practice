#파이썬을 실행할때 python 파일이름 임의문서1 임의문서2로 쳐주셔야되요 예를들어 python ex17.py 1.txt 2.txt
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is {} bytes long".format(len(indata)))

print("Does the output file exist? {}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
