from fastapi import FastAPI
app=FastAPI()
Users={}

@app.get('/')
def root():
  return {"Hello":"World"}

@app.post('/login')
def login(user:str):
  Users.append(user)
  return Users

@app.post('/Signup')
def SignUp(users)





