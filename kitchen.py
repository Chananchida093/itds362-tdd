class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return (
            isinstance(other, Quantity)
            and self.amount == other.amount
            and self.unit == other.unit
        )

    def __repr__(self):
        return f"Quantity({self.amount}, '{self.unit}')"

    def plus(self, other):
        # ยังไม่บวกทันที
        # สร้าง Sum เพื่อเก็บค่าทั้งสองไว้ก่อน
        return Sum(self, other)

    def reduce(self, unit):
        # ตอนนี้รองรับกรณีหน่วยเดียวกันก่อน
        return Quantity(self.amount, unit)


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, unit):
        # บวกจำนวนของ Quantity ทั้งสอง
        total_amount = self.left.amount + self.right.amount

        return Quantity(total_amount, unit)


class Converter:
    def reduce(self, source, unit):
        # ให้ object ที่ส่งเข้ามาจัดการ reduce ตัวเอง
        return source.reduce(unit)


def grams(amount):
    return Quantity(amount, "g")