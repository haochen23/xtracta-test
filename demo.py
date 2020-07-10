
'''
    demo for extract supplier name from ./inputs/invoice.txt, and
    find matched supplier name from ./inputs/suppliernames.txt
    
    Usage: python demo.py --invoice ./inputs/invoice.txt, --suppliernames ./inputs/suppliernames.txt
'''

import config
import utils
import argparse

# set argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--invoice", type=str,
                default="./inputs/invoice.txt",
                help="path to invoice.txt")
ap.add_argument("-s", "--suppliernames", type=str,
                default="./inputs/suppliernames.txt",
                help="path to suppliernames.txt")

args = vars(ap.parse_args())

if __name__ == "__main__":
    supplier_name = utils.extract_sup_name(args["invoice"])
    assert supplier_name == "Demo Company"
    print("Extracted Supplier Name is {}".format(supplier_name))
    supplier_id = utils.find_match(args["suppliernames"], supplier_name, 
                                   config.BATCH_SIZE)
    assert supplier_id == "3153303"