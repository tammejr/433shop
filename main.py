from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Bot Configuration
TOKEN = "7574850672:AAFnpvLklfq5jO9d5d6wPTgm2R0f4AaAQNk"
ADMIN_CHAT_ID = "1453107791"

# Star Packages (Birr and TON)
birr_prices = {
    'star_50': 150,
    'star_75': 230,
    'star_100': 300,
    'star_150': 450,
    'star_250': 750,
    'star_350': 980,
    'star_500': 1400,
    'star_750': 2250,
    'star_1000': 2600,
    'star_1500': 4200,
    'star_2500': 6600,
    'star_5000': 14600,
}

ton_prices = {
    'star_50': 0.15,
    'star_75': 0.21,
    'star_100': 0.37,
    'star_150': 0.53,
    'star_250': 0.87,
    'star_350': 1.21,
    'star_500': 1.75,
    'star_750': 2.64,
    'star_1000': 3.50,
    'star_1500': 5.18,
    'star_2500': 8.69,
}

# Payment Details
ton_wallet = "UQD2YkC_SO8R0ojXprYcCyL-nCNfR0OB9KeukzKlG18920-r"
telebirr = "0946264614"
cbe_account = "1000400243364"
abyssinia_account = "208687538"
account_name = "Nathan Kibru Maregn"


# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("⭐ Buy Star", callback_data='buy_star')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "እንኳን ወደ 4-3-3 Star ሽያጭ Bot በሰላም መጣችሁ 🌟\nStar ልመግዛት ከስር ያለውን 'Buy Star' ይጫኑ.",
        reply_markup=reply_markup
    )


