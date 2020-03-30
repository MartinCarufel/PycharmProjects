import sys

sys.path.append('C:/PythonLibs/PythonPack1')


from modulemartin import Module1
import popup

p = Module1()
p.operation1()

popup.create_popup('Je suis un sale con !\n\n Salut les trou du clu\n\n Je men vais dici')
popup.create_popup('Je suis un sale con !')