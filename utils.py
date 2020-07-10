import config
import ast
from itertools import islice

def extract_sup_name(filepath):
    '''
        Extract supplier name from file, 
        input: filepath for invoice.txt eg: ./inputs/invoice.txt
        return: supplier_name as a string
    '''
    #lines contain supplier name
    sup_name_lines = []
    supplier_name = " "
    
    with open(config.INVOICE_FILE_PATH, 'r') as f:
        for line in f:
            try:
                line = ast.literal_eval(line)
                if (line["page_id"] == config.PAGE_LOCATOR and
                    line["line_id"] == config.LINE_LOCATOR and
                    line["pos_id"] in config.POS_LOCATOR):
                    sup_name_lines.append(line)
            except:
                pass
    if sup_name_lines is not None:
        # sort sup_name_lines by pos_id
        sup_name_lines = sorted(sup_name_lines, key = lambda i: i["pos_id"])
        for line in sup_name_lines:
            supplier_name += line["word"] +' '
    return supplier_name.strip()

def find_match(filepath, supplier_name, batch_size=config.BATCH_SIZE):
    '''
        find match of supplier_name in file eg: in ./inputs/suppliernames.txt
        inputs: 
            -filepath: path to suppliernames.txt
            -supplier_name: string of supplier name
        return:
            -supplier_id: matched supplier_id 
    '''
    supplier_id = ""
    
    with open(filepath, 'r') as f:
        while True:
            next_n_lines = list(islice(f,batch_size))
            if not next_n_lines:
                break

            for line in next_n_lines:
                line = line.strip().split(',')
                if line[1] == supplier_name:
                    supplier_id = line[0]
                    print("Found ID for supplier {}: {}".format(
                        supplier_name,
                        supplier_id))
                    return supplier_id
    if not supplier_id:
        print("The ID for supplier name of {} is not found.".format(supplier_name))

    return supplier_id
                    
