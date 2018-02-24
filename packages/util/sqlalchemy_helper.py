# coding:utf8
# !/usr/bin/python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def set_entity_props(entity, args):
    """ 设置实体对象属性 """

    for column in entity.__table__.columns:
        value = args[column.name]
        if value is None:
            continue

        if type(column.type) == db.DateTime:
            if value is None:
                value = 0
            else:
                value = int(value)

            setattr(entity, column.name, value)

        else:
            setattr(entity, column.name, value)

    return entity

def entity_to_dict(entity):
    """ 转换实体对象为字典 """
    result = {}
    for column in entity.__table__.columns:
        if type(column.type) == db.DateTime:
            value = getattr(entity, column.name)
            if value is None:
                value = 0
            else:
                value = time.mktime(value.timetuple()) * 1000
            result[column.name] = value
        else:
            result[column.name] = getattr(entity, column.name)

    return result
