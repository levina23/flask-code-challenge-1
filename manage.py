from app import create_app, db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from app.models import Restaurant,Restaurant_pizza,Pizzas



app=create_app()
migrate=Migrate(app,db)
manager=Manager(app)

manager.add_command('db', MigrateCommand)
@manager.command
def make_shell_context():
    return dict(db=db, Restaurant=Restaurant, Pizzas=Pizzas, Restaurant_pizza=Restaurant_pizza)

if __name__ == '__main__':
    manager.run()