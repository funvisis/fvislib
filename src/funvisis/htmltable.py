"""
API to work with an HTML compatible table as a list of dicts or a list of
tuples.

An HTML compatible table is an HTML table with simple layout: A row for each
register and a column for each field.

Optionally an unique header for each field. If the headers are present, indexing
is like dicts, otherwise is like tuples.

Example (doctest valid):

>>> import htmltable
>>> html = "<table>\\n" \
"<tr><td>1</td><td>Jesus</td><td>1234</td><td>2</td></tr>\\n" \
"<tr><td>2</td><td>Angela</td><td>4321</td><td>1</td></tr>\\n" \
"</table>"

>>> tuples_table = htmltable.HTMLTable(html).table
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
>>> html = "<table>\\n" \
"<tr><th>id</th><th>name</th><th>official_id</th><th>related_to</th></tr>\\n" \
"<tr><td>1</td><td>Jesus</td><td>1234</td><td>2</td></tr>\\n" \
"<tr><td>2</td><td>Angela</td><td>4321</td><td>1</td></tr>\\n" \
"</table>"  
>>> dicts_table = htmltable.HTMLTable(html).table
>>> angela = dicts_table[1]
>>> angela["name"]
'Angela'
>>>

This code assume that the html passed contains only one table (ideally, only the
chunk beggining with <table> and ending with </table>. You can extract all the 
tables from an html with Beautifulsoup4 findall method::

    Beautifulsoup4.findall('table')
"""

from xml.etree import ElementTree as ET

class HTMLTable(object):

    def __init__(self, html):
        """
        http://stackoverflow.com/a/7315891/344501
        """
        self.table = []
        table = ET.XML(html)
        rows = iter(table)
        if any(column.tag == 'th' for row in table for column in row):
            headers = [col.text for col in next(rows)]
            for row in rows:
                self.table.append(dict(zip(headers, (col.text for col in row))))
        else:
            for row in rows:
                self.table.append(tuple(col.text for col in row))
