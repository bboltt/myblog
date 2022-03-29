from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# url = "mysql+mysqlconnector://root:1990pm0821@124.221.178.162:4306/test"
# inside doker
url = "mysql+mysqlconnector://root:1990pm0821@172.18.0.3:3306/test"
engine = create_engine(url, pool_size=5)
Session = sessionmaker(bind=engine)
