import textwrap
import subprocess
#colors = [(114,111,111),(116,101,114),(115,123,87),(72,89,95),(52,82,51),(95,84,72),(51,95,87),(52,89,95),(84,72,52),(84,95,89),(48,85,95),(52,82,51),(33,125,99),(0,116,102)]
s="MICHAEL: All right Jim, your quarterlies look very good. How the thing is going at the library?JIM: Oh I told you couldn't close it soMICHAEL: So you've come to the master for guidance? (imitating) Is http://tiny.cc/rosvdz this what you're saying grasshopper?JIM: Actually you called me in here, but yeah.MICHAEL: All right, well let me show you how it's done. http://tiny.cc/rosvdz (gets on phone) Yes, I liked to speak to your office manager please. Yes hello this is Michael Scott, I am the regional manager of Dunder Mifflin paper products. Just wanted to talk to you, manager-on-manager. (cut to the office and cut back) All right done deal, thank you very much sir, you're a gentleman and a scholar. Oh I'm sorry, ok, I'm sorry, my mistake. (hangs up) That was a woman I was talking to she had a very low voice. Probably a smoker. So, so that's the way it's done. Michael: (to the camera) I've been in Dundler Mifflin for twelve years, the last four as regional manager. If you want to come through here, (opens the door to the main office) so we have the entire floor, so this is my kingdom, as far as the eye can see, ah this is our receptionist Pam. (goes to the receptionist) Pam, Pam Pam! http://tiny.cc/rosvdz Pam Beesly. Pam has been with us for' for ever, right Pam?"
l=textwrap.wrap(s, 12)
with open("a.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
#exiftool -comment=123 michael.jpg
for i in range(len(l)):
    subprocess.call(["exiftool", "-comment="+l[i],""+content[i]])

    
