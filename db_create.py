from project import db

# create the database and db table
db.create_all()


# commit the changes
db.session.commit()
