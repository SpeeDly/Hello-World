from rest_framework.renderers import BaseRenderer, BrowsableAPIRenderer
from rest_framework.utils import encoders
import json
from django.http.multipartparser import parse_header

import re
all_chars = (unichr(i) for i in xrange(0x110000))
control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
control_char_re = re.compile('[%s]' % re.escape(control_chars))

class BrowsableAPIUnicodeRenderer(BrowsableAPIRenderer):
    def get_content(self, renderer, data,
                    accepted_media_type, renderer_context):
        """
        Get the content as if it had been rendered by the default
        non-documenting renderer.
        """
        if not renderer:
            return '[No renderers were found]'

        renderer_context['indent'] = 4
        content = renderer.render(data, accepted_media_type, renderer_context)

        if not not control_char_re.match(content):
            return '[%d bytes of binary content]'

        #if not all(char in string.printable for char in content):
        #    return '[%d bytes of binary content]'

        return content


class UnicodeJSONRenderer(BaseRenderer):
    """
    Renderer which serializes to json.
    """

    media_type = 'application/json'
    format = 'json'
    encoder_class = encoders.JSONEncoder

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `obj` into json.
        """
        if data is None:
            return ''

        # If 'indent' is provided in the context, then pretty print the result.
        # E.g. If we're being called by the BrowseableAPIRenderer.
        renderer_context = renderer_context or {}
        indent = renderer_context.get('indent', None)

        if accepted_media_type:
            # If the media type looks like 'application/json; indent=4',
            # then pretty print the result.
            base_media_type, params = parse_header(accepted_media_type.encode('ascii'))
            indent = params.get('indent', indent)
            try:
                indent = max(min(int(indent), 8), 0)
            except (ValueError, TypeError):
                indent = None

        return json.dumps(data, cls=self.encoder_class, indent=indent, ensure_ascii=False)