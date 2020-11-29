from collections import OrderedDict

from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response

from Tree.models import Catalog, Function, Parameter, Class
from Tree.serializers import TreeSerializer


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = TreeSerializer

    def list(self, request, *args, **kwargs):
        return Response(self.buildTree())

    def buildTree(self):
        dataMap = TreeViewSet.buildTreeFromQueryset(self.queryset)
        retMap = OrderedDict()
        for k, v in dataMap.items():
            if v.get('isRoot', False):
                retMap[k] = v
        return {
            'index': list(retMap.keys()),
            'data': retMap,
        }

    @staticmethod
    def buildTreeFromQueryset(queryset, keys=None, orderByKeys=None):
        if not hasattr(queryset.model, '_mptt_meta'):
            raise TypeError('queryset must be MPTTModel queryset')

        if not keys:
            opts = queryset.model._mptt_meta
            keys = (
                'id',
                "name",
                opts.level_attr,
                f'{opts.parent_attr}_id',
                opts.tree_id_attr,
            )

        if 'id' not in keys:
            raise ValueError('id must in keys')

        if 'level' not in keys:
            raise ValueError('level must in keys')

        if 'parent_id' not in keys:
            raise ValueError('parent_id must in keys')

        if not orderByKeys:
            orderByKeys = ['id', 'lft']

        if not queryset.ordered:
            queryset = queryset.order_by(*orderByKeys)

        # 组织树数据格式 LIFO
        dataMap = OrderedDict()
        for currentNode in queryset:
            tmp = TreeViewSet.addFunctionOrClass(currentNode)
            currentNodePK = currentNode.pk
            dataMap[currentNodePK] = tmp

            currentNodeParent = currentNode.parent
            if currentNodeParent and currentNodeParent.id in dataMap:
                # 当前节点是子节点，追加到父节点的 child 列表中
                dataMap[currentNodeParent.id]['children'].append(tmp)
        return dataMap

    @staticmethod
    def addFunctionOrClass(cur):
        tmp = {
            "scopedSlots": {
                "title": 'name',
                "key": "id",
            },
            "id": cur.id,
            "name": cur.name,
            "isRoot": cur.is_root_node(),
            "children": list()
        }

        # 如果当前节点是叶子节点，需要添加相应的函数或类到children
        functions = Function.objects.all().filter(belong=cur)
        if cur.is_leaf_node() and functions:
            for func in functions:
                val = model_to_dict(func)
                val["scopedSlots"] = {
                    "title": 'name',
                    "key": "id"
                }

                # 添加参数内容到函数中
                val["parameters"] = list()
                parameters = Parameter.objects.all().filter(belongFunction=func)
                if parameters:
                    for para in parameters:
                        val["parameters"].append(model_to_dict(para))

                tmp["children"].append(val)

        calsses = Class.objects.all().filter(belong=cur)
        if cur.is_leaf_node() and calsses:
            for cla in calsses:
                val = model_to_dict(cla)
                val["scopedSlots"] = {
                    "title": 'name',
                    "key": "id"
                }

                # 添加参数内容到函数中
                val["parameters"] = list()
                parameters = Parameter.objects.all().filter(belongClass=cla)
                if parameters:
                    for para in parameters:
                        val["parameters"].append(model_to_dict(para))

                # 添加类所拥有的函数
                val["children"] = list()
                functions = Function.objects.all().filter(belongClass=cla)
                if functions:
                    for func in functions:
                        value = model_to_dict(func)
                        value["scopedSlots"] = {
                            "title": 'name',
                            "key": "id"
                        }

                        # 添加参数内容到函数中
                        value["parameters"] = list()
                        parameters = Parameter.objects.all().filter(belongFunction=func)
                        if parameters:
                            for para in parameters:
                                value["parameters"].append(model_to_dict(para))
                        val["children"].append(value)

                tmp["children"].append(val)
        return tmp
