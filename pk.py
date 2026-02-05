"""
Primary Key (PK) Implementation
A simple demonstration of primary key concepts in Python.
"""


class PKManager:
    """
    A simple Primary Key manager that demonstrates PK concepts.
    Manages unique identifiers for records.
    """
    
    def __init__(self):
        """Initialize the PK manager with an empty registry."""
        self._registry = {}
        self._next_id = 1
    
    def create_pk(self):
        """
        Generate a new primary key.
        
        Returns:
            int: A unique primary key
        """
        pk = self._next_id
        self._next_id += 1
        return pk
    
    def register(self, pk, data):
        """
        Register data with a primary key.
        
        Args:
            pk (int): The primary key
            data: The data to associate with the PK
            
        Returns:
            bool: True if registration successful, False if PK already exists
        """
        if pk in self._registry:
            return False
        self._registry[pk] = data
        return True
    
    def get(self, pk):
        """
        Retrieve data by primary key.
        
        Args:
            pk (int): The primary key to look up
            
        Returns:
            The data associated with the PK, or None if not found
        """
        return self._registry.get(pk)
    
    def exists(self, pk):
        """
        Check if a primary key exists.
        
        Args:
            pk (int): The primary key to check
            
        Returns:
            bool: True if the PK exists, False otherwise
        """
        return pk in self._registry
    
    def delete(self, pk):
        """
        Delete a record by primary key.
        
        Args:
            pk (int): The primary key to delete
            
        Returns:
            bool: True if deletion successful, False if PK not found
        """
        if pk in self._registry:
            del self._registry[pk]
            return True
        return False
    
    def get_all_pks(self):
        """
        Get all registered primary keys.
        
        Returns:
            list: List of all primary keys
        """
        return list(self._registry.keys())


def main():
    """Example usage of PKManager."""
    manager = PKManager()
    
    # Create and register some records
    pk1 = manager.create_pk()
    manager.register(pk1, {"name": "Alice", "age": 30})
    
    pk2 = manager.create_pk()
    manager.register(pk2, {"name": "Bob", "age": 25})
    
    # Retrieve data
    print(f"PK {pk1}: {manager.get(pk1)}")
    print(f"PK {pk2}: {manager.get(pk2)}")
    
    # Check existence
    print(f"PK {pk1} exists: {manager.exists(pk1)}")
    
    # Delete a record
    manager.delete(pk1)
    print(f"After deletion, PK {pk1} exists: {manager.exists(pk1)}")
    
    # Show all PKs
    print(f"All PKs: {manager.get_all_pks()}")


if __name__ == "__main__":
    main()
