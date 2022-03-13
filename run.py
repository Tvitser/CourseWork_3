import prettytable

from project.config import DevelopmentConfig, TestingConfig
from project.models import Genre
from project.server import create_app, db

app = create_app(DevelopmentConfig)

@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
    }

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
    # with app.app_context():
    #     session = db.session()  # свой json в соответствующий аргумент
    #     cursor = session.execute("""SELECT um.movie_id,m.title, username FROM user
    #     join user_movie um on user.id = um.user_id
    #     join movie m on um.movie_id = m.id""").cursor  # функции post
    #     mytable = prettytable.from_db_cursor(cursor)
    #     mytable.max_width = 30
    #     print("БАЗА ДАННЫХ")
    #     print(mytable)