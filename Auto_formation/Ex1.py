#coding:utf-8



a = 0x099
b = 0x11

c = a & b

print("{}".format(bin(c)))
print("{}".format(bool(c)))

if bool(c):
    print("Les bits 00010001 sont present")