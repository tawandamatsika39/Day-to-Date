day=int(input("Enter day number (e.g 20): "))
month=int(input("Enter month number (i.e January= 1): "))
year=int(input ("Enter year (e.g 1995): "))

toDay={
	 
	 0:"Saturday",
	 1:"Sunday",
	 2:"Monday",
	 3:"Tuesday",
	 4:"Wednesday",
	 5:"Thursday",
	 6:"Friday"
}

if(month==1):
	month=13
	year=year-1
if(month==2):
	month=14
	year=year-1
else:
	month=month

k=year%100
j=year//100

result=day + 13*(month + 1)//5 + k + k//4 + j//4 + 5*j
result=result%7

print(toDay[result])

