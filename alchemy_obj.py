#!/usr/bin/env python

import datetime
import os
import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line, define, options
from tornado.web import RequestHandler, Application


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Float, Date, Enum, Text
from sqlalchemy.ext.declarative import declarative_base

#建立连接与数据库的连接
engine = create_engine('mysql+pymysql://zhang:123@localhost:3306/abcde')
Base = declarative_base(bind=engine)  #创建模型的基础类
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    sex = Column(Enum('男', '女'))
    city = Column(String(40), default='华夏')
    des = Column(Text)
    math = Column(Float, default=0.0)
    english = Column(Float, default=0.0)
    birth = Column(Date, default=datetime.date(1990,1,1))


Base.metadata.create_all()

session = Session()

#bob = Student(name='bob',sex='男',city='北京',des='',math=85.0,english=75.0,birth=datetime.date(1999,9,9))

#pip = Student(name='pip',sex='女',city='重庆',des='就是美丽动人',math=55.0,english=55.0,birth=datetime.date(1995,2,19))

#rob = Student(name='rob',sex='女',city='',des='机器人',math=95.0,english=95.0,birth=datetime.date(1998,2,12))

#jam = Student(name='jam',sex='男',city='深圳',des='小马哥',math=25.0,english=78.0,birth=datetime.date(1989,1,19))

#eva = Student(name='eva',sex='女',city='守望',des='守望先锋',math=99.0,english=99.0,birth=datetime.date(2999,9,9))

#objets = [bob,pip,rob,jam,eva]

#session.add_all(objets)
#session.commit()  #提交到数据库执行
#test = Student(name='name',sex='男',des='dddd')
#session.add_all([test])
#session.commit()
q = session.query(Student)

#test =  q.get(8)
#session.delete(test)
#session.commit()


#查询数据
#q = session.query(Student)
student = q.get(5)
print(student.name,student.sex,student.city,student.des,student.math,student.english,student.math,student.birth)


#根据ID修改数据
stu = q.get(1)
stu.des = '就是无聊'
print(stu)

stu = q.filter(Student.id==3).first()
stu.city = '华夏'
print(stu)
session.commit()



define("host", default='localhost', help="主机地址", type=str)
define("port", default=8000, help="主机端口", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id','1')
        sex = q.get(id).sex
        name = q.get(id).name
        city = q.get(id).city
        dex = q.get(id).des
        math = q.get(id).math
        english = q.get(id).english
        birth = q.get(id).birth
        
        self.render("index.html",sex=sex,name=name,city=city,dex=dex,math=math,english=english,birth=birth)

class BlockHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id','1')
        title = q.get(id).name
        AAAAAA = q.get(id).name
        content = q.get(id).name + q.get(id).sex + q.get(id).des

        self.render('article.html', title=title, content=content, AAAAAA = AAAAAA)



def make_app():
    routes = [
        (r"/", MainHandler),
        (r"/block", BlockHandler),
        #(r"/tttt", StaticTestHandle)
    ]

    # 获取模版目录和静态文件目录的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'temp11')
    static_dir = os.path.join(base_dir, 'jingtai11')

    return tornado.web.Application(routes,
                                   template_path=template_dir,
                                   static_path=static_dir)



if __name__ == "__main__":
    parse_command_line()

    app = make_app()
    print('server running on %s:%s' % (options.host, options.port))
    app.listen(options.port, options.host)

    loop = tornado.ioloop.IOLoop.current()
    loop.start()
    
