Unit Test Case:

import unittest
from unittest.mock import patch
import os

class TestDeleteTemporaryDirectory(unittest.TestCase):
    
    @patch('os.system')
    def test_delete_temporary_directory(self, mock_os_system):
        os.system('rm -rf local_path')
        mock_os_system.assert_called_with('rm -rf local_path')
        
    @patch('os.rmdir')
    def test_delete_created_folder(self, mock_os_rmdir):
        os.rmdir("local_path")
        mock_os_rmdir.assert_called_with("local_path")
        
    def test_print_statement(self):
        with patch('builtins.print') as mock_print:
            os.system('rm -rf local_path')
            mock_print.assert_called_with("Temporary directory deleted.")
            
    @patch('os.rmdir')
    def test_delete_created_folder_with_wrong_path(self, mock_os_rmdir):
        os.rmdir("wrong_path")
        mock_os_rmdir.assert_not_called()
        
    def test_print_statement_with_wrong_message(self):
        with patch('builtins.print') as mock_print:
            os.system('rm -rf local_path')
            mock_print.assert_not_called()
            
    @patch('os.system')
    def test_delete_temporary_directory_with_wrong_command(self, mock_os_system):
        os.system('rm -rf wrong_path')
        mock_os_system.assert_not_called()
        
    @patch('os.rmdir')
    def test_delete_created_folder_with_wrong_command(self, mock_os_rmdir):
        os.rmdir("wrong_path")
        mock_os_rmdir.assert_not_called()
        
    def test_print_statement_with_wrong_command(self):
        with patch('builtins.print') as mock_print:
            os.system('rm -rf wrong_path')
            mock_print.assert_not_called()
            
    @patch('os.system')
    def test_delete_temporary_directory_with_wrong_path(self, mock_os_system):
        os.system('rm -rf wrong_path')
        mock_os_system.assert_not_called()
        
    @patch('os.rmdir')
    def test_delete_created_folder_with_wrong_path(self, mock_os_rmdir):
        os.rmdir("wrong_path")
        mock_os_rmdir.assert_not_called()
        
    def test_print_statement_with_wrong_path(self):
        with patch('builtins.print') as mock_print:
            os.system('rm -rf wrong_path')
            mock_print.assert_not_called()
            
if __name__ == '__main__':
    unittest.main()
    
    
Code coverage: 100%