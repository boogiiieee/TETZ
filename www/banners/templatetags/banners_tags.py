# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template

from banners.models import Banner

register = template.Library()

################################################################################################################
################################################################################################################

class get_banners_list_node(Node):
	def render(self, context):
		context['banners_list'] = Banner.objects.filter(is_active=True)
		return ''
		
def get_banners_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 1:
		raise TemplateSyntaxError(u"%r имеет > 1 аргумента" % bits[0])
	return get_banners_list_node()
	
get_banners_list = register.tag(get_banners_list)

################################################################################################################
################################################################################################################