


#  Developer : Vaasu Devan S
#  Email     : vaasuceg.96@gmail.com
#              www.github.com/VaasuDevanS

#  cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).

# ___________________________________________________________________________________________________________________________ #

# Characters.py contains the Ascii code for the characters.
# Initial cowsay will have lots of characters than this.. But these are my favourite.

from __future__ import print_function
import re

flg=[]

Beavis =  '''
             _------~~-,
          ,'            ,
          /               \\
         /                :
        |                  '
        |                  |
        |                  |
         |   _--           |
         _| =-.     .-.   ||
         o|/o/       _.   |
         /  ~          \\ |
       (____\@)  ___~    |
          |_===~~~.`    |
       _______.--~     |
       \\________       |
                \\      |
              __/-___-- -__
             /            _ \\

            '''

Cheese = '''

     /     \\_/         |
    |                 ||
    |                 ||
   |    ###\\  /###   | |
   |     0  \\/  0    | |
  /|                 | |
 / |        <        |\\ \\
| /|                 | | |
| |     \\_______/   |  | |
| |                 | / /
/||                 /|||
   ----------------|
        | |    | |
        ***    ***
       /___\\  /___\\

       '''

Daemon = '''
            /- _  `-/  '
           (/\\/ \\ \\   /\\
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \\) /====
<----'    `--' `.__,' \\
             |        |
              \\       /
        ______( (_  / \\______
      ,'  ,-----'   |        \\
      `--{__________)        \\/

       '''


Cow = '''

   ^__^
   (oo)\_______
   (__)\       )\/\
       ||----w |
       ||     ||

       '''


Dragon = '''

                           / \\  //\\
            |\\___/|      /   \\//  \\\\
            /0  0  \\__  /    //  | \\ \\
           /     /  \\/_/    //   |  \\  \\
           \@_^_\@'/   \\/_   //    |   \\   \\
           //_^_/     \\/_ //     |    \\    \\
        ( //) |        \\///      |     \\     \\
      ( / /) _|_ /   )  //       |      \\     _\\
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
 (( /// ))      `.   {            }                   /      \\  \\
  (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
             ///.----..>        \\             _ -~             `.  ^-`  ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                  /.-~

         '''


Ghostbusters = '''
                       __---__
                    _-       /--______
               __--( /     \\ )XXXXXXXXXXX\\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\\
          /XXXXX(              )--_  XXXXXXXXXXX\\
         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\
         XXXXX/   /            XXXXXX   \\__ \\XXXXX
         XXXXXX__/          XXXXXX         \\__---->
 ---___  XXX__/          XXXXXX      \\__         /
   \\-  --__/   ___/\\  XXXXXX            /  ___--/=
    \\-\\    ___/    XXXXXX              '--- XXXXXX
       \\-\\/XXX\\ XXXXXX                      /XXXXX
         \\XXXXXXXXX   \\                    /XXXXX/
          \\XXXXXX      >                 _/XXXXX/
            \\XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \\XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""

            '''


Kitty = '''

     ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'

        '''

Meow = """

                  _ ___.--'''`--''//-,-_--_.
      \\`"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_
     /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,
    /\@"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,
   /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)
   `-'``/  /  |  // \\__/\\__  /  \\__/ \\
        `-'  /-\\/  | -|   \\__ \\   |-' |
          __/\\ / _/ \\/ __,-'   ) ,' _|'
         (((__/(((_.' ((___..-'((__,'

        """


Milk = '''

       ____________
       |__________|
      /           /\\
     /           /  \\
    /___________/___/|
    |          |     |
    |  ==\\ /== |     |
    |   O   O  | \\ \\ |
    |     <    |  \\ \\|
   /|          |   \\ \\
  / |  \\_____/ |   / /
 / /|          |  / /|
/||\\|          | /||\\/
    -------------|
        | |    | |
       <__/    \\__>

       '''


