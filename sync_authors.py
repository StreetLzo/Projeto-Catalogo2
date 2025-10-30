# sync_authors.py
from app import create_app
from models import db, User, Project

app = create_app()

with app.app_context():
    projetos = Project.query.all()
    total = 0
    sem_user = 0

    for p in projetos:
        if p.authors_text:
            nomes = [n.strip().lower() for n in p.authors_text.split(',') if n.strip()]
            associados = []
            for nome in nomes:
                user = User.query.filter(db.func.lower(User.name) == nome).first()
                if user and user not in p.authors:
                    p.authors.append(user)
                    associados.append(user.name)
                    total += 1
            if associados:
                print(f"✅ Projeto '{p.title}' vinculado a: {', '.join(associados)}")
            else:
                sem_user += 1
                print(f"⚠️  Nenhum usuário encontrado para '{p.authors_text}' no projeto '{p.title}'")
    db.session.commit()
    print(f"\n✅ Sincronização finalizada!")
    print(f"➡️  {total} associações criadas.")
    print(f"❌ {sem_user} projetos não encontraram autores correspondentes.")
