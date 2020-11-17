from collections import OrderedDict
from rest_framework import viewsets
from rest_framework.response import Response
from Tree.models import Catalog
from Tree.serializers import TreeSerializer


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = TreeSerializer

    def list(self, request, *args, **kwargs):
        treeData = self.buildTree()
        return Response(treeData)

    def buildTree(self):
        return TreeViewSet.tree_queryset_values(self.queryset)

    @staticmethod
    def _tree_queryset_values(qs, keys=None, order_by_keys=None):
        if not hasattr(qs.model, '_mptt_meta'):
            raise TypeError('queryset must be MPTTModel queryset')

        if not keys:
            opts = qs.model._mptt_meta
            keys = (
                'id',
                "name",
                opts.level_attr,
                f'{ opts.parent_attr }_id',
                opts.tree_id_attr,
                opts.left_attr,
                opts.right_attr,
            )

        if 'id' not in keys:
            raise ValueError('id must in keys')

        if 'level' not in keys:
            raise ValueError('level must in keys')

        if 'parent_id' not in keys:
            raise ValueError('parent_id must in keys')

        if not order_by_keys:
            order_by_keys = ['id', 'lft']

        if not qs.ordered:
            qs = qs.order_by(*order_by_keys)

        qs = qs.values(*keys)

        # 组织树数据格式 LIFO
        data_map = OrderedDict()
        for cur_node in qs:
            cur_node_pk = cur_node.get('id')
            # 为当前节点分配子节点数组
            cur_node['children'] = list()
            data_map[cur_node_pk] = cur_node
            cur_node_parent_id = cur_node.get('parent_id')
            if cur_node_parent_id in data_map:
                # 当前节点是子节点，追加到父节点的 child 列表中
                data_map[cur_node_parent_id]['children'].append(cur_node)
                data_map[cur_node_pk]['is_root'] = False
            else:
                data_map[cur_node_pk]['is_root'] = True
        return data_map

    @staticmethod
    def tree_queryset_values(qs, keys=None, order_by_keys=None):
        data_map = TreeViewSet._tree_queryset_values(qs, keys=keys, order_by_keys=order_by_keys)
        ret_map = OrderedDict()
        for k, v in data_map.items():
            if v.get('is_root', False):
                ret_map[k] = v
        data = {
            'index': list(ret_map.keys()),
            'data': ret_map,
        }
        return data
