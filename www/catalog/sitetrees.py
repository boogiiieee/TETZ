# -*- coding: utf-8 -*-

from .models import Category 

from sitetree.utils import tree, item

'''
def make_tree ():
	catalog	= Category.objects.filter(is_active=True)
	title	= []
	url		= []
	for ct in catalog:
		title.append(ct.title)
		url.append(ct.get_category_url())
		#items
	#print title
	#print url
	
	items = item(title, url)
	print items

	return tree('catalog', items)

sitetrees = make_tree()
'''

sitetrees = (
         # Define a tree with `tree` function.
         tree('books', items=[
            # Then define items and their children with `item` function.
           item('Books', 'books-listing', children=[
               item('Book named "{{ book.title }}"', 'books-details', in_menu=False, in_sitetree=False),
                 item('Add a book', 'books-add'),
                 item('Edit "{{ book.title }}"', 'books-edit', in_menu=False, in_sitetree=False)
            ])
        ]),
         # ... You can define more than one tree for your app.
     )