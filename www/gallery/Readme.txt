создание фотогаллереи - фото грузятся из gallery_list

INSTALLED_APPS = (
	...
	'gallery',
	...
)

{% load gallery_tags %}
{% get_gallery_list %}