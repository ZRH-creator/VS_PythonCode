import random

print("--- 欢迎来到猜数字小游戏 ---")
# 随机生成一个 0 到 20 之间的数字
secret_number = random.randint(0, 20)
guess = None

while guess != secret_number:
    # 获取用户输入
    user_input = input("请输入你猜的数字 (0-20): ")
    
    # 简单的错误处理
    if not user_input.isdigit():
        print("请输入有效的数字！")
        continue
        
    guess = int(user_input)

    if guess < secret_number:
        print("太小了，再试一次！")
    elif guess > secret_number:
        print("太大了，再试一次！")
    else:
        print(f"恭喜你！答案确实是 {secret_number}！")

print("游戏结束。")