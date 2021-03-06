import os, json
import MySQLdb as mysql
import sys

   
BASE = os.path.dirname(os.path.realpath(__file__))
FILE_CONFIG = os.path.join(BASE, 'config.json')


ALLOWED_EXTENSIONS = (['xlsx'])
def allowed_file_import(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

try:
    with open(FILE_CONFIG) as config:
        data_json = json.loads(config.read())
except Exception as e:
    print e

status = data_json['status']
STATIC_PATH = data_json['static_path']
GMT = int(data_json['gmt'])

if status == 'production':
    UPLOAD_FOLDER = data_json['upload_folder']
    UPLOAD_url = data_json['upload_url']
    IMPORT_FOLDER = data_json['import_folder']
else:
    UPLOAD_FOLDER = os.path.join(BASE, 'app/static/upload')
    UPLOAD_url = os.path.join('app/static/upload')
    IMPORT_FOLDER = os.path.join(BASE, 'app/static/upload')

