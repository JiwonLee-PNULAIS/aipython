# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KH_3gdXvFuj3s7_a3wRi9Egw97ZdzmpK
"""

a=int(input("정수를 입력하세요.==> "))
if a>5:
  print("a는 5보다 큽니다.")
elif a<=5:
  print("a는 5보다 작거나 같습니다.")
print("프로그램 종료.")

"""A에 할당된 값의 짝수 홀수 여부를 알려주는 프로그램"""

a=int(input("숫자를 입력하세요.==> "))
b=a%2
if b==1:
  print("a는 홀수입니다.")
elif b!=1:
  print("a는 짝수입니다.")
print("프로그램 종료.")

a=int(input("정수를 입력하세요.==> "))
if a>5:
  print("a는 5보다 큽니다.")
elif a<5:
  print("a는 5보다 작습니다.")
else:
  print("a는 5입니다.")
print("프로그램 종료.")

a=10
b=5

if a>5:
  if b<10:
    print("a는 5보다 크고 b는 10보다 작습니다.")

a=10
b=5

if a>5 and b<10:
    print("a는 5보다 크고 b는 10보다 작습니다.")

#입력된 점수의 등급 매기기
score=int(input("점수를 입력하세요.==> "))

if score>100:
  print("잘못된 입력입니다. 점수를 다시 확인해 주십시오.")

elif score>=90:
  grade="A"
  print("당신의 등급은 {}입니다.".format(grade))

elif score>=80:
  grade="B"
  print("당신의 등급은 {}입니다.".format(grade))

elif score>=70:
  grade="C"
  print("당신의 등급은 {}입니다.".format(grade))

elif score>=60:
  grade="D"
  print("당신의 등급은 {}입니다.".format(grade))

else:
  grade="F"
  print("당신의 등급은 {}입니다.".format(grade))

print("프로그램 종료.")

#반복문
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tot=0
for i in a:
  print(i)
  tot+=i
print(tot)

for i in range(1,11):
  print(i)

for i in range(1, 101, 2):
  print(i)

for i in range(2, 101, 2):
  print(i)

for i in range(5):
  if i%2==0:
   break
  print(i)

tot1=0
tot2=0

for i in range(1, 11):
  if i%2==1:
    tot1+=i
  elif i%2==0:
    tot2+=i

print("1부터 10까지의 모든 홀수의 합은 {}, 모든 짝수의 합은 {}입니다.".format(tot1, tot2))

#하나의 숫자 n를 입력 받아서 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n=int(input())
tot=0

for i in range(1, n+1):
  tot+=i

print(tot)