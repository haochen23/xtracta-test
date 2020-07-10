'''
General Configuaration, including:
    Path for input data,
    line, position, page constants to locate supplier name
'''

# invoice txt path
INVOICE_FILE_PATH = './inputs/invoice.txt'
# suppliernames file path
SUPPLIER_FILE_PATH = './inputs/suppliernames.txt'

# line_id to find supplier name
LINE_LOCATOR = 4
# pos_id to find supplier name
POS_LOCATOR = [0, 1]
# page_id to find supplier name
PAGE_LOCATOR = 1

# batch size in processing suppliernames.txt
BATCH_SIZE = 1000