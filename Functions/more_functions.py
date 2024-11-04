def display_mailing_label(name, address1, city, state, zip_code, address2 = None):
# Display a formatted mailing label
    if address2 != None:  # Check if a second address line is provided
        print(f'''
{name}
{address1}
{address2}
{city}, {state} {zip_code}
''')
    else:
        print(f'''
{name}
{address1}
{city}, {state} {zip_code}
''')


