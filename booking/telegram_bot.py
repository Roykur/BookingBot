import telebot
import booking.constants as const

class Telegram_bot(telebot.TeleBot):
    def __init__(self):
        super(Telegram_bot, self).__init__(const.API_KEY)

    def send_results(self, results, params):
        self.send_message(const.GROUP_CHAT_ID,
                          f"<b>I found some deals for you in {params['location']}\nfrom {params['check_in']}"
                          f"to {params['check_out']}\nunder {params['max_price']}€</b>", parse_mode='HTML'
                          )

        for result in results:
            self.send_message(const.GROUP_CHAT_ID, result, parse_mode='HTML')
