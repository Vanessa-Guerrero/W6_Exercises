# Function to get the supplier code (Before the colon)
def get_supplier_code(part_code):

    colon_index = part_code.find(":")   # finding index for colon

    return part_code[:colon_index]      # returns everything up till the colon index

# Function to get the product number (Between the colon and hyphen)
def get_product_num(part_code):

    colon_index = part_code.find(":")   
    hyphen_index = part_code.find("-")  # finding index for hyphen

    return part_code[colon_index + 1:hyphen_index]  # returns 1 + after the colon index up to the hyphen

# Function to get the size (After the hyphen)
def get_size(part_code):

    hyphen_index = part_code.find("-")

    return part_code[hyphen_index + 1:]         # returns 1 + after the hyphen index

# Test part codes
part_codes = ['ACME:123-L', 'DI:12345-M', 'ACE:1-12']

# Using a for loop to call the three part codes and display the results (using inspo from substrings.py)
for code in part_codes:
    supplier = get_supplier_code(code)
    product_num = get_product_num(code)
    size = get_size(code)

    # Converting size to the unabbreviated size text 
    if size == 'L':
        size = 'large'
    elif size == 'M':
        size = 'medium'
    elif size == 'S':
        size = 'small'
    else:             # returned as size if it's something else, in this case a #
        size = size

    # Capitlizing only the first letter of the supplier code if there's more than 2 characters
    if len(supplier) > 2: 
        supplier = supplier.capitalize()
    else:
        supplier = supplier

    print(f'{code.ljust(12)} Part #{product_num}, size {size}, supplied by {supplier}')