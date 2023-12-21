class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        if not self.head:
            self.head = Node(coeff, power)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(coeff, power)

    def delete(self, power):
        current = self.head
        if current.power == power:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.power != power:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def print(self):
        current = self.head
        while current:
            print(f"{current.coeff}x^{current.power}", end = " ")
            current = current.next
        print()

    def add(self, other):
        p1 = self.head
        p2 = other.head
        sum_poly = Polynomial()
        while p1 and p2:
            if p1.power > p2.power:
                sum_poly.insert(p1.coeff, p1.power)
                p1 = p1.next
            elif p1.power < p2.power:
                sum_poly.insert(p2.coeff, p2.power)
                p2 = p2.next
            else:
                sum_poly.insert(p1.coeff + p2.coeff, p1.power)
                p1 = p1.next
                p2 = p2.next
        while p1:
            sum_poly.insert(p1.coeff, p1.power)
            p1 = p1.next
        while p2:
            sum_poly.insert(p2.coeff, p2.power)
            p2 = p2.next
        return sum_poly

    def mul(self, other):
        p1 = self.head
        mul_poly = Polynomial()
        while p1:
            p2 = other.head
            while p2:
                mul_poly.insert(p1.coeff * p2.coeff, p1.power + p2.power)
                p2 = p2.next
            p1 = p1.next
        return mul_poly

def main():
    poly1 = Polynomial()
    poly2 = Polynomial()

    print("Enter the coefficients and powers for the first polynomial:")
    while True:
        coeff = int(input("Enter coefficient: "))
        power = int(input("Enter power: "))
        poly1.insert(coeff, power)
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break

    print("Enter the coefficients and powers for the second polynomial:")
    while True:
        coeff = int(input("Enter coefficient: "))
        power = int(input("Enter power: "))
        poly2.insert(coeff, power)
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break

    while True:
        print("Choose an operation: 1 insert, 2 delete, 3 print, 4 add, 5 mul, 6 exit")
        operation = int(input("Your choice: "))
        if operation == 1:
            coeff = int(input("Enter coefficient: "))
            power = int(input("Enter power: "))
            poly1.insert(coeff, power)
        elif operation == 2:
            power = int(input("Enter power: "))
            poly1.delete(power)
        elif operation == 3:
            poly1.print()
        elif operation == 4:
            sum_poly = poly1.add(poly2)
            sum_poly.print()
        elif operation == 5:
            mul_poly = poly1.mul(poly2)
            mul_poly.print()
        elif operation == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()