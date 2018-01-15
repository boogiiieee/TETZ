# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template

from gallery.models import Gallery

register = template.Library()

################################################################################################################
################################################################################################################

class get_gallery_list_node(Node):
	def render(self, context):
		context['gallery_list'] = Gallery.objects.filter(is_active=True)
		return ''
		
def get_gallery_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 1:
		raise TemplateSyntaxError(u"%r имеет > 1 аргумента" % bits[0])
	return get_gallery_list_node()
	
get_gallery_list = register.tag(get_gallery_list)

################################################################################################################
################################################################################################################