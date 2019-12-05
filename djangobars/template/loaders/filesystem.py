from django.template.loaders.filesystem import Loader as CoreLoader
from djangobars import settings
from .base import BaseHandlebarsLoader


class Loader(BaseHandlebarsLoader, CoreLoader):
    def __init__(self, engine, dirs=None):
        super(Loader, self).__init__(engine, dirs)

    def get_template_sources(self, template_name):
        """
        Returns the absolute paths to "template_name", when appended to each
        directory in "template_dirs". Any paths that don't lie inside one of the
        template dirs are excluded from the result set, for security reasons.
        """
        self.dirs = getattr(settings, 'HANDLEBARS_DIRS', None)
        return super(Loader, self).get_template_sources(template_name)
