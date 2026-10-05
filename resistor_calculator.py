#四环电阻计算器
color_dict = {
    "黑": 0, "棕": 1, "红": 2, "橙": 3, "黄": 4,
    "绿": 5, "蓝": 6, "紫": 7, "灰": 8, "白": 9
}
# 倍率字典 (第三环)
multiplier_dict = {
    "黑": 1, "棕": 10, "红": 100, "橙": 1000, "黄": 10000,
    "绿": 100000, "蓝": 1000000, "紫": 10000000, 
    "金": 0.1, "银": 0.01
}
def user_input():
    while True:
        user_str = input("请输入四环电阻的前三环：",)
        user_str = user_str.replace(" ","").replace(",","，")
        try:
            first,second,third = user_str.split("，")
            num1 = color_dict[first]
            num2 = color_dict[second]
            num3 = multiplier_dict[third]
            return num1,num2,num3
        except ValueError:
            print("你输入的格式不对，请输入三个颜色并用，隔开。")
        except KeyError as e:
            print(f"找不到你输入的颜色{e}，请重新输入。")

def main():
    num1,num2,num3 = user_input()
    result = (num1*10+num2)*num3
    if result >= 1000 and result < 1000000:
        result /= 1000
        print(f"四环电阻的阻值为{result}kΩ")
    elif result >= 1000000:
        result /= 1000000
        print(f"四环电阻的阻值为{result}MΩ")
    else:
        print(f"四环电阻的阻值为{result}Ω")
if __name__ == '__name__':
    main()
