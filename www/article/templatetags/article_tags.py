# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template
from django.template import TemplateSyntaxError
import re

from article.models import Article

register = template.Library()

################################################################################################################
################################################################################################################

class GetArticleListNode(Node):
	def __init__(self, section_id, var_name):
		self.section_id = int(section_id)
		self.var_name = var_name
		
	def render(self, context):
		context[self.var_name] = Article.objects.filter(section=self.section_id)
		return ''                                                         
		
def get_article_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 3: raise TemplateSyntaxError("%r take != 3 arguments" % bits[0])
	return GetArticleListNode(bits[1], bits[2][1:-1])
	
get_article_list = register.tag(get_article_list)

################################################################################################################
################################################################################################################