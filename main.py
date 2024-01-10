from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
async def hello():
   return "Welcome to Yuvabe"
@app.get("/Welcome/default")
async def welcome():
  return "Hi, I am " + "Arthi"
@app.get("/Welcome/{name}")
async def welcome(name):
  return "Hi, I am " + name
@app.get("/book/{book_id}/{book_name}")
async def book(book_id:int, book_name):
  return "bookid:" + str(book_id) ,"bookname:" + book_name
@app.get("/books")
async def book(limit:int):
 a=[
        {"1001":"Python"},
        {"1002":"java"},
        {"1003":"HTML"}   
   ] 
 return {"book data is: {}".format(a[:limit])}
