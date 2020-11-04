import telebot
from telebot import types

bot = telebot.TeleBot('1295931203:AAGv_1YA8thFutEaPM9VGGjlsNC3FqMhZ8c')


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Naruto')
    keyboard.row('My hero academy')
    keyboard.row('HanterxHanter')
    bot.send_message(message.chat.id, 'Choose one Anime from the list!!',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text.lower() == 'naruto':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Saske', 'Obito')
        keyboard.row('Tobirama', 'Madara')
        bot.send_message(message.chat.id, 'Choose one of Naruto Character '
                                          'and I will give you'
                                          'their biography!',
                         reply_markup=keyboard)
    elif message.text.lower() == 'my hero academy':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Bakugo', 'Todoroki', )
        keyboard.row('Midoriya')
        bot.send_message(message.chat.id, 'Chose one of My Hero'
                                          ' Academy Character '
                                          ' and I will give you their '
                                          ' biography! ',
                         reply_markup=keyboard)
    elif message.text.lower() == 'hanterxhanter':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Gon', 'Killua', )
        bot.send_message(message.chat.id, 'Chose one of HanterxHanter'
                                          ' Character '
                                          ' and I will give you '
                                          ' their biography! ',
                         reply_markup=keyboard)
    elif message.text.lower() == 'saske':
        bot.send_message(message.chat.id, '''Sasuke Uchiha
        is one of the last
        surviving members of Konohagakure's Uchiha clan.
        After his older brother,
        Itachi, slaughtered their clan,
        Sasuke made it his mission in life to
        avenge them by killing Itachi. He is added to
        Team 7 upon becoming a ninja and,
        through competition with his rival and best friend,
        Naruto Uzumaki,
        Sasuke starts developing his skills.''')
    elif message.text.lower() == 'obito':
        bot.send_message(message.chat.id, '''Obito Uchiha was a member of
        Konohagakure's Uchiha clan. He was believed
        to have died during the Third
        Shinobi World War, his only surviving
        legacy being the Sharingan he gave
        to his teammate, Kakashi Hatake. In truth,
        Obito was saved from death and
        trained by Madara Uchiha, but the events
        of the war left Obito disillusioned
        with reality, and he inherited Madara's
        plan to create an ideal world.
        Resurfacing under the names of Tobi and Madara Uchiha himself,
        Obito subtly took control of the Akatsuki,
        using them as a means to advance
        his machinations, eventually going public and starting the Fourth
        Shinobi World War. However, towards
        the war's conclusion, Obito had
        a change of heart and, as atonement,
        sacrificed his life to save
        the same world he sought to replace.''')
    elif message.text.lower() == 'tobirama':
        bot.send_message(message.chat.id, '''Tobirama Senju
        was a member of the
        renowned Senju clan, who, together with his
        elder brother and the Uchiha clan,
        founded the first shinobi village: Konohagakure.
        Throughout his lifetime,
        Tobirama would work tirelessly to achieve
        political stability and implement
        the institutions that made the village system work,
        thus ensuring Konoha's
        continuity and prosperity. After his
        brother's death, he would earn
        the title of Second Hokage.''')

    elif message.text.lower() == 'madara':
        bot.send_message(message.chat.id, '''Madara Uchiha
        was the legendary
        leader of the Uchiha clan.
        He founded Konohagakure alongside
        his childhood friend and rival, Hashirama Senju,
        with the intention
        of beginning an era of peace.
        When the two couldn't agree on how to
        achieve that peace, they fought for
        control of the village, a conflict
        which ended in Madara's death. Madara,
        however, rewrote his death and went
        into hiding to work on his own plans.''')
    elif message.text.lower() == 'bakugo':
        bot.send_message(message.chat.id, '''Katsuki is a crude,
        arrogant, short-tempered, and aggressive person,
        especiallyat the beginning of the series.
        Katsuki tends to come off as an anti-hero
        if not downright villainous for those
        not familiar with him.
        This problematic behavior goes all the
        way back to his early childhood
        days when he was known to bully a young,
        Quirkless, Izuku Midoriya.
        However, after being accepted into U.A.
        High School and experiencing several personal defeats,
        one of them even coming from Izuku, Katsuki has
        gradually changed into a
        less antagonistic person, albeit still retaining
        a lot of his unpleasant traits.
        While often portrayed negatively, Katsuki's fierce
        character and competitive
        drive have actually granted him an important
        role among Class 1-A, as a sort
        of inspirational mood-maker.''')
    elif message.text.lower() == 'todoroki':
        bot.send_message(message.chat.id, '''Shoto originall
        had a cold, aloof personality, which stemmed
        from his abusive upbringing
        and complicated family life. Focused and unemotional,
        Shoto preferred to keep to himself instead
        of hanging out with other people.
        After the events of the U.A. Sports Festival,
        however, Shoto notably became more sociable and kind,
        even gaining a sense of humor and occasionally smiling,
        although still retaining some fragments of his previous
        distant attitude. After the Provisional Hero License Course,
        he began opening up more to his classmates and has lightened
        up from his usually serious demeanor. Nonetheless, Shoto is not
        quite used to socializing yet, coming off as a bit dense
        when it comes to understanding certain figures of speech.''')
    elif message.text.lower() == 'midoriya':
        bot.send_message(message.chat.id, '''Izuku is a very timid,
        reserved, and polite boy, frequently overreacting to abnormal
        situations with exaggerated expressions.
        Due to years of being
        looked down on by Katsuki for lacking a Quirk,
        he is initially portrayed as insecure, tearful, vulnerable
        and non-expressive. These traits are especially
        present around Katsuki,
        who also constantly harangued him for his aspirations
        to become a hero.''')
    elif message.text.lower() == 'gon':
        bot.send_message(message.chat.id, '''Gon is an athletic,
        rustic, and friendly boy who is searching for adventure.
        Also, he is not very good at math. However, having spent a
        lot of time in the woods as a child,
        he is very good with animals.
        Gon is an Enhancer, who are known for being simple-minded
        and determined.
        This determination and talent lead to both potential
        allies and potential
        enemies trusting in him and taking his side.
        He has inhuman senses;
        Gon has a heightened sense of smell almost like a dog's,
        he also has very good vision, as well as
        having a very keen taste.
        Gon wants to become a Hunter because he wishes
        to find out the depths of
        an occupation that would cause a father
        to choose the profession over
        being with his own son. Simultaneously,
        his flaws lie in his
        temper and impulsive nature.
        Gon sometimes fails to think things
        through and such actions lead to him suffering.
        Though possessing talent far beyond the norm for his age,
        anytime his abilities are challenged, he feels as if he has
        to prove his antagonist wrong.He continually
        strives to obtain greater power,
        often becoming exceptionally stronger in his anger.
        But Gon's anger also leads to some
        extremely reckless tendencies.
        When his emotions are ignited,
        Gon becomes irrational and completely
        oblivious to anything else.
        While his will is stronger than most and
        he can be very level-headed,
        this clear mind can also make him
        very cold at times. When Gon is cool-headed,
        it is shown that he
        can think very creatively
        and thoughtfully to solve a problem.''')
    elif message.text.lower() == 'killua':
        bot.send_message(message.chat.id, '''Killua Zoldyck
        is initially
        introduced as a cheeky, cheerful kid full
        of mischievous ideas who
        befriends Gon during the Hunter Exam. However,
        his ruthlessness and aptitude in killing shows the other side
        of him — deadly, violent, and bloodthirsty.
        A member of the
        famous Zoldyck Family of assassins, Killua
        has been trained to
        be an assassin since birth and conditioned
        to possess extreme
        tolerance for poison, electricity and pain.
        Although Killua fails
        during his first Hunter Exam by killing
        an opponent, suspected
        to be due to his elder brother Illumi's
        influence, he attends the
        exam again the following year,
        earning his license by eliminating
        all other applicants in the very first trial.
        Killua and Gon learn about Nen from
        Wing and later train
        further under Biscuit Krueger.[ch. 47, 48, 137] He becomes
        one of the first people to beat Greed Island,
        helps stop the
        Chimera Ants, and uses his sibling
        Alluka's special abilities
        to heal the nearly-dead Gon.''')
    else:
        bot.send_message(message.chat.id, 'sorry, i can not find this!')


bot.polling()
