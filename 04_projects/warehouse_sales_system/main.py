import math

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


def parse_positive_number(
    value: str,
    converter: type[int] | type[float] = int,
) -> int | float:
    """
    Converts a string into a positive, finite number.

    Args:
        value (str): The string value to be parsed and converted.
        converter (type[int] | type[float]): Conversion function used to
            transform the input into int or float. Defaults to int.

    Returns:
        int | float: The successfully converted positive and finite number greater than zero.

    Raises:
        ValueError: If the value is invalid, not finite (e.g., inf, nan), or not greater than zero.
    """

    try:
        number = converter(value.strip())
    except ValueError:
        raise ValueError("Invalid input! Please enter valid numbers only.")

    if isinstance(number, float) and not math.isfinite(number):
        raise ValueError("Number must be finite.")
    if number <= 0:
        raise ValueError("Number must be greater than 0.")

    return number


# TODO 1: Refactor converter type hint to use Callable[[str], int | float]
# Why: In this context, int and float act as callable conversion functions rather than just strict types.
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

    while True:
        user_input = input(prompt).strip()

        try:
            value = parse_positive_number(user_input, converter)

        except ValueError:
            print("❌ Invalid input! Please enter valid numbers only.")
            continue

        else:
            return value


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
    Filters products by name and handles user selection from the matches.

    If a single match is found, it returns it immediately. If multiple
    matches are found, it repeatedly prompts the user until a valid
    product number is entered.

    Args:
        search (str): The product name substring used for filtering.
            Defaults to an empty string.

    Returns:
        str | None: The selected product name, or None if no products
            are available or no matching products are found.
    """
    if not products:
        print("❌ No products available.")
        return None

    filtered_names = [name for name in products if search.lower() in name.lower()]

    if not filtered_names:
        print(f"❌ No products found matching '{search}'")
        return None

    if len(filtered_names) == 1:
        return filtered_names[0]

    for idx, name in enumerate(filtered_names, 1):
        print(f"{idx}. {name}")
    while True:
        choice = get_positive_number("Enter product number: ")
        if 1 <= choice <= len(filtered_names):
            selected_product = filtered_names[choice - 1]
            return selected_product
        else:
            print("Invalid choice, try again")


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
            else f"Confirm new price {new_price}?"
        )

        if get_yes_no(msg):
            if not is_new and new_price == old_price:
                print("⚠️ Price unchanged, No update made.")
                return False
            products[product_name]["price"] = new_price
            print(f"Price for '{product_name}' updated successfully")
            return True
        print("🔁 Ok, please enter the correct Price.")


# TODO: Consider supporting product-specific units of measurement
# (e.g., pieces, cartons, and containers) during domain modeling.
def update_quantity(product_name: str, is_new: bool = False) -> bool:
    """
    Initializes or increases a product's stock quantity.

    For existing products, asks for confirmation before adding stock.
    After a successful stock update, refreshes the product's active
    status and checks for low-stock alerts.

    Args:
        product_name (str): The identifier key of the product in inventory.
        is_new (bool): If True, sets the initial stock quantity directly.
            Defaults to False.

    Returns:
        bool: True if the stock is successfully initialized or updated;
            False if the operation is declined.
    """

    if not is_new:
        additional_quantity_prompt = (
            f"Do you want to add additional quantity for '{product_name}': "
        )
        if not get_yes_no(additional_quantity_prompt):
            return False

    while True:
        prompt = (
            f"Enter initial stock quantity for '{product_name}': "
            if is_new
            else f"Enter additional quantity for '{product_name}': "
        )
        quantity = get_positive_number(prompt)

        quantity_confirmation = f"Confirm stock quantity: {quantity}?"

        if get_yes_no(quantity_confirmation):
            if is_new:
                products[product_name]["stock"] = quantity
            else:
                products[product_name]["stock"] += quantity
            print(f"Stock quantity for '{product_name}' updated successfully.")
            update_product_status(product_name)
            display_low_stock_alert(product_name)
            return True

        print("🔁 Please enter the correct quantity again.")


# TODO: Refactor later to follow Single Responsibility Principle (SRP).
# Current issue: Function checks conditions and updates global state at the same time.
def update_product_status(
    product_name: str,
) -> tuple[bool, list[str]]:
    """
    Checks and updates a product's active status based on its price and stock.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        tuple[bool, list[str]]: A tuple containing:
            - bool: True if the product is active, otherwise False.
            - list[str]: Reasons preventing activation ("Price", "Stock").
    """
    reasons = []

    if products[product_name]["price"] <= 0:
        reasons.append("Price")

    if products[product_name]["stock"] <= 0:
        reasons.append("Stock")

    if len(reasons) == 0:
        is_active = True
    else:
        is_active = False
    products[product_name]["is_active"] = is_active

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


def set_low_stock_threshold(
    product_name: str,
) -> None:
    """
    Prompts the user to set a positive integer threshold for low-stock alerts
    or skip the configuration.

    The threshold is stored in the product's inventory record.
    If skipped, the threshold is set to None.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        None
    """

    while True:
        prompt = (
            f"Enter the minimum quantity you would like to have available for the product: '{product_name}'.\n"
            "Note: You will be notified once the stock reaches or falls below the limit.\n"
            "Type 'Skip' or press Enter to leave the threshold unset: "
        )

        user_input = input(prompt).strip().lower()
        if not user_input or user_input == "skip":
            products[product_name]["low_stock_threshold"] = None
            return
        try:
            threshold = parse_positive_number(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a valid positive integer.")
            continue
        # Confirm the threshold value with the user before saving
        if get_yes_no(f"Set low stock threshold to {threshold}?"):
            products[product_name]["low_stock_threshold"] = threshold
            return
        else:
            print(
                "Let's try again. Enter a new threshold, or type 'Skip' or press Enter to leave it unset.\n"
            )


def check_low_stock_alert(product_name: str) -> bool:
    """
    Determines whether a product's stock is at or below its configured
    low-stock threshold.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        bool: True if a threshold is configured and stock is at or below it;
            otherwise, False.
    """
    product = products[product_name]
    threshold = product["low_stock_threshold"]
    # Return True only if a threshold exists and stock is less than or equal to it
    return threshold is not None and product["stock"] <= threshold


def display_low_stock_alert(product_name: str) -> None:
    """
    Displays a low-stock warning for an active product when its stock
    reaches or falls below the configured threshold.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        None
    """
    product = products[product_name]
    # Skip alerts for inactive products
    if not product["is_active"]:
        return

    if check_low_stock_alert(product_name):
        print(
            f"⚠️ LOW STOCK ALERT: {product_name} "
            f"stock is {product['stock']} units "
            f"(Threshold: {product['low_stock_threshold']})."
        )


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
    Creates a new product in inventory and initializes its price, stock, and low stock threshold.

    Args:
        product_name (str): The identifier key of the product in inventory.

    Returns:
        None: This function executes creation steps and does not return a value.
    """

    products[product_name] = {
        "price": 0,
        "stock": 0,
        "is_active": False,
        "low_stock_threshold": None,
    }

    update_price(product_name, is_new=True)
    update_quantity(product_name, is_new=True)
    display_product_status(product_name)
    set_low_stock_threshold(
        product_name
    )  # Prompt user to set an optional low stock alert threshold for the new product


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
        raw_input = "\nEnter product name (or 'exit' to stop): "

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
            print(f"✅ Sale completed,Total: {total_price:.2f} EGP")
            update_product_status(product_name)
            print(f"📦 Remaining stock: {product['stock']}")
            display_low_stock_alert(product_name)
            return True  # Exit after single sale (Single Responsibility)
            # NOTE: later we may add dual mode (Cashier Mode: loop / Admin Mode: single action)

        # 🔴 لو المخزون مش كفاية
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
    Displays all items in the inventory with their price, stock level, status, and threshold.

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
        print(f"\t{'Price':<10}: {data['price']:<10.2f} EGP")
        print(f"\t{'Stock':<10}: {data['stock']:<10} Units")
        print(f"\t{'Status':<10}: {status:<10}")
        threshold = data["low_stock_threshold"]
        threshold_display = "Not set" if threshold is None else threshold
        print(f"\t{'Threshold':<10}: {threshold_display:<10} Units")
        print("-" * 30)


