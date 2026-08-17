# (((((الفصل الأول)))))

# dmopc15c7p2
# line = input()
# total_words = line.count(" ") + 1
# print(total_words)


# حل تاني في حالة لو أن المسافات غير منتظمة
# line = input()
# total_words = len(line.split())
# print(total_words)

####################################################


# problem dmopc14c5p1

# PI = 3.141592653589793

# radius = int(input())
# height = int(input())

# volume = (PI * radius ** 2 * height) / 3

# print(volume)


#############################

# Chapter Exercises page 57

# 1. DMOJ problem wc16c1j1, A Spooky Season

# s = int(input("enter number : "))

# هنا حلقة بتاخد وقت و مساحة أكبر
# o_string = ""
# for i in range (s):
#     o_string += "o"
# print (f"sp{o_string}ky")


# # #---------  حل آخر أفضل -------

# هنا رغم انه بيضرب مباشرة لكن المعالج بيخزن وبعدين يروح يجيب القيمة المخزنة علشان يطبعها 
# s = int(input()) 
# o_string = "o" * s
# print(f"sp{o_string}ky")

# --------   الحلول الأسرع ----------
# هنا بيضرب و يجمع النص و بيخزنه في نفس الوقت وبعدين يطبع فبالتالي أسرع نص الواقت تقريبا
# S = int(input())

# level = 'sp' + 'o' * S + 'ky'

# print(level)


# # ------- 

# num_o = int(input())
# print('sp' + ('o' * num_o) + 'ky')



# 2. DMOJ problem wc15c2j1, A New Hope

# n = int(input())
# print ("A long time ago in a galaxy " + (n - 1) * "far, " + "far away...")
    


# 3. DMOJ problem ccc13j1, Next in Line

# y = int(input())
# m = int(input())

# b = m + (m - y)

# print(b)



#  4. DMOJ problem wc17c1j2, How’s the Weather? (Be careful with thedirection of conversion!)


# c = int(input())
# f = (c * 9 // 5) + 32
# print(f)
    


#  5. DMOJ problem wc18c3j1, An Honest Day’s Work (Hint: how can you determine the number of bottle caps and the total paint requiredby those bottle caps?)

# total_paint = int(input())
# paint_per_badge = int(input())
# price_per_badge = int(input())

# badges = total_paint // paint_per_badge
# remaining_paint = total_paint % paint_per_badge
# total_money = badges * price_per_badge + remaining_paint

# print(total_money)

