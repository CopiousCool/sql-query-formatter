# sql-qyey-formater
 A Python script to format SQL query based on a selected style. Available styles: 1. apexSQL 2. compact 3. Extended 4. MSDN SQL BOL 5. Oracle 6. PostgreSQL

# Name
format_sql - A Python function to format SQL query based on a selected style.

# Description
The format_sql function takes two arguments - query and style. The query argument is a string containing SQL code that needs to be formatted. The style argument is a string that represents the selected formatting style. The function applies specific regex patterns based on the selected formatting style and returns the formatted SQL code.

The script also provides a dictionary style_map that maps the style number to the actual style name. The script prompts the user to select a formatting style by printing out the available styles and asking the user to enter a style number. Once the user selects a style, the script calls the format_sql function with the selected style and the user's SQL code as arguments.

The formatted SQL code is then printed to the console for the user to verify. The user is then prompted to enter a file name to save the formatted SQL code. If the file name is valid, the formatted SQL code is saved to a file with the given name and .sql extension.

# Functions
format_sql(query: str, style: str) -> str:

# Parameters:
query (str): A string containing SQL code that needs to be formatted.
style (str): A string that represents the selected formatting style.
Returns:
A string representing the formatted SQL code.
Variables
style_map:

A dictionary that maps style number to style name.
query:

A string containing SQL code entered by the user.
style:

A string representing the selected formatting style entered by the user.
formatted_query:

A string representing the formatted SQL code returned by format_sql function.
file_name:

A string representing the name of the file where the formatted SQL code is saved.
External Libraries
re: A built-in module in Python that provides support for regular expressions.

# Usage
The script can be run using Python 3.x. Upon running the script, the user is prompted to enter SQL code and select a formatting style. The script then formats the SQL code based on the selected style and prints the formatted SQL code to the console. The user is prompted to enter a file name to save the formatted SQL code.

Note: The script assumes that the user will enter a valid file name and extension. If an invalid file name is entered, the script will raise an exception.
