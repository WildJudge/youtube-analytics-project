import os
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # Получение данных о канале
        channel_info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_data = channel_info.get('items', [])[0]

        if channel_data:
            # Извлечение нужных данных
            channel_title = channel_data['snippet']['title']
            description = channel_data['snippet']['description']
            view_count = channel_data['statistics']['viewCount']
            subscriber_count = channel_data['statistics']['subscriberCount']
            video_count = channel_data['statistics']['videoCount']

            # Вывод информации
            print(f"Название канала: {channel_title}")
            print(f"Описание: {description}")
            print(f"Количество просмотров: {view_count}")
            print(f"Количество подписчиков: {subscriber_count}")
            print(f"Количество видео: {video_count}")
        else:
            print("Канал с указанным ID не найден.")
