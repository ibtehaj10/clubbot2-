from os import lstat
from select import select
from django.shortcuts import render
import mysql.connector
from django.http import HttpResponse,HttpRequest ,JsonResponse
import random
import webbrowser
from .models import Club
from django.shortcuts import render , get_object_or_404 , redirect
import logging
from unicodedata import name
from heyoo import WhatsApp
import datetime
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clubbot"
)



def get_all():
    c = Club.objects.filter(status = 0)
    return c

def seat(request,seatno):
    if request.method == 'POST':
        number = request.POST.get('selectdata')
        print(number)
        return redirect('seat',seatno=int(number))
    x = Club.objects.filter(seat = seatno)
    all_val = get_all()
    lst = [i.seat for i in all_val]
    lstt = set(lst)
    return render(request,'home.html',{'lst':x,'sett':lstt})


def home(request):
    if request.method == 'POST':
        number = request.POST.get('selectdata')
        print(number)
        return redirect('seat',seatno=int(number))
    x = get_all()
    lstt = [i.seat for i in x]
    lstt = set(lstt)
    return render(request,'home.html',{'lst':x,'sett':lstt})

def random_quotes(request):
    x = get_all()
    lst = [i for i in x]
    lstt = [i.seat for i in x]
    lstt = set(lstt)
    random.shuffle(lst)
    return render(request,'home.html',{'lst':lst,'sett':lstt})

def played(request,pk):
    c = get_object_or_404(Club,pk = pk)
    c.status = 1
    c.save()
    return redirect('home')

def search(request,pk):
    c = get_object_or_404(Club,pk = pk)
    song = c.song
    rep = song.replace(" ", "+")
    url = "https://www.youtube.com/results?search_query={}".format(rep)
    webbrowser.open_new_tab(url)
    return redirect('home')


def homemain(request):
    return render(request,'page.html')



id ="100406429479899"
token = "EAAFcZBbRweewBAI8POODV0ePfayXNlRkF3gcaEal8GV5nQXZC3L6SarHEtITNFazpejwnxhutgv0OQF82Bpu7YqzLXztDeFXaQ5yep5NF93kEDsQMTVocOhJcQhJABHZBdnHZARsy45QwrSO4j3NNFf8hTJRzFG8ZBTLP3SwA8A9HJd69KXNcTRvPy696SMvb4BnkQSpKQAZDZD"
messenger = WhatsApp(token=token, phone_number_id=id)
VERIFY_TOKEN = "helloworld"

# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def hook(request):
    if request.method == "GET":
        print("This is GET : ",request.GET)
        myDict = dict(request.GET)
        print(myDict['hub.verify_token'][0])
        if myDict['hub.verify_token'][0] == VERIFY_TOKEN:
            logging.info("Verified webhook")
            response = HttpResponse(myDict["hub.challenge"][0], 200)
            response.mimetype = "text/plain"
            # return render(response,'page.html')
            return response
        # logging.error("Webhook Verification failed")
        # return render("Invalid verification token",'page.html')
            # return "Invalid verification token"

    # Handle Webhook Subscriptions
    data = json.loads(request.body)
    logging.info("Received webhook data: %s", data)
    changed_field = messenger.changed_field(data)

    quest = 0
    if changed_field == "messages":
       
       
        new_message = messenger.get_mobile(data)
        message_type = messenger.get_message_type(data)
        mobile = messenger.get_mobile(data)
        try:
            sname = messenger.get_name(data)
        except:
            pass
        message = messenger.get_message(data)
        greet = ["hi","Hi","hello","Hello","hey","Hey"]
        if message_type == "text":
            # if message in greet:
            
            mycursor = mydb.cursor()

            sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` , `alldone`FROM `club` WHERE `number`= {}".format(mobile)

            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            # last = myresult[-1]
            if myresult != []:
                res = myresult[-1]
                print(res)
                
                
                # if res[3] == 0 and res[4] == "":
                if res[7] == 0:
                    messenger.send_message("please tell your Table number",mobile)
                    mycursor = mydb.cursor()

                    sql = "UPDATE `club` SET `ques1`= {} WHERE `id` = {}".format(1,res[0])
                    # val = ("John", "Highway 21")
                    mycursor.execute(sql)
                    print("\nquest DONE \n")
                    mydb.commit()
                    mycursor = mydb.cursor()

                    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2`, `alldone` FROM `club` WHERE `number`= {}".format(mobile)

                    mycursor.execute(sql)

                    myresult = mycursor.fetchall()
                    if myresult != []:
                        res = myresult[-1]
                        print(res)
                        print("\nnow number is ",res[-2])
                elif myresult[-1][9] == 1:
                    print("new msg")
                    mycursor = mydb.cursor()
                    time = datetime.datetime.now()
                    sql = "INSERT INTO `club`( `number`, `name`, `time`) VALUES ('"+mobile+"','"+sname+"','"+str(time)+"')"
        
                    mycursor.execute(sql)

                    mydb.commit()
                    hook(request)

                    

                elif res[7] == 1 and res[8] == 0:
                    mycursor = mydb.cursor()
                    sql = "UPDATE `club` SET `seat`={},`ques2`={} WHERE `id` = {}".format(int(message),1,res[0])
                    mycursor.execute(sql)
                    messenger.send_message("please tell your song name",mobile)
                    print("\nSeat added \n")
                    mydb.commit()
                    mycursor = mydb.cursor()

                    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` , `alldone`FROM `club` WHERE `number`= {}".format(mobile)

                    mycursor.execute(sql)

                    myresult = mycursor.fetchall()
                    if myresult != []:
                        res = myresult[-1]
                        print(res)
                        print("\nnow q2 is ",res[-1])
                
                elif res[8] == 1 and res[4] == "":
                    mycursor = mydb.cursor()
                    sql = "UPDATE `club` SET `song`='"+message+"',`alldone`=1 WHERE `id` = {}".format(res[0])
                    mycursor.execute(sql)
                    
                    
                    print("\ntable added \n")
                    mydb.commit()
                   
                   
                    mycursor = mydb.cursor()

                    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` FROM `club` WHERE `number`= {}".format(mobile)

                    mycursor.execute(sql)

                    myresult = mycursor.fetchall()
                    thank = "Thank you for joining us your requested song {} will be played shortly".format(message)
                    messenger.send_message(thank,mobile)
                    
                # elif res[9] == 1:
                #     song = res[4]
                    
                else:
                    print("not blank")
                data=[]
                print(message,"is blank")

            elif myresult == [] :
                print("new msg")
                mycursor = mydb.cursor()
                time = datetime.datetime.now()
                sql = "INSERT INTO `club`( `number`, `name`, `time`) VALUES ('"+mobile+"','"+sname+"','"+str(time)+"')"
      
                mycursor.execute(sql)

                mydb.commit()
                hook(request)


             
            # print(myresult[-1][9])
          
    return render(request,'hook.html')
    pass
    return 'ok'