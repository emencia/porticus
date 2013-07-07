# -*- coding: utf-8 -*-
"""
Common templates tags for porticus
"""
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe

from porticus.models import Album

register = template.Library()

class AlbumFragment(template.Node):
    """
    Porticus album ressources as a HTML fragment
    """
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
        :return: the HTML for the album
        """
        html = ''
        
        # Default assume this is directly an instance
        album_instance = self.instance_varname.resolve(context)
        # Assume this is slug
        if isinstance(album_instance, basestring):
            album_instance = Album.objects.get(slug=album_instance)
        # Get the album's ressources
        ressources_list = album_instance.ressources.filter(priority__gt=0)

        # Resolve optional template path
        template_path = settings.PORTICUS_ALBUM_FRAGMENT_TEMPLATE
        if self.template_varname:
            try:
                template_path = self.template_varname.resolve(context)
            except template.VariableDoesNotExist:
                pass
        
        subcontext = {
            'album': album_instance,
            'object_list': ressources_list,
        }
        
        html = template.loader.get_template(template_path).render(template.Context(subcontext))
        
        return mark_safe(html)

@register.tag(name="porticus_album_fragment")
def do_porticus_album_fragment(parser, token):
    """
    Display a album
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError, "You need to specify at less a \"Album\" instance or slug"
    else:
        return AlbumFragment(*args[1:])

do_porticus_album_fragment.is_safe = True
