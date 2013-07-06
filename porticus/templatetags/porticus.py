# -*- coding: utf-8 -*-
"""
Common templates tags for porticus
"""
from django import template
from django.utils.safestring import mark_safe

from porticus.models import Gallery

register = template.Library()

class GalleryFragment(template.Node):
    """
    Porticus gallery ressources as a HTML fragment
    """
    default_template_path = 'porticus/gallery_detail_fragment.html'
    
    def __init__(self, instance_varname, template_varname=None):
        """
        :type insert_instance_varname: string or object ``django.db.models.Model``
        :param insert_instance_varname: Instance variable name or a string for the slug
                                        
        :type template_varname: string
        :param template_varname: (optional) ...
        """
        self.instance_varname = template.Variable(instance_varname)
        self.template_varname = None
        if template_varname:
            self.template_varname = template.Variable(template_varname)
    
    def render(self, context):
        """
        :type context: object ``django.template.Context``
        :param context: Context tag object
        
        :rtype: string
        :return: the HTML for the gallery
        """
        html = ''
        
        # Default assume this is directly an instance
        gallery_instance = self.instance_varname.resolve(context)
        # Assume this is slug
        if isinstance(gallery_instance, basestring):
            gallery_instance = Gallery.objects.get(slug=gallery_instance)
        # Get the gallery's ressources
        ressources_list = gallery_instance.ressources.filter(priority__gt=0)

        # Resolve optional template path
        template_path = self.default_template_path
        if self.template_varname:
            try:
                template_path = self.template_varname.resolve(context)
            except template.VariableDoesNotExist:
                pass
        
        subcontext = {
            'gallery': gallery_instance,
            'object_list': ressources_list,
        }
        
        html = template.loader.get_template(template_path).render(template.Context(subcontext))
        
        return mark_safe(html)

@register.tag(name="porticus_gallery_fragment")
def do_porticus_gallery_fragment(parser, token):
    """
    Display a gallery
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError, "You need to specify at less a \"Gallery\" instance or slug"
    else:
        return GalleryFragment(*args[1:])

do_porticus_gallery_fragment.is_safe = True
