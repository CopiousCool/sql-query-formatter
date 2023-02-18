import re

def format_sql(query, style):
    if style == 'apexSQL':
        query = re.sub(r'\b(FROM|JOIN|WHERE|SET|VALUES|SELECT|INSERT INTO|UPDATE|DELETE FROM)\b', '\n\\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(AND|OR)\b', '\n\\1', query, flags=re.IGNORECASE)
        query = re.sub(r'(?<=[\s\(])\(', '\n(', query)
        return query

    elif style == 'compact':
        query = re.sub('\s+', ' ', query)
        return query
    
    elif style == 'Extended':
        query = re.sub(r'\b(FROM|JOIN|WHERE|SET|VALUES|SELECT|INSERT INTO|UPDATE|DELETE FROM)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(AND|OR)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'(?<=[\s\(])\(', '\n        (', query)
        return query

    elif style == 'MSDN SQL BOL':
        query = re.sub(r'\b(FROM|JOIN|WHERE|SET|VALUES|SELECT|INSERT INTO|UPDATE|DELETE FROM)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(AND|OR)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(ON)\b', '\n        \\1', query, flags=re.IGNORECASE)
        return query

    elif style == 'Oracle':
        query = re.sub(r'\b(FROM|JOIN|WHERE|SET|VALUES|SELECT|INSERT INTO|UPDATE|DELETE FROM)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(AND|OR)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(ON)\b', '\n        \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'(?<=[\s\(])\(', ' (', query)
        return query
        
    elif style == 'PostgreSQL':
        query = re.sub(r'\b(FROM|JOIN|WHERE|SET|VALUES|SELECT|INSERT INTO|UPDATE|DELETE FROM)\b', '\n    \\1', query, flags=re.IGNORECASE)
        query = re.sub(r'\b(AND|OR)\b', '\n    \\1', query, flags=re.IGNORECASE)
        return query

style_map = {
    '1': 'apexSQL',
    '2': 'compact',
    '3': 'Extended',
    '4': 'MSDN SQL BOL',
    '5': 'Oracle',
    '6': 'PostgreSQL'
}

query = input('Enter a SQL query: ')

print('Available styles:')
print('1. apexSQL')
print('2. compact')
print('3. Extended')
print('4. MSDN SQL BOL')
print('5. Oracle')
print('6. PostgreSQL')

style = input('Select a style number: ')

if style in style_map:
    formatted_query = format_sql(query, style_map[style])
    print(formatted_query)
else:
    print('Invalid style selection')

file_name = input('Enter the file name: ') + '.sql'
with open(file_name, 'w') as f:
    f.write(formatted_query)
