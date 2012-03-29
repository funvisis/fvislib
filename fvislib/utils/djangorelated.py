# -*- coding: utf-8 -*-

import os
import datetime
import time
import zipfile

from django.core.files.uploadedfile import SimpleUploadedFile

def get_path_to_app_repo(app_name):
    from django.conf import settings
    return get_path_to_app_repo(settings.project_name, app_name)

def get_path_to_app_repo_(project_name, app_name, model_name=''):
    '''
    Returns a function needed by the 'upload_to' parameter of Django's
    FileField
    '''

    def get_path_function(instance, filename):
        filename_splitted = filename.rsplit('.', 1)
#        return time.strftime(os.path.join('{}/{}/%Y/%m/%d/'.format(project_name, app_name), '.'.join([filename_splitted[0], datetime.datetime.now().isoformat(), filename_splitted[1]])))
        return time.strftime(
            os.path.join(
                project_name,
                app_name, model_name,
                '%Y', '%m', '%d',
                '.'.join([
                        filename_splitted[0],
                        datetime.datetime.now().isoformat(),
                        filename_splitted[1]])))
    
    return get_path_function

def open_zip_file(zip_file) :
    if isinstance(zip_file, SimpleUploadedFile) and os.path.isfile(zip_file.temporary_file_path()):
        return zipfile.ZipFile(zip_file.temporary_file_path())
    else:
        return zipfile.ZipFile(zip_file)

def load_zip_file(zip_file):
    zip = open_zip_file(zip_file)
    bad_file = zip.testzip()
    if bad_file:
        raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
    count = 1
    files = {}
    for filename in zip.namelist():
        if filename.startswith('__'): # do not process meta files
            continue
        data = zip.read(filename)
        files[filename] = data
    zip.close()
    return files

def verify_image(_file):
    if len(_file) == 0:
        return False
    # Required PIL classes may or may not be available from the root namespace
    # depending on the installation method used.
    try:
        import Image
    except ImportError:
        try:
            from PIL import Image
        except ImportError:
            raise ImportError('Unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.')
    from cStringIO import StringIO
    try:
        # the following is taken from django.newforms.fields.ImageField:
        #  load() is the only method that can spot a truncated JPEG,
        #  but it cannot be called sanely after verify()
        trial_image = Image.open(StringIO(_file))
        #trial_image.load()
        # verify() is the only method that can spot a corrupt PNG,
        #  but it must be called immediately after the constructor
        trial_image = Image.open(StringIO(_file))
        trial_image.verify()
    except:
        return False
    return True

