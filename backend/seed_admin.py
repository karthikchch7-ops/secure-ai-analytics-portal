# Simple script to seed an admin user in the database
import os
from backend.app.database import SessionLocal, engine
from backend.app import models, security

models.Base.metadata.create_all(bind=engine)

DB = SessionLocal()
email = os.environ.get('SEED_ADMIN_EMAIL','admin@example.com')
password = os.environ.get('SEED_ADMIN_PASSWORD','Admin@123')

existing = DB.query(models.User).filter(models.User.email==email).first()
if existing:
    print('Admin already exists')
else:
    admin = models.User(email=email, hashed_password=security.get_password_hash(password), is_admin=True)
    DB.add(admin)
    DB.commit()
    print('Admin user created:', email)
