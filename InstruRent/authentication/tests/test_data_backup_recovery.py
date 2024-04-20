from django.test import TestCase
from .utils import backup_database, restore_database

class DataBackupTestCase(TestCase):
    def test_database_backup(self):
        # Test the database backup function
        result = backup_database()
        self.assertTrue(result, "Backup should be successful")

    def test_database_restore(self):
        # Test the database restore function
        result = restore_database()
        self.assertTrue(result, "Restore should be successful")
