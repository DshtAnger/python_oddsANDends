#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-18 00:49:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

#ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 定义Pet对象:
class Pet(Base):
    # 表的名字:
    __tablename__ = 'pet'

    # 表的结构:
    name = Column(String(20), primary_key=True)
    owner = Column(String(20))
    species = Column(String(20))
    sex = Column(String(1))


# 初始化数据库连接:
#SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)



'''####################################################################################
#由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象:
#创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='3', name='Alice')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
#可见，关键是获取session，然后把对象添加到session，最后提交并关闭。Session对象可视为当前数据库连接。
#####################################################################################'''


#####################################################################################
#有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()
#####################################################################################
