import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

database_url = 'sqlite:////home/giedrius/venv/lss_app/src/database/'
database_name = 'app.db'

engine = create_engine(database_url + database_name, echo=True)

# Will return engine instance
Base = declarative_base()

# Define your data model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

# Create the database tables
Base.metadata.create_all(engine)