Stegosaurus = '''
                                     / `.   .' "
                             .---.  <    > <    >  .---.
                             |    \\  \\ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \\~~~\\.'                    `./~~~/
       ---------   \\__/                        \\__/
      .'  O    \\     /               /       \\  "
     (_____,    `._.'               |         }  \\/~~~/
      `----.          /       }     |        /    \\__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>

              '''


Stimpy = '''
        .    _  .
       |\\_|/__/|
       / / \\/ \\  \\
      /__|O||O|__ \\
     |/_ \\_/\\_/ _\\ |
     | | (____) | ||
     \\/\\___/\\__/  //
     (_/         ||
      |          ||
      |          ||\\
       \\        //_/
        \\______//
       __ || __||
      (____(____)

        '''


Turkey = '''

                                             ,+*^^*+___+++_
                                       ,*^^^^              )
                                    _+*                     ^**+_
                                  +^       _ _++*+_+++_,         )
              _+^^*+_    (     ,+*^ ^          \\+_        )
             {       )  (    ,(    ,_+--+--,      ^)      ^\\
            { (\@)    } f   ,(  ,+-^ __*_*_  ^^\\_   ^\\       )
           {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
          ( /  (    (        ,___    ^*+_+* )   <    <      \\
           U _/     )    *--<  ) ^\\-----++__)   )    )       )
            (      )  _(^)^^))  )  )\\^^^^^))^*+/    /       /
          (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
         (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
          *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
          \\             \\_)^)_)) ))^^^^^^^^^^))^^^^)
           (_             ^\\__^^^^^^^^^^^^))^^^^^^^)
             ^\\___            ^\\__^^^^^^))^^^^^^^^)\\\\
                  ^^^^^\\uuu/^^\\uuu/^^^^\\^\\^\\^\\^\\^\\^\\^\\
                     ___) >____) >___   ^\\_\\_\\_\\_\\_\\_\\)
                    ^^^//\\\\_^^//\\\\_^       ^(\\_\\_\\_\\)
                      ^^^ ^^ ^^^ ^

           '''


Turtle = '''

                                               ___-------___
                                           _-~~             ~~-_
                                        _-~                    /~-_
             /^\\__/^\\         /~  \\                   /    \\
           /|  O|| O|        /      \\_______________/        \\
          | |___||__|      /       /                \\          \\
          |          \\    /      /                    \\          \\
          |   (_______) /______/                        \\_________ \\
          |         / /         \\                      /            \\
           \\         \\^\\\\         \\                  /               \\     /
             \\         ||           \\______________/      _-_       //\\__//
               \\       ||------_-~~-_ ------------- \\ --/~   ~\\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \\_\\      \\.
                         (_(___/                         \\_____)_)


        '''


Tux = '''

        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/

    '''

