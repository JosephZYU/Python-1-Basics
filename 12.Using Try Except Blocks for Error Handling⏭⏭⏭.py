"""
The purpose of try/excep is to make your comments as explicit as possible

🧠 对于try/excep，越清晰越好！

1. Make sure to put the more specific at the TOP!
2. Place the more general one at the bottom
3. Finall, place what you what to do in the "else" clause


NOTE: finally achieve whatever needs be done! Regardless

    最后通过finally实现无论如何都需要做的是，比如关闭文件，数据库


f.read() -> YES - it reads ALL lines of the that file
"""

try:
    f = open('corrupt_file.txt')

    # if f.name == 'corrupt_file.txt':
    #     raise Exception

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally ...")
