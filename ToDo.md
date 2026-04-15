 : الترتيب 

 دالة المستخدمين

 --------------------------------------------

# 1) DATA
products = {...}

# 2) HELPERS (أدوات مساعدة)
def select_product(): ...

# 3) VIEW (عرض)
def view_products(): ...

# 4) UPDATE LOGIC
def update_price(): ...
def update_quantity(): ...
def update_existing_product(): ...

# 5) CREATE
def add_new_product(): ...

# 6) MAIN FLOW
def adding_product(): ...

# 7) ENTRY POINT
if __name__ == "__main__":
    adding_product()