"write a python program to enter P,T,R and calculate simple interest and coumpond interest."

principal=int(input("enter the number:"))
time=int(input("enter the time:"))
rate=int(input("enter the rate:"))
simple_intrest=(principal*time*rate)/100
compound_intrest=principal*(1+rate/100)**time-1
print("simple intrest is",simple_intrest)
print("compound intrest is" ,compound_intrest)

