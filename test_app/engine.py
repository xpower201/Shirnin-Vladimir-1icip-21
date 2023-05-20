from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/auf")
session = Session(bind=engine)

def add_data(login, password):
    session.execute(text(f"INSERT INTO public.auth(login, password) VALUES ('{login}', '{password}')"))
    session.commit()
    session.close()