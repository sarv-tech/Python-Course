class laptop:
    storage_type = "SSD"    # Class Attribute

    def __init__(self, RAM, storage):
        self.RAM = RAM          # Instance Attribute
        self.storage = storage
        
    @classmethod         # Class Decorator
    def get_storage_type(cls):        # Class Methods
        print(f"storage type = {cls.storage_type}")
    
    def get_info(self):    # Instance Methods
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = laptop("8GB", "512GB")

l1.get_storage_type()