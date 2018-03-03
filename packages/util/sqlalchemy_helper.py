# coding:utf8
# !/usr/bin/python
import time
from datetime import datetime
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
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                
            setattr(entity, column.name, value)

        else:
            setattr(entity, column.name, value)

    return entity


def entity_to_dict(entity):
    """ 转换实体对象为字典 """
    result = {}
    for column in entity.__table__.columns:
        if type(column.type) == db.DateTime:
            # 日期类型的转换
            value = getattr(entity, column.name)
            if value is None:
                value = 0
            else:
                value = time.mktime(value.timetuple()) * 1000
            result[column.name] = value
        elif type(column.type) == db.DECIMAL:
            # 十进制类型
            value = getattr(entity, column.name)
            result[column.name] = float(value)
        else:
            result[column.name] = getattr(entity, column.name)

    return result
