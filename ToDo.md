 : الترتيب 

 دالة المستخدمين

 --------------------------------------------

قاموس البيانات (Data) → products = {...} 

دوال الأدوات (Helpers) → select_product() 

دوال التحديث الأساسية (Actions) → update_price(), update_quantity() 

دوال العمليات الكبيرة (Coordinators) → update_existing_product(), add_new_product()

الدالة الرئيسية (Main Coordinator) → adding_product() --> بيطلع منها ياأما يضيف منتج جديد أو يحدث منتج موجود بعد البحث عن المنتج ومعرفة هل موجود ولا لاء 

نقطة الانطلاق → if __name__ == "__main__"

