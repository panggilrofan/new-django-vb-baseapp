# pylint: disable=W0613

import datetime
import os

from slugify import slugify

__all__ = ['save_file']


def save_file(instance, filename, upload_to='upload/%Y/%m/%d/'):
    """

    By default, this saves to : `MEDIA_ROOT/upload/2017/09/06/`

    You can customize this. In your `models.py`:

        from vb_baseapp.utils import save_file as custom_save_file

        def my_custom_uploader(instance, filename):

            # do your stuff
            # at the end, call:

            my_custom_upload_path = 'images/%Y/'
            return custom_save_file(instance, filename, upload_to=my_custom_upload_path)

        class MyModel(models.Model):
            image = models.FileField(
                upload_to='my_custom_uploader',
                verbose_name=_('profile image'),
            )

    """

    file_basename, file_extension = os.path.splitext(filename)

    safe_basename = slugify(file_basename)
    extension = file_extension.lower()
    file_savename = f'{safe_basename}{extension}'
    now = datetime.datetime.now()
    upload_to = now.strftime(upload_to)
    return f'{upload_to}{file_savename}'
