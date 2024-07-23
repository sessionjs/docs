import os
import shutil

def copy_get(config, **kwargs):
  site_dir = config['site_dir']
  shutil.copy('docs/static/googleaf976fe97260dc6a.html', site_dir)