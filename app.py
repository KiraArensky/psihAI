from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import os
from datetime import timedelta

from scripts.gigaChat import answerGiga, gigaSystem, censor_and_paraphrase

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

    user_message = censor_and_paraphrase(user_message)
    bot_reply = answerGiga(gigaSystem, user_message)
    bot_reply = censor_and_paraphrase(bot_reply)

    session['chat_history'].append({'sender': 'user', 'text': user_message})
    session['chat_history'].append({'sender': 'bot', 'text': bot_reply})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
