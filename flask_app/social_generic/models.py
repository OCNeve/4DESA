from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from enum import Enum
 



Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50))
    email = Column(String(320), unique=True, nullable=False)

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, Sequence('posts_id_seq'), primary_key=True)
    creator_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    date = Column(Date, unique=True, nullable=False, default=datetime.now)

    user = relationship('Users', foreign_keys='Posts.creator_id')


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, Sequence('videos_id_seq'), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    date = Column(Date, unique=True, nullable=False, default=datetime.now)

    post = relationship('Posts', foreign_keys='Comments.post_id')


class Images(Base):
    __tablename__ = 'images'

    id = Column(Integer, Sequence('images_id_seq'), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    path = Column(String(255), unique=True, nullable=False)

    post = relationship('Posts', foreign_keys='Images.post_id')


class Videos(Base):
    __tablename__ = 'videos'

    id = Column(Integer, Sequence('videos_id_seq'), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    path = Column(String(255), unique=True, nullable=False)

    post = relationship('Posts', foreign_keys='Videos.post_id')





class Models(Enum):
    users = Users
    posts = Posts
    comments = Comments
    images = Images
    videos = Videos


"""
print(Models.users) => Models.users
print(Models.users.name) => users
print(Models.users.value) => Users
print(list(Models)) => [<Models.users: Users>, <Models.posts: Posts>, <Models.comments: Comments>, <Models.images: Images>, <Models.videos: Videos>]
"""