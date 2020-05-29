'''
Query methods in SQLAlchemy
'''

#SELECT * FROM ...;
MyModel.query.all()


#Fetch first result OR None
MyModel.query.first()


#SELECT * FROM ... WHERE ...;
MyModel.query.filter_by(my_table_attribute='some value')


#similar to filterby, but instead specify attributes on a given model
MyModel.query.filter(MyOtherModel.some_attr='some value')
OrderItem.query.filter(Product.id=3)


#ORDER BY
MyModel.order_by(MyModel.created_at)
MyModel.order_by(db.desc(MyModel.created_at))


#SLECT * FROM ... LIMIT 100;
Order.query.limit(100).all()


#SELECT COUNT(*) FROM ...;
query = Task.query.filter(completed=True)
query.count()


#get object by ID
model_id = 3
MyModel.query.get(model_id)


#Bulk delete
query = Task.query.filter_by(category='Archived')
query.delete()


#JOIN
Driver.query.join('vehicles')
