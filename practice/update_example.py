'''
Update

SQL commands:

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
'''

#SQLAlchemy ORM:
user = User.query.get(some_id)
user.name = 'Some new name'
db.session.commit()


#jinja if statement == Python if statement
{% if users %}
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
{% endif %}
