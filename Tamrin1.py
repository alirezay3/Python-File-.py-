class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def get_element_at_index(self, index):
        if index < len(self.queue):
            return self.queue[index]
        else:
            return "Index out of range"

    def is_empty(self):
        return len(self.queue) == 0

def get_user_input():
    print("Choose an operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Get element at index")
    print("4. Exit")
    return int(input("Enter your choice (1-4): "))

my_queue = MyQueue()

while True:
    choice = get_user_input()

    if choice == 1:
        item = input("Enter the item to enqueue: ")
        my_queue.enqueue(item)
        print(f"Item '{item}' enqueued.")

    elif choice == 2:
        item = my_queue.dequeue()
        print(f"Dequeued item: {item}")

    elif choice == 3:
        index = int(input("Enter the index: "))
        element = my_queue.get_element_at_index(index)
        print(f"Element at index {index}: {element}")

    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please enter a valid option (1-4).")
