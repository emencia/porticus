# -*- coding: utf-8 -*-
"""
Common templates tags for porticus
"""
from six import string_types
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404

from porticus.models import Gallery, Album


register = template.Library()


class GalleryList(template.Node):
    """
    Gallery list (without any pagination) as a HTML fragment
    """
    def __init__(self, template_varname=None, instance_varname=None):
        """
        :type insert_instance_varname: string or object ``django.db.models.Model``
        :param insert_instance_varname: Instance variable name or a string slug for
                                        the current gallery

        :type template_varname: string
        :param template_varname: (optional) ...
        """
        self.template_varname = None
        if template_varname:
            self.template_varname = template.Variable(template_varname)
        self.instance_varname = None
        if instance_varname:
            self.instance_varname = template.Variable(instance_varname)

    def render(self, context):
        """
        :type context: object ``django.template.Context``
        :param context: Context tag object

        :rtype: string
        :return: the HTML for the list
        """
        # Default assume this is directly an instance
        current_gallery = None
        if self.instance_varname:
            current_gallery = self.instance_varname.resolve(context)
            if current_gallery:
                # Assume this is slug
                if isinstance(current_gallery, string_types):
                    current_gallery = Gallery.objects.get(slug=current_gallery, publish=True)
                # Only accept Gallery model instance
                elif not isinstance(current_gallery, Gallery):
                    raise template.TemplateSyntaxError("You can only specify a Gallery instance or a slug")

        # Resolve optional template path
        template_path = settings.PORTICUS_GALLERIES_TEMPLATE_FRAGMENT
        if self.template_varname:
            try:
                resolved_var = self.template_varname.resolve(context)
            except template.VariableDoesNotExist:
                pass
            else:
                if resolved_var:
                    template_path = resolved_var

        gallery_list = Gallery.publish.all()

        subcontext = {
            'object_list': gallery_list,
            'current_gallery': current_gallery,
        }

        html = template.loader.get_template(template_path).render(template.Context(subcontext))

        return mark_safe(html)


@register.tag(name="porticus_gallery_list")
def do_porticus_gallery_list(parser, token):
    """
    Display the gallery list

    Usage : ::

        {% porticus_gallery_list [Optional template path] [Optional Gallery slug or instance] %}
    """
    args = token.split_contents()
    return GalleryList(*args[1:])


do_porticus_gallery_list.is_safe = True


class AlbumFragment(template.Node):
    """
    Album ressources as a HTML fragment
    """
    def __init__(self, instance_varname, template_varname=None):
        """
        :type insert_instance_varname: string or object ``django.db.models.Model``
        :param insert_instance_varname: Instance variable name or a string slug

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
        # Default assume this is directly an instance
        album_instance = self.instance_varname.resolve(context)
        # Assume this is slug
        if isinstance(album_instance, string_types):
            album_instance = Album.objects.get(slug=album_instance, publish=True)
        # Get the album's ressources
        ressources_list = album_instance.ressource_set.filter(publish=True)

        # Resolve optional template path
        template_path = settings.PORTICUS_ALBUM_TEMPLATE_FRAGMENT
        if self.template_varname:
            try:
                template_path = self.template_varname.resolve(context)
            except template.VariableDoesNotExist:
                pass

        subcontext = {
            'gallery_object': album_instance.gallery,
            'album_object': album_instance,
            'ressource_list': ressources_list,
        }

        html = template.loader.get_template(template_path).render(template.Context(subcontext))

        return mark_safe(html)


@register.tag(name="porticus_album_fragment")
def do_porticus_album_fragment(parser, token):
    """
    Display a album

    Usage : ::

        {% porticus_album_fragment [Optional Album slug or instance] [Optional template path] %}
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError("You need to specify at less an \"Album\" instance or slug")
    else:
        return AlbumFragment(*args[1:])


do_porticus_album_fragment.is_safe = True


def porticus_album_list(gallery_instance):
    """
    Return a queryset list from a Gallery, this is a flat list of albums, not recursive

    Usage : ::

        {% porticus_album_list [Gallery slug or instance] as gallery_albums %}
    """
    if isinstance(gallery_instance, string_types):
        return get_object_or_404(Gallery, slug=gallery_instance, publish=True).album_set.filter(level=0)

    return gallery_instance.album_set.filter(level=0)


register.assignment_tag(porticus_album_list)


#@register.filter(name='embed')
#def embed(value):
    #return value.replace('watch?v=', 'embed/')
