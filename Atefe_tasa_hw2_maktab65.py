class Credit_travel_kart:                             #کلاس برای کارت متروی اعتباری
    def __init__(self,credit):
        self.credit=credit
    def write_off(self):                               #متد برای کم کردن اعتبار از کارت مترو
        if self.credit!=0:
            self.credit=self.credit-1                #اگراعتبار برابر 0 نبود یک واحد ازش کم کن
            print("you can pass!")
        else:
            print("you are out of credit!")           #در غیر این صورت اگر اعتبار 0 بود پیغام مناسب را چاپ کن

    def charge(self):                                  #متد برای شارژ کردن کارت به میزان یک واحد
        self.credit=self.credit+1
    def show_credit(self):                             #متد برای نشان دادن میزان شارژ کارت بلیط
        if self.credit==0:
            print("you are out of credit!")
        else:
            print(f"your credit is:{self.credit}")

class Credit_time_kart(Credit_travel_kart):              #کلاس کارت اعتباری مدت دار که این کلاس فرزند کلاس بالا است
    def __init__(self,credit,expiration):                #متد سازنده که دو پارامتر اعتبار و تاریخ انقضا را میگیرد
        self.expiration=str(expiration)
        Credit_travel_kart.__init__(self,credit)
    def check_expiration(self,current_date):              #متد برای تشخیص دادن گذشته شدن اعتبار کارت که یا مقدارtrue برمیکرداند یا مقدار false
        yearE,monthE,dayE=self.expiration.split('/')       #متغیر نمونه self.expiration را از هم جدا میکند و داخل 3 متغیر میریزد
        yearC,monthC,dayC =current_date.split('/')
        if yearC<=yearE:                                  #مقایسه تاریخ کنونی با تاریخ انقضای کارت
            if yearC<yearE:
                return True
            elif yearC==yearE:
                if monthC<monthE:
                    return True
                elif monthC>monthE:
                    return False
                elif monthC==monthE:
                    if dayC<=dayE:
                        return True
                    elif dayC>dayE:
                        return False
        elif yearC>yearE:
            return False

class Single_travel_kart:                             #کلاس برای بلیط تک سفره
    def __init__(self,credit=1):
        self.credit=credit
    def write_off(self):
        if self.credit==1:
            self.credit=0
            print("you can pass!")
        elif self.credit==0:
            print("you can not use this for more than one trip!")
#من ورودی ها را داخل برنامه گرفتم به شرح زیر از هز کلاس یک شی ساختم
single=Single_travel_kart()                        #ایجاد شی از کلاس کارت تک سفره
single.write_off()                          #دفعه اول استفاده از کارت تک سفره سیستم اجازه عبور به مسافر را میدهد
single.write_off()                         #یک واحد دیگر از اعتبار کارت تک سفره کم میکنیم و بار دوم سیستم اجازه عبور به مسافر رل نمیدهد
print("\n","\n")
credit_time=Credit_time_kart(7,'1400/7/27')        #ایجاد شی از کلاس کارت اعتباری مدت دار اعتبار آنرا 7 در نظر گرفتم و تاریخ انقضای آنرا 1400/7/27
if credit_time.check_expiration('1400/7/28')==True:  #تاریخ کنونی را 1400/7/28 در نظر گرفتم
    print("you can pass!")
    credit_time.write_off()
    credit_time.show_credit()
else:
    print("your kart is expired!")
print("\n","\n")
credit=Credit_travel_kart(9)
credit.show_credit()
for i in range(10):
    credit.charge()
credit.show_credit()
































