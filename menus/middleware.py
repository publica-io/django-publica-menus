from django.http import Http404
from django.core.urlresolvers import resolve
from django.conf import settings

from .models import Link


class LinkURLFallbackMiddleware(object):

    def process_response(self, request, response):
        '''
        Look through the Link models to see if we have a Custom URL and if so 
        call the corresponding view
        '''

        if response.status_code != 404:
            return response # No need to check for a page for non-404 responses.
        try:

            try:
                link = Link.objects.get(url=request.path)
            except Link.DoesNotExist:
                pass
            else:
                url = None
                try:
                    url = link.content_type.model_class().get_list_url()
                    url = link.content_object.get_absolute_url()
                except AttributeError:
                    pass

                if url is not None:
                    view, args, kwargs = resolve(url)

                    kwargs['request'] = request
                    try:
                        response = view(*args, **kwargs)
                    except Http404:
                        pass
                    else:
                        response.render()
            return response

        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response

        except:
            if settings.DEBUG:
                raise
            return response
        # else:
        #     return response