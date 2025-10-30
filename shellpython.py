from app import create_app
from models import db, User
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

# Cria um usuário admin
admin = User(
    name="Administrador",
    email="admin@catalogo.com",
    password_hash=generate_password_hash("123456"),
    is_admin=True
)

# Salva no banco
db.session.add(admin)
db.session.commit()

print("✅ Usuário administrador criado com sucesso!")
