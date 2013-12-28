import sys
sys.path.append("../")

import unittest
import teFileHandler

file_csv1 = "test_data\\csv_files\\csv1.csv"
file_log1 = "test_data\\log_files\\log1.log"
file_pcap1 = "test_data\\pcap_files\\pcap1.pcap"
file_pcap2 = "test_data\\pcap_files\\pcap1.pcap"
file_txt = "test_data\\txt_files\\txt1.txt"

file_doc1 = "test_data\\bad_files\\bad1.docx"
file_xls1 = "test_data\\bad_files\\bad2.xlsx"

dir_parent = "test_data"
dir_bad_files = "test_data\\bad_files"
dir_csv_files = "test_data\\csv_files"
dir_log_files = "test_data\\log_files"
dir_mixed_files = "test_data\\mixed_files"
dir_pcap_files = "test_data\\pcap_files"
dir_txt_files = "test_data\\txt_files"

# setup test env:
# Clear anything left behind
# Create directories
# Populate with files
def setup_module():
  import dataSetup
  dataSetup.DeleteAll()
  dataSetup.CreateDirectories()
  dataSetup.CreateAllFiles()

# Teardown Env:
# Delete everything
def teardown_module():
  import dataSetup
  dataSetup.DeleteAll()

def test_isPcapFile_pcap_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_pcap_files)
  for f in files:
    assert teFileHandler.isPcapFile(f) == True

def test_isPcapFile_csv_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_csv_files)
  for f in files:
    assert teFileHandler.isPcapFile(f) == False

def test_isPcapFile_log_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_log_files)
  for f in files:
    assert teFileHandler.isPcapFile(f) == False

def test_isPcapFile_txt_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_txt_files)
  for f in files:
    assert teFileHandler.isPcapFile(f) == False    

def test_isPcapFile_bad_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_bad_files)
  for f in files:
    assert teFileHandler.isPcapFile(f) == False    
# import dataSetup
# dataSetup.DeleteAll()
# dataSetup.CreateDirectories()
# dataSetup.CreateAllFiles()

# test_isPcapFile_pcaps()

# dataSetup.DeleteAll()

# # Make sure the parent dir is a dir, and no files found
# def test_getFilesFromDirectory_dir_parent():
#   assert teFileHandler.getFilesFromDirectory(dir_parent) == (True, [])

# # find all the files recursivly from the parent dir
# def test_getFilesFromDirectory_dir_parent_recurs():
#   assert teFileHandler.getFilesFromDirectory(dir_parent, True) == (True, ['test_data\\csv_files\\csv1.csv', 'test_data\\log_files\\log1.log', 'test_data\\mixed_files\\csv1.csv', 'test_data\\mixed_files\\log1.log', 'test_data\\mixed_files\\pcap1.pcap', 'test_data\\mixed_files\\pcap2.pcap', 'test_data\\mixed_files\\txt1.txt', 'test_data\\pcap_files\\pcap1.pcap', 'test_data\\pcap_files\\pcap2.pcap', 'test_data\\txt_files\\txt1.txt']) 

# # find all the pcap files in the pcap dir
# def test_getFilesFromDirectory_dir_pcap_files():
#   assert teFileHandler.getFilesFromDirectory(dir_pcap_files) == (True, ['test_data\\pcap_files\\pcap1.pcap', 'test_data\\pcap_files\\pcap2.pcap'])