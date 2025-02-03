# Short Name Generator

A simple Python program that generates name initials by taking the first letter of the user's name and the first letter of their full name.

## Description
The program performs the following:
1. Prompts for user's name input
2. Prompts for user's full name input
3. Converts input names to uppercase
4. Validates the inputs
5. Creates initials from the first letter of each name

## Requirements
- Python 3.x

## How to Use
1. Run the program:
```bash
python ShortName.py
```

2. Follow the on-screen instructions:
   - Enter your name
   - Enter your full name

## Usage Example
```
== Welcome To The Short Name Gen ==

Enter Your Name: John
Enter Your Full Name: John Smith
```
The result will be:
```
J,J
```

## Error Checking
The program checks for:
- Empty name inputs
- Inputs containing only spaces

## Notes
- All input letters are automatically converted to uppercase
- The initials are separated by a comma (",")

## Contributing
You can contribute to the program development by:
- Adding additional formatting options
- Improving input validation
- Adding support for different languages
- Adding options to customize the separator between letters

## Features That Could Be Added
- Allow custom separator instead of comma
- Add support for middle names
- Add option to choose letter case (uppercase/lowercase)
- Implement input length validation
- Add option to save results to a file

## Known Issues
- No handling for special characters
- No limit on input length
- No validation for numeric inputs

## License
This program is available for free use and modification.

## Authors
[Your Name/Organization]

## Version
1.0.0
