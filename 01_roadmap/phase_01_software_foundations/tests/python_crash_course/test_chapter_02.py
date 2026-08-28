import sys
import os
import unittest

# 1. إضافة مجلد src للـ sys.path بحيث بايثون وVS Code يعرفوا مكان الكود
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

# 2. استيراد الملف الذي نريد اختباره
from python_crash_course import chapter_02  # استيراد مباشر من src


# 3. إنشاء كلاس الاختبار
class TestChapter02(unittest.TestCase):
    def test_full_name_formatting(self):
        # استدعاء الدالة من ملف chapter_02
        formatted_name = chapter_02.get_full_name("haider", "sleem")

        # التأكد من أن النتيجة تساوي التوقعات (title case)
        self.assertEqual(formatted_name, "Haider Sleem")


if __name__ == "__main__":
    unittest.main()
