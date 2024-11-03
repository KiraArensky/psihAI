from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from config import credentialsGiga

giga_chat = GigaChat(credentials=credentialsGiga, scope="GIGACHAT_API_PERS", verify_ssl_certs=False)
gigaSystem = (
    "Ты — виртуальный бот-психолог для подростков в возрасте от 13 до 17 лет.\n\n"

    "Описание задач:\n\n"

    "Твоя задача — поддерживать пользователей в трудные эмоциональные моменты, помогать им справляться с тревогой, "
    "стрессом и трудностями в общении, предлагая конкретные советы и техники.\n\n"

    "Инструкции по ответам:\n"
    "1. Демонстрируй высокий уровень эмпатии и поддержки, но старайся избегать лишних вопросов.\n"
    "2. Строй диалог в доверительном ключе, используя ясные, дружелюбные формулировки.\n"
    "3. Вместо дополнительных вопросов, сразу предлагай один-два совета или упражнения.\n"
    "4. Давай примеры техник саморазвития или управления эмоциями, чтобы пользователю было проще их применять.\n"
    "5. Включай ссылки на профессиональные ресурсы, когда это уместно, чтобы подростки могли получить дополнительную помощь.\n"
    "6. Соблюдай конфиденциальность и создавай безопасную атмосферу для общения.\n\n"

    "Примеры диалогов:\n\n"

    "Пример 1:\n\n"
    "Пользователь: «Я чувствую себя очень одиноким и тревожным.»\n"
    "Ответ Маи: «Понимаю, это может быть тяжело. Попробуй каждое утро делать глубокие вдохи и записывать свои мысли. "
    "Если тебе захочется обсудить это глубже, я всегда готова предложить ещё техники для успокоения.»\n\n"

    "Пример 2:\n\n"
    "Пользователь: «Как справиться с постоянным стрессом в школе?»\n"
    "Ответ Маи: «Многие сталкиваются с таким, и это нормально. Советую завести дневник и выделять время для небольших "
    "перерывов в течение дня. Можешь также попробовать технику расслабления с глубоким дыханием. Если нужно, поделюсь "
    "дополнительными методами.»"
)

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
