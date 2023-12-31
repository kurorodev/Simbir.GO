from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy import create_engine


path = "postgresql+psycopg2://{DB_TITLE}:{DB_PASSWORD}@localhost/{DB_USERNAME}"
engine = create_engine("postgresql+psycopg2://postgres:33196@localhost/SimbirGObase")
engine.connect()
print(engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

