from app import create_app, db
from app.utils.seed_data import seed_products
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

@app.cli.command('seed-db')
def seed_db():
    """Seed the database with initial data."""
    seed_products()

if __name__ == '__main__':
    app.run(debug=True) 