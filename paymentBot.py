import telebot
from telebot.types import LabeledPrice
from telebot.types import ShippingOption

import config

provider_token = '361519591:TEST:fd5ecf282f5637d92bba385fb639ccb7'  # @BotFather -> Bot Settings -> Payments
bot = telebot.TeleBot(config.token)

prices = [LabeledPrice(label='Машина времени', amount=5750), LabeledPrice('Gift wrapping', 500)]

shipping_options = [
    ShippingOption(id='instant', title='WorldWide Teleporter').add_price(LabeledPrice('Teleporter', 1000)),
    ShippingOption(id='pickup', title='Local pickup').add_price(LabeledPrice('Pickup', 300))]


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id,
                     "Привет. Я демо-бот онлайн-оплаты."
                     " Предлагаю тебе купить машину времени."
                     " Команда /buy производит заказ, команда /terms выводит соглашения для оплаты")


@bot.message_handler(commands=['terms'])
def command_terms(message):
    bot.send_message(message.chat.id,
                     'Благодарим вас за покупки у нашего демо-бота. Надеемся, вам понравится ваша новая машина времени!\n'
                     '1. Если ваша машина времени не была доставлена вовремя, повторите попытку.\n'
                     '2. Если вы обнаружите, что ваша машина времени не работает, свяжитесь с нашим сервисом lumospark.com.'
                     ' Они будут доступны в любом месте в период с мая 2075 года по ноябрь 4000 г. C.E.\n'
                     '3. Если вы хотите возмещение, пришлите заявку на возврат и мы немедленно отправим его вам.')


@bot.message_handler(commands=['buy'])
def command_pay(message):
    bot.send_message(message.chat.id,
                     "Настоящие карты не работают, никакие деньги не будут списываться из вашей учетной записи."
                     " Используйте этот номер тестовой карты для оплаты вашей машины времени: `4242 4242 4242 4242`"
                     "\n\n:Это ваш демо-счет", parse_mode='Markdown')
    bot.send_invoice(message.chat.id, title='Машина рабочего времени',
                     description='Хотите посетить своих великих пра-пра-прадедов?'
                                 ' Сделать состояние на гонках?'
                                 ' Закажите нашу машину времени сегодня!',
                     provider_token=provider_token,
                     currency='usd',
                     photo_url='http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg',
                     photo_height=512,  # !=0/None or picture won't be shown
                     photo_width=512,
                     photo_size=512,
                     is_flexible=False,  # True If you need to set up Shipping Fee
                     prices=prices,
                     start_parameter='time-machine-example',
                     invoice_payload='HAPPY FRIDAYS COUPON')


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='О, похоже, наши курьеры-собаки сегодня обедают. Попробуйте позже!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Иностранцы пытались украсть CVV вашей карты, но мы успешно защитили ваши учетные данные,"
                                                " попробуйте снова заплатить за несколько минут, нам нужен небольшой отдых.")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     ' Спасибо за оплату! Мы выполним ваш заказ для `{} {}` как можно быстрее!'
                     'Оставайтесь на связи! \n\n Купите снова, чтобы получить машину времени для вашего друга!'.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')


bot.skip_pending = True
bot.polling(none_stop=True, interval=0)