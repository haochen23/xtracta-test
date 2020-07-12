
'''
    demo for finding matched supplier name from ./inputs/suppliernames.txt
    in the ./inputs/invoice.txt
    
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
    # path to invoice.txt
    invoice_path = "./inputs/invoice.txt"
    
    # path to suppliernames.txt
    supplier_path = "./inputs/suppliernames.txt"
    
    # read and process invoice
    invoice_words = utils.read_process_invoice(invoice_path)
    
    # find matched supplier name in the invoice
    supplier_name = utils.find_match(invoice_words, supplier_path, batch_size=1000)
    
    assert supplier_name == "Demo Company"
    if supplier_name:
        print("Matched Supplier Name is {}.".format(supplier_name))
    else:
        print("Match not found.")
    
    