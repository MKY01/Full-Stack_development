#Overall Steps to Set Up & Run Migrations

##1. Bootstrap database migrate commands:
link to the Flask app models and database, link to command line scripts for running migrations,
set up folders to store migrations (as versions of the database)
See the __pycache__ folder


##2. Run initial migration to create tables for SQLAlchemy models, recording the initial schema:
ala git init && first git commit. Replaces use of db.create_all()

###$flask db init
Create initial migrations directory structure.


##3. Migrate on changes to our data models
  - Make changes to the SQLAlchemy models
  - Allow Flask-Migrate to auto-generate a migration script based on the changes
  - Fine-tune the migration scripts
  - Run the migration, aka “upgrade” the database schema by a “version”

##$flask db migrate
Detects the model changes to be made, and creates a migration file with upgrade and downgrade logic set up.
migrate = Migrate(app,db)

###$flask db upgrade
Runs the upgrade command in the migration file, to apply the migration.

(optionally)
###$flask db downgrade
Runs the downgrade command in the migration file, to roll back the migration.
