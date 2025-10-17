from fastapi import FastAPI,status,HTTPException,Depends,APIRouter
from validation import Product
from db import get_db
import models
from sqlalchemy.orm import Session

router = APIRouter(tags=["router"])

@router.get("/products/",status_code=status.HTTP_200_OK)
def products_list(db:Session=Depends(get_db)):
    item = db.query(models.Grocery).all()
    return item

@router.get("/product/{id}",status_code=status.HTTP_200_OK)
def product_id(id:int,db:Session=Depends(get_db)):
    item = db.query(models.Grocery).filter(models.Grocery.id==id).first()
    
    if item is not None:
        return item
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "invalid id")

@router.post("/products/")
def new_product(new:Product,db:Session=Depends(get_db)):
        new_post = models.Grocery(**new.dict())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
   

@router.put("/products/{id}")
def update_product(id:int,update:Product,db:Session=Depends(get_db)):
    posts_query = db.query(models.Grocery).filter(models.Grocery.id==id)
    posts = posts_query.first()
    if(posts==None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="id not found")
    
    posts_query.update(update.dict(),synchronize_session=False)
    db.commit()
    

@router.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
     item = db.query(models.Grocery).filter(models.Grocery.id==id).first()
     if item==None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="product not found")
     
     db.delete(item)
     db.commit()
     raise HTTPException(status_code=status.HTTP_200_OK,detail="successfully deleted")