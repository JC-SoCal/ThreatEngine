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

def test_isFile_good_files():
  for f in [file_csv1,file_log1,file_pcap1,file_pcap2,file_txt]:
    assert teFileHandler.isFile(f) == True

def test_isFile_bad_files():
  for f in [file_doc1,file_xls1]:
    assert teFileHandler.isFile(f) == False    

def test_isFile_directories():    
  for d in [dir_parent,dir_bad_files,dir_csv_files,dir_log_files,dir_mixed_files,dir_pcap_files,dir_txt_files]:
    assert teFileHandler.isFile(d) == False