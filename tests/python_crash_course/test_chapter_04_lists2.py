import sys
import os
import unittest

# 1️⃣ إضافة مجلد src للـ sys.path مؤقتًا للوصول لملفات الكود الأصلي
# المسار هنا بيطلع لمجلدين لفوق عشان يوصل لمجلد src بناءً على الصورة
# current_file_path = __file__
# current_dir = os.path.dirname(current_file_path)
# relative_path_to_src = os.path.join(current_dir, "..", "..", "src")
# absolute_src_path = os.path.abspath(relative_path_to_src)
# sys.path.append(absolute_src_path)


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

# 2️⃣ استيراد الملف الذي نريد اختباره من داخل حزمة python_crash_course
from python_crash_course import chapter_04_lists2


class TestChapter04Lists2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """تجهيز البيانات مرة واحدة قبل تشغيل الاختبارات"""
        # بنفترض إنك معرف متغير اسمه numbers في ملف chapter_04_lists2.py
        cls.numbers = chapter_04_lists2.numbers

    def test_list_length(self):
        """اختبار أن القائمة تحتوي على مليون عنصر بالضبط"""
        self.assertEqual(len(self.numbers), 1000000, "يجب أن يكون طول القائمة مليون")

    def test_min_value(self):
        """اختبار أن أصغر رقم هو 1"""
        self.assertEqual(min(self.numbers), 1, "أصغر رقم يجب أن يكون 1")

    def test_max_value(self):
        """اختبار أن أكبر رقم هو مليون"""
        self.assertEqual(max(self.numbers), 1000000, "أكبر رقم يجب أن يكون 1,000,000")

    def test_correct_sum(self):
        """اختبار أن مجموع الأرقام مطابق للناتج الصحيح"""
        expected_sum = 500000500000
        actual_sum = sum(self.numbers)
        self.assertEqual(
            actual_sum, expected_sum, f"المجموع يجب أن يكون {expected_sum}"
        )


if __name__ == "__main__":
    # تشغيل الاختبارات وطباعة النتائج في الـ Terminal
    unittest.main()
