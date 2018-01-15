# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template

from headstuff.models import HeadStuff

register = template.Library()

################################################################################################################
################################################################################################################

class get_headstuff_list_node(Node):
	def render(self, context):
		context['headstuff_list'] = HeadStuff.objects.filter(is_active=True)
		return ''
		
def get_headstuff_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 1:
		raise TemplateSyntaxError(u"%r имеет > 1 аргумента" % bits[0])
	return get_headstuff_list_node()
	
get_headstuff_list = register.tag(get_headstuff_list)

################################################################################################################
################################################################################################################