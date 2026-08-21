#변수
#동적 타이핑 언어
a=2
b=3
print(a,end="")
print(b)
print(a,b,sep=",")

#a=2,b=3
a=2,b
print(a)
print(type(a))

a=2; b=3
print(a,b)

x=y=z=0

a,b=2,3
print(a,b)

#값 스왑
temp=a
a=b
b=temp
print(a,b)

a,b=b,a
print(a,b)

#변수명 규칙 (=c)
#문자, 숫자, 언더바만 ㄱㄴ
#숫자로 시작 x
#대소문자 구분
#예약어 x
name2="pororo"
_name="pororo"
#class="test"
#name!="test"
이름="뽀로로"
print(이름)

student_name="crong"
studentName="crong"
MAX_COUNT=100
