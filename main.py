from myapi import create_app, db

app = create_app()  # aqui você cria o app
with app.app_context():
    db.create_all()  # cria as tabelas

if __name__ == '__main__':
    app.run(debug=True)
