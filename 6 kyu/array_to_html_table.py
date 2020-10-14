'''
Overview
The task is simple - given a 2D array (list), generate an HTML table representing the data from this array.

You need to write a function called to_table/toTable, that takes three arguments:

data - a 2D array (list),
headers - an optional boolean value. If True, the first row of the array is considered a header (see below). Defaults to False,
index - an optional boolean value. If True, the first column in the table should contain 1-based indices of the corresponding row. If headers arguments is True, this column should have an empty header. Defaults to False.
and returns a string containing HTML tags representing the table.
The table header is optional. If header argument is False then the table starts with <tbody> tag, ommiting <thead>.

So, for example:

to_table([["lorem", "ipsum"], ["dolor", "sit amet"]], True, True)
returns

"<table><thead><tr><th></th><th>lorem</th><th>ipsum</th></tr></thead><tbody><tr><td>1</td><td>dolor</td><td>sit amet</td></tr></tbody></table>"
As you can see, no linebreaks or whitespaces (except for the ones present in the array values) are included, so the HTML code is minified.

IMPORTANT NOTE: if the value in the array happens to be None, the value of the according cell in the table should be en ampty string ("")! Otherwise, just use a string representation of the given value, so, dependent on the language, the output can be slightly different. No additional parsing is needed on the data.
'''
def to_table(data, header=False, index=False):
    output = '<table>'
    if header==True:
        body = data[1::]
        output+='<thead><tr>'
        if index == True:
            output+='<th></th>'
        for el in data[0]:
            output+='<th>{}</th>'.format(el)
        output+='</tr></thead>'
    else:
        body = data
    output+='<tbody>'
    for i,el in enumerate(body):
        output+='<tr>'
        if index==True:
                output+='<td>{}</td>'.format(i+1)
        for x in el:
            if x == None:
               output+='<td></td>'
            else:
                output+='<td>{}</td>'.format(x)
        output+='</tr>'
    output+='</tbody></table>'
    return output
