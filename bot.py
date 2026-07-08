import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    [InlineKeyboardButton("📚 تعلم الفيوتشر", callback_data="learn")],
    [InlineKeyboardButton("📈 التوصيات", callback_data="signals")],
    [InlineKeyboardButton("🔷 التسجيل في MEXC", url="https://promote.mexc.com/b/FuturePro")],
    [InlineKeyboardButton("🔶 التسجيل في Bybit", url="https://partner.bybit.com/b/futurepro")],
    [InlineKeyboardButton("📢 قناة تيليجرام", url="https://t.me/+ECmgQ45jpR9lYjM0")],
    [InlineKeyboardButton("📘 صفحة فيسبوك", url="https://www.facebook.com/AlmutadawilAldhaki")],
    [InlineKeyboardButton("📰 أخبار العملات", callback_data="news")],
    [InlineKeyboardButton("🛡️ إدارة رأس المال", callback_data="risk")],
    [InlineKeyboardButton("💬 التواصل مع الإدارة", callback_data="support")],
]

reply_markup = InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحبًا بك في بوت المتداول الذكي\n\n"
        "اختر أحد الخيارات التالية:",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "learn":
        text = (
            "📚 تعلم الفيوتشر\n\n"
            "الفيوتشر هو تداول يعتمد على توقع حركة السعر.\n\n"
            "✅ Long = ربح عند صعود السعر.\n"
            "✅ Short = ربح عند هبوط السعر.\n"
            "✅ استخدم وقف الخسارة دائمًا."
        )

    elif query.data == "signals":
        text = (
            "📈 التوصيات\n\n"
            "سيتم نشر التوصيات اليومية هنا.\n\n"
            "مثال:\n"
            "العملة: BTCUSDT\n"
            "الدخول: 105000\n"
            "الهدف: 106500\n"
            "وقف الخسارة: 104500"
        )

    elif query.data == "news":
        text = (
            "📰 أخبار العملات\n\n"
            "سيتم نشر آخر أخبار سوق العملات الرقمية هنا."
        )

    elif query.data == "risk":
        text = (
            "🛡️ إدارة رأس المال\n\n"
            "• لا تخاطر بأكثر من 2% من رأس مالك في الصفقة.\n"
            "• استخدم وقف الخسارة.\n"
            "• لا تدخل برافعة مالية عالية دون خطة."
        )

    elif query.data == "support":
        text = (
            "💬 التواصل مع الإدارة\n\n"
            "راسلنا عبر تيليجرام:\n"
            "@YOUR_USERNAME"
        )

    else:
        text = "حدث خطأ."

    await query.message.reply_text(
        text,
        reply_markup=reply_markup,
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
