import time
from booking.booking import Booking
from booking.handle_results import Results
from booking.telegram_bot import Telegram_bot

def check_prices(params):
    with Booking() as bot:
        bot.landing_page()
        bot.accept_cookies()
        bot.change_language()
        bot.place_to_go(params['location'])
        bot.dates(check_in_date=params['check_in'], check_out_date=params['check_out'])
        # press submit button
        bot.submit()

        bot.close_sign_in_window()
        bot.apply_filters()
        bot.refresh()  # to let the bot fetch the data properly
        results = Results(driver=bot)
        results = results.handle_results(max_price=params['max_price'])

    # print what we got and when
    print(results)
    curr_time = time.localtime()
    print(f'{curr_time.tm_hour}:{curr_time.tm_min}')

    # send results via the telegram bot
    if results:
        telegram_bot = Telegram_bot()
        telegram_bot.send_results(results, params)


# main loop
while True:
    parameters = {'location': 'Israel Dead Sea', 'check_in': '2022-11-16', 'check_out': '2022-11-17', 'max_price': 250}
    check_prices(parameters)
    time.sleep(60*30)  #scrape every 30 minutes
