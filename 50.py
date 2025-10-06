#۵۰ پروژه
#1. شمارش تعداد حروف و اعداد در یک متن
text = input("یک متن وارد کنید: ")

letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)

print("تعداد حروف:", letters)
print("تعداد اعداد:", digits)

# #2. جدول ضرب یک عدد
# n = int(input("یک عدد وارد کنید: "))
# for i in range(1, 11):
#     print(f"{n} × {i} = {n * i}")
# #3. معکوس کردن رشته
# text = input("یک متن وارد کنید: ")
# print("معکوس متن:", text[::-1])

# #4. تبدیل رشته به بزرگ و کوچک
# text = input("یک متن وارد کنید: ")
# print("حروف بزرگ:", text.upper())
# print("حروف کوچک:", text.lower())
# #5. تولید رمز عبور تصادفی
# import random
# import string

# length = int(input("طول رمز عبور را وارد کنید: "))
# chars = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(chars) for _ in range(length))

# print("رمز عبور:", password)

# #🔹 پروژه‌های ۶ تا ۱۰
# #6. محاسبه مجموع اعداد تا n
# n = int(input("یک عدد وارد کنید: "))
# total = sum(range(1, n + 1))
# print("مجموع از 1 تا", n, "=", total)
# #7. بررسی زوج یا فرد بودن
# n = int(input("یک عدد وارد کنید: "))
# if n % 2 == 0:
#     print("عدد زوج است")
# else:
#     print("عدد فرد است")

# #8. پیدا کردن بزرگترین عدد در لیست
# numbers = [12, 45, 7, 89, 23, 67]
# print("لیست اعداد:", numbers)
# print("بزرگترین عدد:", max(numbers))

# #9. تولید دنباله فیبوناچی
# n = int(input("تعداد جملات فیبوناچی را وارد کنید: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# #10. شمارش کلمات یک جمله
# sentence = input("یک جمله وارد کنید: ")
# words = sentence.split()
# print("تعداد کلمات:", len(words))

# #🔹 پروژه‌های ۱۱ تا ۲۰
# #11. حدس عدد (Guessing Game)
# import random
# secret = random.randint(1, 10)
# guess = int(input("یک عدد بین 1 تا 10 حدس بزن: "))
# if guess == secret:
#     print("آفرین! درست حدس زدی 🎉")
# else:
#     print("اشتباه شد! عدد درست:", secret)

# #12. شمارش حروف یک رشته
# text = input("یک متن وارد کنید: ")
# print("تعداد کاراکترها:", len(text))

# #13. چاپ جدول ضرب
# n = int(input("عدد را وارد کنید: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# #14. چک کردن اول بودن عدد
# n = int(input("یک عدد وارد کنید: "))
# is_prime = True
# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("عدد اول است")
# else:
#     print("عدد اول نیست")

# #15. محاسبه فاکتوریل	

# n = int(input("یک عدد وارد کنید: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print("فاکتوریل", n, "=", fact)

# #16. معکوس کردن رشته
# text = input("یک متن وارد کنید: ")
# print("معکوس متن:", text[::-1])
# #17. یافتن کوچکترین عدد در لیست
# numbers = [34, 7, 23, 89, 2, 56]
# print("لیست اعداد:", numbers)
# print("کوچکترین عدد:", min(numbers))
# #18. شمارش تعداد تکرار کاراکتر
# text = input("یک متن وارد کنید: ")
# char = input("کدام کاراکتر را می‌خواهید بشمارید؟ ")
# print("تعداد", char, "در متن:", text.count(char))

# #19. محاسبه معدل
# grades = []
# for i in range(5):
#     grade = float(input(f"نمره {i+1} را وارد کنید: "))
#     grades.append(grade)

# average = sum(grades) / len(grades)
# print("معدل:", average)

# #20. بازی پرتاب تاس
# import random
# dice = random.randint(1, 6)
# print("🎲 عدد روی تاس:", dice)


# #🔹 پروژه‌های ۲۱ تا ۳۰
# #21. محاسبه محیط و مساحت دایره
# import math
# r = float(input("شعاع دایره را وارد کنید: "))
# area = math.pi * r**2
# perimeter = 2 * math.pi * r
# print("مساحت:", area)
# print("محیط:", perimeter)
# #22. محاسبه معدل وزنی
# grades = [18, 15, 19]
# weights = [3, 2, 4]
# weighted_avg = sum([g*w for g, w in zip(grades, weights)]) / sum(weights)
# print("معدل وزنی:", weighted_avg)
# #23. تبدیل دما (سانتیگراد ↔ فارنهایت)

# c = float(input("دما به سانتیگراد: "))
# f = (c * 9/5) + 32
# print("به فارنهایت:", f)


# #24. شمارش اعداد زوج و فرد در لیست
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = len([n for n in numbers if n % 2 == 0])
# odd = len(numbers) - even
# print("تعداد زوج:", even)
# print("تعداد فرد:", odd)

# #25. مجموع اعداد زوج تا n
# n = int(input("یک عدد وارد کنید: "))
# even_sum = sum([i for i in range(1, n+1) if i % 2 == 0])
# print("مجموع اعداد زوج تا", n, "=", even_sum)

# #26. بازی سنگ، کاغذ، قیچی
# import random
# choices = ["سنگ", "کاغذ", "قیچی"]
# user = input("سنگ، کاغذ یا قیچی؟ ")
# computer = random.choice(choices)
# print("کامپیوتر:", computer)

