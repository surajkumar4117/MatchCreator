from fastapi import FastAPI
from pydantic import BaseModel
from mysql_connection import get_connection
import bcrypt



app=FastAPI()


class userSignup(BaseModel):
  name:str
  email:str
  password:str
  

@app.get('/')
def root():
  return {"Hello":"World"}

@app.post('/login')
def login(user:str):
  Users.append(user)
  return Users



@app.post('/signup')
def signup(user:userSignup):
  conn=get_connection()
  cursor = conn.cursor()
  try:
    query="select email from users where email=%s"
    value=(user.email,)
    cursor.execute(query,value)
    existing_user=cursor.fetchone()

    if existing_user:
      return {"message":"user already exits"}

    hashed=bcrypt.hashpw(user.password.encode('utf-8'),bcrypt.gensalt())
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (user.name, user.email, hashed.decode('utf-8'))
    
    cursor.execute(query,values)
    conn.commit()

    return {"message": "User created"}
  finally:
    cursor.close()
    conn.close()
    
  
  







