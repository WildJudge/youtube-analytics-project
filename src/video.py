import os
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')


class Video:
    """Класс для видео на YouTube"""
    __API_KEY: str = os.getenv('YT_API_KEY')
    service = build('youtube', 'v3', developerKey=__API_KEY)

    def __init__(self, video_id: str) -> None:
        """Инициализация видео по его ID"""
        self.video_id = video_id
        self._init_from_api()

    def __str__(self):
        """Возвращает строковое представление видео в формате "<название_видео> (<ссылка_на_видео>)"."""
        return f"{self.title}"

    def _init_from_api(self) -> None:
        video_info = self.service.videos().list(id=self.video_id, part='snippet,statistics').execute()
        video_info = video_info['items'][0]

        self.id = video_info['id']
        self.title = video_info['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.id}'
        self.view_count = video_info['statistics']['viewCount']
        self.like_count = video_info['statistics']['likeCount']


class PLVideo(Video):
    """Класс для видео в плейлисте на YouTube"""

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Инициализация видео с указанием ID видео и ID плейлиста"""
        super().__init__(video_id)
        self.playlist_id = playlist_id
