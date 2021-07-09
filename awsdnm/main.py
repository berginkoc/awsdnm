import kivy
from kivy.app import App
from kivy.uix.label import Label
import pymysql


class UygulamaApp(App):
    db = pymysql.connect('database-1.*****.us-east-1.rds.amazonaws.com', 'admin', '12345678')
    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()

    sql1 = '''use deneme'''
    cursor.execute(sql1)
    sql2 = '''select * from person'''
    cursor.execute(sql2)
    data1 = cursor.fetchall()

    def build(self):
        return Label(text=str(UygulamaApp.data1))


if __name__ == "__main__":
    UygulamaApp().run()

# import pymysql
#
# db = pymysql.connect('database-1.*****.us-east-1.rds.amazonaws.com', 'admin', '12345678')
# cursor = db.cursor()
# cursor.execute("select version()")
# data = cursor.fetchone()
#
# sql1 = '''use deneme'''
# cursor.execute(sql1)
# #
# # sql = '''
# # create table person(
# # id int not null auto_increment,
# # fname text,
# # lname text,
# # primary key (id)
# # )
# # '''
# # cursor.execute(sql)
# list = [["Burak", "Erginkoc"], ["1111", "22222"]]
#
# for i in list:
#     sql3 = '''insert into person(fname,lname) values('%s','%s')''' % (i[0], i[1])
#     cursor.execute(sql3)
# db.commit()
#
#
# sql2 = '''select * from person'''
# cursor.execute(sql2)
# data1 = cursor.fetchall()
# print(data1)
