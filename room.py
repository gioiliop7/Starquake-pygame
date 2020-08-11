import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

Eikona1 = pygame.sprite.Group()
Eikona2 = pygame.sprite.Group()
Eikona3 = pygame.sprite.Group()

class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    
    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map1 = """---------------
m-m-------------m---
m-m-------------m---
m-mmmmmmmmmmmkkkkkkk
m------------------m
mm-------mm---kk---m
m----pp-----------pp
p--m-----mk---km---p
p------pkm---------p
p------------mm----p
kkk--kkk--mm------kk
k------------p-----k
k-----mmm-------m---
k--mm-----------m---
kkkkkkkkkkkkkkkkkkkk""".splitlines()

    game_map = [list(lst) for lst in game_map1]

    tl = {}
    tl["p"] = mov_img = pygame.image.load('mov.png')
   # Eikona1.add(mov_img)
    tl["m"] = mple_img = pygame.image.load('mple.png')
    #Eikona2.add(mple_img)
    tl["k"] = kitrino_img = pygame.image.load('kitrino.png')
   #Eikona3.add(kitrino_img)


class Room2(Room):
    """This creates all the walls in room 2"""
    
    game_map2 = """
d------------------d
d------------------d
d------rrrr--------d
dr---bb-----bbbrrrrd
d-----------------dd
d-----rbr--------rdd
d------------------d
d----rrryy---------d
d------------------d
dbb----------------d
--------rb---rr---bd
----bbb--------rr---
--------------------
rrrrrrrrrrrrrrrrrrrr
    """.splitlines()

    game_map = [list(lst) for lst in game_map2]

    tl = {}
    tl["r"] = dirt_img = pygame.image.load('red.png')
    tl["b"] = grass_img = pygame.image.load('blue.png')
    tl["d"] = grass_img = pygame.image.load('red2.png')
    tl["a"] = grass_img = pygame.image.load('blue2.png')



class Room3(Room):
    """This creates all the walls in room 3"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map3 = """
--------------------
--------------------
baaaaaaaaaaaaaaaaaaa
bb--o-----a--------b
bm----------------ab
bm----bbbb--------ab
b-----aaaaaam-----bb
b----aaaammmma----bb
b--------------aa-bb
baaaaaa---aa------bb
bm-----------aa--bbb
-----mmmmmmm---aaaae
--aa--------ab------
aaaaaaaaaaaaaaaa-aaa
    """.splitlines()

    game_map = [list(lst) for lst in game_map3]

    tl = {}
    tl["b"] = lb_img = pygame.image.load('lb.png')
  #  Eikona1.add(lb_img)
    tl["m"] = lm_img = pygame.image.load('lm.png')
   # Eikona2.add(lm_img)
    tl["a"] = la = pygame.image.load('la.png')
   # Eikona3.add(la)
    tl["e"] =exit = pygame.image.load('exit.png')

class Room4(Room):
    """This creates all the walls in room 1"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map4 = """
--------------------
--------------------
oooooooooooooooooooo
k------------------k
km----------mm-----k
k----pp-----------ok
k--m-----ok---km---k
k------pkm---------k
k------------mm----k
koo--kko--mm------kk
k------------p-----k
k-----mmm-------m---
---pp-----------m---
pppppppppppppppppppp""".splitlines()

    game_map = [list(lst) for lst in game_map4]

    tl = {}
    tl["k"] = mov_img = pygame.image.load('k1.png')
   # Eikona1.add(mov_img)
    tl["m"] = mple_img = pygame.image.load('k2.png')
    #Eikona2.add(mple_img)
    tl["p"] = kitrino_img = pygame.image.load('k3.png')
   #Eikona3.add(kitrino_img)
    tl["o"] = kokkino_img = pygame.image.load('k4.png')

class Room5(Room):
    """This creates all the walls in room 3"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map5 = """
