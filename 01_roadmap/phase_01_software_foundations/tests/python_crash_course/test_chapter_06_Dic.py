from python_crash_course.chapter_06_Dic import cities

def test_cities_structure():
    # التأكد أن "القاهرة" موجودة في القاموس الكبير
    assert "cairo" in cities
    
    # التأكد أن معلومة "الدولة" للقاهرة هي "egypt"
    assert cities["cairo"]["country"] == "egypt"

def test_cities_details():
    # 1. التأكد أن كل مدينة تحتوي على الثلاث معلومات المطلوبة (Country, Population, Fact)
    for city, info in cities.items():
        assert "country" in info
        assert "population" in info
        assert "fact" in info

    # 2. التأكد أن "عدد السكان" دائماً رقم موجب (وليس نصاً أو رقماً سالباً)
    for city, info in cities.items():
        assert isinstance(info["population"], int)
        assert info["population"] > 0