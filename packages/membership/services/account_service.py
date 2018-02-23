# coding:utf8
# !/usr/bin/python
import sqlalchemy

from ..models.account import Account as model, db

from ...util.sqlalchemy_helper import set_model_props


class AccountService:

    def __init__(self):
        """ 初始化函数 """
        self.query = model.query

    def save(self, args):
        """
        保存对象
        :param args: 参数信息
        :return: 错误码
        """

        param = self.query.filter_by(id=args.id).first()
        if param is None:
            return self.insert(args)
        else:
            return self.update(args)

    def insert(self, args):
        """
        新建对象
        :param args: 参数信息
        :return: 错误码
        """

        param = model()

        # 复制属性信息
        set_model_props(param, args)

        db.session.add(param)
        db.session.commit()

        return 0, u"Success"

    def update(self, args):
        """
        更新对象
        :param args: 参数信息
        :return: 错误码
        """

        param = self.query.filter_by(id=args.id).first()

        # 设置对象属性信息
        set_model_props(param, args)

        db.session.merge(param)
        db.session.commit()

        return 0, u"Success"

    def delete(self, id):
        """ 删除对象 """

        param = self.query.filter_by(id=id).first()

        if param is None:
            return False, 'object #' + str(id) + ' not found'

        db.session.delete(param)
        db.session.commit()

        return 0, u"Success"

    def findOne(self, id):
        """ 查询某条信息 """
        param = self.query.filter_by(id=id).first()

        return 0, u"Success", param

    def findAll(self):
        """ 查询列表信息 """

        return self.query.order_by(model.id.desc()).all()

    def getPaging(self, args):
        """ 获取列表信息 """

        filters = ''
        
        if args.id is not None and len(args.id) > 0:
            filters = sqlalchemy.and_(filters, args.id == model.id)

        if args.name is not None and len(args.name) > 0:
            filters = sqlalchemy.and_(filters, model.name.like("%" + args.name + "%"))

        return self.query.filter(filters).order_by(model.id.desc()).all()