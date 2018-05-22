# coding=utf-8
def param():
    from grab import Grab
    KOL = 1	 #КОЛИЧЕСТВО ЦИКЛОВ СКРИПТА
    for m in range(KOL):
	    g = Grab()
	    g.go('http://192.168.100.6:10002/login/WebVision/ses_Fithness/')
	    g.set_input('user', 'root')
	    g.set_input('pass', 'GfhjkmKf;f123')
	    g.submit()
	    g.go('http://192.168.100.6:10002/WebVision/ses_Fithness4/pg_so/pg_6/pg_mn/pg_1?com=attrsBr&tm')
	    name1,name2,full,mass1=[],[],[],[]
	    for elem in g.doc.select('//w[*]/el[@id="text"]'): name1.append(elem.text()) #Холодилка название параметров
	    for elem in g.doc.select('//w[*]/el[@id="arg0val"]'): mass1.append(elem.text())#Холодилка значения
    global full2
    name1 = [x for x in name1 if x != '%1'] #Удаляем ненужные значения
    name1=(name1[2],name1[3],name1[8],name1[9],name1[29],name1[49],name1[32],name1[33],name1[4],name1[31],name1[60]) #Собираем названия
    mass1=(mass1[0],mass1[1],mass1[4],mass1[5],mass1[9],mass1[30],mass1[10],mass1[11],mass1[3],mass1[12],mass1[39]) # Собираем значения
    full= [a +" = "+ str(b) for a, b in zip(name1, mass1)] #В список 2 списка
    return full
