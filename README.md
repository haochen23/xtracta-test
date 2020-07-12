# Test Demo for Extracting and Matching Supplier Name in OCR Extracted TXT files

## Demo Notebook

You can refer to this [demo notebook](https://colab.research.google.com/drive/10ckSJRa4o5f8ma_h4aF2Q1TCp28r9L4V?usp=sharing) on how to use the code.

## Usage:

First clone and cd to the repo
```
git clone https://github.com/haochen23/xtracta-test.git
cd xtracta-test
```

__Run the Demo__ in command line:

```python
# windows
python demo.py --invoice ./inputs/invoice.txt, --suppliernames ./inputs/suppliernames.txt

# Or linux
python3 demo.py --invoice ./inputs/invoice.txt, --suppliernames ./inputs/suppliernames.txt
```
or simply using default arguments

```python
#windows
python demo.py

#Or linux
python3 demo.py
```

## Fuctions

There are two main functions in the `utils.py`:
- `read_process_invoice(invoice_txt)` Read and process invoice.txt and return a list object contains words in the same line in the invoice
- `find_match(invoice_words, supplier_txt, batch_size = 1000)` Finds loop through the supplier names in suppliernames.txt and return a match (if found)in the invoice. We set a batch_size=1000 to process 1000 line at a time. It is useful in reading large size files.

__Assumptions__:
1. I assume invoice.txt is small that can be read directly, so I did not add a batch_size for `read_process_invoice` function.
2. I assume suppliername.txt can be very large, so using a defined batch_size=1000 to process it.

