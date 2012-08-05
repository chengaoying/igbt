#coding=gbk
import os
import sys

telcomOperators = [
	"telcomsh",		
	"telcomgd",
	"telcomjs",
	"telcomfj",
	"telcomCommon",
]

serviceProviders = [
	"ohyeah",
	"the9",
	"winside",
]

def paramStr():
	return " ".join(sys.argv[1:])

def readTelcomOperator():
	print "��ѡ�������Ӫ�̣�"
	print "1.�Ϻ�����"
	print "2.�㶫����"
	print "3.���յ���"
	print "4.��������"
	print "5.��������"
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