c-------------------
t------------------c
cccccccccccctttttttt
t------h-----------t
tt-----------c-----c
t---t------t-------t
c------------------t
c----tctctccttctt--c
c------------------t
t---------h--------c
tc-h------------h--t
t----ccttct--------t
-------------------c
cccccccccccccccccccc
    """.splitlines()

    game_map = [list(lst) for lst in game_map5]

    tl = {}
    tl["c"] = dirt_img = pygame.image.load('yellow_circle.png')
    tl["t"] = dirt_img = pygame.image.load('purple_circle.png')
    tl["h"] = dirt_img = pygame.image.load('particle2.png')

class Room6(Room):
    """This creates all the walls in room 3"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map6 = """aaa----------------a
aaa----------------a
a-----------------aa
a------rrrr--------a
ab---bb-----bbbrrrra
d------------------a
d-----bbr--------raa
a------------------d
a----rrrbb---------a
a------------------a
dbb----------------a
a-------br---bb---ra
a---rrr--------rr--a
a------------------a
rrrrrrrrrrrrrrrrr--r
        """.splitlines()

    game_map = [list(lst) for lst in game_map6]

    tl = {}
    tl["r"] = dirt_img = pygame.image.load('red.png')
    tl["b"] = grass_img = pygame.image.load('blue.png')
    tl["d"] = grass_img = pygame.image.load('red2.png')
    tl["a"] = grass_img = pygame.image.load('blue2.png')

class Room7(Room):
    """This creates all the walls in room 3"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map7 = """s------------------s
s------------------s
ssssssssssssssss---s
s------------------s
sx----------sss----x
x------------------x
x----------------xxx
s------------------x
x------------------s
q------------------s
qq-----------------s
q-----------------sq
q---ssq----s--q----q
q------------------q
qqqqsssxxqqsxsxqx--s
        """.splitlines()

    game_map = [list(lst) for lst in game_map7]

    tl = {}
    tl["s"] = dirt_img = pygame.image.load('n3.png')
    tl["x"] = grass_img = pygame.image.load('n2.png')
    tl["q"] = grass_img = pygame.image.load('n2.png')


class Room8(Room):
    """This creates all the walls in room 3"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map8 = """s------------------s
s--------------s--ss
s--------------s---s
sxx----------------s
sx---xx------------x
x------------------x
x----xxs---------xxx
s----------ss------x
x----xx------------s
q------------------s
qq-ss--------------s
q------sx---------sq
----ssq----s--q-----
--------------------
qqqqsssxxqqsxsxqxqqs
        """.splitlines()

    game_map = [list(lst) for lst in game_map8]

    tl = {}
    tl["s"] = dirt_img = pygame.image.load('n2.png')
    tl["x"] = grass_img = pygame.image.load('n3.png')
    tl["q"] = grass_img = pygame.image.load('n2.png')
    
class Room9(Room):
    """This creates all the walls in room 1"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map9 = """
mm-----------------m
mm-----------------m
mkkkkkmmmkkkmmmppppp
m------------------k
mm-------mm---kk---k
m----pp-----------kk
p--m-----mk---km---k
p------pkm---------k
p------------kk----k
kkk--mmm--pp------kk
-------------m-----k
------mmm-------m--k
--- mm--------m--mmk
mk-mkpmkpmkpmkpmkpmk
        """.splitlines()

    game_map = [list(lst) for lst in game_map9]

    tl = {}
    tl["p"] = mov_img = pygame.image.load('mov.png')
    tl["m"] = mple_img = pygame.image.load('mple.png')
    tl["k"] = kitrino_img = pygame.image.load('kitrino.png')


class Room10(Room):
    """This creates all the walls in room 10"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map10 = """a-----------------a
a-------------------
a-------------------
aa-----bbbaaabbaamma
bb--o-----a--------a
bm----------------ma
bm----bbbb--------ma
b-----aabba-------aa
b----ab-----------ma
b--------------bb-ma
ba--------aa------bb
bm-----------aa--amm
b----mmmmmmm---eaaea
b-aa--------ba-----a
b-bbbbbbbbbbbbbbbbbb
    """.splitlines()

    game_map = [list(lst) for lst in game_map10]

    tl = {}
    tl["b"] = lb_img = pygame.image.load('lb.png')
  #  Eikona1.add(lb_img)
    tl["m"] = lm_img = pygame.image.load('lm.png')
   # Eikona2.add(lm_img)
    tl["a"] = la = pygame.image.load('la.png')


class Room11(Room):
    """This creates all the walls in room 2"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map11 = """a-----------------a
