import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Med:
    _lst: tuple = (
        '- Профессор, вы лично будете меня оперировать?\n- Да, хочу, знаете ли, проверить поговорку "Глаза не видят, руки помнят"...',
        '- Доктор, меня беспокоит, что в последнее время я себя хорошо чувствую.\n- Хм-м, голубчик, при многих серьезных болезнях люди чувствуют себя хорошо...',
        '- Доктор, как мне это вылечить?\n- Сейчас загуглю.\n- А, может, я сам?\n- Вот давайте не будем самолечением заниматься...',
        '- Через три дня приходите на проверку, манту водой не мочить.\n- Доктор, а святой водой можно?',
        '- Итак, больной, чем вы, на ваш взгляд, могли отравиться?\n- Сухим кормом для собак. Моя собака почувствовала себя плохо, и я решил проверить, не корм ли тому причина.',
        '- Доктор, у меня музыка в голове играет.\n- И что?\n- Я такую не слушаю.',
        '- Доктор, а вы сможете избавить меня от целлюлита?\n- Нет, но я подскажу, где продаются дешевые леопардовые лосины.',
        'Доктор плохого не посоветует, но и хорошего не разрешит.',
        'Как говорят платные венерологи - одни на ошибках молодости учатся, другие на них зарабатывают.',
        '- Пристрелите его, чтоб не мучился.\n- Доктор! У нас частная клиника, а не государственная, здесь так нельзя.',
        '- Больной, вы водочкой балуетесь?\n- Нет, доктор, у меня это серьезно.',
        '- Способы восстановления организма зависят от состояния больного и уровня насыщения кислородом крови.\n- Безусловно, и чем больше состояние, тем эффективнее способы.',
        'Экзамен в медвузе. Профессор - студенту:\n- Назовите стандартное оборудование прививочного кабинета.\n- Спирт, кушетка, медсестра.',
        '- Знаете ли вы, почему больничные санитары такие крепкие и здоровые?\n- Так они медицинский спирт витаминами закусывают!',
        '- Вот и грибы пошли... - задумчиво вздохнула медсестра, промывая желудок пациенту.',
        'На помощь станциям переливания крови пришли генетики, скрестив пчёл с комарами.\nС одного улья новый гибрид собирает до 200 литров крови в месяц.',
        '- Представляете, как нужно было психовать людям средневековья, чтобы вызвать эпидемию чумы?',
        '- Есть на борту гомеопат?\n- А что случилось?\n- Астрологу плохо!',
        'В мединституте могут отчислить не только за неуспеваемость, но и за красивый почерк!',
        'Из обсуждения древних людей:\n- Конечно, люди болели меньше. Практически один раз...',
        '- У моего бывшего, похоже, коронавирус, но он не знает об этом.\n- С чего ты решила?\n- Он потерял вкус. Вчера я его видела с новой подругой - чучундра, каких мало.',
        'Психиатр поздравляет своего пациента с прогрессом в лечении.\n- И это вы называете прогрессом? Полгода назад я был Наполеоном, а сейчас я - никто...',
        '- Как называется доктор, выезжающий на вызовы по домам?\n- Врач-парацетамолог.',
        'Современные стоматологи сперва лечат не зубы, а психологические травмы после советской стоматологии.',
        'Хирург пациенту, лежащему на операционном столе:\n- Операция будет демонстрироваться по телевидению, поэтому постарайтесь почаще улыбаться!',
        'Два главных вопроса любому врачу: 1) Я буду жить? 2) А пить можно?',
        'Доктор предложил мне пропить железо. Теперь у меня нет машины и гаража...',
        'Когда лётчик обращается к пассажирам по громкой связи, понимаешь, что почерк врачей\n- это не самая неразборчивая вещь на свете.',
        'После посещения пластической клиники эконом-класса лица клиентов выглядят дёшево, но сердито.',
        'Психиатр получает деньги, задавая пациентам те же вопросы, которые его жена задает ему дома каждый день.',
        'Тот неловкий момент, когда вся твоя семья радовалась, что у них будет личный доктор,\nа ты закончил универ и стал психиатром.',
        '- К врачу живая очередь?\n- Пока еще да.',
        'Известного врача спросили, что такое здоровье.\n- Здоровье, - ответил профессор, - это когда у вас каждый день болит в другом месте...',
        'Как уверяют врачи, пятьдесят граммов коньяка за ужином\n- это не просто не полезно, но еще и мало.',
        '- Доктор, я жалуюсь на бессонницу, сегодня ночью, например:\nпросыпался 12 раз и ни разу после этого не заснул.',
        'Хирургия - это разбушевавшаяся терапия!',
        '- Доктор, с помощью интернета я уже выяснил причины своих недомоганий.\nНо решил зайти к вам, чтобы услышать альтернативное мнение...',
        'Вниманию студентов 5-го курса мединститута!\nЗавтра в аудитории 47 вам будут ломать руки, чтобы почерк соответствовал врачебным стандартам.',
        'Иногда думаю: "Как  классно  было  бы  завести отношения".\nПотом  смотрю  на  свой  график и  добавляю:\n"Вот тут, в октябре... на  пару  часов... наверное..."',
        'Учишься  шесть лет  в  медицинском, потом  два года  интернатуры.\nА пациенты  больше верят  Малахову...',
        '- Доктор, я больше не могу выдерживать эту диету, вчера чуть не откусила ухо мужу.\n- Подумаешь, всего каких-то 80 калорий.',
        'Наркоз был общий, а хирург - местный...',
        'Заключение хирурга:\n"Задета не только кора головного мозга, но и, так сказать, сама его древесина..."',
        '- Ф-фу, - облегченно вздохнул хирург, выходя из операционной.\n- Подумать только, еще 2 дня - и пациент выздоровел бы без моей помощи.',
        'Больной:\n- А процедура будет проходить с анестезией?\nВрач:\n- Конечно! Анестезия Петровна, подержите больного...',
        'В реанимацию привозят раненого с ножом, торчащим между лопатками.\n- Больно? - спрашивает хирург.\n- Только когда смеюсь.',
        '- Почему вы не пьете лекарства?\n- Они же противные.\n- А вы пейте лекарства и думайте, что это коньяк.\n- Лучше уж я буду пить коньяк и думать, что пью лекарства.',
        'Неправильно говорить "жаба душит".\nПравильно говорить - "амфибиотропная асфиксия".',
        'Любая болезнь смертельна, если правильно гуглить.',
        'Это просто вопрос времени, когда к моему имени и фамилии добавят слово "синдром"'
    )

    @property
    def prikol(self) -> str:
        return random.choice(self._lst)


med = Med()
