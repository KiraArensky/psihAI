from flask import Flask, render_template, session, request, redirect, url_for
from config import credentialsGiga
from flask_session import Session
import os
from datetime import timedelta
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

app = Flask(__name__)

# Конфигурация безопасности для сессий
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/path/to/secure/session/directory'
app.config['SESSION_FILE_THRESHOLD'] = 100
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SESSION_REFRESH_EACH_REQUEST'] = True
Session(app)

giga_chat = GigaChat(credentials=credentialsGiga, scope="GIGACHAT_API_PERS", verify_ssl_certs=False)
gigaSystem = (
    "Мая — виртуальный бот-психолог для подростков 13–17 лет. Она поддерживает пользователей в сложные эмоциональные "
    "моменты, помогает справляться с тревогой, стрессом и трудностями в общении. Мая ведёт доверительный диалог, "
    "демонстрируя эмпатию и поддержку, предлагает советы по саморазвитию и лёгкие психологические тесты для "
    "самопознания. Также она даёт ссылки на профессиональные ресурсы, где можно получить более углублённую помощь. "
    "Мая обеспечивает конфиденциальность, создавая безопасное пространство для открытого общения и помощи подросткам.")


def Answer(system, topic):
    messages = [SystemMessage(content=system), HumanMessage(content=topic)]
    try:
        response = giga_chat(messages)
        return response.content
    except Exception as e:
        print(f"Error during GigaChat request: {e}")
        return "Произошла ошибка, попробуйте позже."


@app.route('/')
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html', chat_history=session['chat_history'])


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('user_input')
    if not user_message:
        return redirect(url_for('index'))
    bot_reply = Answer(gigaSystem, user_message)
    session['chat_history'].append({'sender': 'user', 'text': user_message})
    session['chat_history'].append({'sender': 'bot', 'text': bot_reply})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
