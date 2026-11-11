# file=open("student.txt","w")
# file.write("python\n")
# file.write("java\n")
# file.write("sql\n")
# # print(file.read())
# file.close()
#
# file=open("student.txt","a")
# file.write("html\n")
# file.write("css\n")
# file.close()
#
# file = open("student.txt", "r")
# print(file.read())
# file.close()

#1st question
# with open("data.txt","w") as f:
#     f.write("hello\n")
#     f.write("python\n")
# with open("data.txt","r") as f:
#     data=f.read()
#     print(len(data))

#2nd question
# with open("line.txt","w") as f:
#     f.write("hello\n")
#     f.write("python programming\n")
#     f.write("java programming\n")
#     f.write("python\n")
# with open("line.txt","r") as f:
#     files=f.readlines()
#
#     for line in files:
#         if len(line.strip())>10:
#             print(line.strip())

#4th question
# with open("data.txt","w") as f:
#     data=f.write("hello python programming language")
#     # print(data)
# with open("data.txt","r") as f:
#     file=f.read(10)
#     print(file)
#     print(f.tell())
#     f.seek(0)
#     print(f.read())

