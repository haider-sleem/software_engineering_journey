التحديات التقنية وحلولها (Technical Challenges)


1. مشكلة مسارات النظام (Path Resolution Issue)
الوصف:
عند البدء في بناء هيكل المشروع، واجهت مشكلة ModuleNotFoundError. كان بايثون غير قادر على التعرف على ملفات الكود المصدري (src) عند تشغيل الاختبارات (tests) بسبب اختلاف المجلدات الأساسية (Working Directory).

الحل المقترح بمساعدة ChatGPT:
تم الانتقال من استخدام المسارات الثابتة (Hard-coded Paths) إلى المسارات الديناميكية (Dynamic Paths) باستخدام متغير بايثون السحري __file__.

الكود المستخدم للحل:

Python
import sys
import os

# تحديد مسار المجلد الحالي لملف التست ومن ثم الصعود للأعلى للوصول لـ src
base_path = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(base_path, "../../src"))

sys.path.append(src_path)
لماذا هذا الحل احترافي؟

Portability: الكود سيعمل على أي جهاز (Windows/Linux) دون تعديل المسارات يدوياً.

Robustness: لا يعتمد على المكان الذي تفتح منه الـ Terminal؛ فالمسار يُحسب دائماً بالنسبة لموقع الملف نفسه.

Clean Architecture: يسمح بفصل ملفات الاختبار عن ملفات الكود المصدري مع الحفاظ على سهولة الاستيراد (Importing).


##################################################

