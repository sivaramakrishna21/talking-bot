import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import json
import requests

num = 1
def assistant_speaks(output):
	global num
	num += 1
	print("PerSon : ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False)
	file = 'voice.mp3'
	toSpeak.save(file)
	print(file)
	playsound.playsound("voice.mp3", True)
	os.remove(file)

def sendMessage(number,text):

    url = "https://www.fast2sms.com/dev/bulk"
    my_data = {
        'sender_id': 'FSTSMS',
        
        'message': text,
        
        'language': 'english',
        'route': 'p',
        'numbers': number    
    }
    headers = {
        'authorization': 'auth key should be given here from api',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST",
                                url,
                                data = my_data,
                                headers = headers)
    returned_msg = json.loads(response.text)
    print(returned_msg['message'])
        
def get_audio(time):
    
    while(True):
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Speak...")
            
            # recording the audio using speech recognition
            audio = rObject.listen(source, phrase_time_limit = 30)
        print("Stop.") # limit 5 secs

        try:
            text = rObject.recognize_google(audio, language ='en-US')
            print("You : ", text)
            return text
        except:
            assistant_speaks("Could not understand your audio, PLease try again !")
            return get_audio(20)
            #return 0
            
def addToJson(Menu_dict):
    json.dump(Menu_dict,open("combined.json","w"),indent=4)
    print("done")
    

def getPrice(name):
    f = open('Menu.json',)
    data = json.load(f)

    for i in data:
        for j in data[i]:
            if j["Name"].lower() == name.lower():
                print("getPrice : "+j["Price"])
                return j["Price"]

def calculatePrice(Final_order_list):
    value=0
    for i in range(len(Final_order_list)):
        price = getPrice(Final_order_list[i]["Name"])
        Final_order_list[i]["Price"] = int(Final_order_list[i]["Quantity"]) * int(price)
        value+= int(Final_order_list[i]["Quantity"]) * int(price)
    return value

if __name__ == "__main__":
    #assistant_speaks("Hi, can you tell your order?")
    greeting = get_audio(10)
    if(greeting.lower() == 'hello bot'):

        assistant_speaks("hi, how can I help you")
        BenchNumber = 1
        numbers = { "one" :1, "two" :2, "three":3, "four":4, "five":5,"six":6, "seven": 7}

        Menu_dict={}

        Voice = get_audio(5)

        if(Voice.lower() == 'start order'):
            assistant_speaks("Hi, can you please tell your name?")
            name = get_audio(5)

            assistant_speaks("Hi, Welcome " + name)

            assistant_speaks("Recording order")

            order = get_audio(60)

            Final_order_list=[]
            assistant_speaks("Would you like to complete order")

            endOrder = get_audio(5).lower()

            if( endOrder.lower()== 'yes complete'):
                assistant_speaks("COuld you please provide your mobile number")
                MobileNumer = get_audio(20)
                MobileNumer=MobileNumer.replace(" ","")
            order_list=order.split(' ')#['one','cake','two']
           
            d={}

            for item in order_list:
                if(item == 'and'):
                    continue
                if item in numbers.keys():
                    d["Quantity"]=numbers[item]
                    d["Price"]=120
                    d["Name"]=""
                    Final_order_list.append(d)
                elif(item>'0' and item<'9'):
                    d["Quantity"]=int(item)
                    d["Price"]=120
                    d["Name"]=""
                    Final_order_list.append(d)
                else:
                    if item[len(item)-3:] == 'and':
                        Final_order_list[-1]["Name"]+=item[:-3]
                    Final_order_list[-1]["Name"]+=item
                d={}

            TotalCost = calculatePrice(Final_order_list)
            flag = {}
            flag["BenchNo"] = BenchNumber
            flag["Order"] = Final_order_list
            flag["Total cost"] = TotalCost
            flag["Mobile Number"] = MobileNumer

            Menu_dict[name]=flag

        addToJson(Menu_dict)
        paymentText = "Hello there, to proceed with your payment, please use this link https://websitemine2112.000webhostapp.com/payment/index.html"
        receiptText = "Your order is confirmed.Receipt is availble at https://websitemine2112.000webhostapp.com/payment/index.html"

        sendMessage(MobileNumer,paymentText)

        sendMessage(MobileNumer,receiptText)
