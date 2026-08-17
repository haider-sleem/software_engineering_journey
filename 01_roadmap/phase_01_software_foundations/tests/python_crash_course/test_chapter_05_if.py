from python_crash_course.chapter_05_if import is_username_available

def test_username_logic():
    currents = ["Ali", "Sara", "Admin"]
    
    # 1. متوقع True (اسم جديد)
    assert is_username_available("Haider", currents)
    
    # 2. متوقع False (اسم موجود) فبنحط not عشان التست ينجح
    assert not is_username_available("Ali", currents)
    
    # 3. متوقع False (حالة الأحرف) فبنحط not
    assert not is_username_available("SARA", currents)

def test_empty_inputs():
    # 4. متوقع True (قائمة فاضية)
    assert is_username_available("any_name", [])