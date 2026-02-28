import sys
import os
import unittest

# 1️⃣ إضافة مجلد src للـ sys.path مؤقتًا
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

# 2️⃣ استيراد الملف الذي نريد اختباره
from python_crash_course import chapter_03_lists  # نستورد الملف كامل


# 3️⃣ إنشاء كلاس الاختبار
class TestChapter03Lists(unittest.TestCase):
    def test_guest_list(self):
        # استدعاء المتغير Guest_List من الملف الأصلي
        guest_list = chapter_03_lists.Guest_List

        # 3️⃣ طباعة القائمة (اختياري للعرض أثناء التعلم)
        print("Guest list after additions:", guest_list)

        # 4️⃣ اختبار الطول
        self.assertEqual(len(guest_list), 7, "Guest list should have 7 people")

        # 5️⃣ اختبار أول وآخر عنصر
        self.assertEqual(guest_list[0], "Nana", "First guest should be Nana")
        self.assertEqual(guest_list[-1], "Tamara", "Last guest should be Tamara")


if __name__ == "__main__":
    unittest.main()
