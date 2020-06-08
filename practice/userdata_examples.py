'''
Getting user data in Flask, 3 methods fror getting user data from a view --> controller.

1. For URL query parameters listed as key-value pairs at the end of a URL, preceeding a "?".

2. For form input, use request.form to read the 'value' from a form input(text/number/password), by the 'name' attribute.

3. For data type application/json, user request.data. it retreives JSON as a string --> lists and dictionaries
'''

www.example.com/home?key=value
/foobar?field1=value1
value = request.args.get('field1')


request.form.get('<name>') #the name attribute on the input HTML element
username = request.form.get('username')
password = request.form.get('password')

#both requests.args.get and requests.form.get accept an optionaol 2nd parameter, set to a default value, in case it is empty.
request.args.get('foobar', 'default')


#request.data retreives JSON as a string, then call json.loads on it to turn it inot lists and dictionaries.
data_string = request.data
data_dictionary = json.loads(data_string)
