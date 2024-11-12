def get_soc_sec_tax(gross_pay):
    tax_rate = 6.2 / 100  # 6.2% tax rate
    return round(gross_pay * tax_rate, 2)

def get_medicare_tax(gross_pay):
    tax_rate = 1.45 / 100  # 1.45% tax rate
    return round(gross_pay * tax_rate, 2)

def get_federal_tax(gross_pay, withholding_code):

    if withholding_code == 0:
        tax_rate = 23 / 100 
    elif withholding_code == 1:
        tax_rate = 21 / 100
    elif withholding_code == 2:
        tax_rate = 19.5 / 100
    elif withholding_code == 3:
        tax_rate = 18.5 / 100
    elif withholding_code >= 4:
        tax_rate = 18 / 100 - (0.005 * (withholding_code - 4))
    else:
        return "Invalid witholding code"

    return round(gross_pay * tax_rate, 2)


# Example calculations for 3 persons

# Person 1
gross_pay_1 = 750
withholding_code_1 = 0
print(f'''
Person1:  gross pay ${gross_pay_1}  witholding code {withholding_code_1}

Social Security Tax: ${get_soc_sec_tax(gross_pay_1)}
Medicare Tax: ${get_medicare_tax(gross_pay_1)}
Federal Tax: ${get_federal_tax(gross_pay_1, withholding_code_1)}
''')

# Person 2
gross_pay_2 = 1550
withholding_code_2 = 2
print(f'''Person2:  gross pay ${gross_pay_2}  witholding code {withholding_code_2}

Social Security Tax: ${get_soc_sec_tax(gross_pay_1)}
Medicare Tax: ${get_medicare_tax(gross_pay_1)}
Federal Tax: ${get_federal_tax(gross_pay_1, withholding_code_1)}
''')


# Person 3
gross_pay_3 = 1100
withholding_code_3 = 5
print(f'''Person3:  gross pay ${gross_pay_3}  witholding code {withholding_code_3}

Social Security Tax: ${get_soc_sec_tax(gross_pay_1)}
Medicare Tax: ${get_medicare_tax(gross_pay_1)}
Federal Tax: ${get_federal_tax(gross_pay_1, withholding_code_1)}
''')
