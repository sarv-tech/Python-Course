class laptop:
    storage_type = "SSD"    # Class Attribute

    def __init__(self, RAM, storage):
        self.RAM = RAM          # Instance Attribute
        self.storage = storage
    
    def get_info(self):    # Instance Methods
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = laptop("8GB", "512GB")
l2 = laptop("16GB", "256")

l1.get_info()