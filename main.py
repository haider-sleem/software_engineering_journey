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
products = {}


def get_yes_no(prompt):
    """
    A help function to assist with user approval (yes/no).
    It continues to ask the user until they enter the correct answer.
    """
    while True:
        choice = input(f"{prompt} (Yes/No): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        if choice in ["no", "n"]:
            return False
        print("❌ Invalid input! Please enter 'Yes' or 'No' only.")


# دالة رئيسية بتحدد هل المنتج موجود ولا لأ
# عاوزين يكون في خاصية برضه يفحص بالباركود هل المنتج موجود ولا لاء ولو موجود يطلع كل بياناته تلقائي
# دالة مسؤولة عن البحث عن المنتج واختياره
# دالة منفصلة علشان لما نستخدمها تاني في البيع
def select_product():
    """Search for products by name and return the user's selected product name."""
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


# دالة لتحديث السعر فقط
def update_price(product_name, is_new=False):
    """Update or set the price for a specific product with validation and confirmation."""
    while True:
        old_price = products[product_name].get("price", 0) if not is_new else None

        if not is_new:
            change_price = f"Change price? (current: {products[product_name]['price']})"
            # إستدعاء دالة تأكيد الرغبة في تغيير السعر و الخروج في حالة عدم الرغبة ب ريتيرن
            if not get_yes_no(change_price): 
                return False
            
        prompt = (
            f"Enter price for new item '{product_name}': "
            if is_new
            else f"Enter new price for '{product_name}': "
        )
        price_input = input(prompt).strip()

        try:
            new_price = float(price_input)
            if new_price <= 0:
                print("Price must be greater than 0")
                continue
        except ValueError:
            print("❌ Invalid number!")
            continue

        msg = (
            f"Set initial price to {new_price}?"
            if is_new
            else f"Confirm new price {new_price}?"
        )

        confirm = input(f"{msg} (Yes/No): ").strip().lower()

        if confirm == "yes":
            if not is_new and new_price == old_price:
                print("⚠️ Price unchanged. No update made.")
                return False
            products[product_name]["price"] = new_price
            return True
        elif confirm == "no":
            continue
        else:
            print("Please enter Yes or No only!")
            continue


# دالة لتحديث الكمية (إضافة كمية جديدة)
# هل محتاجين تفريعة لتحديد وحدة الكمية قطعة كرتونة كونتنر مثلا ؟
def update_quantity(product_name, is_new=False):  # المشتراة
    """Handle inventory restocking by setting initial amounts or adding to existing supplies."""
    while True:
        if not is_new:
            choice = (
                input(
                    f"Do you want to add additional quantity for '{product_name}': (Yes/No) "
                )
                .strip()
                .lower()
            )

            if choice == "no":
                return False
            elif choice != "yes":
                print("❌ Please enter Yes or No only")
                continue

        while True:
            prompt = (
                f"Set quantity for the new added item '{product_name}': "
                if is_new
                else f"Enter additional quantity for '{product_name}': "
            )
            new_quantity = input(prompt)

            # التحقق إن المدخل رقم
            if new_quantity.isdigit():
                quantity_confirmation = (
                    input(
                        f"Are you sure you want to add '{new_quantity}' to stock ? (Yes/No)"
                    )
                    .strip()
                    .lower()
                )
                if quantity_confirmation == "yes":
                    amount = int(new_quantity)
                    if is_new:
                        products[product_name]["stock"] = amount
                    else:
                        products[product_name]["stock"] += amount
                    return True
                    """
                    ممكن تستخدم الـ 👆Ternary Operator
                    products[product_name]["stock"] = int(new_quantity) if is_new else products[product_name]["stock"] + int(new_quantity)
                    return True
                    """
                elif quantity_confirmation == "no":
                    print("Ok, Reenter the correct amount please.")

                else:
                    print("❌ Please enter Yes or No only")

            else:
                print("Enter digit only")
                continue  # سايبها للتوضيح


# دالة لتحديث حالة المنتج
def update_product_status(product_name):
    """Check and update product active status based on price and stock availability."""
    reasons = []

    if products[product_name]["price"] <= 0:
        reasons.append("Price")

    if products[product_name]["stock"] <= 0:
        reasons.append("Stock")

    is_active = len(reasons) == 0
    products[product_name]["is_active"] = is_active
    # السطر السابق بطريقة أوضح
    """
    # لو قائمة الأسباب فاضية (يعني مفيش مشاكل)
    if len(reasons) == 0:
    is_active = True
    else:
        is_active = False

    # بعدين نخزن النتيجة في بيانات المنتج
    products[product_name]["is_active"] = is_active
    """

    return is_active, reasons


# دالة أساسية لتحديث منتج موجود
def update_existing_product(product_name):
    """Update price, quantity, and status for an already existing product in inventory."""

    price_changed = update_price(product_name)
    quantity_changed = update_quantity(product_name)

    if price_changed:
        print(f"Price for '{product_name}' updated successfully")

    if quantity_changed:
        print(f"Quantity for '{product_name}' updated successfully")

    is_active, reasons = update_product_status(product_name)

    if is_active:
        print(f"\n✅ Product '{product_name}' is ACTIVE")
    else:
        print(f"⚠️ Product '{product_name}' is INACTIVE. Missing: {', '.join(reasons)}")


# # دالة لإضافة منتج جديد
def add_new_product(product_name, is_new=True):
    """Create a new product entry and initialize its price and stock levels."""
    products[product_name] = {
        "price": 0,
        "stock": 0,
        "is_active": False,
    }

    price_changed = update_price(product_name, is_new=True)
    quantity_changed = update_quantity(product_name, is_new=True)

    if price_changed:
        print(f"Price for '{product_name}' updated successfully")

    if quantity_changed:
        print(f"Quantity for '{product_name}' updated successfully")

    is_active, reasons = update_product_status(product_name)

    if is_active:
        print(f"\n✅ Product '{product_name}' is ACTIVE")
    else:
        print(f"⚠️ Product '{product_name}' is INACTIVE. Missing: {', '.join(reasons)}")


def sell_product():
    """
    Process a sale by checking product availability, validating stock, and updating inventory levels.
    """
    while True:
        product_to_be_sold = input(
            "\nEnter product name or barcode (or 'exit' to stop): "
        ).strip()

        if not product_to_be_sold:
            continue

        if product_to_be_sold.lower() == "exit":
            return
        # HACK: Searching via next() is fine for small inventory,
        # but needs optimization (O(1) lookup) as the database grows.
        product_name = next(
            (name for name in products if name.lower() == product_to_be_sold.lower()),
            None,
        )

        if product_name is None:
            print(f"❌ Product '{product_to_be_sold}' not found in inventory.")
            continue
        product = products[product_name]
        #  If product isn't active
        if not product["is_active"]:
            print(f"⚠️ Product '{product_name}' is inactive and cannot be sold.")
            continue

        while True:
            quantity_input = input(f"\nEnter quantity for {product_name}: ").strip()

            try:
                quantity_to_be_sold = int(quantity_input)
                if quantity_to_be_sold <= 0:
                    print("❌ Quantity must be greater than 0.")
                    continue

            except ValueError:
                print("❌ Please enter valid numbers only.")
                continue

            stock = product["stock"]

            #  If product is active
            if quantity_to_be_sold <= stock:
                product["stock"] -= quantity_to_be_sold
                total_price = quantity_to_be_sold * product["price"]
                print(f"✅ Sale completed,Total: {total_price} EGP")
                update_product_status(product_name)
                print(f"📦 Remaining stock: {product['stock']}")
                return  # Exit after single sale (Single Responsibility)
                # NOTE: later we may add dual mode (Cashier Mode: loop / Admin Mode: single action)

            # 🔴 المخزون مش كفاية
            else:
                print("❌ Not enough stock!")
                print(f"Available: {stock}")

                # 🔥 (هنا مكان ميزة التصنيع اللي انت عايز تضيفها بعدين)
                # مثال مستقبلي:
                # allow = input(f"Allow sale with production? Note:[Stock is {stock}] (Yes/No): ").strip().lower()

                while True:
                    modify = (
                        input("Do you want to modify the quantity? (Yes/No): ")
                        .strip()
                        .lower()
                    )

                    if modify == "yes":
                        break
                    elif modify == "no":
                        # خروج من عملية البيع للمنتج ده
                        print("❌ Sale cancelled.")
                        return
                    else:
                        print("Please enter Yes or No only.")
                        continue

                continue  # مش هيخرج إلا في حالة طلب التعديل علشان يعيد إدخال الكمية


# دالة عرض المنتجات
def view_products():
    """Display all products in inventory with their price, stock, and status."""

    if not products:
        print("No products available..!, add products first to display.")
        return

    print("\n" + "=" * 30)
    print("      CURRENT INVENTORY      ")
    print("=" * 30)

    for idx, (name, data) in enumerate(products.items(), 1):
        status = "ACTIVE" if data.get("is_active", False) else "INACTIVE"
        print(f"{idx}- {name}:")
        print(f"\tPrice:  {data['price']:<10.2f} EGP")
        print(f"\tStock:  {data['stock']:<10} Units")
        print(f"\tStatus: {status:<10}")
        print("-" * 20)


# الدالة الرئيسية
def adding_product():
    """Entry point to manage products; automatically toggles between Add and Update modes based on existence."""
    while True:
        # 1. اسأل عن الاسم مباشرة (ده قلب التطوير)
        product_name = input(
            "Enter product name or barcode  (or press Enter for all): "
        ).strip()

        if not product_name:
            print("Name cannot be empty!")
            continue
        # 2. البرنامج هو اللي بيشيك (مش اليوزر اللي بيقرر)
        existing_name = next(
            (name for name in products if name.lower() == product_name.lower()), None
        )
        if existing_name:
            print(f"--- Product '{existing_name}' found! Switching to Update mode ---")
            update_existing_product(existing_name)

        else:
            print(
                f"--- Product '{product_name}' isn't found! Switching to Add new mode ---"
            )
            while True:
                name_confirmition = (
                    input(
                        f"Are you sure you want to creat a new product named ''{product_name}!'' ? (Yes/No):"
                    )
                    .strip()
                    .lower()
                )

                if name_confirmition == "yes":
                    add_new_product(product_name)
                    break

                elif name_confirmition == "no":
                    print("Ok, please enter the correct name.")
                    break
                else:
                    print("Invalaid entire! , please choosse Yes or No.")
                    continue
            if (
                name_confirmition == "no"
            ):  # لو العلم مرفوع، اعمل continue للوب الكبيرة (خانة الاسم)
                continue

        # 3. سؤال الاستمرار (زي ما هو عندك)
        while True:
            continue_choice = (
                input("\nDo you want to manage another product? (Yes/No): ")
                .strip()
                .lower()
            )
            if continue_choice == "yes":
                break
            elif continue_choice == "no":
                print("Exiting system...")
                return
            else:
                print("Please enter Yes or No only!!")


# نقطة بداية البرنامج
if __name__ == "__main__":
    adding_product()
