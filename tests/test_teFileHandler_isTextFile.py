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

def test_isTextFile_csv_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_csv_files)
  for f in files:
    assert teFileHandler.isTextFile(f) == True

def test_isTextFile_log_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_log_files)
  for f in files:
    assert teFileHandler.isTextFile(f) == True

def test_isTextFile_txt_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_txt_files)
  for f in files:
    assert teFileHandler.isTextFile(f) == True

def test_isTextFile_bad_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_bad_files)
  for f in files:
    assert teFileHandler.isTextFile(f) == False

def test_isTextFile_pcap_files():
  status, files = teFileHandler.getFilesFromDirectory(dir_pcap_files)
  for f in files:
    assert teFileHandler.isTextFile(f) == False