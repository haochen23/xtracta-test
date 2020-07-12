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

__Running the Tests__:

Run the tests to test functions in `utils.py`.
```python
#windows
python -m pytest

# Or linux
python3 -m pytest
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