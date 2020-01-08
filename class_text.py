#!: coding:utf-8
# 三到四

def __init__(self, name, weight, high):
    self.name = weight
    self.weight = weight
    self.high = high
def update_weight(self, weight):
    self.weight = weight

cls_dict = {
    '__init__': __init__,
    'update_weight': update_weight
}

import types
Person = types.new_class("Person", (), {}, lambda ns: ns.update(cls_dict))
Person.__module__ = __name__
if __name__ == "__main__":
    p = Person("23333", 50, 170)
    print(dir(p))
    p.update_weight(30)
    print(p.weight)