from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import logging

# Bot Configuration
TOKEN = "7574850672:AAFnpvLklfq5jO9d5d6wPTgm2R0f4AaAQNk"
ADMIN_CHAT_ID = "1453107791"

# Star Packages (Birr and TON)
birr_prices = {
    'star_50': 180,
    'star_75': 250,
    'star_100': 300,
    'star_150': 450,
    'star_250': 750,
    'star_350': 1050,
    'star_500': 1500,
    'star_750': 2250,
    'star_1000': 3000,
    'star_1500': 4500,
    'star_2500': 7000,
    'star_5000': 15000,
}
0
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

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
⭐️ Welcome to 4-3-3 Star Service! ⭐️
We are here to make your experience seamless and enjoyable. Below are some frequently asked questions to guide you:

🔹 General Questions:

1. How do I purchase stars?  
- Tap 'Buy Star' and select the payment method (Birr or TON). Choose the package you want and follow the instructions.

2. What payment methods are available?  
- We currently accept:  
  - Telebirr:
  - CBE (Commercial Bank of Ethiopia): 
  - Abyssinia Bank: 
  - TON (crypto payments).

3. Is there a discount for bulk purchases?  
- Yes! Orders of 4000 stars or more receive a 5% discount.

4. What if I need a custom number of stars?  
- Contact us directly for custom packages or large orders.
 
5. Do you accept international payments?  
- At the moment, we primarily accept local payments. TON is available for international users.

🔹 Order Process:

6. How do I confirm my payment?  
- After making the payment, upload a screenshot as proof. We will verify and process your order shortly.

8. How long does it take to receive stars after payment?  
- Typically, stars are delivered within 5-15 minutes after payment verification. Delays may occur during high traffic, but we ensure prompt delivery.

8. What if I make a mistake during the payment?  
- Please contact support immediately with your payment details, and we will assist you.

🔹 Account and Security:

9. Do I need to provide my Telegram username for the purchase?  
- Yes, to deliver stars directly to your account, we require your Telegram username.

10. Is my information safe with you?  
- Absolutely! We prioritize your privacy and never share your details with third parties.

🔹 Support and Contact:

11. How can I contact support?  
- You can reach us directly through the bot by typing /support or contact us at 0946264614.

12. What should I do if my order is delayed?  
- If you haven’t received your stars within 30 minutes, please message us directly, and we will resolve the issue promptly.

13. Can I request a refund?  
- Refunds are available in the case of failed or incorrect orders. Please ensure to provide proof of payment for a faster resolution.

🔹 Additional Information:

14. Can I purchase stars for someone else?  
- Yes! Provide their Telegram username during the purchase process.

15. Do stars expire?  
- No, stars do not expire and can be used at any time.

🔹 Need Further Assistance?  
- If you have any questions not covered here, please don't hesitate to reach out! We're here to help.  

🌟 Thank you for choosing 4-3-3 Star Service! 🌟
"""
    keyboard = [
        [InlineKeyboardButton("📞 Contact Support", url=f"https://t.me/TammeJr")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(help_text, reply_markup=reply_markup)



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
    await update.callback_query.message.reply_text("Star እንዲገዛበት የምትፈልጉትን የ Telegram Username ያስገቡ !:")


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

    keyboard = [[InlineKeyboardButton("Screenshot", callback_data='send_screenshot')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(payment_message, reply_markup=reply_markup, parse_mode="Markdown")


# Prompt for Screenshot Upload
async def handle_send_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("Please upload a screenshot of the payment. Screenshot ልካችሁ ከቆየ @TammeJr ላይ ያናግሩኝ.")


# Handle Screenshot Upload and Admin Notification
async def handle_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        photo = update.message.photo[-1].file_id

        # Ensure user_data has required keys to avoid KeyError
        recipient_username = context.user_data.get('recipient_username', 'Unknown')
        package = context.user_data.get('package', 'Unknown')
        buyer_chat_id = update.effective_user.id

        keyboard = [
            [InlineKeyboardButton("✅ Verify", callback_data=f"verify_{buyer_chat_id}_{recipient_username}_{package}")],
            [InlineKeyboardButton("❌ Reject", callback_data=f"reject_{buyer_chat_id}_{recipient_username}_{package}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send photo to admin for verification
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
        await update.message.reply_text("Thank you! Your payment is being verified. for support contact @tammejr")

    except Exception as e:
        logging.error(f"Screenshot Error: {e}")
        await update.message.reply_text("Screenshot እንደገና ያስገቡ - An error occurred while processing your screenshot. Please try again.")


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
    app.add_handler(CommandHandler("help", help_command))  # Register help command
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
