import csv
from numpy import random

class Quiz:
    def __init__(self,id,question,answer):
        self.id=id
        self.question=question
        self.answer=answer
    def compare(self,user_answer):
        if user_answer==None:
            return None
        if user_answer==self.answer:
            return True
        else:
            return False
    def __str__(self):
        return self.question

class TrueFalse(Quiz):
    def __init__(self,id,question, answer):
        Quiz.__init__(self,id,question, answer)
    def compare(self,user_answer):
        if self.answer=='true':
            if user_answer==1:
                return True
            elif user_answer==2:
                return False
            elif user_answer==None:        #اگر کاربر هیچ پاسخی وارد نکرد مقدار None را برگردان
                return None
        elif self.answer=='false':
            if user_answer==2:
                return True
            elif user_answer==1:
                return False
            elif user_answer==None:
                return None
    def add_to_file(self,writer_object):  #متدی برای اضافه کردن سوال صحیح و غلط ساخته شده به فایل سوالات صحیح و غلط
        with open('truefalse.csv',mode='a') as csvfile:
            writer_object.writerow(self.__dict__)
    '''
    در  اینستنس متد بالا به جای آرگومان  رایتر آبجکت  شی رایتر قرار خواهد گرفت که در  خط 107 مقدار دهی شده است
    ''' 
                     
class MultipleChoise(Quiz):
    def __init__(self,id,question,option1,option2,option3,option4,answer):
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.option4=option4
        Quiz.__init__(self,id,question, answer)
    def add_to_file(self,writer_object):
        with open('multiplechoise.csv',mode='a') as f:
            writer_object.writerow(self.__dict__)
    def __str__(self):
        return f"{self.question}\n1){self.option1}\n2){self.option2}\n3){self.option3}\n4){self.option4}"


class ShortAnswer(Quiz):
    def __init__(self,id,question,answer):
        Quiz.__init__(self,id,question,answer)

    def add_to_file(self,writer_object):
        with open('shortanswer.csv',mode='a') as csv_file:
            writer_object.writerow(self.__dict__)
    

class Point:
    def __init__(self,point):
        self.point=point
        self.statuse=''

    def winner_check(self):
        if self.point>=40:
            self.statuse='winner'
        else:
            self.statuse='loser'
    def add_lowoff_point(self,value):#به ازای هر پاسخ غلط 3 امتیاز از امتیاز کاربر کم میکند و به ازای هر پاسخ درست 10 امتیاز به امتیز کاربر اضافه میکند
        if value==True:
            self.point=self.point+10
        elif value==False:
            self.point=self.point-3
        elif value==None:
            pass
    def __str__(self):
        return self.point
#در قسمت زیر برای فایل سوال های جواب کوتاه هدری درست میشود
with open('shortanswer.csv',mode='a') as csv_file:
    fieldnames=['id','question','answer']
    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
short_q1=ShortAnswer(1,'where is the iran capitel?','tehran')    #آبجکت هایی از کلاس پاسخ کوتاه ایجاد کردم تا درون فایل إخیره کنم
short_q2=ShortAnswer(2,'who was the former king of iran?','mohammadrezapahlavi')
short_q3=ShortAnswer(3,'who is the president of unitedstates?','joebiden')
short_q4=ShortAnswer(4,'what color is my haircolor?','black')
short_q5=ShortAnswer(5,'where is the capital of italy?','rom')
for i in range(5):
    if i==0:
        short_q1.add_to_file(writer)
    elif i==1:
        short_q2.add_to_file(writer)
    elif i==2:
        short_q3.add_to_file(writer)
    elif i==3:
        short_q4.add_to_file(writer)  #مشخصه های هر شی را در قالب دیکشنری  در داخل فایل إخیره میکنیم
    elif i==4:
        short_q5.add_to_file(writer)

with open('truefalse.csv',mode='a') as csvfile:
    fieldnames=['id','question','answer']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
