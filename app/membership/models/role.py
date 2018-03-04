# coding:utf8
# !/usr/bin/python
from sqlalchemy import text
from ...util.sqlalchemy_helper import db

class Role(db.Model):
    __tablename__ = 'ge_role'

    id = db.Column(db.String, primary_key=True)
    code = db.Column(db.String(30), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    globalName = db.Column(db.String(100), nullable=True)
    pinYin = db.Column(db.String(100), nullable=True)
    type = db.Column(db.Integer, nullable=True)
    parentId = db.Column(db.String(36), nullable=True)
    organizationUnitId = db.Column(db.String(36), nullable=True)
    enableEmail = db.Column(db.Integer, nullable=True)
    effectScope = db.Column(db.Integer, nullable=True)
    locking = db.Column(db.Integer, nullable=True)
    orderId = db.Column(db.String(20), nullable=True)
    status = db.Column(db.Integer, nullable=True)
    remark = db.Column(db.String(200), nullable=True)
    fullPath = db.Column(db.String(400), nullable=True)
    distinguishedName = db.Column(db.String(800), nullable=True)
    modifiedDate = db.Column(db.DateTime, nullable=True)
    createdDate = db.Column(db.DateTime, nullable=True, server_default=text('CURRENT_TIMESTAMP'))
