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

def test_getStats_dir_parent_recur():
  status,files = teFileHandler.getFilesFromDirectory(dir_parent, True)
  sortedFiles = teFileHandler.sortFilesByType(files)
  assert teFileHandler.getStats(sortedFiles) == [{'domains': 1, 'ips': 8, 'filename': ['test_data\\mixed_files\\pcap1.pcap']}, {'domains': 2, 'ips': 23, 'filename': ['test_data\\mixed_files\\pcap2.pcap']}, {'domains': 1, 'ips': 8, 'filename': ['test_data\\pcap_files\\pcap1.pcap']}, {'domains': 2, 'ips': 23, 'filename': ['test_data\\pcap_files\\pcap2.pcap']}, {'domains': 1, 'ips': 3, 'md5hashes': 3, 'sha1hashes': 3, 'filename': 'test_data\\csv_files\\csv1.csv'}, {'domains': 0, 'ips': 6, 'md5hashes': 0, 'sha1hashes': 0, 'filename': 'test_data\\log_files\\log1.log'}, {'domains': 1, 'ips': 3, 'md5hashes': 3, 'sha1hashes': 3, 'filename': 'test_data\\mixed_files\\csv1.csv'}, {'domains': 0, 'ips': 6, 'md5hashes': 0, 'sha1hashes': 0, 'filename': 'test_data\\mixed_files\\log1.log'}, {'domains': 2, 'ips': 6, 'md5hashes': 6, 'sha1hashes': 5, 'filename': 'test_data\\mixed_files\\txt1.txt'}, {'domains': 2, 'ips': 6, 'md5hashes': 6, 'sha1hashes': 5, 'filename': 'test_data\\txt_files\\txt1.txt'}]