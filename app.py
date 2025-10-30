# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, abort
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from dotenv import load_dotenv
import uuid

from models import db, User, Project, Favorite

from forms import RegisterForm, LoginForm, ProjectForm

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)




load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'troca_urgentemente'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') or 'sqlite:///catalog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ---------- Rotas ----------
    @app.route('/')
    def index():
        q = request.args.get('q', '').strip()
        page = request.args.get('page', 1, type=int)
        if q:
            projects = Project.query.filter(
                (Project.title.ilike(f'%{q}%')) |
                (Project.description.ilike(f'%{q}%')) |
                (Project.authors_text.ilike(f'%{q}%'))
            ).order_by(Project.created_at.desc())
        else:
            projects = Project.query.order_by(Project.created_at.desc())
        projects = projects.paginate(page=page, per_page=10, error_out=False)
        return render_template('index.html', projects=projects, q=q)

    
    

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password_hash, form.password.data):
                login_user(user, remember=form.remember.data)
                flash('Bem-vindo!', 'success')
                return redirect(url_for('index'))
            flash('Credenciais incorretas.', 'danger')
        return render_template('login.html', form=form)
    
        # === REGISTRO DE USUÁRIO COM FOTO DE PERFIL ===
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()

        if form.validate_on_submit():
            from werkzeug.security import generate_password_hash
            from werkzeug.utils import secure_filename
            import uuid, os

            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user:
                flash('E-mail já cadastrado. Faça login ou use outro e-mail.', 'warning')
                return redirect(url_for('register'))

            # Processa a foto de perfil, se houver
            foto_nome = None
            if form.foto.data:
                arquivo = form.foto.data
                nome_seguro = secure_filename(arquivo.filename)
                foto_nome = f"{uuid.uuid4().hex}_{nome_seguro}"
                upload_path = os.path.join(app.config['UPLOAD_FOLDER'], foto_nome)
                arquivo.save(upload_path)

            # Cria o novo usuário
            novo_user = User(
                name=form.name.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data),
                foto_perfil=foto_nome
            )

            db.session.add(novo_user)
            db.session.commit()
            flash('Cadastro realizado com sucesso! Faça login para continuar.', 'success')
            return redirect(url_for('login'))

        return render_template('register.html', form=form)


    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Desconectado.', 'info')
        return redirect(url_for('index'))

    def allowed_file(filename):
        return '.' in filename

    @app.route('/project/new', methods=['GET', 'POST'])
    @login_required
    def create_project():
        form = ProjectForm()
        if form.validate_on_submit():
            filename = None
            if form.file.data:
                f = form.file.data
                orig = secure_filename(f.filename)
                unique = f"{uuid.uuid4().hex}_{orig}"
                path = os.path.join(app.config['UPLOAD_FOLDER'], unique)
                f.save(path)
                filename = unique
            project = Project(
                title=form.title.data,
                description=form.description.data,
                file_path=filename,
                authors_text=form.authors.data
            )
            # tenta associar autores registrados por nome (opcional)
            names = [n.strip() for n in form.authors.data.split(',') if n.strip()]
            for name in names:
                u = User.query.filter(User.name.ilike(name)).first()
                if u and u not in project.authors:
                    project.authors.append(u)

            db.session.add(project)
            db.session.commit()
            flash('Projeto publicado!', 'success')
            return redirect(url_for('index'))
        return render_template('project_create.html', form=form)

    @app.route('/project/<int:project_id>')
    def project_detail(project_id):
        project = Project.query.get_or_404(project_id)
        is_fav = False
        if current_user.is_authenticated:
            is_fav = Favorite.query.filter_by(user_id=current_user.id, project_id=project.id).first() is not None
        return render_template('project_detail.html', project=project, is_fav=is_fav)

    @app.route('/uploads/<filename>')
    def uploads(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

    @app.route('/project/<int:project_id>/favorite', methods=['POST'])
    @login_required
    def favorite_toggle(project_id):
        project = Project.query.get_or_404(project_id)
        fav = Favorite.query.filter_by(user_id=current_user.id, project_id=project.id).first()
        if fav:
            db.session.delete(fav)
            db.session.commit()
            flash('Removido dos favoritos.', 'info')
        else:
            fav = Favorite(user_id=current_user.id, project_id=project.id)
            db.session.add(fav)
            db.session.commit()
            flash('Adicionado aos favoritos.', 'success')
        return redirect(request.referrer or url_for('project_detail', project_id=project.id))

    def can_edit(project):
        return current_user.is_authenticated and (current_user.is_admin or current_user in project.authors)

    @app.route('/project/<int:project_id>/edit', methods=['GET', 'POST'])
    @login_required
    def edit_project(project_id):
        project = Project.query.get_or_404(project_id)
        if not can_edit(project):
            abort(403)
        form = ProjectForm(obj=project)
        if form.validate_on_submit():
            project.title = form.title.data
            project.description = form.description.data
            project.authors_text = form.authors.data
            # arquivo novo?
            if form.file.data:
                f = form.file.data
                orig = secure_filename(f.filename)
                unique = f"{uuid.uuid4().hex}_{orig}"
                path = os.path.join(app.config['UPLOAD_FOLDER'], unique)
                f.save(path)
                project.file_path = unique
            # atualizar associação de autores por nome (tenta encontrar usuários)
            project.authors = []
            names = [n.strip() for n in form.authors.data.split(',') if n.strip()]
            for name in names:
                u = User.query.filter(User.name.ilike(name)).first()
                if u:
                    project.authors.append(u)
            db.session.commit()
            flash('Projeto atualizado.', 'success')
            return redirect(url_for('project_detail', project_id=project.id))
        # preencher campo authors com texto salvo
        if request.method == 'GET':
            form.authors.data = project.authors_text
        return render_template('edit_project.html', form=form, project=project)

    @app.route('/project/<int:project_id>/delete', methods=['POST'])
    @login_required
    def delete_project(project_id):
        project = Project.query.get_or_404(project_id)
        if not can_edit(project):
            abort(403)
        # remover arquivo fisico (opcional)
        if project.file_path:
            try:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project.file_path))
            except Exception:
                pass
        db.session.delete(project)
        db.session.commit()
        flash('Projeto excluído.', 'info')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_panel():
        if not current_user.is_admin:
            abort(403)
        projects = Project.query.order_by(Project.created_at.desc()).all()
        users = User.query.order_by(User.name).all()
        return render_template('admin.html', projects=projects, users=users)
    
    # === FAVORITOS ===
    @app.route('/favoritos')
    @login_required
    def favoritos():
        favs = Favorite.query.filter_by(user_id=current_user.id).all()
        projetos = [fav.project for fav in favs]
        return render_template('favoritos.html', projetos=projetos)

    # === PERFIL DO USUÁRIO ===
    @app.route('/perfil', methods=['GET', 'POST'])
    @login_required
    def perfil():
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')

            if nome:
                current_user.name = nome
            if email:
                current_user.email = email
            if senha:
                from werkzeug.security import generate_password_hash
                current_user.password_hash = generate_password_hash(senha)

            db.session.commit()
            flash('Informações atualizadas com sucesso!', 'success')
            return redirect(url_for('perfil'))

        return render_template('perfil.html')

    return app  


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
