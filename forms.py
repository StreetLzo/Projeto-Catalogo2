# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed

class RegisterForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirme a senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class ProjectForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Descrição', validators=[DataRequired()])
    authors = StringField('Autores (separe por vírgula)', validators=[DataRequired()])
    file = FileField('Arquivo (pdf, imagens ou zip)', validators=[FileAllowed(['pdf','png','jpg','jpeg','zip'])])
    submit = SubmitField('Publicar')
