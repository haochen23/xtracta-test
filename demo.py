
'''
    demo for extract supplier name from ./inputs/invoice.txt, and
    find matched supplier name from ./inputs/suppliernames.txt
    
    Usage: python demo.py --invoice ./inputs/invoice.txt, --suppliernames ./inputs/suppliernames.txt
'''

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
    invoice_path = "./inputs/invoice.txt"
    supplier_path = "./inputs/suppliernames.txt"
    invoice_words = utils.read_process_invoice(invoice_path)
    supplier_name = utils.find_match(invoice_words, supplier_path, batch_size=1000)
    assert supplier_name == "Demo Company"
    print("Matched Supplier Name is {}".format(supplier_name))
    
    