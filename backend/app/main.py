from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, security, auth, database
from .database import engine
from datetime import timedelta

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure AI Analytics Portal - Backend")

@app.post('/auth/register', response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(auth.get_db)):
    db_user = auth.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = security.get_password_hash(user.password)
    new = models.User(email=user.email, hashed_password=hashed, is_admin=False)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@app.post('/auth/token', response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(auth.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get('/users/me', response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user

@app.post('/train')
def train_demo(current_user: models.User = Depends(auth.get_current_active_user)):
    # Placeholder for training pipeline. In notebooks we provide training code.
    return {"status": "training started (demo placeholder)", "user": current_user.email}

@app.post('/predict')
def predict_demo(data: dict, current_user: models.User = Depends(auth.get_current_active_user)):
    # Placeholder: echo input
    return {"prediction": "demo", "input": data}
