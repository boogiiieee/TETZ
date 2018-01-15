# -*- coding: utf-8 -*-

from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetree.utils import tree, item

print '----------------------------------'
register_dynamic_trees((

    # Gather all the trees from `catalog`,
    #compose_dynamic_tree('catalog'),

    # or gather all the trees from `catalog` and attach them to `main` tree root,
    compose_dynamic_tree('catalog', target_tree_alias='TopMenu'),

    # or gather all the trees from `catalog` and attach them to `for_catalog` aliased item in `main` tree,
    #compose_dynamic_tree('catalog', target_tree_alias='main', parent_tree_item_alias='for_catalog'),

    # or even define a tree right at the process of registration.
    #compose_dynamic_tree((
    #    tree('dynamic', items=(
    #        item('dynamic_1', 'dynamic_1_url', children=(
    #            item('dynamic_1_sub_1', 'dynamic_1_sub_1_url'),
    #        )),
    #        item('dynamic_2', 'dynamic_2_url'),
    #    )),
    #)),
))