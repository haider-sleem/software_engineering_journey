# # 1-  إنشاء دالة للمستخدم

# #  purchaser --> storekepeer / staff == cashir عاوزين نبدل
# def choose_user_type():
#     user_role = input(
#         "choose your role : 1 for admin - 2 for purchaser and 3 for staff : "
#     )
#     if user_role.isdigit():
#         user_role = int(user_role)
#         if user_role in (1, 2, 3):
#             if user_role == 1:
#                 return "Admin"
#             if user_role == 2:
#                 return "purchaser"
#             if user_role == 3:
#                 return " staff"

#         else:
#             print("choice avalid number from (1-3)")
#             return choose_user_type()

#     else:
#         print("Enter digit only from (1-3)")
#         return choose_user_type()


# choose_user_type()


################222222222222222222222222222222222#################
# #######222222222222222222222222222222222########################


# # # 2- إنشاع دوال للمنتجات
products = {"product_name": {"price": 1000, "quantity": 20}}


# دالة رئيسية بتحدد هل المنتج موجود ولا لأ
# عاوزين يكون في خاصية برضه يفحص بالباركود هل المنتج موجود ولا لاء ولو موجود يطلع كل بياناته تلقائي
def adding_product():
    while True:
        product_name = input("Is the product already available? : (Yes / No): ").strip()

        # لو المنتج موجود → تحديث
        if product_name.lower() == "yes":
            update_existing_product()

        # لو المنتج جديد → إضافة
        elif product_name.lower() == "no":
            add_new_product()

        # إدخال غلط
        else:
            print("Please enter Yes or No only!! ")
            continue

        while True:
            choice = input("Do you want to continue? (Yes/No): ").strip()

            if choice.lower() == "yes":
                break  # يرجع لأول اللوب ويبدأ من جديد
            elif choice.lower() == "no":
                print("Exiting system...")
                return  # يخرج من الدالة نهائيًا
            else:
                print("Please enter Yes or No only!! ")


# دالة مسؤولة عن البحث عن المنتج واختياره
# دالة منفصلة علشان لما نستخدمها تاني في البيع


def select_product():
    search = input("Enter product name  (or press Enter for all): ").strip()

    # فلترة المنتجات بناءً على البحث
    filtered_names = [
        name for name in products.keys() if search.lower() in name.lower()
    ]

    # لو مفيش نتائج
    if not filtered_names:
        print("No products found")
        return None

    # عرض المنتجات للمستخدم
    for idx, name in enumerate(filtered_names, 1):
        print(f"{idx}. {name}")

    # اختيار المنتج برقم
    while True:
        choice = input("Enter product number: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(filtered_names):
                selected_name = filtered_names[choice - 1]
                return selected_name
            else:
                print("Invalid choice, try again")

        else:
            print("Invalid choice, try again")


# دالة أساسية لتحديث منتج موجود


def update_existing_product():
    selected_name = select_product()  # اختيار المنتج

    if selected_name:
        update_price(selected_name)  # تحديث السعر
        update_quantity(selected_name)  # تحديث الكمية


# دالة لتحديث السعر فقط


def update_price(product):
    while True:
        edit_price = input(
            f"Do you need to change the price (current price: {products[product]['price']})? (Yes/No): "
        ).strip()

        if edit_price.lower() == "yes":
            new_price = input("Enter new price: ").strip()

            # التحقق من صحة السعر
            try:
                new_price = float(new_price)
            except ValueError:
                print("Invalid price")
                continue

            # تأكيد التعديل
            confirmation = input(
                f"Are you sure you want to change the price to {new_price} ? (Yes/No): "
            ).strip()

            if confirmation.lower() == "yes":
                products[product]["price"] = new_price  # تحديث السعر
                break
            elif confirmation.lower() == "no":
                continue
            else:
                print("Please enter Yes or No only!! ")

        elif edit_price.lower() == "no":
            break
        else:
            print("Please enter Yes or No only!! ")


# دالة لتحديث الكمية (إضافة كمية جديدة)
# هل محتاجين تفريعة لتحديد وحدة الكمية قطعة كرتونة كونتنر مثلا ؟


def update_quantity(product):  # المشتراة
    while True:
        new_quantity = input("Enter additional quantity: ")

        # التحقق إن المدخل رقم
        if new_quantity.isdigit():
            products[product]["quantity"] += int(new_quantity)  # إضافة الكمية
            break
        else:
            print("Enter digit only")
            continue  # سايبها للتوضيح
    print(f"Product {product} updated successfully")

    #  ممكن هنا مستقبلاً نسأله: هل عاوز يحدث منتج تاني ؟


################################3333333333333333333333333333333###############################################33333333333333333333333333333333333##############
# # دالة لإضافة منتج جديد
def add_new_product():

    while True:
        new_product_name = input("Enter the new product name : ").strip()

        if new_product_name in products:
            print("Product already exists")
            continue

        if new_product_name:  # هل ممكن يدخل بالبار كود
            name_confirmition = input(
                f"Are you sure the name {new_product_name} is correct ? (Yes/No):"
            ).strip()
            if name_confirmition.lower() == "yes":
                products[new_product_name] = {
                    "price": 0,
                    "quantity": 0,
                    "is_active": False,
                }

                update_price(new_product_name)
                update_quantity(new_product_name)

                if (
                    products[new_product_name]["price"] > 0
                    and products[new_product_name]["quantity"] > 0
                ):
                    products[new_product_name]["is_active"] = True
                break
            else:
                print("Ok, enter the correct name please")
                continue
        else:
            print("Product name cannot be empty")
            continue


# نقطة بداية البرنامج
if __name__ == "__main__":
    adding_product()
