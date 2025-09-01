import os
import telegram
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

# البيانات المضمنة مباشرة في الكود - استبدل هذه القيم بمعلوماتك الحقيقية
BOT_TOKEN = '8430439548:AAGwv8wklw155KjjdMzfU9qiwoP5nlsowoA'  # استبدل بتوكن بوتك الحقيقي
CHAT_ID = '1002695113378'  # استبدل بمعرف محادثتك الحقيقي
VIDEO_URL = 'https://drive.googleapis.com/uc?export=download&id=1ELHdkIcV1aV-7fUcge6Qroj9tNDMJcdY'  # استبدل برابط الفيديو الحقيقي
MESSAGE_TEXT = 'متبقي 30 دقيقة على افتتاح السوق الامريكي'  # استبدل بالرسالة التي تريدها

bot = telegram.Bot(token=BOT_TOKEN)

async def send_daily_message():
    """إرسال الرسالة والفيديو في الساعة 14:00"""
    try:
        today = datetime.now().weekday()
        
        # 5: السبت، 6: الأحد - لا نرسل في هذه الأيام
        if today >= 5:
            print(f"اليوم هو {'السبت' if today == 5 else 'الأحد'}، لا يتم الإرسال")
            return
        
        print(f"بدأ الإرسال في {datetime.now()}")
        
        # إرسال الرسالة النصية
        await bot.send_message(chat_id=CHAT_ID, text=MESSAGE_TEXT)
        
        # إرسال الفيديو
        await bot.send_video(chat_id=CHAT_ID, video=VIDEO_URL)
        
        print(f"تم الإرسال بنجاح في {datetime.now()}")
    except Exception as e:
        print(f"حدث خطأ أثناء الإرسال: {e}")

async def main():
    # جدولة المهمة يومياً الساعة 14:00 (2 مساءً) - حسب توقيت UTC
    # بالنسبة للسعودية (UTC+3)، اضبط الساعة على 11:00 لتكون 14:00 في السعودية
    scheduler = AsyncIOScheduler()
    trigger = CronTrigger(hour=11, minute=0)  # 11:00 UTC = 14:00 في السعودية
    
    scheduler.add_job(send_daily_message, trigger)
    
    print("بدأ تشغيل بوت التلجرام والجدولة...")
    print(f"سيتم الإرسال يومياً في الساعة 14:00 بتوقيت السعودية (11:00 UTC)")
    print(f"ما عدا يومي السبت والأحد")
    print(f"التوكن: {BOT_TOKEN}")
    print(f"معرف المحادثة: {CHAT_ID}")
    print(f"رابط الفيديو: {VIDEO_URL}")
    print(f"الرسالة: {MESSAGE_TEXT}")
    
   try:
    await asyncio.Future()  # يعمل إلى أجل غير مسمى
except (KeyboardInterrupt, SystemExit):
    pass

if __name__ == "__main__":
    asyncio.run(main())




