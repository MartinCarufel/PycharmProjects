#coding:utf-8


def many_arg(*arg):
    list = ["element1", "element2", "element3", "element4", "element5", "element6", "element7", "element8"]
    print(list)
    for i in range(0, len(arg),2):
        print("{} : {}" .format(arg[i], arg[i+1]))
        list[arg[i]] = arg[i+1]
    print(list)



many_arg(2, "allo", 5, "salut")