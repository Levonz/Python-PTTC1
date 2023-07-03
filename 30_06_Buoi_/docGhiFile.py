file = open('30_06_Buoi_/test2.txt','w')
file.write("In dong nay vao file")
file.write("\nDay la dong thu 2")
file.close()

file = open('30_06_Buoi_/test2.txt','a')
file.write("\nThem dong nay bang append")
file.close()


with open('30_06_Buoi_/test2.txt','r') as f:
    contents = f.read()
    print(contents)
    

with open('30_06_Buoi_/test2.txt','r') as f:
    contents = f.readline()
    print(contents)
    

with open('30_06_Buoi_/test2.txt','r') as f:
    contents = f.readlines()
    print(contents)
