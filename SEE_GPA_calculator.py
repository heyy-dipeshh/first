print("you can calculate your result of SEE exam")
print()
print()
# this is for theory credit hour 
eng_ch_th=A=3.75
nep_ch_th=B=3.75
math_ch_th=C=3.75
sci_ch_th=D=3.75
soc_ch_th=E=3
omath_ch_th=F=3
acc_ch_th=G=3
#this is for pratical credit hour
eng_ch_pr=a=1.25
nep_ch_pr=b=1.25
math_ch_pr=c=1.25
sci_ch_pr=d=1.25
soc_ch_pr=e=1
omath_ch_pr=f=1
acc_ch_pr=g=1
# This is total credit hour 
eng_ch=Aa=5
nep_ch=Bb=5
math_ch=Cc=5
sci_ch=Dd=5
soc_ch=Ee=4
omath_ch=Ff=4
acc_ch=Gg=4
print("for your information")
print()
print("67.5 to 75 = 4.0")
print("60 to 67.5 = 3.6")
print("52.5 to 60 = 3.2")
print("45 to 52.5 = 2.8")
print("37.5 to 45 = 2.4")
print("30 to 37.5 = 2.0")
print("26.5 to 30 = 1.6")
print("Below 26.25 = NG")
print()
print()
print()
print()
print("Now enter your expected marks in GPA. you can see the number to GPA in upper part")
print()
print("we assume that your pratical marks is 4 GPA. almost every school give pratical 4 GPA. if you think you wont get pratical 4 gpa then your result might be different")
print()
a1=float(input("enter the marks of english in GPA: "))
a2=float(input("enter the marks of nepali in GPA: "))
a3=float(input("enter the marks of math in GPA: "))
a4=float(input("enter the marks of science in GPA: "))
a5=float(input("enter the marks of social in GPA: "))
a6=float(input("enter the marks of o math or ecomoics in GPA: "))
print()
print("if you are from computer then first you have to convert your marks into 75 and then check your GPA from upper table to convert do this. marks*75/50 to convert in 75 from 50")
print("if you are from account then no problem ")
print()
a7=float(input("enter the marks of account or computer in GPA: "))
print()
print()
# this is the pratical marks add
p=32 #for upper part add
l=32 #for lower divide
eng=(3.75*a1+5)/5
nep=(3.75*a2+5)/5
math=(3.75*a3+5)/5
sci=(3.75*a4+5)/5
soc=(3*a5+4)/4
omath=(3*a6+4)/4
acc=(3*a7+4)/4
print()
print("hence this is your result of each subject: ")
print()
print("english:", eng)
print("Nepali:", nep)
print("math:", math)
print("science:", sci)
print("social", soc)
print("omath or eco", omath)
print("computer or account", acc)
total=(eng+nep+math+sci+soc+omath+acc)/7
print()
print()
print("Your total GPA is:", total)
print()
print()
if(total>3.6):
  print("you got A+")
elif(total>3.2 and total==3.6):
  print("you got A")
elif(total>2.8 and total==3.2):
  print("you got B+")
elif(total>2.4 and total==2.8):
  print("you got B")
elif(total>2 and total==2.4):
  print("you got C+")
elif(total>1.6 and total==2):
  print("you got D+")
elif(total<1.6):
  print("you got NG")
else:
	print("invalid input")

print("beautiful girls can contact me. instagram: dipeshbhattarai01 ")
