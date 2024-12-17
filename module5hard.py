# Задание "Свой YouTube":
import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if self.nickname == other.nickname:
            return True

    def __hash__(self, password):
        return hash(self.password)


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title


class UrTube:

    def __init__(self):

        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname, password):

        for tmp_user in self.users:
            if nickname == tmp_user.nickname and hash(password) == tmp_user.password:
                self.current_user = tmp_user

    def register(self, nickname, password, age, ):
        join_user = User(nickname, password, age)
        if join_user not in self.users:
            self.users.append(join_user)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for video in other:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, pattern: str):
        find_list = list()
        for video in self.videos:
            if video.title.lower().find(pattern.lower()) != -1:
                find_list.append(video.title)
        return find_list

    def watch_video(self, title):
        if self.current_user is None:
            return print(f'Войдите в аккаунт, чтобы смотреть видео')
        for x in self.videos:
            if x.title == title:
                if x.adult_mode and self.current_user.age < 18:
                    return print(f'Вам нет 18 лет, пожалуйста покиньте страницу')

                for time_play in range(1, x.duration + 1):
                    print(time_play, end=' ')
                    time.sleep(1)
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
