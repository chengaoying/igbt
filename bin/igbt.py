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
	print "请选择电信运营商："
	print "1.上海电信"
	print "2.广东电信"
	print "3.江苏电信"
	print "4.福建电信"
	print "5.湖南电信"
	print "6.深圳天威"
	print "7.甘肃电信"
	print "8.其他电信"
	telcom = telcomOperators[0]
	while True:
		text=raw_input("请输入[默认:1]：")
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
			print "输入的选项有误，请重新输入。"
	print "\n"
	return telcom

def readServiceProvider():
	print "请选择接入平台："
	print "1.欧耶平台"
	print "2.九城平台"
	print "3.掌世界平台"
	print "4.鼎亿平台"
	print "5.盛翼平台"
	print "6.杭州视线"
	sp = serviceProviders[0]
	while True:
		text=raw_input("请输入[默认:1]：")
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
			print "输入的选项有误，请重新输入。"
	print "\n"
	return sp

telcom = readTelcomOperator()
sp = readServiceProvider()
props = " -Ptelcom="+telcom + " -Psp="+sp+" "
gradleCmd = "gradle "+props+paramStr()
os.system(gradleCmd)