truefalse_q1=TrueFalse(1,'irans capital is tabriz. \n1)true\n2)false','false')
truefalse_q2=TrueFalse(2,'paris famouse tower is pizza.\n1)true\n2)false','false')
truefalse_q3=TrueFalse(3,'president of unitet states is joe biden.\n1)true\n2)false','true')
truefalse_q4=TrueFalse(4,'world war 2 was in 2020 year.\n1)true\n2)false','false')
truefalse_q5=TrueFalse(5,'asia is the bigest continent.\n1)true\n2)false','true')
for i in range(5):
    if i==0:
        truefalse_q1.add_to_file(writer)
    elif i==1:
        truefalse_q2.add_to_file(writer)
    elif i==2:
        truefalse_q3.add_to_file(writer)
    elif i==3:
        truefalse_q4.add_to_file(writer)
    elif i==4:
        truefalse_q5.add_to_file(writer)

with open('multiplechoise.csv',mode='a') as f:
    fieldnames=['id','question','option1','option2','option3','option4','answer']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
object1=MultipleChoise(1,'where is the iran capitel?','2','tabriz','tehran','shiraz','paris')
object2=MultipleChoise(2,'who was the former king in iran?','3','foad','malek_abloallah','mohammadrezapahlavi','soltansolleyman')
object3=MultipleChoise(3,'who is the president of unitedstates?','1','joebiden','barakobama','trump','bosch')
object4=MultipleChoise(4,'whate is the result of adding 20 to 23?','2','65','43','20','13')  
object5=MultipleChoise(5,'which city has saffron in iran?','4','tehran','andimeshk','orumiyeh','mashhad')
for i in range(5):
    if i==0:
        object1.add_to_file(writer)
    elif i==1:
        object2.add_to_file(writer)
    elif i==2:
        object3.add_to_file(writer)
    elif i==3:
        object4.add_to_file(writer)
    elif i==4:
        object5.add_to_file(writer)
process={'Q':0,'correct':0,'wrong':0,'score':0,'remaining':5} 
'''
آرگومان تابع زیر برای این هست که بدانیم چندمین سوالی هست که داریم به کاربر نشان میدهیم
  در واقع نشان میدهد که کدام یک از آن 5
سوالی هست که در حال ساختن آن هستیم
'''
def Make_shortanswer_question(n):
    """

    """
    global process  
    with open('shortanswer.csv',mode='r') as csv_file:
        x1=random.randint(1,5)
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            row_dict=dict(row)
            if row_dict['id']==x1:
                user_point=Point(process['score']) #از دیکشنری تعریف شده در بالا مقدار  امتیاز رو بیرون میکشیم و با اون آبجکتی از کلاس امتیاز میسازیم تا نشان دهنده امتیاز کاربر تا به این لحظه باشد
                Q=ShortAnswer(row_dict['id'],row_dict['question'],row_dict['answer'])
                user_answer=input(f"{n}){Q}")
                if Q.compare(user_answer)==True:
                    print("your answer is true.")
                    user_point.add_lowoff_point(True)
                    process['Q']=process['Q']+1
                    process['correct']=process['correct']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                elif Q.compare(user_answer)==False:
                    print("your answer is not true.")
                    user_point.add_lowoff_point(False)
                    process['Q']=process['Q']+1
                    process['wrong']=process['wrong']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                elif Q.compare(user_answer)==None:
                    print("you didnt answer")
                    user_point.add_lowoff_point(None)
                    process['Q']=process['Q']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                if n==5: #اگر پنجمین سوال باشد که طرح میکنیم برنده شدن یا بازنده شدن کاربر را مشخص کن
                    print(f"you are {user_point.statuse}")
def Make_truefalse_question(n):
    global process
    with open('truefalse.csv',mode='r') as csvfile:
        x1=random.randint(1,5)
        csv_reader=csv.DictReader(csvfile)
        for row in csv_reader:
            row_dict=dict(row)
            if row_dict['id']==x1:
                user_point=Point(process['score'])
                Q=TrueFalse(row_dict['id'],row_dict['question'],row_dict['answer'])
                user_answer=input(f"{n}){Q}")
                if Q.compare(user_answer)==True:
                    print("your answer is true.")
                    user_point.add_lowoff_point(True)
                    process['Q']=process['Q']+1
                    process['correct']=process['correct']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                elif Q.compare(user_answer)==False:
                    print("your answer is not true.")
                    user_point.add_lowoff_point(False)
                    process['Q']=process['Q']+1
                    process['wrong']=process['wrong']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                elif Q.compare(user_answer)==None:
                    print("you didnt answer")
                    user_point.add_lowoff_point(None)
                    process['Q']=process['Q']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                user_point.winner_check()
                if n==5:
                    print(f"you are {user_point.statuse}")