# Payment Method Selection
async def buy_star(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💵 በ ብር ለመግዛት", callback_data='pay_birr')],
        [InlineKeyboardButton("🔹 በ Ton ለመግዛት", callback_data='pay_ton')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "የምትፈልጉትን የክፍያ አማራጭ ይምረጡ:",
        reply_markup=reply_markup
    )


# Display Birr Packages
async def show_birr_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['payment_method'] = 'birr'
    keyboard = [
        [InlineKeyboardButton(f"⭐ 50 Stars - {birr_prices['star_50']} Birr", callback_data='star_50')],
        [InlineKeyboardButton(f"⭐ 100 Stars - {birr_prices['star_100']} Birr", callback_data='star_100')],
        [InlineKeyboardButton(f"⭐ 250 Stars - {birr_prices['star_250']} Birr", callback_data='star_250')],
        [InlineKeyboardButton(f"⭐ 350 Stars - {birr_prices['star_350']} Birr", callback_data='star_350')],
        [InlineKeyboardButton(f"⭐ 500 Stars - {birr_prices['star_500']} Birr", callback_data='star_500')],
        [InlineKeyboardButton(f"⭐ 750 Stars - {birr_prices['star_750']} Birr", callback_data='star_750')],
        [InlineKeyboardButton(f"⭐ 1000 Stars - {birr_prices['star_1000']} Birr", callback_data='star_100')],
        [InlineKeyboardButton(f"⭐ 1500 Stars - {birr_prices['star_1500']} Birr", callback_data='star_1500')],
        [InlineKeyboardButton(f"⭐ 2500 Stars - {birr_prices['star_2500']} Birr", callback_data='star_2500')],
        [InlineKeyboardButton(f"⭐ 5000 Stars - {birr_prices['star_5000']} Birr", callback_data='star_5000')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "💵 በ ብር መግዛት የምትፈልጉትን መጠን ይምረጡ:",
        reply_markup=reply_markup
    )


# Display TON Packages
async def show_ton_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['payment_method'] = 'ton'
    keyboard = [
        [InlineKeyboardButton(f"⭐ 50 Stars - {ton_prices['star_50']} TON", callback_data='star_50')],
        [InlineKeyboardButton(f"⭐ 100 Stars - {ton_prices['star_100']} TON", callback_data='star_100')],
        [InlineKeyboardButton(f"⭐ 250 Stars - {ton_prices['star_250']} TON", callback_data='star_250')],
        [InlineKeyboardButton(f"⭐ 350 Stars - {ton_prices['star_350']} TON", callback_data='star_350')],
        [InlineKeyboardButton(f"⭐ 500 Stars - {ton_prices['star_500']} TON", callback_data='star_500')],
        [InlineKeyboardButton(f"⭐ 750 Stars - {ton_prices['star_750']} TON", callback_data='star_750')],
        [InlineKeyboardButton(f"⭐ 1000 Stars - {ton_prices['star_1000']} TON", callback_data='star_1000')],
        [InlineKeyboardButton(f"⭐ 1500 Stars - {ton_prices['star_1500']} TON", callback_data='star_1500')],
        [InlineKeyboardButton(f"⭐ 2500 Stars - {ton_prices['star_2500']} TON", callback_data='star_2500')]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "🔹 በ Ton መግዛት የምትፈልጉትን መጠን ይምረጡ:",
        reply_markup=reply_markup
    )


# Ask for Telegram Username
async def request_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    package = update.callback_query.data
    context.user_data['package'] = package
    await update.callback_query.message.reply_text("Star እንዲገዛበት የምትፈልጉትን የ Telegram Username ያስገቡ - ያለ Telegram Username መግዛት አንችልም!:")


# Send Payment Details Based on Method
async def payment_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    recipient_username = update.message.text
    context.user_data['recipient_username'] = recipient_username
    package = context.user_data['package']
    payment_method = context.user_data['payment_method']

    if payment_method == 'birr':
        amount = birr_prices[package]
        payment_message = (
            f"💵 ከስር በተዘረዘሩት የክፍያ አማራጮች {amount} Birr ይላኩ:\n"
            f"1. Telebirr - {telebirr}\n"
            f"2. CBE - {cbe_account}\n"
            f"3. Abyssinia - {abyssinia_account}\n\n"
            f"Name: {account_name}\n\n"
            "ክፍያ የፈፀማችሁበት ማረጋገጫ Screenshot የሚከተለውን ማስፈንጠሪያ ተጭነው ያስገቡ."
        )
    else:
        amount = ton_prices[package]
        payment_message = (
            f"🔹 Please send {amount} TON to the wallet below:\n\n"
            f"`{ton_wallet}`\n\n"
            "ክፍያ የፈፀማችሁበት ማረጋገጫ Screenshot የሚከተለውን ማስፈንጠሪያ ተጭነው ያስገቡ."
        )

    keyboard = [[InlineKeyboardButton("ብሩን አስገብቻለሁ", callback_data='send_screenshot')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(payment_message, reply_markup=reply_markup, parse_mode="Markdown")


# Prompt for Screenshot Upload
async def handle_send_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("Please upload a screenshot of the payment.")


# Handle Screenshot Upload and Admin Notification
async def handle_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1].file_id
    recipient_username = context.user_data['recipient_username']
    package = context.user_data['package']
    buyer_chat_id = update.effective_user.id

    keyboard = [
        [InlineKeyboardButton("✅ Verify", callback_data=f"verify_{buyer_chat_id}_{recipient_username}_{package}")],
        [InlineKeyboardButton("❌ Reject", callback_data=f"reject_{buyer_chat_id}_{recipient_username}_{package}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        ADMIN_CHAT_ID,
        photo,
        caption=f"📩 *New Order!*\n\n"
                f"👤 *Recipient Username:* @{recipient_username}\n"
                f"⭐️ *Package:* {package.replace('star_', '')} Stars\n\n"
                "Please verify the payment:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    await update.message.reply_text("4-3-3ን ስለተጠቀሙ እናሰመግናለን ክፍያ መፈፀማችሁን ለማረጋገጥ እየሞከርን ስለሆነ ጥቂት ይጠብቁን.")


# Verification Handler
async def verify_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Limit to 3 splits to avoid too many values
    data = query.data.split('_', 3)
    buyer_chat_id, recipient_username, package = data[1], data[2], data[3]

    # Notify the buyer of successful verification
    await context.bot.send_message(
        chat_id=buyer_chat_id,
        text=f"✅ Your payment for *{package.replace('star_', '')} Stars* (Username: @{recipient_username}) has been verified!",
        parse_mode="Markdown"
    )

    # Update admin message
    await query.edit_message_caption(
        caption=f"✅ Payment for @{recipient_username} - {package.replace('star_', '')} Stars has been Verified.",
        parse_mode="Markdown"
    )


# Rejection Handler
async def reject_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Limit to 3 splits to avoid too many values
    data = query.data.split('_', 3)
    buyer_chat_id, recipient_username, package = data[1], data[2], data[3]

    # Notify the buyer of rejection
    await context.bot.send_message(
        chat_id=buyer_chat_id,
        text=f"❌ Your payment for *{package.replace('star_', '')} Stars* (Username: @{recipient_username}) was rejected.",
        parse_mode="Markdown"
    )

    # Update admin message
    await query.edit_message_caption(
        caption=f"❌ Payment for @{recipient_username} - {package.replace('star_', '')} Stars has been Rejected.",
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buy_star, pattern='^buy_star$'))
    app.add_handler(CallbackQueryHandler(show_birr_packages, pattern='^pay_birr$'))
    app.add_handler(CallbackQueryHandler(show_ton_packages, pattern='^pay_ton$'))
    app.add_handler(CallbackQueryHandler(request_username, pattern='^star_'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, payment_details))
    app.add_handler(MessageHandler(filters.PHOTO, handle_screenshot))
    app.add_handler(CallbackQueryHandler(handle_send_screenshot, pattern='^send_screenshot$'))
    app.add_handler(CallbackQueryHandler(verify_order, pattern='^verify_'))
    app.add_handler(CallbackQueryHandler(reject_order, pattern='^reject_'))

    app.run_polling()


if __name__ == "__main__":
    main()
