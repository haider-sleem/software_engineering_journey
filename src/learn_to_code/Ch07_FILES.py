# # Problem #16: USACO 2020 January Bronze Contest problem Word Processor.
# input_file = open("word.in", "r")

# line1 = input_file.readline().split()
# n = int(line1[0])
# k = int(line1[1])
# words = input_file.readline().split()
# output_file = open("word.out", "w")
# line = ""
# chars_on_line = 0
# for word in words:
#     if chars_on_line + len(word) <= k:
#         line = line + word + " "
#         chars_on_line += len(word)
#     else:
#         output_file.write(line.rstrip() + "\n")
#         line = word + " "
#         chars_on_line = len(word)
# output_file.write(
#     line.rstrip() + "\n"
# )  # لضمان كتابة السطر الأخير إذا كان غير ممتلى ولم يدخل الإيلس
# input_file.close()
# output_file.close()


# # Problem #17: USACO 2019 February Bronze Contest problem The Great Revegetation.
# def read_cows(input_file, num_cows):
#     favorites = []
#     for _ in range(num_cows):
#         lst = input_file.readline().split()
#         lst[0] = int(lst[0])
#         lst[1] = int(lst[1])
#         favorites.append(lst)
#     return favorites


# def cows_with_favorite(favorites, pasture):
#     cows = []
#     for i in range(len(favorites)):
#         if favorites[i][0] == pasture or favorites[i][1] == pasture:
#             cows.append(i)
#     return cows


# def types_used(favorites, cows, pasture_types):
#     used = []
#     for cow in cows:
#         pasture_a = favorites[cow][0]
#         pasture_b = favorites[cow][1]

#         if pasture_a < len(pasture_types):
#             used.append(pasture_types[pasture_a])

#         if pasture_b < len(pasture_types):
#             used.append(pasture_types[pasture_b])

#     return used


# def smallest_available(used):
#     grass_type = 1
#     while grass_type in used:
#         grass_type += 1
#     return grass_type


# def write_pastures(output_file, pasture_types):
#     pasture_types_str = []

#     for pasture_type in pasture_types:
#         pasture_types_str.append(str(pasture_type))

#     output = "".join(pasture_types_str)
#     output_file.write(output + "\n")


# # =========================
# # MAIN PROGRAM (التنفيذ)
# # =========================

# input_file = open("revegetate.in", "r")
# output_file = open("revegetate.out", "w")

# # قراءة أول سطر
# lst = input_file.readline().split()
# num_pastures = int(lst[0])
# num_cows = int(lst[1])

# # قراءة بيانات الأبقار
# favorites = read_cows(input_file, num_cows)

# # بداية الحل
# pasture_types = [0]

# for i in range(1, num_pastures + 1):

#     cows = cows_with_favorite(favorites, i)
#     eliminated = types_used(favorites, cows, pasture_types)
#     pasture_type = smallest_available(eliminated)

#     pasture_types.append(pasture_type)

# # إخراج النتيجة
# pasture_types.pop(0)
# write_pastures(output_file, pasture_types)

# input_file.close()
# output_file.close()


##### Chapter Exercises page 255 ########

# 1. USACO 2018 December Bronze Contest problem Mixing Milk
