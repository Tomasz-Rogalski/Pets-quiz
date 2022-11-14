import random
from django import template

register = template.Library()


@register.simple_tag
def random_image():
    '''roll random image path from images list'''
    images_paths = ['dogcat1.png','dogcat2.png','dogcat3.png']
    return random.choice(images_paths)
