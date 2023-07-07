class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step


couter1 = MyCounterV2(value=0, step=1)
print(couter1.value)

couter1.count_up()
print(couter1.value)

couter1.count_up()
print(couter1.value)

couter2 = MyCounterV2(value=0, step=3)
print(couter2.value)

couter2.count_up()
print(couter2.value)

couter2.count_up()
print(couter2.value)
