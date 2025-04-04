from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from sqlalchemy.orm import sessionmaker

models.Base.metadata.create_all(bind=engine)

def create_item(db: Session, name: str, description: str = None):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def update_item(db: Session, item_id: int, name: str = None, description: str = None):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        if name:
            item.name = name
        if description:
            item.description = description
        db.commit()
        db.refresh(item)
        return item
    return None

def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False

if __name__ == "__main__":
    # Example Usage
    engine = engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create a session
    db = SessionLocal()

    try:
        # Create
        new_item = create_item(db, name="Example Item", description="This is an example item.")
        print(f"Created item: {new_item.name}")

        # Read
        read_item_obj = read_item(db, new_item.id)
        print(f"Read item: {read_item_obj.name}")

        # Update
        updated_item = update_item(db, new_item.id, name="Updated Item Name")
        print(f"Updated item name: {updated_item.name}")

        # Delete
        delete_item(db, new_item.id)
        print(f"Deleted item with id: {new_item.id}")

    finally:
        db.close()
