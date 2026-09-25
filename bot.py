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


# ============================================================
# BOT SETTINGS
# ============================================================

BOT_TOKEN = "8958291442:AAG1DsHaHBG0MJgnjICW-llaKI4OVbC-0ok"

# Example:
# https://yourusername.github.io/CU-Shuttle-Bot/
MINI_APP_URL = "https://rakibul5656.github.io/cu-shuttle/"


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "🚍 CU → NM",
                callback_data="cu_nm"
            )
        ],
        [
            InlineKeyboardButton(
                "🚍 NM → CU",
                callback_data="nm_cu"
            )
        ],
        [
            InlineKeyboardButton(
                "🚶 I'm not in the Shuttle",
                callback_data="not_in_shuttle"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# /start
# ============================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        "🚌 CU SHUTTLE LIVE\n\n"
        "আপনি কী করতে চান?\n\n"
        "আপনার গন্তব্য/রুট নির্বাচন করুন:",

        reply_markup=main_menu()
    )


# ============================================================
# BUTTON HANDLER
# ============================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    # --------------------------------------------------------
    # CU → NM
    # --------------------------------------------------------

    if query.data == "cu_nm":

        route_name = "CU → NM"

        mini_app_url = (
            f"{MINI_APP_URL}?route=cu_nm"
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "📍 Continue",
                    web_app=WebAppInfo(
                        url=mini_app_url
                    )
                )
            ]
        ]

        await query.message.reply_text(

            "🚍 আপনার নির্বাচিত রুট:\n"
            f"<b>{route_name}</b>\n\n"

            "📍 Location tracking শুরু করতে "
            "নিচের button চাপুন।\n\n"

            "GPS permission দিলে আপনার location "
            "shuttle-এর current location estimate করতে "
            "ব্যবহার করা হবে।",

            reply_markup=InlineKeyboardMarkup(keyboard),

            parse_mode="HTML"
        )


    # --------------------------------------------------------
    # NM → CU
    # --------------------------------------------------------

    elif query.data == "nm_cu":

        route_name = "NM → CU"

        mini_app_url = (
            f"{MINI_APP_URL}?route=nm_cu"
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "📍 Continue",
                    web_app=WebAppInfo(
                        url=mini_app_url
                    )
                )
            ]
        ]

        await query.message.reply_text(

            "🚍 আপনার নির্বাচিত রুট:\n"
            f"<b>{route_name}</b>\n\n"

            "📍 Location tracking শুরু করতে "
            "নিচের button চাপুন।\n\n"

            "GPS permission দিলে আপনার location "
            "shuttle-এর current location estimate করতে "
            "ব্যবহার করা হবে।",

            reply_markup=InlineKeyboardMarkup(keyboard),

            parse_mode="HTML"
        )


    # --------------------------------------------------------
    # NOT IN SHUTTLE
    # --------------------------------------------------------

    elif query.data == "not_in_shuttle":

        await query.message.reply_text(

            "🚶 <b>আপনি বর্তমানে কোনো shuttle-এ নেই।</b>\n\n"

            "আপনার location tracking প্রয়োজন নেই।\n\n"

            "যখন shuttle-এ উঠবেন, আবার /start দিয়ে "
            "আপনার route নির্বাচন করতে পারবেন।",

            parse_mode="HTML"
        )


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    print(
        "ERROR:",
        context.error
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print("================================")
    print("CU Shuttle Bot")
    print("Starting...")
    print("================================")


    application = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    application.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )


    application.add_error_handler(
        error_handler
    )


    print("Bot is running...")
    print("Press Ctrl+C to stop.")


    application.run_polling()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()