def Make_multiplechoise_question(n):
    global process
    with open('multiplechoise.csv',mode='r') as f:
        x1=random.randint(1,5)
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            row_dict=dict(row)
            if row_dict['id']==x1:
                user_point=Point(process['score'])
                Q=MultipleChoise(row_dict['id'],row_dict['question'],row_dict['option1'],row_dict['option2'],
                row_dict['option3'],row_dict['option4'],row_dict['answer'])
                user_answer=input(f"{n}){Q}")
                if Q.compare(user_answer)==True:
                    print("your answer is true.")
                    user_point.add_lowoff_point(True)
                    process['Q']=process['Q']+1
                    process['correct']=process['correct']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                elif Q.compare(user_answer)==False:
                    print("your answer is not true.")
                    user_point.add_lowoff_point(False)
                    process['Q']=process['Q']+1
                    process['wrong']=process['wrong']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                elif Q.compare(user_answer)==None:
                    print("you didnt answer")
                    user_point.add_lowoff_point(None)
                    process['Q']=process['Q']+1
                    process['score']=user_point.point
                    process['remaining']=process['remaining']-1
                if n==5:
                    print(f"you are {user_point.statuse}")
def MakeQuiz():
    global process  
    #تابعی برای  بیرون کشیدن 5 سوال رندوم از میان 15 سوالی که درون آن 3 فایل ذخیره شده است
    Make_shortanswer_question(1)  #  3 سوال اول را به ترتیب از 3 نوع موجود میسازیم
    print(process)
    Make_truefalse_question(2)
    print(process)
    Make_multiplechoise_question(3)
    print(process)
    y1=random.randint(1,3)
    if y1==1:
        Make_shortanswer_question(4)
        print("Q\t\tcorrect\t\twrong\t\tscore\t\tremaining")
        print(f"{process['Q']}\t\t{process['correct']}\t\t{process['wrong']}\t\t{process['score']}\t\t{process['remaining']}")
    elif y1==2:
        Make_truefalse_question(4)
        print("Q\t\tcorrect\t\twrong\t\tscore\t\tremaining")
        print(f"{process['Q']}\t\t{process['correct']}\t\t{process['wrong']}\t\t{process['score']}\t\t{process['remaining']}")
    elif y1==3:
        Make_multiplechoise_question(4)
        print("Q\t\tcorrect\t\twrong\t\tscore\t\tremaining")
        print(f"{process['Q']}\t\t{process['correct']}\t\t{process['wrong']}\t\t{process['score']}\t\t{process['remaining']}")
    y2=random.randint(1,3)
    if y2==1:
        Make_shortanswer_question(5)
        print("Q\t\tcorrect\t\twrong\t\tscore\t\tremaining")
        print(f"{process['Q']}\t\t{process['correct']}\t\t{process['wrong']}\t\t{process['score']}\t\t{process['remaining']}")
    elif y2==2:
        Make_truefalse_question(5)
        print("Q\t\tcorrect\t\twrong\t\tscore\t\tremaining")
        print(f"{process['Q']}\t\t{process['correct']}\t\t{process['wrong']}\t\t{process['score']}\t\t{process['remaining']}")
    elif y2==3:
        Make_multiplechoise_question(5)
        print("Q\t\tcorrect\t\twrong\t\tscore\t\tremaining")
        print(f"{process['Q']}\t\t{process['correct']}\t\t{process['wrong']}\t\t{process['score']}\t\t{process['remaining']}")

MakeQuiz()



     
     

     
     
     




                    

                     
        

        
        

         

 

        



        

