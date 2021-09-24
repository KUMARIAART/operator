"python program to covert the days into years,weeks,and days."

print("enter the day::")
day,year,week=int(input()),None,None
year=(int)(day/365)
week=(int)(day%365)/7
day=(int)(day-((year*365)+(week)))
print(year,"year,",week,"week,and",day,"days")

