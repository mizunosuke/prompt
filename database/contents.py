# from sqlalchemy import Column, Integer, String, Text, DateTime, Sequence
# from .setting import ENGINE, Base
# from datetime import datetime


# class Content(Base):
#     """
#     ContentModel
#     """
#     __tablename__ = 'contents'
#     id = Column(Integer, primary_key=True)
#     question = Column(Text)
#     answer = Column(Text)
#     created_at = Column('created', DateTime, default=datetime.now, nullable=False)
#     updated_at = Column('modified', DateTime, default=datetime.now, nullable=False)


# def main():
#     Base.metadata.create_all(bind=ENGINE)


# if __name__ == "__main__":
#     main()