def calculate_inventory_value() -> tuple[float, list[tuple[str, int, float]]]:
    """
    Calculate the total financial value of the inventory.

    The inventory value is computed as the sum of (price * stock) for all
    products that have a valid price (> 0) and a stock greater than 0.

    Returns:
        tuple[float, list[tuple[str, int, float]]]:
            - float: The total inventory value.
            - list[tuple[str, int, float]]: Products that have stock but no
              valid price, stored as (name, stock, price).
    """
    total_inventory_value = 0.0
    products_without_price: list[tuple[str, int, float]] = []

    for name, data in products.items():
        if data["price"] > 0 and data["stock"] > 0:
            total_inventory_value += data["price"] * data["stock"]
        elif data["stock"] > 0 and data["price"] <= 0:
            products_without_price.append((name, data["stock"], data["price"]))

    return total_inventory_value, products_without_price


def display_inventory_value() -> None:
    """
    Display the total inventory value and warn about products that have
    stock but no valid price.

    Returns:
        None: This function only prints output to the console.
    """
    if not products:
        print(
            "\nNo products available..!, add products first to calculate inventory value.\n"
        )
        return

    total_value, products_without_price = calculate_inventory_value()

    print(f"\nTotal inventory value: {total_value:.2f}.")
    print("=" * 10)

    if products_without_price:
        print("Note ⚠️ : The following products have stock but no price:\n")
        for idx, (name, stock, price) in enumerate(products_without_price, 1):
            print(
                f"\t{idx}. {name.title()}: has stock ({stock}) but its price is {price:.2f}.\n"
            )


def handle_product() -> None:
    """
    Handle the workflow for adding a new product or updating an existing one.

    The function repeatedly prompts the user until they choose to exit.

    Returns:
        None: The function performs product management operations without
        returning a value.
    """
    while True:
        prompt = "Enter product name (or 'exit' to stop): "  # (or press Enter for all)

        user_input = get_non_empty_text(prompt)

        display_name = user_input.title()
        search_name = user_input.lower()

        if search_name == "exit":
            return
        # TODO: Searching via next() is fine for small inventory,
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
                f"Are you sure you want to create a new product named '{user_input}'?"
            )
            if get_yes_no(name_confirmation):
                add_new_product(display_name)

            else:
                continue

        # TODO:
        # Should the "manage another product" workflow be moved to a dedicated
        # handle_product_flow() function when separating workflow from business logic?
        continue_choice = "\nDo you want to manage another product? : "
        if get_yes_no(continue_choice):
            continue

        return


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
        "Inventory Valuation",
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
            case "Inventory Valuation":
                display_inventory_value()
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
