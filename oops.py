class Node(self, name, id, type):
    def __init__(self):
        self.name = name
        self.id = id
        self.type = type

    def get_name(self):
        print(f"name is {self.name}")