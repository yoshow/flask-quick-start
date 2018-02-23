# -*- coding:utf8 -*-
# !/usr/bin/python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    """ """

    __tablename__ = "tb_Account"

    """ 帐号唯一标识 """
    id = db.Column(db.String, primary_key=True)
    """ 代码 """
    code = db.Column(db.String(30), nullable=True)
    """ 姓名 """
    name = db.Column(db.String(50), nullable=True)
    """ 全局名称 """
    globalName = db.Column(db.String(100), nullable=True)
    """ 显示名称 """
    displayName = db.Column(db.String(50), nullable=True)
    """ 拼音 """
    pinYin = db.Column(db.String(100), nullable=True)
    """ 登录名 """
    loginName = db.Column(db.String(50), nullable=True)
    """ 密码 """
    password = db.Column(db.String(50), nullable=True)
    """ 最近一次密码修改时间 """
    passwordChangedDate = db.Column(db.DateTime, nullable=True)
    """ 身份证号码 """
    identityCard = db.Column(db.String(30), nullable=True)
    """ 帐号类型 """
    type = db.Column(db.Integer, nullable=True)
    """ 已验证的电话号码 """
    certifiedMobile = db.Column(db.String(50), nullable=True)
    """ 已验证的邮箱 """
    certifiedEmail = db.Column(db.String(50), nullable=True)
    """ 已验证的头像 """
    certifiedAvatar = db.Column(db.String(100), nullable=True)
    enableExchangeEmail = db.Column(db.Integer, nullable=True)
    isDraft = db.Column(db.Integer, nullable=True)
    """ 锁定 0 不锁定, 1 锁定 """
    locking = db.Column(db.Integer, nullable=True)
    """ 排序 """
    orderId = db.Column(db.String(20), nullable=True)
    """ 状态 0 禁用 1 启用 """
    status = db.Column(db.Integer, nullable=True)
    """ 备注信息 """
    remark = db.Column(db.String(200), nullable=True)
    """ 最近一次登陆的 IP 地址 """
    iP = db.Column(db.String(20), nullable=True)
    """ 最近一次登陆时间 """
    loginDate = db.Column(db.DateTime, nullable=True)
    """ LDAP 唯一识别名称 """
    distinguishedName = db.Column(db.String(800), nullable=True)
    """ 最近一次修改时间 """
    modifiedDate = db.Column(db.DateTime, nullable=True)
    """ 创建时间 """
    createdDate = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        """ """
        result = {}
        for column in self.__table__.columns:
            if type(column.type) == db.DateTime:
                value = getattr(self, column.name)
                if value is None:
                    value = 0
                else:
                    value = int(value)
                result[column.name] = value
            else:
                result[column.name] = getattr(self, column.name)

        return result
