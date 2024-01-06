from flask import request, redirect, send_from_directory, render_template, make_response
from werkzeug.utils import secure_filename
from Src.controller.Converter import Converter

from Src.constants.constants import ALLOWED_EXTENSIONS, ALLOWED_IMAGE_EXTENSIONS, ALLOWED_DOCUMENT_EXTENSIONS,  ALLOWED_CSV_EXTENSIONS, ALLOWED_PPT_EXTENSIONS, ALLOWED_EXCEL_EXTENSIONS
from Src.util.logger import custom_logger
from Src.util.util import allowed_file
import os
import logging

class ConversionController:
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger(__name__)
        self.converter = Converter()

    def convert_to_pdf(self, input_path, output_path):
        file_extension = input_path.rsplit('.', 1)[1].lower()
        print(f"File extension: {file_extension}")
        custom_logger.debug(f"File Extension: {file_extension}")
        if file_extension in ALLOWED_IMAGE_EXTENSIONS:
            self.converter.convert_image_to_pdf(input_path, output_path)
        elif file_extension in ALLOWED_DOCUMENT_EXTENSIONS:
            self.converter.convert_doc_to_pdf(input_path, output_path)
        elif file_extension in ALLOWED_CSV_EXTENSIONS:
            self.converter.convert_csv_to_pdf(input_path,output_path)
        elif file_extension in ALLOWED_PPT_EXTENSIONS:
            self.converter.convert_ppt_to_pdf(input_path,output_path)
        elif file_extension in ALLOWED_EXCEL_EXTENSIONS:
            self.converter.convert_excel_to_pdf(input_path,output_path)
        else:
            self.logger.error(f"unsupported file type: {file_extension}")

    def upload(self):
        if 'file' not in request.files:
            self.logger.error('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            self.logger.error('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            converted_filename = f"{os.path.splitext(filename)[0]}_converted.pdf"
            converted_file_path = os.path.join(self.app.config['CONVERTED_FOLDER'], converted_filename)

            file.save(file_path)
            custom_logger.debug(f"File Uploaded: {filename}")
            self.convert_to_pdf(file_path, converted_file_path)

            try:
                return render_template('conversion.html', upload_success=True, converted_filename=converted_filename)
            finally:
                os.remove(file_path)
        else:
            self.logger.error('Invalid file type. Please upload a supported file.')
            return render_template('conversion.html', upload_success=False)

    def download(self,filename):
        file_path=os.path.join(self.app.config['CONVERTED_FOLDER'],filename)
        if not os.path.exists(file_path):
            return make_response("file note found",404)
        else:
                try:
                    response= make_response(send_from_directory(self.app.config['CONVERTED_FOLDER'], filename, as_attachment=True))
                    os.remove(file_path)
                    custom_logger.debug(f"File downloaded: {filename}")
                    return response
                except Exception as e:
                    self.logger.error(f"error during download: {e}")
                    return make_response("error during download", 500)
