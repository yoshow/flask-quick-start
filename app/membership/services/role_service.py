# coding:utf8
# !/usr/bin/python
import sqlalchemy

from ..models.role import Role as model, db

from ...util.sqlalchemy_helper import set_entity_props

class RoleService:
    def __init__(self):
        """ 初始化函数 """
        self.query = model.query
    
    def save(self, args):
        """
        保存对象
        :entity args: 参数信息
        :return: 错误码
        """

        entity = self.query.filter_by(id=args.id).first()

        if entity is None:
            return self.insert(args)
        else:
            return self.update(args)

    def insert(self, args):
        """
        新建对象
        :entity args: 参数信息
        :return: 错误码
        """

        entity = model()

        # 设置对象属性信息
        set_entity_props(entity, args)

        db.session.add(entity)
        db.session.commit()

        return 0, u"Success"
        
    def update(self, args):
        """
        更新对象
        :entity args: 参数信息
        :return: 错误码
        """

        entity = self.query.filter_by(id=args.id).first()

        # 设置对象属性信息
        set_entity_props(entity, args)

        db.session.merge(entity)
        db.session.commit()

        return 0, u"Success"

    def delete(self, id):
        """ 删除对象 """

        entity = self.query.filter_by(id=id).first()

        if entity is None:
            return 1, 'object #' + str(id) + ' not found'

        db.session.delete(entity)
        db.session.commit()

        return 0, u"Success"

    def findOne(self, id):
        """ 查询某条信息 """

        entity = self.query.filter_by(id=id).first()

        return 0, u"Success", entity
 
    def findAll(self):
        """ 查询列表信息 """

        return self.query.order_by(model.id.desc()).all()

    def getPaging(self, args):
        """分页查询列表信息"""

        filters = ''
        
        if args.id is not None and len(args.id) > 0:
            filters = sqlalchemy.and_(filters, args.id == model.id)

        if args.name is not None and len(args.name) > 0:
            filters = sqlalchemy.and_(filters, model.name.like("%" + args.name + "%"))

        return self.query.filter(filters).order_by(model.id.desc()).all()
