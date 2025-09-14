# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next 
        pass


'''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def add_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
        pass
    def print_list(self):
        temp = self.head
        if self.head is None:
            print("The Waitlist is empty.")
        else:
            while temp:
                print("Current Waitlist:")
                print(temp.name,  end='')
                temp = temp.next
            print()
    def add_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        print(f"{new_data} has been added to the end of the waitlist")
    def search(self, value):
        current = self.head
        position = 1
        while current:
            if current.name == value:
                return print(f"'{value}' found at position {position} in the waitlist")
            current = current.next
            position += 1
        return print(f"'{value}' is not found in the waitlist")
    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.name == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"'{value}' has been deleted from the waitlist")
                return
            prev = current
            current = current.next
        print(f"'{value}' could not be found on the waitlist")



'''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Addds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
            # Call the add_end method
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            # Call the remove method
            
            
        elif choice == "4":
            waitlist.print_list()
            # Print out the entire linked list using the print_list method.
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

waitlist_generator()

# Call the waitlist_generator function to start the program


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
# My list is a linked list, which means it uses methods to add in numerical order values, or in this case names, 
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
