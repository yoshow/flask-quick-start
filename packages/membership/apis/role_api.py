# coding:utf8
# !/usr/bin/python
""" 
RoleAPI File
"""
from app_logging import logger
from flask import Response, json, request
from flask_restful import Resource, reqparse
from ..services.role_service import RoleService as service
from ...util.sqlalchemy_helper import entity_to_dict


requestParser = reqparse.RequestParser()

requestParser.add_argument('id', type=unicode)
requestParser.add_argument('code', type=unicode)
requestParser.add_argument('name', type=unicode)
requestParser.add_argument('globalName', type=unicode)
requestParser.add_argument('pinYin', type=unicode)
requestParser.add_argument('type')
requestParser.add_argument('parentId', type=unicode)
requestParser.add_argument('organizationUnitId', type=unicode)
requestParser.add_argument('enableEmail')
requestParser.add_argument('effectScope')
requestParser.add_argument('locking')
requestParser.add_argument('orderId', type=unicode)
requestParser.add_argument('status')
requestParser.add_argument('remark', type=unicode)
requestParser.add_argument('fullPath', type=unicode)
requestParser.add_argument('distinguishedName', type=unicode)
requestParser.add_argument('modifiedDate')
requestParser.add_argument('createdDate')


class RoleAPI(Resource):

    def __init__(self):
        self.res = Response(status=200)
        self.res.content_type = 'application/json; charset=utf-8'
        self.service = service()

    def get(self, id):
        """ 查询对象 """

        code, message, data = self.service.findOne(id)
        self.res.data = json.dumps(
            {'code': code, 'message': message, 'data': entity_to_dict(data)}, ensure_ascii=False)

        return self.res

    def post(self):
        """ 保存对象 """
        args = requestParser.parse_args()

        code, message = self.service.save(args)
        self.res.data = json.dumps(
            {'code': code, 'message': message}, ensure_ascii=False)

        return self.res

    def put(self, id):
        """ 更新对象 """
        args = requestParser.parse_args()

        code, message = self.service.save(args)
        self.res.data = json.dumps(
            {'code': code, 'message': message}, ensure_ascii=False)

        return self.res

    def delete(self, id):
        """ 删除对象 """

        code, message = self.service.delete(id=id)
        self.res.data = json.dumps(
            {'code': code, 'message': message}, ensure_ascii=False)

        return self.res


class RoleQueryAPI(Resource):

    def __init__(self):
        self.res = Response(status=200)
        self.res.content_type = 'application/json; charset=utf-8'
        self.service = service()

    def post(self):
        """ 查询 """
        parser = reqparse.RequestParser()
        parser.add_argument('scene')

        args = requestParser.parse_args()

        if args.scene == 'query':
            # getPaging 查询列表记录
            parser = reqparse.RequestParser()
            parser.add_argument('name')

            code, message, data = self.service.findAll(args)
            self.res.data = json.dumps(
                {'code': code, 'message': message, 'data': data}, ensure_ascii=False)

        elif args.scene == 'findAll':
            # findAll 查询列表记录
            parser = reqparse.RequestParser()
            parser.add_argument('name')

            code, message, data = self.service.findAll(args)
            self.res.data = json.dumps(
                {'code': code, 'message': message, 'data': data}, ensure_ascii=False)

        return self.res
