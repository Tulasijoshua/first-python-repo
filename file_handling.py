# f1 = open("file_1.txt", "x")
# f1 = open("file_1.txt", "r")
# f1 = open('file_1.txt')
# data = f1.read()
# print(data)

# w - This will open the file in write mode. If file exist it will overwrite the things in it. I
# f1 = open("file_1.txt", "w")
# f1.write("Welcome to jenny's lectures")
# print(f1.read())

# r+ - This will open the file in both read and write mode. If file doesn't exist it will raise an error.
# f1 = open("file_1.txt", "r+")
# print(f1.tell())
# f1.write("Hi")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# # f1.write("This is python course")

# w+ - It will open the file in read and write mode. It overwrite the previous content. It create a new file if the file doesn't exist
# f1 = open("file_1.txt", "w+")
# print(f1.tell())
# f1.write("Hi welcome")
# print(f1.tell())
# f1.write("This is Python course")
# print(f1.tell())
# f1.seek(0)
# print(f1.tell())
# data = f1.read()
# print(data)
# print(f1.tell())
# f1.close()

# a - It will open the file in append or write mode. The file handler exist at the end of the file
# It create a new file if file doesn't exist. You can't read in append mode
# f1 = open("file_1.txt", "a")
# f1.write("Hello students")
# print(f1.read())

# a+ - Append and read
# f1 = open("file_1.txt", "a+")
# f1 = open("C:Users\tulas\Desktop\myFile.txt", "a+")
# f1 = open("myFile.txt", "r")

# print(f1.tell())
# f1.seek(0)
# # f1.write("Hello students")
# print(f1.read())
# f1.write("Jenny's lectures")

f1 = open("Joshua_pic.jpg", "rb")
f2 = open("Joshua_pic2.jpg", "wb")
for i in f1:
    f2.write(i)
# print(f1.read())
