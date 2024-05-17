from flask import Flask, render_template, request, send_from_directory, after_this_request
from flask_wtf import FlaskForm
from wtforms import FileField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from libs.stl_to_obj import stl_to_obj
from libs.csv_to_stl import convert_to_stl
import os

ALLOWED_EXTENSIONS = set(['csv', 'stl'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feup'




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    checkbox1 = BooleanField('csv to stl')
    checkbox2 = BooleanField('stl to obj')
    checkbox3 = BooleanField('csv to obj')
    convert = SubmitField('Convert and download')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('static/files/' + filename)
        if 'convert' in request.form:
            if form.checkbox1.data and form.checkbox2.data or form.checkbox1.data and form.checkbox3.data or form.checkbox2.data and form.checkbox3.data or form.checkbox1.data and form.checkbox2.data and form.checkbox3.data:
                return 'Please select only one option'
            if form.checkbox1.data: # csv to stl
                initial_extension = '.csv'
                final_extension = '.stl'  
                filename = process_file_csv_to_stl(filename)
            if form.checkbox2.data: # stl to obj
                initial_extension = '.stl'
                final_extension = '.obj'
                filename = process_file_stl_to_obj(filename)

            @after_this_request
            def remove_file(response):
                try:
                    os.remove('static/files/' + filename)
                    os.remove('static/files/' + filename.replace(initial_extension, final_extension))
                except Exception as error:
                    app.logger.error("Error removing or closing downloaded file handle", error)
                return response

            return send_from_directory('static/files/', filename.replace(initial_extension, final_extension), as_attachment=True)

    return render_template('index.html', form=form)

# stl to obj
def process_file_stl_to_obj(filename):
    print('Processing {filename} with function 1')
    stl_to_obj('static/files/' + filename)
  
    return filename

# csv to stl
def process_file_csv_to_stl(filename):
    print(f'Processing {filename} with function 2')
    convert_to_stl('static/files/' + filename, checkbox_action=True)
    return filename

if __name__ == '__main__':
    app.run(debug=True)