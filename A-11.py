"""
身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリ実装
参考となるWebアプリ https://keisan.casio.jp/exec/system/1161228732
小数点第2位まで表示する

"""


class BMI:
    pass


bmi = BMI()
bmi.height = int(input("身長、入力して-(cm):")) / 100
bmi.weight = int(input("体重、入力して-(kg):"))
print(bmi.height)
print(bmi.weight)
