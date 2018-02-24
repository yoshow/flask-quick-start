# -*- coding:utf8 -*-
# !/usr/bin/python
"""

"""
from app_logging import logger
from flask import Response, json, request
from flask_restful import Resource, reqparse
from ..services.account_service import AccountService as service
from ...util.sqlalchemy_helper import entity_to_dict


requestParser = reqparse.RequestParser()
requestParser.add_argument('id', type=unicode)
requestParser.add_argument('code', type=unicode)
requestParser.add_argument('name', type=unicode)
requestParser.add_argument('globalName', type=unicode)
requestParser.add_argument('displayName', type=unicode)
requestParser.add_argument('pinYin', type=unicode)
requestParser.add_argument('loginName', type=unicode)
requestParser.add_argument('password', type=unicode)
requestParser.add_argument('passwordChangedDate')
requestParser.add_argument('identityCard', type=unicode)
requestParser.add_argument('type')
requestParser.add_argument('certifiedMobile', type=unicode)
requestParser.add_argument('certifiedEmail', type=unicode)
requestParser.add_argument('certifiedAvatar', type=unicode)
requestParser.add_argument('enableExchangeEmail')
requestParser.add_argument('isDraft')
requestParser.add_argument('locking')
requestParser.add_argument('orderId', type=unicode)
requestParser.add_argument('status')
requestParser.add_argument('remark', type=unicode)
requestParser.add_argument('ip', type=unicode)
requestParser.add_argument('loginDate')
requestParser.add_argument('distinguishedName', type=unicode)
requestParser.add_argument('modifiedDate')
requestParser.add_argument('createdDate')


class AccountAPI(Resource):

    def __init__(self):
        self.name = 'api:/membership/account'
        logger.info(self.name + ' INIT')
        self.res = Response(status=200)
        self.res.content_type = 'application/json; charset=utf-8'
        self.service = service()

    def get(self, id):
        """ 查询对象 """

        logger.info(self.name + ', method:GET')
        code, message, data = self.service.findOne(id)
        self.res.data = json.dumps({'code': code, 'message': message, 'data': entity_to_dict(data)}, ensure_ascii=False)

        return self.res

    def post(self):
        """ 保存对象 """

        logger.info(self.name + ', method:POST')
        args = requestParser.parse_args()

        code, message = self.service.save(args)
        self.res.data = json.dumps({'code': code, 'message': message}, ensure_ascii=False)

        return self.res

    def put(self, id):
        """ 更新对象 """

        logger.info(self.name + ', method:PUT')
        args = requestParser.parse_args()

        code, message = self.service.update(args)
        self.res.data = json.dumps({'code': code, 'message': message}, ensure_ascii=False)

        return self.res

    def delete(self, id):
        """ 删除对象 """

        code, message = self.service.delete(id=id)
        self.res.data = json.dumps({'code': code, 'message': message}, ensure_ascii=False)

        return self.res


class AccountQueryAPI(Resource):

    def __init__(self):
        self.name = 'api:/membership/account/query'
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
            self.res.data = json.dumps({'code': code, 'message': message, 'data': data}, ensure_ascii=False)

        elif args.scene == 'findAll':
            # findAll 查询列表记录
            parser = reqparse.RequestParser()
            parser.add_argument('name')

            code, message, data = self.service.findAll(args)
            self.res.data = json.dumps({'code': code, 'message': message, 'data': data}, ensure_ascii=False)

        return self.res
