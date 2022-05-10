from table import roman_numerals_table

def main():
    """
        Serves as the main entry point of the application.
    """

    arabic_number = input("Enter an arabic (decimal) number: ").strip()
    roman_numeral = convert(arabic_number)
    if (roman_numeral == None):
        print("\nError: Can't convert empty or non-digit values.")
        return

    if not (roman_numeral.strip()):
        print(f"\nNo roman numeral equivalent exists for the number {arabic_number}.")
        return

    print(f"\nThe roman numeral equivalent of the number {arabic_number} is {roman_numeral}.")
    return

def convert(arabic_number: str):
    """
        Converts an arabic (decimal) number to its roman numeral equivalent.
    """

    if not (arabic_number.lstrip('-').isdigit()):
        return None
    
    roman_equivalent = ""
    arabic_number = int(arabic_number)
    if (arabic_number > 0):
        numerals = []
        while (arabic_number != 0):            
            for value, symbol in roman_numerals_table:                
                if (value <= arabic_number):                    
                    numerals.append(symbol)
                    arabic_number -= value
                    break
                pass

            pass

        roman_equivalent = roman_equivalent.join(numerals)
        pass

    return roman_equivalent

if __name__ == "__main__":
    main()
    pass