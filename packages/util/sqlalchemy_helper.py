# coding:utf8
# !/usr/bin/python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def set_model_props(param, args):
    """ 设置对象属性 """

    for column in param.__table__.columns:
        value = args[column.name]
        if value is None:
            continue

        if type(column.type) == db.DateTime:
            if value is None:
                value = 0
            else:
                value = int(value)

            setattr(param, column.name, value)

        else:
            setattr(param, column.name, value)

    return param
