"write a python program to enter marks of five subject and calculate total,average and percentage."

english=int(input("enter english marks:"))
maths=int(input("enter  maths marks:"))
computer=int(input("enter computer marks:"))
hindi=int(input("enter hindi marks:"))
science=int(input("enter science marks"))
total=english+maths+computer+hindi+science
average=total/5
percentage=(total/500)*100
print("total marks",total)
print("average marks",average)
print("percentage",percentage)
