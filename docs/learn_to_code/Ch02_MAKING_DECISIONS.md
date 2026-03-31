Problem #3: Winning Team (DMOJ problem ccc19j1.) page 58

--- طريقة حل المسألة بطريقة إحترافية غير حل الكتاب مع تحليلها--

'''
def calculate_total(three, two, one):
    return three * 3 + two * 2 + one


def get_team_score(team_name):
    print(f"--- {team_name} ---")
    three = int(input())
    two = int(input())
    one = int(input())
    return calculate_total(three, two, one)


apple = get_team_score("Apples")
banana = get_team_score("Bananas")


if apple > banana:
    print("A")
elif banana > apple:
    print("B")
else:
    print("T")

--------------------------  التحليل -----------------



## 1️⃣ كيف يحقق مبدأ **Clean Code**

* **وضوح الأسماء (Naming)**

  * `calculate_total` → اسم واضح يصف وظيفة الدالة بدقة: حساب مجموع النقاط.
  * `get_team_score` → اسم واضح يفهم منه أنها **تجمع مدخلات الفريق وتحسب النتيجة**.
    ✅ هذا يقلل أي غموض ويجعل الكود self-documenting.

* **فصل المسؤوليات (Separation of Concerns)**

  * دالة واحدة مسئولة عن الحساب (`calculate_total`).
  * دالة أخرى مسئولة عن جمع المدخلات (`get_team_score`).
  * مقارنة النتائج وطباعة النتيجة في القسم الأخير منفصلة.
    ✅ هذا يسهل تعديل أي جزء دون التأثير على الأجزاء الأخرى.

* **تقليل التكرار (DRY Principle)**

  * لم نكرر منطق الحساب لكل فريق، استخدمنا دالة `calculate_total`.
  * أي تعديل على طريقة الحساب يتم مرة واحدة فقط في الدالة.

* **سهولة القراءة والفهم (Readability)**

  * الكود مقسم منطقيًا: إدخال → معالجة → قرار → إخراج.
  * كل خطوة واضحة بدون خلط بين الأمور.

---

## 2️⃣ مفاهيم تصميم مهمة

* **تقسيم الكود إلى دوال (Modularity)**

  * كل دالة تقوم بمهمة محددة، يمكن إعادة استخدامها بسهولة.
  * يسمح بإضافة فرق جديدة أو أنواع مختلفة من الرميات بدون تعديل الكود الرئيسي.

* **إعادة الاستخدام (Reusability)**

  * يمكن استخدام `calculate_total` لأي نوع من النقاط أو أي فريق آخر.
  * يمكن استدعاء `get_team_score` لأي عدد فرق دون كتابة نفس الـ input مرة أخرى.

* **قابلية التوسعة (Scalability)**

  * إضافة فريق ثالث أو تغيير عدد أنواع الرميات يتطلب تعديل بسيط فقط في الدوال.
  * الكود معدّ للتوسع دون إعادة كتابة منطق الحساب أو مقارنة النتائج.

---

## 3️⃣ مقارنة بأساليب أبسط أو سريعة

* **الأسلوب السريع (loop مع input مباشرة)**

  * يخلط بين الإدخال والمعالجة، مما يصعب الفهم أو إعادة الاستخدام.
  * صعب التعديل أو التوسع.
  * يصعب اختبار الدوال أو استخدام الـ automated tests.

* **لماذا هذا الحل أكثر احترافية**

  * واضح ومنظم
  * قابل للتعديل والاختبار بسهولة
  * يقلل الأخطاء المحتملة أثناء التعديل أو التوسع

* **متى يُفضّل استخدام كل أسلوب**

  * الأسلوب المنظم بالدوال → للمشاريع، التمارين الكبيرة، الاختبارات، المسابقات الرسمية
  * الأسلوب المباشر → للمسائل السريعة جدًا أو تجربة فكرة واحدة قصيرة

---

## 4️⃣ تحليل الأداء (Performance)

* **Time Complexity**:

  * O(1) لكل فريق → العمليات محدودة وثابتة
* **فرق الأداء مع الحلول الأخرى**:

  * الحلول المباشرة لا يوجد فرق كبير عمليًا هنا
  * الفائدة الحقيقية ليست الأداء، بل **المرونة، الصيانة، والفهم**

---

## 5️⃣ كيف يساعدك هذا الأسلوب

* **حل مسائل أخرى مشابهة بشكل أسرع**:

  * بمجرد كتابة دوال حسابية واستدعاءها، يمكنك حل أي مسألة حساب نقاط أو تقييم نتائج فرق مختلفة.

* **تقليل الأخطاء أثناء البرمجة**:

  * كل دالة صغيرة → أقل فرصة لخلط المنطق مع الإدخال أو الطباعة
  * أي خطأ يتم تحديده وتصحيحه بسهولة في دالة واحدة

* **التفكير المنظم (Problem Solving Mindset)**:

  * تعلم كيفية فصل المدخلات عن المعالجة عن القرار
  * هذا يكوّن عادة تحليل المسألة قبل كتابة أي كود

---

## 6️⃣ قاعدة عامة أو نموذج تفكير

**نموذج أي مسألة مشابهة:**

1. **حدد المدخلات المطلوبة** → ما هي البيانات التي ستدخل؟
2. **افصل منطق الحساب أو المعالجة** → دالة واحدة لكل عملية حسابية
3. **استعمل دوال صغيرة قابلة لإعادة الاستخدام** → DRY
4. **حدد القرار أو المقارنة منفصلًا** → if/elif/else أو أي منطق اتخاذ قرار
5. **الإخراج النهائي فقط بعد كل المعالجة** → لتقليل الأخطاء

---

## 7️⃣ مثال آخر يمكن تطبيق نفس الأسلوب

**مسألة:** حساب درجات اختبار الطلاب في 3 مواد ومعرفة الأعلى.

python
def calculate_total(math, physics, chemistry):
    return math + physics + chemistry

def get_student_score():
    math = int(input())
    physics = int(input())
    chemistry = int(input())
    return calculate_total(math, physics, chemistry)

alice = get_student_score()
bob = get_student_score()

if alice > bob:
    print("Alice")
elif bob > alice:
    print("Bob")
else:
    print("Tie")


✅ نفس الأسلوب: دوال منفصلة، إعادة استخدام، نظافة الكود، قابلية التوسع

---


'''

# ---------------------------------------

# Problem #4: Telemarketer or not ( DMOJ problem ccc18j1.) page 72

# Chapter 02: Making Decisions

## 🎯 Key Concepts
- **Membership Testing:** Using `in` with `Tuples` for cleaner conditions.
- **Boolean Logic:** Mastering `and`, `or`, and `not`.

## 🛠 Pro Tools
### Input Redirection
To run code with automated inputs:
`python file.py < input.txt` (CMD/Bash)
`Get-Content input.txt | python file.py` (PowerShell)
((((Problem: RedirectionNotSupported error in PowerShell when using <.
Cause: PowerShell handles input redirection differently than standard shells.
Solution: Switch the terminal to Command Prompt (CMD) or use the piping command: Get-Content file.txt | python code.py.))))

## 💡 Senior Tip
Always keep your logic **Positive & Direct**. Avoid double negatives to reduce cognitive load.



