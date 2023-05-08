from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, create_session

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/shool")
session = Session(bind=engine)

session = create_session(bind=engine)

def add_data():
    session.execute(text(f"INSERT INTO public.student(dull_name, number_class, index_class) VALUES ('(full_name)', '(number_class)', '(index_class)')"))
    session.commit()
    session.close()
