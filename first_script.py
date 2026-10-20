name = input("请输入你的名字：")
a = int(input("请输入你的年龄："))
b = float(input("请输入你准备每天花多少钱："))

print(f"你好，{name}")

if a <18 and b >100:
    print(f"都没满18岁啦~ 但是也不能花这么多钱")
elif a< 18:
    print(f"还没成年呢花这么多就好啦")
elif b >100:
    print(f"花这么多干什么 你不用养家吗")
else:
    print(f"已经成年，而且花销控制得不错")

print(f"你今年 {a} 岁")
print(f"你每天的预算是 {b} 元")

if b <=30:
    print(f"每日花销正常")
elif  b <= 100:
    print(f"有点超标")
else:
    print(f"比较超标")



money = b * 30

print(f"按照每天 {b} 元计算，一个月预算是 {money} 元")