Cyber = '''

                                                                         oo:
                                                                         :C8c
                                                                        coO88c
                                                                        c88O88C
 8:oc                                                                  .OO88O8Co                                                                 :CccC
    CcCco:                  CoO                                        c88O88O8C                                        cc:                  oCcCcc
       CcOOooco              oCCcC                                     o8O8o88Oc                                     ocOoo               CcoOCco
          ocOOOCcO:           coO8OcO:                                cC888o888o                                 .ooOOOc:           oCcCOOCc:
             ccO888Oooc        :c8888OCo:                             cC888o8O8o                              ccCOO88Oc:        8coOO8OCo:
                ocC8O88OCcOc     cO888888Ccc                          cCO88o8O8o                           ocOO8888OOo     oCcOOO88OCo:
                   ocC8O88O8OooC  oO88888O88OcO:                      :C888oO88o                        ooOO88O8888Co  ocoOO888OOoc:
                      ooC8O88888OCcoC888O8O8888OooO                   :OO88o888o                    ccCO88O8888O8OoocCOO8888OOoo:
                         ooC888O8888O888O88O8888O8OCcc                :OO8Oo8O8o                 ccOO88O88888888OOOO8888O8OoC:
                            :oCO888O88O88OO8O88888888OOco:            :O88Oo888o             :CoOO888O88O8888O88888888OOoc:
                               OoCOO8888O8O:COO8888O88888OooO         :O8O8oO88o          CcCOO8888O8O888Oo:OO88888OOoO
                                  :ooO88888OC:OcOOO88888888O8CcC      :O8O8o88Oo       ccCO8O88O8888O8Oco cO888OOOcO
                                     :CoOO88OC   CcCO88O88O88888Oco:  .O8O8oO88o   :ooOO88O8O88O8OOCoo   cO88OOco
                                         CoO8OC     :coOO88O8888888OoocO88OoO88occCO88O88O888O8OcC:    :oOOOcc
                                            CoOO       :OcOO8O888O8888CO88Oo888oO888O88888OOCcC        oOc8
                                               o:          ccCO888O88OCO8O8o8O8oO888888OOoo:          OC
                                                              :CoOO888CO888o888oOO8OOOcO:
                                                                 :ocCOCO8O8o8O8oOCccc
                                                               .CoOOOOcO888oO88o88OOOco
                                                            CoCOOO888OCO888o888o8888O88Ooc:
                                          Ccc            ocCO8O888O888COO8Oo888o888888888O8Ccc            ooo
                                       ccOOo         :CoO8888O888O8OOcoO888oO8OoooOOO8888O888OOco          cOCo.
                                    :oC888c:      @oCO8888888O88OCcC  .O888o888o   ocOO8O88O888O8OooO      :o88Ooo:
                                 :oCO8888oo    ocO8888888888OOoc:     .O888o88Oo      ccCO8O88888O888CcC    co88O8OoO
                              :CoOO88O88Cc :CoOO8888888888OcO         .O888o8O8o         .ooOO888O8888O8Occ  oO88888OOco
                           :OcO88O88O88OOcCO888O88888OOCcC   :ccoCC::o:OOO8o8O8o:oc.Cooco.   CcCOO8O888O88OOooCO888O888OOcC
                         OcO888888O8O88O88888O8O888OoCo      cO8O88888888OOOOOO8O8888888O.      oooOO888O888888OOO888O88888OcC
                      8cOO88O888O888O8888888O888Oc::         cO8O888O8OOOOOOOOOOOOO88888O.         :ccO8O888888888O888O8888O88Occ
                   ccOO88O88O8OO8O888O888888OCoo             cco.:c:o.OO8888888Oo :co:cCc.             ccCO88O88888O88OOOOO8O8888Coo
                OcCO888O8OocCoOO88O888O8OOcO:                        :CO888888OOc                         cooO88888888O8COOcCOO8O888Coo
             ooCO8O8OCcCo  :c888O8888OCcC                             o8OCoooC8Oc                             ccOO8888888Oo   oCoOOO888CC:
          :oCO8OOooC      :c888888Ooo                                 CoCOOOOOCc8                                coCO8888OOc       ocCOO88oc
       :CoOOCcc          oo88O8Oco                                    CO8O88O88oc                                    CcO8O8Oc:         oCcO8Oco
    :ocOooC             CCO8CcO                                       ooCooooCO:                                        CcCOOco             ocCOcC
  c:cO:                OCoC:                                           ooCOOOCco                                           ooooo                OoccC
Oc                    :C                                               CO88888C:                                              :Oo                   :o
                                                                      ccOocccCCo
                                                                      oOO8O8O88o
                                                                       CcoCOCco

'''


def about():

    print('''

             Original Author---> Tony Monroe (tony@nog.net)       # Thanks to him... !
             For Python     ---> Vaasu Devan S
             Email          ---> vaasuceg.96@gmail.com
             __version__    ---> 1.0

             visit my github page @ www.github.com/VaasuDevanS

             Cowsay for GNU/Linux is very very famous.
			 It would be fun and cool to have those characters in python..

             Available Characters (in python):
             ==============================================
             |'beavis'     'dragon'         'tux'         |
             |'turtle'     'ghostbusters'   'turkey'      |
             |'cheese'     'kitty'          'stegosaurus' |
             |'daemon'     'meow'           'stimpy'      |
             |'cow'        'milk'           'cyber'       |
             ==============================================

             syntax:-

             >>> import cowsay
             >>> cowsay.<character-name>(text-message)

                            (or)

             >>> from cowsay import *
             >>> <character-name>(text-message)

             Example:-

             >>> import cowsay
             >>> cowsay.tux("Python is fun")

                 _______________
                < Python is fun >
                -----------------
                               \\
                                \\
                                 \\
                                   .--.
                                  |o_o |
                                  |:_/ |
                                //   \\ \\
                                (|     | )
                               /'\\_   _/`\\
                               \\___)=(___/


            Enjoy coding with python and cowsay   :)

        ''')

