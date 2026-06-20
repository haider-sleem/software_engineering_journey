# # 1. USACO 2018 December Bronze Contest problem Mixing Milk
import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "mixmilk.in")
out_path = os.path.join(current_path, "mixmilk.out")


with open(in_path, "r") as file_input, open(out_path, "w") as file_output:
    # تخزين السعات والحليب في قوائم (Lists) لتسهيل التعامل معها
    c = [0, 0, 0]
    m = [0, 0, 0]

    # قراءة البيانات
    for i in range(3):
        line = file_input.readline().split()
        c[i] = int(line[0])
        m[i] = int(line[1])

    # حلقة التكرار لـ 100 عملية صب
    for i in range(100):
        source = i % 3
        target = (i + 1) % 3

        # حساب الكمية التي يمكن صبها
        amount_to_pour = min(m[source], c[target] - m[target])

        # تحديث القيم
        m[source] -= amount_to_pour
        m[target] += amount_to_pour

    # كتابة النتائج
    for amount in m:
        file_output.write(str(amount) + "\n")
