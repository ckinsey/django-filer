from django.conf import settings
from filer.server.backends.default import DefaultServer
from filer.storage import PublicFileSystemStorage, PrivateFileSystemStorage
from filer.utils.loader import load_object, storage_factory
import os
import urlparse

FILER_SUBJECT_LOCATION_IMAGE_DEBUG = getattr(settings, 'FILER_SUBJECT_LOCATION_IMAGE_DEBUG', False)

FILER_IS_PUBLIC_DEFAULT = getattr(settings, 'FILER_IS_PUBLIC_DEFAULT', False)

FILER_STATICMEDIA_PREFIX = os.path.normpath( getattr(settings, 'FILER_STATICMEDIA_PREFIX', os.path.join(settings.MEDIA_URL,'filer/') ) ) + '/'

FILER_PUBLICMEDIA_PREFIX = os.path.normpath( getattr(settings, 'FILER_PUBLICMEDIA_PREFIX', 'filer_public') )
FILER_PRIVATEMEDIA_PREFIX = os.path.normpath( getattr(settings, 'FILER_PRIVATEMEDIA_PREFIX', 'filer_private') )

# please don't change these in settings for now. all media dirs must be beneath MEDIA_ROOT!
FILER_PUBLICMEDIA_URL = os.path.normpath( getattr(settings, 'FILER_PUBLICMEDIA_URL', os.path.join(settings.MEDIA_URL,FILER_PUBLICMEDIA_PREFIX) ) )
FILER_PUBLICMEDIA_ROOT = os.path.abspath( os.path.join(settings.MEDIA_ROOT, FILER_PUBLICMEDIA_PREFIX ) )

FILER_PRIVATEMEDIA_URL = os.path.normpath( getattr(settings, 'FILER_PRIVATEMEDIA_URL', os.path.join(settings.MEDIA_URL,FILER_PRIVATEMEDIA_PREFIX) ) )
FILER_PRIVATEMEDIA_ROOT = os.path.abspath( os.path.join(settings.MEDIA_ROOT, FILER_PRIVATEMEDIA_PREFIX ) )


FILER_ADMIN_ICON_SIZES = (
        '16', '32', '48', '64', 
)

# Public media (media accessible without any permission checks)
FILER_PUBLICMEDIA_STORAGE = load_object(getattr(
                    settings,
                    'FILER_PUBLICMEDIA_STORAGE',
                    storage_factory(
                        klass=PublicFileSystemStorage,
                        location=os.path.abspath(
                            os.path.join(settings.MEDIA_ROOT,
                                         'filer')),
                        base_url=urlparse.urljoin(settings.MEDIA_URL,
                                                  'filer/')
                    )))
FILER_PUBLICMEDIA_UPLOAD_TO = load_object(getattr(settings, 'FILER_PUBLICMEDIA_UPLOAD_TO', 'filer.utils.generate_filename.by_date'))
FILER_PUBLICMEDIA_THUMBNAIL_STORAGE = load_object(getattr(
                    settings,
                    'FILER_PUBLICMEDIA_THUMBNAIL_STORAGE',
                    storage_factory(
                        klass=PublicFileSystemStorage,
                        location=os.path.abspath(
                            os.path.join(settings.MEDIA_ROOT,
                                         'filer_thumbnails')),
                        base_url=urlparse.urljoin(settings.MEDIA_URL,
                                                  'filer_thumbnails/')
                    )))


# Private media (media accessible through permissions checks)
FILER_PRIVATEMEDIA_STORAGE = load_object(getattr(
                    settings,
                    'FILER_PRIVATEMEDIA_STORAGE',
                    storage_factory(
                        klass=PrivateFileSystemStorage,
                        location=os.path.abspath(
                            os.path.join(settings.MEDIA_ROOT,
                                         '../smedia/filer/')),
                        base_url=urlparse.urljoin(settings.MEDIA_URL,
                                                  '/smedia/filer/')
                    )))
FILER_PRIVATEMEDIA_UPLOAD_TO = load_object(getattr(settings, 'FILER_PRIVATEMEDIA_UPLOAD_TO',
                                       'filer.utils.generate_filename.by_date'))
FILER_PRIVATEMEDIA_THUMBNAIL_STORAGE = load_object(getattr(
                    settings,
                   'FILER_PRIVATEMEDIA_THUMBNAIL_STORAGE',
                    storage_factory(
                        klass=PrivateFileSystemStorage,
                        location=os.path.abspath(
                            os.path.join(settings.MEDIA_ROOT,
                                         '../smedia/filer_thumbnails/')),
                        base_url=urlparse.urljoin(settings.MEDIA_URL,
                                                  '/smedia/filer_thumbnails/')
                    )))
FILER_PRIVATEMEDIA_SERVER = getattr(settings, 'FILER_PRIVATEMEDIA_SERVER', DefaultServer())
FILER_PRIVATEMEDIA_THUMBNAIL_SERVER = getattr(settings, 'FILER_PRIVATEMEDIA_THUMBNAIL_SERVER', DefaultServer())
