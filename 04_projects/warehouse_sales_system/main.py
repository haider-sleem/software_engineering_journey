import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("main.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

products = {}


# دالة للتأكد إن المستخدم مش هيدخل نص فاضي إلا لو كان مسموح
def get_non_empty_text(
    prompt: str, allow_empty: bool = False
) -> str:  # هل ممكن نحتاج إن البرومت يكون رقم
    """
    Captures text input from the user and strips whitespace.

    Args:
        prompt (str): Message displayed to the user.
        allow_empty (bool): If True, empty input is accepted. Defaults to False.

    Returns:
        str: The entered text, which can be empty if allow_empty is True.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input and not allow_empty:
            print("❌ Input cannot be empty! Please enter a valid text.")
            continue

        return user_input


# دالة وظيفتها تاخد رد من المستخدم لنا تكون الإجابة ب نعم او لا فقط
def get_yes_no(prompt: str) -> bool:
    """
    Prompts the user for a confirmation and ensures a valid yes/no response.

    Args:
        prompt (str): Message displayed to the user asking for confirmation.

    Returns:
        bool: True if the user confirms (yes/y), False if they decline (no/n).
    """
    while True:
        choice = input(f"{prompt} (Yes/No): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        if choice in ["no", "n"]:
            return False
        print("❌ Invalid input! Please enter 'Yes' or 'No' only.")


# دالة التأكد من إدخال أرقام صالحة
# TODO 1: Refactor converter type hint to use Callable[[str], int | float]
# Why: In this context, int and float act as callable conversion functions rather than just strict types.
# TODO 2:
# Should this function be split into:
# - parse_positive_number() for validation/conversion
# - get_positive_number() for input/retry handling?
def get_positive_number(
    prompt: str,
    converter: type[int] | type[float] = int,
) -> int | float:
    """
    Repeatedly requests user input until a valid positive number is provided.

    Args:
        prompt (str): Message displayed to the user.
        converter (type[int] | type[float]): Conversion function used to
            transform the input into int or float. Defaults to int.

    Returns:
        int | float: The converted positive number greater than zero.
    """

    # TODO: Later, check if 'converter' is strictly int or float, and raise a TypeError if it's not.
    while True:
        user_input = input(prompt).strip()

        try:
            value = converter(user_input)
            if value <= 0:
                print("❌ Number must be greater than 0 ..!")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers only.")


def get_menu_choice(options: list[str]) -> str:
    """
    Display numbered menu options, repeatedly prompt the user until a valid
    choice is entered, then return the selected option text.
    """
    while True:
        # عرض الخيارات تلقائياً مرقمة تبدأ من 1
        for idx, option in enumerate(options, start=1):
            print(f"{idx}: {option}")

        prompt = "Enter the number of your choice: "
        user_input = input(prompt).strip()

        # 1. محاولة تحويل الإدخال إلى رقم صحيح
        try:
            choice = int(user_input)
        # 2. إذا فشل التحويل (حدث ValueError)
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
        # 3. إذا نجح التحويل بدون أخطاء
        else:
            # التحقق من أن الرقم داخل النطاق
            if 1 <= choice <= len(options):
                return options[choice - 1]  # إرجاع النص بنجاح
            else:
                print(
                    f"❌ Invalid choice! Please select a number between 1 and {len(options)}."
                )


# TODO:
# Revisit select_product() after learning Enum.
# Distinguish between "not found" and "cancelled" without overloading None.
# Support barcode search to find a product and display all its information.
def select_product(search: str = "") -> str | None:
    """
    Filters products by a search term and handles user selection from the matches.

    If a single direct match is found, it returns it immediately. If multiple
    matches are found, it loops indefinitely until the user enters a valid list number.

    Args:
        search (str): The product name or barcode substring to filter by. Defaults to "".

    Returns:
        str | None: The selected product name, or None ONLY if no matching products exist.
    """

    if not products:
        logger.info("Product selection failed | Reason: Inventory is empty.")
        print("❌ No products available.")
        return None

    # فلترة المنتجات بناءً على البحث
    filtered_names = [name for name in products if search.lower() in name.lower()]

    # لو مفيش نتائج
    if not filtered_names:
        logger.info(
            "No products found | Search term: '%s'.",
            search,
        )
        print(f"❌ No products found matching '{search}'")
        return None

    if len(filtered_names) == 1:
        return filtered_names[0]

    # عرض المنتجات للمستخدم
    for idx, name in enumerate(filtered_names, 1):
        print(f"{idx}. {name}")
    # اختيار المنتج برقم
    while True:
        choice = get_positive_number(
            "Enter product number: "
        )  # طيب لو المستخدم مش هيكتب والإختيار تاتش؟؟
        if 1 <= choice <= len(filtered_names):
            selected_product = filtered_names[choice - 1]
            return selected_product
        else:
            print("Invalid choice, try again")


# دالة لتحديث السعر فقط
def update_price(product_name: str, is_new: bool = False) -> bool:
    """
    Manages the pricing lifecycle of a product by setting or modifying it.

    Args:
        product_name (str): The identifier key of the product in inventory.
        is_new (bool): If True, initializes a new price without checking historical data.
            Defaults to False.

    Returns:
        bool: True if the price is successfully updated or initialized,
            False if the process is declined or the price remains identical.
    """
    if not is_new:
        old_price = products[product_name].get("price", 0)
        change_price_prompt = f"Do you want to change price? (current: {old_price:.2f})"
        # إستدعاء دالة تأكيد الرغبة في تغيير السعر و الخروج في حالة عدم الرغبة ب ريتيرن
        if not get_yes_no(change_price_prompt):
            return False
    while True:
        prompt = (
            f"Enter price for new item '{product_name}': "
            if is_new
            else f"Enter new price for '{product_name}': "
        )
        new_price = get_positive_number(prompt, converter=float)

        msg = (
            f"Set initial price to {new_price}?"
            if is_new
            else f"Confirm new price to {new_price}?"
        )

        if get_yes_no(msg):
            if not is_new and new_price == old_price:
                print(
                    "⚠️ Price unchanged, No update made, Reason: the old price is equal to the new price."
                )
                return False
            products[product_name]["price"] = new_price
            if is_new:
                logger.info(
                    "Price initialized | Product: '%s' | Price: %.2f EGP",
                    product_name,
                    new_price,
                )
            else:
                logger.info(
                    "Price updated | Product: '%s' | Old price: %.2f EGP | New price: %.2f EGP",
                    product_name,
                    old_price,
                    new_price,
                )
            if is_new:
                print(f"Initial price for '{product_name}' set successfully.")
            else:
                print(f"Price for '{product_name}' updated successfully.")
            return True
        print("🔁 Ok, please enter the correct Price.")


# دالة لتحديث الكمية (إضافة كمية جديدة)
# هل محتاجين تفريعة لتحديد وحدة الكمية قطعة كرتونة كونتنر مثلا ؟
def update_quantity(product_name: str, is_new: bool = False) -> bool:  # المشتراة
    """Manages the inventory stock of a product by initializing or incrementing its quantity.

    Args:
        product_name (str): The identifier key of the product in inventory.
        is_new (bool): If True, initializes a new stock level directly.
            Defaults to False.

    Returns:
        bool: True if the stock quantity is successfully updated or initialized,
            False if the process is declined.
    """

    if not is_new:
        additional_quantity_prompt = (
            f"Do you want to add additional quantity for '{product_name}': "
        )
        if not get_yes_no(additional_quantity_prompt):
            return False

    while True:
        prompt = (
            f"Set quantity for the new added item '{product_name}': "
            if is_new
            else f"Enter additional quantity for '{product_name}': "
        )
        new_quantity = get_positive_number(prompt)

        # التحقق إن المدخل رقم
        quantity_confirmation = (
            f"Are you sure you want to add '{new_quantity}' to stock ?"
        )

        if get_yes_no(quantity_confirmation):
            if is_new:
                products[product_name]["stock"] = new_quantity
            else:
                products[product_name]["stock"] += new_quantity
            print(f"Quantity for '{product_name}' updated successfully")
            return True

        print("🔁 Please enter the correct quantity again.")


# دالة لتحديث حالة المنتج
# TODO: Refactor later to follow Single Responsibility Principle (SRP).
# Current issue: Function checks conditions and updates global state at the same time.
def update_product_status(
    product_name: str,
) -> tuple[bool, list[str]]:
    """
    Checks and updates if a product is active based on its price and stock.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        tuple[bool, list[str]]: A tuple containing:
            - bool: True if the product satisfies all conditions to be ACTIVE, False otherwise.
            - list[str]: A list of missing requirements ("Price", "Stock") causing inactivity.
    """
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


def display_product_status(product_name: str) -> None:
    """
    Prints the current active or inactive status of a product to the terminal.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        None: This function only prints output to the console.
    """
    is_active, reasons = update_product_status(product_name)

    if is_active:
        print(f"\n✅ Product '{product_name}' is ACTIVE")
    else:
        print(f"⚠️ Product '{product_name}' is INACTIVE. Missing: {', '.join(reasons)}")


# دالة أساسية لتحديث منتج موجود
def update_existing_product(
    product_name: str,
) -> None:
    """
    Updates the price, stock quantity, and active status of an existing product.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        None: This function executes updates and does not return a value.
    """

    update_price(product_name)
    update_quantity(product_name)
    display_product_status(product_name)


# # دالة لإضافة منتج جديد
def add_new_product(
    product_name: str,
) -> None:
    """
    Creates a new product in inventory and sets its price and stock.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        None: This function executes creation steps and does not return a value.
    """

    products[product_name] = {
        "price": 0,
        "stock": 0,
        "is_active": False,
    }

    update_price(product_name, is_new=True)
    update_quantity(product_name, is_new=True)
    display_product_status(product_name)


def sell_product() -> bool | None:
    """
    Processes a product sale by validating stock and updating inventory.

    Returns:
        bool | None:
            - True: If the sale succeeds.
            - False: If cancelled due to insufficient stock.
            - None: If the user explicitly exits the process (Not a failure).
    """
    while True:
        raw_input = "\nEnter product name or barcode (or 'exit' to stop): "

        user_input = get_non_empty_text(raw_input).lower()

        # TODO: Revisit exit/cancellation handling after learning Error Handling.
        # Choose an explicit control-flow mechanism that clearly distinguishes
        # exit, cancellation, failure, and success.
        if user_input == "exit":
            return None

        product_name = select_product(user_input)
        if product_name is None:
            continue
        product = products[product_name]
        if not product["is_active"]:
            logger.warning(
                "Sale rejected | Reason: Product is inactive | Product: '%s'.",
                product_name,
            )
            print(f"⚠️ Product '{product_name}' is inactive and cannot be sold.")
            continue

        prompt = f"\nEnter quantity for {product_name}: "
        # NOTE: Is it necessary to explicitly type 'quantity_to_be_sold: int' for the IDE's sake?
        # Or is relying on the function's default behavior enough since Python works fine at runtime?
        quantity_to_be_sold = get_positive_number(prompt)

        stock = product["stock"]

        if quantity_to_be_sold <= stock:
            product["stock"] -= quantity_to_be_sold
            total_price = quantity_to_be_sold * product["price"]
            update_product_status(product_name)
            logger.info(
                "Sale completed | Product: '%s' | Quantity sold: %d | Total: %.2f EGP | Remaining stock: %d",
                product_name,
                quantity_to_be_sold,
                total_price,
                product["stock"],
            )
            print(f"✅ Sale completed,Total: {total_price:.2f} EGP")
            print(f"📦 Remaining stock: {product['stock']}")
            return True  # Exit after single sale (Single Responsibility)
            # NOTE: later we may add dual mode (Cashier Mode: loop / Admin Mode: single action)

        # 🔴 لو المخزون مش كفاية
        logger.warning(
            "Sale rejected | Product: '%s' | Reason: Insufficient stock | Requested quantity: %d | Available stock: %d",
            product_name,
            quantity_to_be_sold,
            stock,
        )
        print("❌ Not enough stock!")
        print(f"Available stock : {stock}")

        # 🔥 (هنا مكان ميزة التصنيع اللي ممكن نضيفها بعدين)
        # مثال مستقبلي:
        # allow = input(f"Allow sale with production? Note:[Stock is {stock}] (Yes/No): ").strip().lower()

        modify_quantity = "Do you want to modify the quantity? "

        if get_yes_no(modify_quantity):
            continue

        # خروج من عملية البيع للمنتج ده
        print("❌ Sale cancelled.")
        return False


# دالة عرض المنتجات
def view_products() -> None:
    """
    Displays all items in the inventory with their price, stock level, and status.

    Returns:
        None: This function only prints the inventory data to the terminal.
    """
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
def handle_product() -> None:
    """
    Handle the workflow for adding a new product or updating an existing one.

    The function repeatedly prompts the user until they choose to exit.

    Returns:
        None: The function performs product management operations without
        returning a value.
    """
    while True:
        # 1. اسأل عن الاسم مباشرة (ده قلب التطوير)
        prompt = "Enter product name or barcode (or 'exit' to stop): "  # (or press Enter for all)

        user_input = get_non_empty_text(prompt)

        display_name = user_input.title()
        search_name = user_input.lower()

        if search_name == "exit":
            return
        # 2. البرنامج هو اللي بيشيك (مش اليوزر اللي بيقرر)
        # HACK: Searching via next() is fine for small inventory,
        # but needs optimization (O(1) lookup) as the database grows.
        existing_name = next(
            (name for name in products if name.lower() == search_name),
            None,
        )
        if existing_name:
            print(f"--- Product '{existing_name}' found! Switching to Update mode ---")
            update_existing_product(existing_name)

        else:
            print(
                f"--- Product '{user_input}' isn't found! Switching to Add new mode ---"
            )

            name_confirmation = (
                f"Are you sure you want to creat a new product named '{user_input}'?"
            )
            if get_yes_no(name_confirmation):
                add_new_product(display_name)

            else:
                continue

        # 3.سؤال الاستمرار
        # TODO:
        # Should the "manage another product" workflow be moved to a dedicated
        # handle_product_flow() function when separating workflow from business logic?
        continue_choice = "\nDo you want to manage another product? : "
        if get_yes_no(continue_choice):
            continue

        return

        # كود تعليمي
        # if not get_yes_no("Do you want to manage another product?"):
        #     print("Exiting system...")
        #     return


def cashier_menu() -> None:
    """
    Display the cashier menu and dispatch the selected cashier operation.
    """
    # نحدد الخيارات في قائمة مرنة وسهلة التعديل مستقبلاً (مثلاً لإضافة Refund)
    cashier_options = ["Selling", "Back"]

    while True:
        choice = get_menu_choice(cashier_options)
        match choice:
            case "Selling":
                sell_product()
            case "Back":
                print("Going back to main menu...")
                break


# TODO:
# Consider introducing dedicated workflow functions (e.g., update_quantity_flow,
# update_price_flow) when the application grows or is migrated to an API.
def inventory_menu() -> None:
    """
    Display the inventory menu and dispatch inventory operations.
    """

    inventory_options = [
        "View Products",
        "Add Or Update Product",
        "Update Quantity",
        "Update Price",
        "Back",
    ]

    while True:
        choice = get_menu_choice(inventory_options)

        match choice:
            case "View Products":
                view_products()

            case "Add Or Update Product":
                handle_product()

            case "Update Quantity":
                product_name = select_product()
                if product_name:
                    update_quantity(product_name)

            case "Update Price":
                product_name = select_product()
                if product_name:
                    update_price(product_name)

            case "Back":
                print("Going back to main menu...")
                break


def main() -> None:
    """
    Display the main menu and dispatch the selected application module.
    """

    main_options = ["Cashier Menu", "Inventory Menu", "Exit"]

    while True:
        choice = get_menu_choice(main_options)

        match choice:
            case "Cashier Menu":
                cashier_menu()

            case "Inventory Menu":
                inventory_menu()

            case "Exit":
                print("Exiting the program...")
                break


if __name__ == "__main__":
    main()
