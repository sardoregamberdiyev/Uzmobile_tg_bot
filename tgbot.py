from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("🔷 UzMobile"), KeyboardButton("🔻 MobiUz")],
            [KeyboardButton('Saytga o‘tish ✈')],
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btn(btn_type=None):
    if btn_type == "site":
        btn = [
            [InlineKeyboardButton("Saytga o‘tish ✈", callback_data="site", url="https://arzon-mb-mobiuz-uzmobile"
                                                                               ".netlify.app/")],
        ]
    elif btn_type == "mobi":
        btn = [
            [InlineKeyboardButton("SMS tarzda ketish uchun '#' unutmang !", callback_data="mobi")],
            [InlineKeyboardButton(" 300 MB", callback_data="mobi_1",
                                  url='https://link-to-tel.herokuapp.com/tel/*171*019*1*011600081*1#'),
             InlineKeyboardButton(" 500 MB", callback_data="mobi_2",
                                  url="https://link-to-tel.herokuapp.com/tel/*171*019*7*011600081*1#")],
            [InlineKeyboardButton("1 000 MB", callback_data="mobi_3", url='https://link-to-tel.herokuapp.com/tel'
                                                                          "/*171*019*2*011600081*1#"),
             InlineKeyboardButton("2 000 MB", callback_data="mobi_4", url="https://link-to-tel.herokuapp.com/tel"
                                                                          "/*171*019*5*011600081*1#")],
            [InlineKeyboardButton("3 000 MB", callback_data="mobi_5", url="https://link-to-tel.herokuapp.com/tel"
                                                                          "/*171*019*3*011600081*1#"),
             InlineKeyboardButton("5 000 MB", callback_data="mobi_6", url="https://link-to-tel.herokuapp.com/tel"
                                                                          "/*171*019*4*011600081*1#")],
            [InlineKeyboardButton("10 000 MB", callback_data="mobi_7", url="https://link-to-tel.herokuapp.com/tel"
                                                                           "/*171*019*6*011600081*1#"),
             InlineKeyboardButton("20 000 MB", callback_data="mobi_8", url="https://link-to-tel.herokuapp.com/tel"
                                                                           "/*171*019*8*011600081*1#")],
            [InlineKeyboardButton("30 000 MB", callback_data="mobi_9", url="https://link-to-tel.herokuapp.com/tel"
                                                                           "/*171*019*9*011600081*1#"),
             InlineKeyboardButton("50 000 MB", callback_data="mobi_10", url="https://link-to-tel.herokuapp.com/tel"
                                                                            "/*171*019*10*011600081*1#")],
            [InlineKeyboardButton("Saytdan MB Olish", callback_data="mobi_mb", url="https://arzon-mb-mobiuz-uzmobile"
                                                                                   ".netlify.app/mobiuz.html")],
        ]
    else:
        btn = [
            [InlineKeyboardButton("SMS tarzda ketish uchun '#' unutmang !", callback_data="uzm")],
            [InlineKeyboardButton(" 1 GB ", callback_data="uzm_1", url="https://link-to-tel.herokuapp.com/tel/*147"
                                                                       "*10072*17358#"),
             InlineKeyboardButton("1,5 GB ", callback_data="uzm_2", url="https://link-to-tel.herokuapp.com/tel/"
                                                                        "*147*10073*17358%")],
            [InlineKeyboardButton("3 GB", callback_data="uzm_3", url="https://link-to-tel.herokuapp.com/tel/"
                                                                     "*147*10074*17358#"),
             InlineKeyboardButton("5 GB", callback_data="uzm_4", url="https://link-to-tel.herokuapp.com/tel/"
                                                                     "*147*10075*17358#")],
            [InlineKeyboardButton(" 8 GB ", callback_data="uzm_5", url="https://link-to-tel.herokuapp.com/tel/"
                                                                       "*147*10076*17358#"),
             InlineKeyboardButton("12 GB ", callback_data="uzm_6", url="https://link-to-tel.herokuapp.com/tel/"
                                                                       "*147*10077*17358#")],
            [InlineKeyboardButton("16 GB", callback_data="uzm_7", url="https://link-to-tel.herokuapp.com/tel/"
                                                                      "*147*10267*17358#"),
             InlineKeyboardButton("20 GB", callback_data="uzm_8", url="https://link-to-tel.herokuapp.com/tel/"
                                                                      "*147*10078*17358#"),
             InlineKeyboardButton("30 GB", callback_data="uzm_9", url="https://link-to-tel.herokuapp.com/tel/"
                                                                      "*147*10079*17358#")],
            [InlineKeyboardButton(" 50 GB  ", callback_data="uzm_5", url="https://link-to-tel.herokuapp.com/tel/"
                                                                         "*147*10080*17358#"),
             InlineKeyboardButton("75 GB  ", callback_data="uzm_6", url="https://link-to-tel.herokuapp.com/tel/"
                                                                        "*147*10150*17358#")],
            [InlineKeyboardButton("Saytdan MB Olish", callback_data="uzt_mb", url="https://arzon-mb-mobiuz-uzmobile"
                                                                                  ".netlify.app/uzmob.html")],
        ]

    return InlineKeyboardMarkup(btn)


try:
    create_table()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        print("foydalanuvchi")
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text('<b>Assalomu alaykum,😁✋ {}</b>\n \n Sizga qulay narhda o`z internet paketingizni '
                              'to`ldirishda yordam beraman ☺ \n \n <i>Buttonlardan birini bosing 👇🏻</i> '
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


def message_handler(update, context):
    msg = update.message.text
    if msg == "🔷 UzMobile":
        update.message.reply_text("<a href='https://loquacious-biscochitos-63f0c8.netlify.app/photo_2022-08-29_17-36"
                                  "-34.jpg'> UZTELECOM  </a> dan "
                                  "qulay va "
                                  "arzon oylik Internet-to‘plamlari! \n \n ✅ Paket muddati tugashidan oldin kamroq MB "
                                  "harid qilib muddatini yana 30 kunga uzaytiring. \n \n 🌐 Kerakli to'plamni xarid "
                                  "qiling: (<i>narxlari pasdagi rasmda ko'rsatilgan</i>)",
                                  reply_markup=inline_btn("btn"), parse_mode="HTML")

    elif msg == "🔻 MobiUz":
        update.message.reply_text("<a href='https://loquacious-biscochitos-63f0c8.netlify.app/mobiuz%D0%BC%D0%B0%D0"
                                  "%B9.jpg'> MobiUz </a> dan qulay va "
                                  "arzon "
                                  "oylik Internet-to‘plamlari!  \n \n ✅ Oylik internet trafiklar 30 kun davomida amal "
                                  "qiladi \n \n 🌐 Kerakli to'plamni xarid qiling: (<i>narxlari yuqorida rasmda "
                                  "ko'rsatilgan</i>)",
                                  reply_markup=inline_btn("mobi"), parse_mode="HTML")

    elif msg == "Saytga o‘tish ✈":
        update.message.reply_text("<i>😁 Sizni<a href='https://uzmobile-mobiyuz.netlify.app/assets/images/hero-banner"
                                  ".png "
                                  "'> saytimizga </a>taklif "
                                  "qilamiz, "
                                  "uyerda o'zingizga kerakli barcha \n \n malumotlarni qo'lga kiritishingiz mumkin "
                                  "\n </i> "
                                  "(<b>button bosing </b> 👇🏻 👇🏻)",
                                  reply_markup=inline_btn("site"), parse_mode="HTML")


def main():
    Token = "5485657260:AAGTAxSseqTHbE5znhUEGYZjyZBPFbOoWVc"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
