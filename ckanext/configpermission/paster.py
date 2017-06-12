from ckan.lib.cli import CkanCommand


class InitCommand(CkanCommand):
    """
    Initialize database tables.
    """
    max_args = 0
    min_args = 0
    usage = __doc__
    summary = __doc__.strip().split('\n')[0]

    def command(self):
        self._load_config()
        from .model import create_tables
        create_tables()


class CreateDefaultDataCommand(CkanCommand):
    """
    Initialize database tables.
    """
    max_args = 0
    min_args = 0
    usage = __doc__
    summary = __doc__.strip().split('\n')[0]

    def command(self):
        self._load_config()
        from .model import create_default_data
        from .plugin import permissions
        create_default_data(permissions=permissions)