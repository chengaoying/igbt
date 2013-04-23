#coding=gbk
import os
import sys

telcomOperators = [
	"telcomsh",		
	"telcomgd",
	"telcomjs",
	"telcomfj",
	"telcomhn",
	"tianweisz",
	"telcomgs",
	"telcomah",
	"telcomCommon",
]

serviceProviders = [
	"ohyeah",
	"the9",
	"winside",
	"dijoy",
	"shengyi",
	"shixian",
]

def paramStr():
	return " ".join(sys.argv[1:])

def readTelcomOperator():
	print "��ѡ�������Ӫ�̣�"
	print "1.�Ϻ�����"
	print "2.�㶫����"
	print "3.���յ���"
	print "4.���ϵ���"
	print "5.���ϵ���"
	print "6.��������"
	print "7.������ţ���δ���룩"
	print "8.���յ���"
	print "9.�������ţ��½���������"
	telcom = telcomOperators[0]
	while True:
		text=raw_input("������[Ĭ��:1]��")
		if text == "":
			break
		else: 
			try:
				num = int(text)
				if num>=1 and num<=len(telcomOperators):
					telcom = telcomOperators[num-1]
					break;
			except:
				pass
			print "�����ѡ���������������롣"
	print "\n"
	return telcom

def readServiceProvider():
	print "��ѡ�����ƽ̨��"
	print "1.ŷҮƽ̨"
	print "2.�ų�ƽ̨"
	print "3.������ƽ̨"
	print "4.����ƽ̨"
	print "5.ʢ��ƽ̨"
	print "6.�������ߣ���δ���룩"
	sp = serviceProviders[0]
	while True:
		text=raw_input("������[Ĭ��:1]��")
		if text == "":
			break
		else: 
			try:
				num = int(text)
				if num>=1 and num<=len(serviceProviders):
					sp = serviceProviders[num-1]
					break;
			except:
				pass
			print "�����ѡ���������������롣"
	print "\n"
	return sp

telcom = readTelcomOperator()
sp = readServiceProvider()
props = " -Ptelcom="+telcom + " -Psp="+sp+" "
gradleCmd = "gradle "+props+paramStr()
os.system(gradleCmd)