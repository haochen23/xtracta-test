# Test Demo for Extracting and Matching Supplier Name in OCR Extracted TXT files

## Usage:

__Run the Demo__:

```
python demo.py --invoice ./inputs/invoice.txt, --suppliernames ./inputs/suppliernames.txt
```
or simply using default arguments

```
python demo.py
```

## Fuctions

There are two main functions in the `utils.py`:
- `extract_sup_name(filepath)` Extracts supplier name from file, eg: ./inputs/invoice.txt
- `find_match(filepath, supplier_name, batch_size=config.BATCH_SIZE)` Finds matched supplier_name from file, eg: ./inputs/suppliernames.txt. We set a batch_size=config.BTACH_SIZE (which is 1000) to process 1000 line at a time. It is useful in reading large size files.

__Assumptions__:
1. I assume invoice.txt is small that can be read directly, so I did not add a batch_size for `extract_sup_name` function.
2. I assume suppliername.txt can be very large, so using a defined batch_size to process it.

## Limitations:
The extraction of supplier name process heavily relies on `'pos_id', 'line_id', 'page_id'` to identify the name of supplier (they are defined in `config.py`), which means changing the template structure of invoice would make my extraction function useless.

So we need a layout prediction model to predict the `'pos_id', 'line_id', 'page_id'` attributes for the supplier name.