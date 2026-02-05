"""
Unit tests for PK (Primary Key) implementation.
"""

import unittest
from pk import PKManager


class TestPKManager(unittest.TestCase):
    """Test cases for PKManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = PKManager()
    
    def test_create_pk_generates_unique_ids(self):
        """Test that create_pk generates unique sequential IDs."""
        pk1 = self.manager.create_pk()
        pk2 = self.manager.create_pk()
        pk3 = self.manager.create_pk()
        
        self.assertEqual(pk1, 1)
        self.assertEqual(pk2, 2)
        self.assertEqual(pk3, 3)
    
    def test_register_new_pk(self):
        """Test registering data with a new PK."""
        pk = self.manager.create_pk()
        data = {"name": "Test", "value": 123}
        
        result = self.manager.register(pk, data)
        
        self.assertTrue(result)
        self.assertEqual(self.manager.get(pk), data)
    
    def test_register_duplicate_pk_fails(self):
        """Test that registering a duplicate PK fails."""
        pk = self.manager.create_pk()
        self.manager.register(pk, "data1")
        
        result = self.manager.register(pk, "data2")
        
        self.assertFalse(result)
        self.assertEqual(self.manager.get(pk), "data1")
    
    def test_get_nonexistent_pk_returns_none(self):
        """Test that getting a non-existent PK returns None."""
        result = self.manager.get(999)
        self.assertIsNone(result)
    
    def test_exists_returns_correct_status(self):
        """Test that exists correctly identifies PK presence."""
        pk = self.manager.create_pk()
        
        self.assertFalse(self.manager.exists(pk))
        
        self.manager.register(pk, "data")
        self.assertTrue(self.manager.exists(pk))
    
    def test_delete_existing_pk(self):
        """Test deleting an existing PK."""
        pk = self.manager.create_pk()
        self.manager.register(pk, "data")
        
        result = self.manager.delete(pk)
        
        self.assertTrue(result)
        self.assertFalse(self.manager.exists(pk))
    
    def test_delete_nonexistent_pk_returns_false(self):
        """Test that deleting a non-existent PK returns False."""
        result = self.manager.delete(999)
        self.assertFalse(result)
    
    def test_get_all_pks(self):
        """Test retrieving all registered PKs."""
        pk1 = self.manager.create_pk()
        pk2 = self.manager.create_pk()
        pk3 = self.manager.create_pk()
        
        self.manager.register(pk1, "data1")
        self.manager.register(pk2, "data2")
        self.manager.register(pk3, "data3")
        
        all_pks = self.manager.get_all_pks()
        
        self.assertEqual(len(all_pks), 3)
        self.assertIn(pk1, all_pks)
        self.assertIn(pk2, all_pks)
        self.assertIn(pk3, all_pks)
    
    def test_get_all_pks_after_deletion(self):
        """Test that get_all_pks reflects deletions."""
        pk1 = self.manager.create_pk()
        pk2 = self.manager.create_pk()
        
        self.manager.register(pk1, "data1")
        self.manager.register(pk2, "data2")
        self.manager.delete(pk1)
        
        all_pks = self.manager.get_all_pks()
        
        self.assertEqual(len(all_pks), 1)
        self.assertEqual(all_pks[0], pk2)


if __name__ == "__main__":
    unittest.main()