__version__ = 1.0
__name__ = 'cowsay' #For python


def String_processing(args):

    args=str(args)
    length=len(args)
    lines=args.split("\n")
    lines=[i.strip() for i in lines]
    lines=[i for i in lines if len(i)!=0]
    length=len(lines)

    if length==1:
        flag=len(lines[0])
        if flag<50:
            print("  "+"_"*flag)
            print("< "+lines[0]+" "*(flag-len(lines[0])+1)+">")
            print("  "+"="*flag)
            flg.append(flag)
        else:
            args=list("".join(lines[0]))
            for j,i in enumerate(args):
                if j%50==0:
                    args.insert(j,"\n")
            String_processing("".join(args))

    else:
        flag=len(max(lines,key=len))
        if all(len(i)<50 for i in lines):
            print("  "+"_"*flag)
            print(" /"+" "*flag+"\\")
            for i in lines:
                print("| "+i+" "*(flag-len(i)+1)+"|")
            print(" \\"+" "*flag+"/")
            print("  "+"="*flag)
            flg.append(flag)
        else:
            new_lines=[]
            for i in lines:
                if len(i)>50:
                    args=list("".join(i))
                    for j,i in enumerate(args):
                        if j%50==0:
                            args.insert(j,"\n")
                    new_lines.append("".join(args))
                else:
                    new_lines.append(i+"\n")
            String_processing("".join(new_lines))


# Functions start here..

def beavis(args):

    try :
        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")

        char_lines=Beavis.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*flag+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Beavis...")


def cheese(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Cheese.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Cheese...")



def daemon(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Daemon.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Daemon...")


def cow(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")

        char_lines=Cow.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Cow...")


def dragon(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Dragon.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Dragon...")



def ghostbusters(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Ghostbusters.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Ghostbusters...")


def kitty(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\")

        char_lines=Kitty.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+3)+i)

    except : print("Can't Say...!! Give something much more easier to Ms.Kitty...")


def meow(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\")

        char_lines=Meow.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Meow...")



def milk(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Milk.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+5)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Milk...")



def stegosaurus(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Stegosaurus.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.stegosaurus...")



def stimpy(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Stimpy.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag+4)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Stimpy...")


def turkey(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\")

        char_lines=Turkey.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Turkey...")



def turtle(args):

    try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\")
        print(" "*(flag+8)+"\\",end='')

        char_lines=Turtle.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag-3)+i)

    except : print("Can't Say...!! Give something much more easier to Mr.Turtle...")



def tux(args):

    #try :

        String_processing(args)
        flag=flg[-1]

        print(" "*(flag+5)+"\\")
        print(" "*(flag+6)+"\\")
        print(" "*(flag+7)+"\\",end='')

        char_lines=Tux.split('\n')
        char_lines=[i for i in char_lines if len(i)!=0]

        for i in char_lines:
            print(" "*(flag)+i)

    #except : print("Can't Say...!! Give something much more easier to Mr.Tux...")


chars = [beavis , cheese , daemon , cow , dragon , ghostbusters , kitty , meow , milk , stegosaurus , stimpy , turkey , turtle , tux]

char_names = ['beavis', 'cheese', 'daemon', 'cow', 'dragon', 'ghostbusters', 'kitty', 'meow', 'milk', 'stegosaurus', 'stimpy', 'turkey', 'turtle', 'tux']

# End of File #
