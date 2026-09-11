# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

langs.append("go")  # 끝에 추가
print(langs)

langs.insert(2, "c#")  # 인덱스 2에 "c#" 추가
print(langs)

langs[3] = "javascript"  # 인덱스 3을 "javascript"로 변경
print(langs)

langs.remove("c++")  # "c++" 삭제 (첫번째 데이터만 삭제)
print(langs)

langs.pop(1)  # 인덱스 1 삭제
print(langs)

langs.pop()  # 인덱스 생략 시 마지막 항목 삭제
print(langs)

print(langs.index("python"))  # "python" 인덱스 찾기

langs.reverse()  # 리스트 순서를 거꾸로 뒤집기
print(langs)

langs.sort()  # 오름차순 정렬
print(langs)

langs.sort()  # 내림차순 정렬
print(langs)

langs.clear()  # 모든 item 삭제
print(langs)

# 리스트 복사
ori = [1, 2, 3]

result = ori.copy()
print(result)
result.append(10)
print(ori, result)


# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]

result2 = ori.copy()
result2[0].append(100)

print(ori, result2)

# 깊은 복사를 하려면?
import copy

result2 = copy.deepcopy(ori)
result2[0].append(1000)
print(ori, result2)


# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1])  # x 출력하기
print(nested_list)  # b 출력하기
print(nested_list)  # 2 출력하기

# 리스트 언패킹
num = [1, 2, 3, 4]

print(*num)

a, b, c, d = num
print(a, b, c, d)

a, *b, c = num
print(a, b, c)

num2 = [5, 6]
print(num + num2)

print([*num, *num2])


# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어", "과학"]
scores = [80, 90, 95]

print(zip(subjects, scores))
print(a, b, c)

for subject, score in zip(subjects, scores):
    print(f"{subject}:{score}점")

# x자체를 원소 하나로
print([zip(subjects, scores)])

# x를 순회해서 리스트에 넣
print(list(zip(subjects, scores)))

print(["python"])
print(list("python"))

# ===========================================================
#  List Comprehension
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
result = []
for i in range(10):
    result.append((i + 1) * (i + 1))
print(result)


result = [x**2 for x in range(1, 11)]
print(result)

# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)
result = [x**2 for x in range(1, 11) if x % 2 == 0]
print(result)

# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기
result = ["짝" if x % 2 == 0 else "홀" for x in range(1, 11)]
print(result)

# 각 이름의 길이로 이루어진 리스트 만들기
names = ["pororo", "crong", "poby", "eddy"]
result = [len(name1) for name1 in names]
print(result)

# 길이가 5 이상인 이름만 뽑기
result = [n for n in names if len(n) >= 5]
print(result)

# 중첩 for문도 가능
# x=012
# y=012
# x*y
result = [x * y for x in range(3) for y in range(3)]
print(result)

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
scores = [85, 42, 73, 55, 90, 68, 35, 100]

result = [n for n in scores if n >= 60]
print(result)  # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
result = ["합격" if n <= 60 else "불합격" for n in scores]
print(
    result
)  # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
result = [i for i in range(1,101) if not i%3 or not i%5]
result = [i for i in range(1, 101) if i % 3 == 0 or i % 5 == 0]
print(sum(result))  # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
words = ["apple", "banana", "kiwi", "mango"]

result = [n for n in words if "n" in n]
result=[w for w in words]
print(result)  # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
scores = [
    [91, 81, 71],  # 학생 1
    [100, 90, 80],  # 학생 2
    [80, 70, 60],  # 학생 3
]


std1=scores[0]
std2=scores[1]
std3=scores[2]

result=[sum(score)/len(score) for score in zip(std1,std2,std3)]
print(result)
result=[round(sum(score)/len(score),2) for score in zip(std1,std2,std3)]
print(result)
result = [sum(scores[i])/3 for i in range(3)]
print(result)  # ✅ [80.0, 90.0, 70.0]


print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))