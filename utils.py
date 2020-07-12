'''
    util functions
        read_read_process_invoice(invoice_txt): 
            read and process invoice.txt file, return a list object 
            contains words from the same line in the invoice
    
        find_match(invoice_words, supplier_txt, batch_size = 1000):
            find a match (if found) of supplier name from suppliernames.txt 
            in the invoice.txt file
'''

import ast
from itertools import islice
import pandas as pd
def read_process_invoice(invoice_txt):
    '''
        Read invoice.txt, and return processed invoice
        input: 
            invoice_txt - path to invoice.txt file eg: ./inputs/invoice.txt
        return: 
            sameline_words - a list contains words from the same line in the invoice
    '''
    # initialize invoice lines 
    invoice = []
    word_list = []
    with open(invoice_txt, 'r') as f:
        for line in f:
            try:
                line = ast.literal_eval(line)
                invoice.append(line)
            except:
                pass
    # only keep "word", "pos_id", "line_id", "page_id" fields in word_list
    for item in invoice:
        word_list.append([item["word"], item["pos_id"], item["line_id"], item["page_id"]])
        
    invoice_df = pd.DataFrame(word_list, 
                              columns=["word", "pos_id", "line_id", "page_id"])
    # save all line_ids to find words in the same line
    invoice_line_ids = sorted(list(set(invoice_df["line_id"].values)))
    
    sameline_word_df = []
    for i in invoice_line_ids:
        sameline_word_df.append(
            # suppose supplier name appears on invoice page_id == 1
            invoice_df[(invoice_df["line_id"]==i).values & (invoice_df["page_id"]==1).values]
            )
    # words in the same line, a list of strings
    sameline_words = []
    for i in range(len(sameline_word_df)):
        sameline_word_df[i] = sameline_word_df[i].sort_values(by=["pos_id"])
        sameline_words.append(' '.join(sameline_word_df[i]["word"].tolist()))
    return sameline_words



def find_match(invoice_words, supplier_txt, batch_size = 1000):
    """
        find supplier name in suppliernames.txt matches in the inovice
        
        inputs:
            invoice_words - sameline_words in the invoice process by read_process_invoice()
            supplier_txt - path to suppliernames.txt eg. inputs/suppliernames.txt
            batch_size=1000 - process 1000 line in the suppliernames.txt at a time, to deal with large file
    """
    with open(supplier_txt, 'r') as f:
        # skip header line
        next(f)
        while True:
            next_n_lines = list(islice(f,batch_size))
            if not next_n_lines:
                break
            # read batch_size=1000 lines at a time
            for line in next_n_lines:
                supplier = line.strip().split(',')[1]       
                # find matched supplier
                for words in invoice_words:
                    if str(supplier) in words:
                        return supplier
    return None
                    
