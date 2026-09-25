from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚍 আমি Shuttle CU → NM-এ আছি",
                callback_data="cu_nm"
            )
        ],
        [
            InlineKeyboardButton(
                "🚍 আমি Shuttle NM → CU-এ আছি",
                callback_data="nm_cu"
            )
        ],
        [
            InlineKeyboardButton(
                "📍 Shuttle Location",
                callback_data="view_location"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚌 CU SHUTTLE LIVE\n\n"
        "আপনি কী করতে চান?",
        reply_markup=reply_markup
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    if query.data == "cu_nm":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📍 Start Tracking",
                    web_app=WebAppInfo(
                        url="https://github.com/rakibul5656/cu-shuttle/blob/main/index.html"
                    )
                )
            ]
        ]

        await query.message.reply_text(
            "🚍 আপনি Shuttle 1 select করেছেন।\n\n"
            "GPS tracking শুরু করতে নিচের button চাপুন।",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "nm_cu":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📍 Start Tracking",
                    web_app=WebAppInfo(
                        url="https://github.com/rakibul5656/cu-shuttle/blob/main/index.html"
                    )
                )
            ]
        ]

        await query.message.reply_text(
            "🚍 আপনি Shuttle 2 select করেছেন।\n\n"
            "GPS tracking শুরু করতে নিচের button চাপুন।",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "view_location":

        await query.message.reply_text(
            "📍 Live shuttle location এখনো setup করা হয়নি।"
        )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("CU Shuttle Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
