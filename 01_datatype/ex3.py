#불리언
#t or f

a=True
print(a,type(a))

print(1<0)
print(1>0)
print(1==0)
print(1!=0)

print("apple">"apple")

#bool()
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool([10]))
print(bool([]))

#none 자료형
a=None
print(a,type(a))
print(bool(a))

if a is None:
    print("값이 없습니다")
    