
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class UploadCsvFileForm(FlaskForm):
    file_upload = FileField('Upload data file', validators=[FileAllowed(['csv','xlsx'])])
    submit = SubmitField('Upload')