d-d----------------bd
d-d-------------bb-d
d-dddddbbbbbbbbbbbbd
d----rr------------d
-----r------------dd
------bbr--------rdd
-------------z-----d
-----rrryy---------d
d------------------d
dbb--------z-------d
-------------rr----d
----rbr--------rr--d
-------------------d
rrrrrrrrrrbrbrbrbbbr
    """.splitlines()

    game_map = [list(lst) for lst in game_map11]

    tl = {}
    tl["r"] = dirt_img = pygame.image.load('red.png')
    tl["b"] = grass_img = pygame.image.load('blue.png')
    tl["d"] = grass_img = pygame.image.load('red2.png')
    tl["a"] = grass_img = pygame.image.load('blue2.png')
    tl["z"] = grass_img = pygame.image.load('particle.png')

class Room12(Room):
    """This creates all the walls in room 2"""

    # This is a list of walls. Each is in the form [x, y, width, height]
    game_map12 = """
d------------------d
d------------------d
d------bbbb--------d
dr---rr-----bbbrrrrd
-----r------------dd
------bbr-----------
-------------z------
-----rrryy----------
d-------------------
dbb--------z-------d
-------------rr----d
---------------rr---
dd---bb--rr--bb-----
dddddddddddddddddddd
    """.splitlines()

    game_map = [list(lst) for lst in game_map12]

    tl = {}
    tl["r"] = dirt_img = pygame.image.load('red.png')
    tl["b"] = grass_img = pygame.image.load('blue.png')
    tl["d"] = grass_img = pygame.image.load('red2.png')
    tl["a"] = grass_img = pygame.image.load('blue2.png')
    tl["z"] = grass_img = pygame.image.load('particle.png')
    
class Room13(Room):

    game_map13 = """q------------------s
q-----------------ss
q---------------xsss
ss-----------------s
ss--xxx-----sss----x
x--s----------------
x--xxs-----------xx-
s--------ss---------
x------xx-----------
q------------------s
qq-ss-------------ss
q------sx---------sq
q---ssq----s--q-----
q-------------------
----sssxxqqsxsxqxqqs
        """.splitlines()

    game_map = [list(lst) for lst in game_map13]

    tl = {}
    tl["s"] = dirt_img = pygame.image.load('n3.png')
    tl["x"] = grass_img = pygame.image.load('n2.png')
    tl["q"] = grass_img = pygame.image.load('n2.png')
    
class Room14(Room):

    game_map14 = """s------------------s
s-------------------
s------------------s
ss----------------ss
ss--xxx-----sss----x
x--s----xxx--------x
x----xxs---------xxx
s--------ss--qq----x
x----xx------------s
q-----------sssss--s
qq-ss--------------s
q------sx---qqqq--sq
q---ssq----s--q----s
q------------------s
q--ssssxxqqsxsxqxq-s
        """.splitlines()

    game_map = [list(lst) for lst in game_map14]

    tl = {}
    tl["s"] = dirt_img = pygame.image.load('n3.png')
    tl["x"] = grass_img = pygame.image.load('n2.png')
    tl["q"] = grass_img = pygame.image.load('n2.png')

class Room15(Room):

    game_map15 = """
--------------------
--------------------
ssssssssssssssssssss
ss--xxx-----sss----x
x--s---------------x
x----xxs---------xxx
s--------ss--------x
x----xx------------s
q------------------s
qq-ss-------------ss
q------sx---------sq
q---ssq----s--q-----
q-------------------
q--ssssxxqqsxsxqxqqs
        """.splitlines()

    game_map = [list(lst) for lst in game_map15]

    tl = {}
    tl["s"] = dirt_img = pygame.image.load('n3.png')
    tl["x"] = grass_img = pygame.image.load('n2.png')
    tl["q"] = grass_img = pygame.image.load('n2.png')

