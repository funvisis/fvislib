"""
API to work with an HTML compatible table as a list of dicts or a list of
tuples.

An HTML compatible table is an HTML table with simple layout: A row for each
register and a column for each field.

Optionally an unique header for each field. If the headers are present, indexing
is like dicts, otherwise is like tuples.

Example:

>>> import htmltable
>>> html = \"""
<table>
<tr><td>1</td><td>Jesus</td><td>1234</td><td>2</td></tr>
<tr><td>2</td><td>Angela</td><td>4321</td><td>1</td></tr>
<table>
\"""
>>> tuples_table = htmltable.HTMLTable(html)
>>> tuples_table[0]
('1', 'Jesus', '1234', '2')
>>> tuples_table[1]
('2', 'Angela', '4321', '1')
>>> angela = tuples_table[1]
>>> angela[2]
'4321'
>>> angela["name"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tuple indices must be integers, not str
>>> html = \"""
<table>
<tr><th>id</th><th>name</th><th>official_id</th><th>related_to</th></tr>
<tr><td>1</td><td>Jesus</td><td>1234</td><td>2</td></tr>
<tr><td>2</td><td>Angela</td><td>4321</td><td>1</td></tr>
<table>
\"""
>>> dicts_table = htmltable.HTMLTable(html)
>>> angela = dicts_table[1]
>>> angela["name"]
'Angela'
>>>
"""
