#for 문

#for (int i=0;i<10;i++)
#for i in iterable 객체:

for i in range(5):
    print(i,end=" ")
print()

a=range(5)
print(a.start, a.stop, a.step)

#1~5
for i in range(1,6):
    print(i,end=" ")
print()

#1~10, 2씩 띄어서
for i in range(1,6,2):
    print(i,end=" ")
print()

#5,4,3,2,1
for i in range(5,0,-1):
    print(i,end=" ")
print()

#1~10힙
tot=0
for i in range(1,11):
    tot+=i
print(f"tot={tot}")

print(sum(range(1,11)))

s="😊😊😊😊👍👍👍🤣"

for c in s:
    print(c,end=" ")
print()

print(len(s))

#구구단 출력
#2*1=2 2*2=4
#..
#9*1=9
for i in range(1,10,1):
    for j in range(1,10,1):
        print(f"{i}*{j}={i*j:<5d}",end="")
    print()
else:
    print("End")
