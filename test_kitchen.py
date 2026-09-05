# ☐  200 g × 3 = 600 g
#☐ การคูณต้องไม่เปลี่ยนค่าของอ็อบเจ็กต์เดิม
#☐ ปริมาณสองค่าที่มีทั้งตัวเลขและหน่วยเท่ากันถือว่าเท่ากัน
#☐ 1 oz ไม่เท่ากับ 1 g
#☐  200 g + 300 g = 500 g
#☐ 200 g + 1 oz แปลงผลลัพธ์เป็นกรัมโดยใช้อัตราแปลงหน่วย
#☐  (200 g + 1 oz) × 2
# test_kitchen.py
from kitchen import Quantity, Sum, Converter, grams


def test_grams():
    assert grams(200) == Quantity(200, "g")


def test_quantity_equality():
    assert grams(200) == grams(200)


def test_quantity_not_equal():
    assert grams(200) != grams(300)


def test_simple_addition():
    total = grams(200).plus(grams(300))

    converter = Converter()

    assert converter.reduce(total, "g") == grams(500)