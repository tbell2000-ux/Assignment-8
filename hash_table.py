class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key: str, number: str):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
            return

        current = self.data[index]
        prev = None
        while current:
            if current.key == key:
                current.value.number = number
                return
            prev = current
            current = current.next
        prev.next = new_node

    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if not current:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}:", end="")
                while current:
                    print(f" - {current.value}", end="")
                    current = current.next
                print()  # new line


# Test your hash table implementation here.
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    print("\n--- Adding Contacts ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n--- Search Test ---")
    contact = table.search("John")
    print("Search result:", contact)

    print("\n--- Collision Handling Test ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  # may collide
    table.print_table()

    print("\n--- Duplicate Key Test ---")
    table.insert("Rebecca", "999-444-9999")  # update existing
    table.print_table()

    print("\n--- Search Missing Contact ---")
    print(table.search("Chris"))  # None


# A hash table is the right structure for fast lookups because it allows you to find data almost instantly using a key instead of searching through everything one by one.
# It uses a hash function to turn a key, like a name, into an index in an array. This makes operations like insert, search, and delete run in constant time on average, which is much faster than using a list or tree where you might have to go through multiple elements or nodes.
# The main idea is that the hash function directs you straight to where the data should be stored or found.
# To handle collisions, I used a method called separate chaining. This means that each index in the hash table can store a linked list of nodes if more than one key hashes to the same spot.
# When inserting a new contact, the program checks if the key already exists; if it does, it updates the value instead of creating a duplicate. If it doesn’t exist, it simply adds the new node to the end of the linked list at that index.
# This way, even if multiple contacts hash to the same location, they can all be stored without overwriting each other.
# An engineer might choose a hash table over a list or tree when they need very quick access to data using unique keys, like names or IDs.
# It’s especially useful when searching and inserting often, and when order doesn’t matter as much as speed.
