import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import config
import utils

def test_extract_sup_name():
    assert utils.extract_sup_name(config.INVOICE_FILE_PATH) == "Demo Company"
    
def test_find_match():
    assert utils.find_match(config.SUPPLIER_FILE_PATH, "Demo Company") == "3153303"
    assert utils.find_match(config.SUPPLIER_FILE_PATH, "Arbitrary XXXYYY") == ""
    assert utils.find_match(config.SUPPLIER_FILE_PATH, "") == ""