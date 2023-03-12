# micropython-wake-word
micropython persian wake word detection with poor converted ML functions


bruh

I just wanted to do it for fun.
But in reality that was just pain in the ass for months. listen, DO NOT DO THIS AGAIN

what you need :
raspberry pi pico
MAX4466 microphone(OUT PIN ----- 28GPIO PIN)


in your pc : 
sckit-learn -> for creating your ML model
m2cgen      -> for converting your created model, to a python function(that is good to use in micropython)
python-minimizer

note : you CAN NOT make your created .py file larger than 26kb. because you will get some memory error on raspberry pi pico.


دوستان فارسی زبانی که مراجعه کردند، این نتیجه برای من مناسبه ولی باید بگم که ممکنه با اون چیزی که شما میخواد نتیجه فرق داشته باشه
شما میتونید دوتا فایل زیر رو داخل رزبری پایتون آپلود کنید و بعد فایل تست ریکوگنیشن رو اجرا کنین
svm_min10.py
test_recognition.py

با گفتن خاموش و روشن، ال ای دی روی برد خاموش و روشن میشه. اگه 10 بار پشت سر هم روشن بگین، همچنان روشن میمونه ولی وقتی خاموش بگید خاموش میشه

برای ساخت مدل و فایل مدنظر خودتون، اول باید سمپل ضبط کنید. پس فایل سمپل کریتور رو آپلود کنین، خط دهم سمپل نیم رو عوض کنین و کلمه مدنظر خودتون رو بزارید
مثلا من گذاشتم off
و شروع به ضیط کنید. حدود 3 دهم ثانیه طول میکشه فرایند ضبط کردن هر سمپل
بعد میگه اینتر بزنین که بره سمپل بعدی
وقتی اینتر میزنین نیم ثانیه وامیسته بعد میگه صحبت کنین

بعد از ضبط سمپل هاتون، فولدرای ایجاد شده رو کپی و در یک فولدر به اسم Samples پیست(paste) کنین
فایل samples_to_csv.py رو اجرا کنید
فایل خروجی csv میشه دیتاست شما
به هر طریقی که دوست دارید مدلتون رو بسازید
در نهایت، از طریق m2cgen ازش خروجی بگیرید
و از طریق python-minimizer
https://pypi.org/project/python-minimize/
حجم فایل خودتون رو کم کنید و بعد آپلودش کنین


در نهایت هم یه لینک میدم که گویا از روش های بهتری برای این کار استفاده میکنه
سعی کنین از C++ استفاده کنید برای ماشین لرنینگ روی رزبری پای پیکو
و اینکه چون رمش خیلی نتیجه ای که بدست میارید به شدت محدود شده هست
https://www.youtube.com/watch?v=w_sCTPDuutQ