# if user == computer:
#     print("مساوی شد!")
# elif (user == "سنگ" and computer == "قیچی") or \
#      (user == "کاغذ" and computer == "سنگ") or \
#      (user == "قیچی" and computer == "کاغذ"):
#     print("بردی! 🎉")
# else:
#     print("باختی 😢")

# #27. تبدیل لیست به رشته
# lst = ["سلام", "به", "پایتون"]
# sentence = " ".join(lst)
# print(sentence)

# #28. شمارش حروف بزرگ و کوچک
# text = input("یک متن وارد کنید: ")
# upper = sum(1 for c in text if c.isupper())
# lower = sum(1 for c in text if c.islower())
# print("حروف بزرگ:", upper)
# print("حروف کوچک:", lower)

# #29. محاسبه توان

# base = int(input("پایه را وارد کنید: "))
# exp = int(input("توان را وارد کنید: "))
# print("نتیجه:", base ** exp)


# #30. محاسبه میانگین لیست
# numbers = [12, 45, 67, 89, 23]
# avg = sum(numbers) / len(numbers)
# print("میانگین لیست:", avg)
# #🔹 پروژه‌های ۳۱ تا ۴۰
# #31. شمارش تعداد کلمات در یک متن
# text = input("یک متن وارد کنید: ")
# words = text.split()
# print("تعداد کلمات:", len(words))


# #32. برعکس کردن یک لیست
# lst = [1, 2, 3, 4, 5]
# print("لیست برعکس:", lst[::-1])

# # 33. پیدا کردن بیشترین عدد در لیست
# numbers = [12, 45, 7, 89, 23]
# print("بیشترین عدد:", max(numbers))

	
# # 34. پیدا کردن کمترین عدد در لیست
# numbers = [12, 45, 7, 89, 23]
# print("کمترین عدد:", min(numbers))

# # 35. چاپ جدول ضرب
# n = int(input("عدد را وارد کنید: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)
# # 36. تشخیص عدد اول
# num = int(input("عدد را وارد کنید: "))
# if num > 1 and all(num % i != 0 for i in range(2, num)):
#     print("عدد اول است")
# else:
#     print("عدد اول نیست")


# # 37. محاسبه میانگین نمرات کاربر
# n = int(input("تعداد نمرات: "))
# grades = [float(input(f"نمره {i+1}: ")) for i in range(n)]
# print("میانگین:", sum(grades)/len(grades))


# # 38. چاپ فیبوناچی تا n
# n = int(input("تعداد جملات فیبوناچی: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b




# # 39. محاسبه مساحت مثلث (قاعده × ارتفاع ÷ ۲)
# base = float(input("قاعده: "))
# height = float(input("ارتفاع: "))
# area = 0.5 * base * height
# print("مساحت مثلث:", area)

# # 40. ساخت لیست از اعداد زوج بین ۱ تا ۱۰۰
# evens = [i for i in range(1, 101) if i % 2 == 0]
# print(evens)
# #🔹 پروژه‌های ۴۱ تا ۵۰
# # 41. تبدیل لیست به مجموعه (حذف عناصر تکراری)
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique = set(lst)
# print("لیست بدون تکرار:", unique)


# # 42. شمارش تعداد وقوع یک کلمه در متن
# text = "python is fun and python is powerful"
# word = "python"
# print(f"کلمه '{word}' {text.count(word)} بار تکرار شده است.")

# # 43. چاپ اعداد فرد از ۱ تا ۵۰
# for i in range(1, 51, 2):
#     print(i, end=" ")


# # 44. ساخت یک ماشین حساب ساده
# a = float(input("عدد اول: "))
# b = float(input("عدد دوم: "))
# op = input("عملگر (+, -, *, /): ")

# if op == "+":
#     print("نتیجه:", a + b)
# elif op == "-":
#     print("نتیجه:", a - b)
# elif op == "*":
#     print("نتیجه:", a * b)
# elif op == "/":
#     print("نتیجه:", a / b if b != 0 else "تقسیم بر صفر مجاز نیست")
# else:
#     print("عملگر نامعتبر")

# # 45. چاپ مثلث ستاره‌ای
# n = int(input("تعداد سطرها: "))
# for i in range(1, n + 1):
#     print("*" * i)
# # 46. حدس عدد (بازی ساده)

# import random
# number = random.randint(1, 10)
# guess = int(input("یک عدد بین 1 تا 10 حدس بزن: "))

# if guess == number:
#     print("آفرین! درست حدس زدی 🎉")
# else:
#     print(f"اشتباه بود! عدد درست {number} بود.")


# # 47. جمع ارقام یک عدد
# num = int(input("یک عدد وارد کنید: "))
# total = sum(int(digit) for digit in str(num))
# print("مجموع ارقام:", total)

# # 48. معکوس کردن یک رشته
# text = input("یک متن وارد کنید: ")
# print("معکوس:", text[::-1])
# # 49. بررسی رشته‌ی پالیندروم (مثل: "madam")
# text = input("یک متن وارد کنید: ")
# if text == text[::-1]:
#     print("پالیندروم است ✅")
# else:
#     print("پالیندروم نیست ❌")

# # 50. شمارش حروف هر کلمه در یک جمله
# sentence = input("یک جمله وارد کنید: ").split()
# for word in sentence:
#     print(word, ":", len(word))

