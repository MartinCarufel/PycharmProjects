#coding:utf-8


import re
from robobrowser import RoboBrowser


browser = RoboBrowser(history=True)
browser.open('https://game.planetarion.com/bcalc.pl')

form = browser.get_form()
form['def_metal_asteroids']
form['def_metal_asteroids']=target.size
form['action']='save'
browser.submit_form(form)