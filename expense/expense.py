import sqlite3 as db
import datetime
from datetime import date,datetime


def init():
	conn=db.connect("expense.db")
	cur=conn.cursor()
	sql='''create table if not exists expense (name string,amount number,date date,day string)'''
	cur.execute(sql)
	conn.commit()

def show():
	conn=db.connect("expense.db")
	cur=conn.cursor()
	print("\nDetails:")
	sql='''
	select * from expense
	'''
	cur.execute(sql)
	print(cur.fetchall())
	conn.commit()
	conn.close()


def insert(name,cost,date,day):
	init()
	conn=db.connect("expense.db")
	cur=conn.cursor()
	sql='''
	insert into expense values(
		'{}',
		{},
		'{}',
		'{}'
	)
	'''.format(name,cost,date,day)
	cur.execute(sql)
	conn.commit()


def daily(date):
	conn=db.connect("expense.db")
	cur=conn.cursor()
	if(date):
		sql='''
		select sum(amount) from expense where date='{}'
		'''.format(date)
		cur.execute(sql)
		if(cur!=None):
			print("Daily Expense of provided Day is:",*cur.fetchall()[0])	
	conn.commit()
	conn.close()


def weekly(year,month,noofweek):
	conn=db.connect("expense.db")
	cur=conn.cursor()
	if(month<=9):
		month="{0:0=2d}".format(month)
	else:
		month=str(month)
	year=str(year)
	week=1
	while(week<=noofweek):
		balance=0
		if(week==1):
			for i in range(1,8):
				date=year + "-" + month + "-" + "{0:0=2d}".format(i)
				sql='''
				select sum(amount) from expense where date='{}'
				'''.format(date)
				cur.execute(sql)
				s=cur.fetchall()[0][0]
				if(s!=None):
					balance+=int(s)	
			print("Week 1 Expense:",balance)
			week+=1
		elif(week==2):
			for i in range(8,15):
				date=year + "-" + month + "-" + "{0:0=2d}".format(i)
				sql='''
				select sum(amount) from expense where date='{}'
				'''.format(date)
				cur.execute(sql)
				s=cur.fetchall()[0][0]
				if(s!=None):
					balance+=int(s)		
			print("Week 2 Expense:",balance)
			week+=1
		elif(week==3):
			for i in range(15,22):
				date=year + "-" + month + "-" + "{0:0=2d}".format(i)
				sql='''
				select sum(amount) from expense where date='{}'
				'''.format(date)
				cur.execute(sql)
				s=cur.fetchall()[0][0]
				if(s!=None):
					balance+=int(s)		
			print("Week 3 Expense:",balance)
			week+=1
		elif(week==4):
			for i in range(22,29):
				date=year + "-" + month + "-" + "{0:0=2d}".format(i)
				sql='''
				select sum(amount) from expense where date='{}'
				'''.format(date)
				cur.execute(sql)
				s=cur.fetchall()[0][0]
				if(s!=None):
					balance+=int(s)	
			print("Week 4 Expense:",balance)
			week+=1
		elif(week==5):
			for i in range(29,32):
				date=year + "-" + month + "-" + "{0:0=2d}".format(i)
				sql='''
				select sum(amount) from expense where date='{}'
				'''.format(date)
				cur.execute(sql)
				s=cur.fetchall()[0][0]
				if(s!=None):
					balance+=int(s)		
			print("Week 5 Expense:",balance)
			week+=1
		else:
			print("Invalid No.of weeks")
	conn.commit()
	conn.close()


def week_limit(cost,date,week1,week2,week3,week4,week5):
	conn=db.connect("expense.db")
	cur=conn.cursor()
	w1=['01','02','03','04','05','06','07']
	w2=['08','09','10','11','12','13','14']
	w3=['15','16','17','18','19','20','21']
	w4=['22','23','24','25','26','27','28']
	w5=['29','30','31']
	d=date.day
	if(str(d)  in w1):
		balance=0
		for i in range(1,8):
			sql='''
			select sum(amount) from expense where date='{}'
			'''.format(date)
			cur.execute(sql)
			s=cur.fetchall()[0][0]
			if(s!=None):
				balance+=int(s)	
		if(balance>week1):
			print("You Have exceeded the max expense of this week")
			return 0
		else:
			return 1
	elif(str(d) in w2):
		balance=0
		for i in range(8,15):
			sql='''
			select sum(amount) from expense where date='{}'
			'''.format(date)
			cur.execute(sql)
			s=cur.fetchall()[0][0]
			if(s!=None):
				balance+=int(s)	
		if(balance>week1):
			print("You Have exceeded the max expense of this week")
			return 0
		else:
			return 1
	elif(str(d) in w3):
		balance=0
		for i in range(15,22):
			sql='''
			select sum(amount) from expense where date='{}'
			'''.format(date)
			cur.execute(sql)
			s=cur.fetchall()[0][0]
			if(s!=None):
				balance+=int(s)	
		if(balance>week1):
			print("You Have exceeded the max expense of this week")
			return 0
		else:
			return 1
	elif(str(d) in w4):
		balance=0
		for i in range(22,28):
			sql='''
			select sum(amount) from expense where date='{}'
			'''.format(date)
			cur.execute(sql)
			s=cur.fetchall()[0][0]
			if(s!=None):
				balance+=int(s)	
		if(balance>week1):
			print("You Have exceeded the max expense of this week")
			return 0
		else:
			return 1
	elif(str(d) in w3):
		balance=0
		for i in range(28,32):
			sql='''
			select sum(amount) from expense where date='{}'
			'''.format(date)
			cur.execute(sql)
			s=cur.fetchall()[0][0]
			if(s!=None):
				balance+=int(s)	
		if(balance>week1):
			print("You Have exceeded the max expense of this week")
			return 0
		else:
			return 1
	conn.commit()
	conn.close()
		

#Application Starts from here
print("Let's Track Your Expenses")
print("Set Your Weekly max Expenditure")
week1=int(input("Week1:"))
week2=int(input("Week2:"))
week3=int(input("Week3:"))
week4=int(input("Week4:"))
week5=int(input("Week5:"))
print()

while(1):
	
	option=int(input("\nEnter Your choice\n1.Add Expense\n2.Details of expense\n3.Daily Expense\n4.Weekly Expense\n5.Exit\n"))
	if(option==1):
		name_of_product = input("\nEnter the Name of Product:")
		cost = int(input("Cost of the Product:"))
		temp=date.today()
		if(week_limit(cost,temp,week1,week2,week3,week4,week5)==0):
			choice=input("Do You want to continue enter yes/no:")
			if(choice=='yes'):
				insert(name_of_product,cost,temp,temp.strftime("%A"))
			else:
				print("Try next week")
	elif(option==2):
		show()
	elif(option==3):
		date=input("\nEnter date of which you want total expense in format(year-month-date):")
		daily(date)
	elif(option==4):
		print("\nEnter year & month of which you want weekly expense")
		y=int(input("Year:"))
		months=["january","february","march","april","may","june","july","august","setemper","october","november","december"]
		month=input("Month:").lower()
		m=months.index(month)
		w=int(input("Enter Expense of how many Weeks you want:"))
		weekly(y,m+1,w)
	elif(option==5):
		quit()
		
	else:
		print("\nInvalid Option")




























