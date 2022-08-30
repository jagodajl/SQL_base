from sqlalchemy_ex_02 import students

ins = students.insert()

ins

str(ins)

ins.compile().params

ins = students.insert().values(name='Eric', lastname='Idle')

ins.compile().params


if __name__ == '__main__':
    print('PyCharm')
