# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template
from django.template import TemplateSyntaxError

from catalog.models import Category

register = template.Library()

################################################################################################################
################################################################################################################

class GetCatalogListNode(Node):
	def render(self, context):
		context['catalog_list_tag'] = Category.objects.filter(is_active=True)
		return ''
		
def get_catalog_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 1: raise TemplateSyntaxError("%r take > 1 argument" % bits[0])
	return GetCatalogListNode()
	
get_catalog_list = register.tag(get_catalog_list)

################################################################################################################
################################################################################################################