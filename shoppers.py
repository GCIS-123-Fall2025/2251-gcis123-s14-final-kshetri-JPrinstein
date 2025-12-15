"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ["__code","__name","__price"]

    def __init__(self,code,name,price):
        self.__code = code
        self.__name = name
        self.__price = price

    def get_code(self):
        return self.__code
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def is_equal(self,other):
        return self.__code == other.__code
    
    def __str__(self):
        output = '(' + str(self.__code) + ", " + str(self.__name) + ", " + str(self.__price) + ')'
        return output


# manual test from main() method
def main():     
  item1 = Item("ABCD-1234","Silky Camisole",24)
  item2 = Item("ABCD-1234","Test Item",13)
  item3 = Item("Woo-1234","Fresh Biscuit",12)

  print(item1)
  print(item2)
  print(item3)

  items = [str(item1),str(item3),str(item2)]
  print(items)

  items.sort()
  print(items)

  print(item1.is_equal(item2))

if __name__ == "__main__":    main()