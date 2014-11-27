from django.db import models

from entropy.mixins import LinkURLMixin, TitleMixin, EnabledMixin, SlugMixin
from images.mixins import ImageMixin

from .settings import URL_NAMES


class Link(LinkURLMixin, ImageMixin):
    '''
    Admin defined link for use in menus and about the site.
    '''

    # url
    # gfk

    # Raises AppRegistryNotReady when calling in model runtime
    def _get_urls():
        from django.core import urlresolvers

        resolver = urlresolvers.get_resolver(None)
        patterns = sorted([
            (key, value[0][0][0])
            for key, value in resolver.reverse_dict.items()
            if isinstance(key, str)
        ])

        return patterns

    title = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, choices=URL_NAMES)

    def __unicode__(self):
        if self.url:
            return u'%s (%s)' % (self.title, self.url)
        else:
            return u'%s' % self.title

    def get_url(self):
        '''
        Return the custom url or get_abs url
        '''
        # If a URL is specified, use that first
        if self.url:
            return self.url

        if self.content_type:

            if self.object_id:
                try:
                    obj = self.content_object
                except AttributeError:
                    return '' # raise a validation error

                if obj is None:
                    return ''

                return obj.get_absolute_url()
            else:
                try:
                    return self.content_type.model_class().get_list_url()
                except AttributeError:
                    return '' # raise a validation error

        return '' # raise a validation error

    def get_content_type(self):
        if self.content_type:
            return self.content_type.model
        return None


# class MenuInstance(models.Model):
#     '''
#     An instantiation of a Menu on a given Platform and Position
#
#     Menu's display in their given Position across all Links.
#     '''
#
#     platforms = models.ManyToManyField(
#         'channels.Channel')
#
#     position = models.ForeignKey(
#         'positions.Position')


class Menu(EnabledMixin, SlugMixin, TitleMixin):
    '''
    An ordered collection of Links
    '''
    # title
    # short_title
    # slug
    # enabled
    pass


class MenuItem(models.Model):
    menu = models.ForeignKey('Menu', related_name='items')
    link = models.ForeignKey('Link', related_name='links')
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, related_name='children', blank=True)

    class Meta:
        ordering = ('order', )

    def __unicode__(self):
        return u'%s :: %s' % (
            self.menu,
            self.link)

    def get_url(self, prefix):
        return self.link.get_url(prefix)

    def __getitem__(self, key):
        '''Allow dict access to Link attributes'''
        return getattr(self.link, key)
