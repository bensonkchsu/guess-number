import random
import xml.etree.ElementTree as ET

def load_settings(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def guess_the_number(x1, x2, max_attempts):
    target_number = random.randint(x1, x2)
    attempts = 0

    print(f"猜一個在 {x1} 到 {x2} 之間的數字！")

    while attempts < max_attempts:
        guess = int(input("你的猜測是："))

        attempts += 1

        if guess == target_number:
            print(f"恭喜你！你猜對了，目標數字是 {target_number}")
            break
        elif guess < target_number:
            print("太低了，再猜一次。")
        else:
            print("太高了，再猜一次。")

        remaining_attempts = max_attempts - attempts
        print(f"你還有 {remaining_attempts} 次猜測機會。")

    if attempts == max_attempts:
        print(f"遊戲結束，你已用完所有猜測機會。目標數字是 {target_number}。")

# 讀取設定
file_path = 'setting.xml'
x1, x2, max_attempts = load_settings(file_path)

# 開始遊戲
guess_the_number(x1, x2, max_attempts)