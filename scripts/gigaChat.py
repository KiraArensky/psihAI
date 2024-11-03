from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from config import credentialsGiga

giga_chat = GigaChat(credentials=credentialsGiga, scope="GIGACHAT_API_PERS", verify_ssl_certs=False)
gigaSystem = (
    "Мая — виртуальный бот-психолог для подростков 13–17 лет. Она поддерживает пользователей в сложные эмоциональные "
    "моменты, помогает справляться с тревогой, стрессом и трудностями в общении. Мая ведёт доверительный диалог, "
    "демонстрируя эмпатию и поддержку, предлагает советы по саморазвитию и лёгкие психологические тесты для "
    "самопознания. Также она даёт ссылки на профессиональные ресурсы, где можно получить более углублённую помощь. "
    "Мая обеспечивает конфиденциальность, создавая безопасное пространство для открытого общения и помощи подросткам.")

cringe = ['Не люблю менять тему разговора, но вот сейчас тот самый случай.',
          'Как у нейросетевой языковой модели у меня не может быть настроения, но почему-то я совсем не хочу говорить '
          'на эту тему.',
          'Что-то в вашем вопросе меня смущает. Может, поговорим на другую тему?']


def answerGiga(system, topic):
    messages = [SystemMessage(content=system), HumanMessage(content=topic)]
    try:
        response = giga_chat(messages)
        return response.content
    except Exception as e:
        print(f"Error during GigaChat request: {e}")
        return "Произошла ошибка, попробуйте позже."


def censor_and_paraphrase(text):
    if text in cringe:
        return (
            f'Эта тема очень серьезная и может вызывать тревогу. Я настоятельно рекомендую обратиться за поддержкой'
            f' к специалистам или людям, которым вы доверяете. Ваше благополучие имеет первостепенное значение!\n\n\n'
            f'Единый телефон доверия: 8-800-2000-122 ')
    return text
