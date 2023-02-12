###############################################
# Manage
# --------------------
# Run this file to initialize the database tables
#
###############################################

def deploy():
    """Run deployment tasks."""
    from createapp import create_app,db
    from models import Patterns

    app = create_app()
    app.app_context().push()

    # create database and tables
    db.create_all()

deploy()