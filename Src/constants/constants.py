import os

UPLOAD_FOLDER='upload' # temp storage
CONVERTED_FOLDER='output'# temp storage
#TEMP_FOLDER="tmp"
LIBREOFFICE_PATH = '/usr/bin'
LOG_FOLDER='logs'
os.environ['UNO_PATH'] = LIBREOFFICE_PATH
#ALLOWED_EXTENSIONS={'jpg','jpeg','png','doc','docx','csv','xlsx','ppt','pptx'}
ALLOWED_EXTENSIONS={
            'pptx', 'ppt', 'pps', 'ppsx', 'odp',
            'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'pbm', 'pgm', 'ppm', ' xbm', 'webp',
            'doc', 'docx', 'docm', 'dot', 'dotm', 'dotx', 'odt', 'rtf', 'txt', 'wps', 'xml', ' xps',
            'xlsx', 'xlsm', 'xltx', 'csv', 'pdf', 'odt', 'ods', 'odp', 'odg', 'odf'
}
ALLOWED_IMAGE_EXTENSIONS={'jpg', 'jpeg', 'png', ' gif', ' bmp', 'tiff', 'pbm', 'pgm', 'ppm', 'xbm', 'webp'}
ALLOWED_DOCUMENT_EXTENSIONS={'doc', 'docx', 'docm', 'dot', 'dotm', 'dotx', 'odt', 'rtf', 'txt', 'wps'}
ALLOWED_CSV_EXTENSIONS={'csv'}
ALLOWED_PPT_EXTENSIONS={'pptx', 'ppt', 'pps', 'ppsx', 'odp'}
ALLOWED_EXCEL_EXTENSIONS={'xps',
            'xlsx', 'xlsm', 'xltx', 'csv', 'pdf', 'odt', 'ods', 'odp', 'odg', 'odf'}