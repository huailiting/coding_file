#coding=utf-8
import sys
import json
def start():
	i=raw_input("input your instructions:")
	if int(i)==1:
		addinfo()
	if int(i)==2:
		searchinfo()
	if int(i)==3:
		deleteinfo()
	if int(i)==4:
		editinfo()
def addinfo():
	print"input your infomation:"
	name=raw_input("input your name:")
	phoneno=raw_input("input your phoneno:")
	address=raw_input("input your address:")
	email=raw_input("input your email:")
	info={}
	info['Name']=name
	info['Phoneno']=phoneno
	info['Address']=address
	info['email']=email
	store(info)
def store(filename):
	with open("filename.json",'a+') as f:
		f.write(json.dumps(filename))
		f.write('\n')
	print json.dumps(filename,ensure_ascii = False, encoding = "gb2312", indent =0)
	f.close()
def searchinfo():
	s_name=raw_input("input the name:")
	sf=open('filename.json','r')
	for line in sf:
		line=line.strip()
		if not line:
			continue
		s_record=json.loads(line,'gb2312')
		if s_record.has_key('Name')and s_record['Name']==s_name:
			print line
	sf.close()
def deleteinfo():
	d_name=raw_input("input the name:")
	ff=open('filename.json','r+')
	lines=ff.readlines()
	ff.close()
	wf=open('filename.json','w')
	print "2222"
	for d_line in lines:
		d_line=d_line.strip()
		if not d_line:
			continue
		records=json.loads(d_line,'gb2312')
		if records.has_key('Name')and records['Name']==d_name:
			print "5555"
		else:
			wf.write(d_line)
	wf.close()
	print "delete ok"
def editinfo():
	e_name=raw_input("input the name:")
	en_name=raw_input("input the new name:")
	en_phoneno=raw_input("input the new phoneno:")
	en_address=raw_input("input the new address:")
	en_email=raw_input("input the new email:")
	print"2133333333333"
	fff=open('filename.json','w+')
	print"2133333333333"
	for e_line in fff:
		print"2133333333333"
		e_line=e_line.strip()
		if not e_line:
			continue
		e_record=json.loads(e_line,'gb2312')
		if e_record.has_key('Name')and e_record['Name']==e_name:
			e_record['Name']=en_name
			e_record['Phoneno']=en_phoneno
			e_record['Address']=en_address
			e_record['email']=en_email
			f.write(json.dumps(e_record))
			print e_record
			print "test"
	fff.close()
	print "edit ok"
start()