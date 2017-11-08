import pygame  # Thank you pygame.org!!!  

vec = pygame.math.Vector2
import random
import math
import time

pygame.init()
wth = 600
hgt = 600
fps = 60

title = 'my game'
# icon = 'gameicon'


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lightred = (255, 25, 25)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
lightblue = (0, 155, 155)
grey = (80, 80, 80)
lightgrey = (100, 100, 100)
darkgrey = (40, 40, 40)
blurple = (90, 90, 255)
pink = (255, 90, 255)
hotpink = (255, 50, 90)
lime = (0, 255, 90)
peach = (255, 255, 90)
pumpkin = (255, 190, 40)
junglegreen = (100, 200, 40)
purple = (255, 0, 255)

all_color_list = [black,
                  white,
                  red,
                  lightred,
                  green,
                  blue,
                  yellow,
                  lightblue,
                  grey,
                  lightgrey,
                  darkgrey,
                  blurple,
                  pink,
                  hotpink,
                  lime,
                  peach,
                  pumpkin,
                  junglegreen,
                  purple]

# Ive defined some extras in this framework---remember these or only sugestions ;)
TILESIZE = 50
backround_color = hotpink

color_fun = random.choice([all_color_list])




# images path go here

#####################################################################################################################
def make_image(imageDir, x, y, w, h, resize=False, reX=wth, reY=hgt):
    imageD = pygame.image.load(imageDir)
    image = pygame.Surface((w, h))
    image.blit(imageD, (0, 0), (x, y, w, h))
    if resize:
        image = pygame.transform.scale(image, (wth, hgt))
    return image


######################################################################################################################

class Buttons(pygame.sprite.Sprite):
    def __init__(self, game, img_default, img_hover, img_clicked, Xpos, Ypos, scene=None):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.s = scene
        self.img_d = img_default
        self.img_h = img_hover
        self.img_c = img_clicked
        self.image = pygame.image.load(self.img_d).convert()
        self.rect = self.image.get_rect()
        self.rect.x = Xpos
        self.rect.y = Ypos
        self.rect.midtop = (Xpos, Ypos)
        self.clicked = False
        self.hover = False
        self.follow = False

        self.button_bool = True

    def update(self):
        self.hits_v_1()
        if self.follow:
            self.rect.x, self.rect.y = self.game.mpos

    def hits_v_1(self):
        if self.rect.x + self.rect.width > self.game.mpos[0] > self.rect.x and self.rect.y + self.rect.height > \
                self.game.mpos[1] > self.rect.y:
            # print('woot woot')
            self.hover = True
            if not self.clicked:
                self.image = pygame.image.load(self.img_h)
            if self.clicked:
                self.image = pygame.image.load(self.img_c)


        else:
            self.hover = False
            if not self.clicked:
                self.image = pygame.image.load(self.img_h)
            if self.clicked:
                self.image = pygame.image.load(self.img_c)

    def drag_drop(self):
        if self.hover:
            if self.clicked:
                self.follows = True
        else:
            self.follows = False

    def button_scene(self):
        if self.clicked:
            self.s.button_page_turner()
            self.button_bool = False
        if not self.button_bool:
            self.game.screen.blit(self.s.image, (self.s.x, self.s.y))

    def button_events_mousedown(self, button_id, Print=True):
        self.button = button_id

        # print('mouse button down at ' + str(self.game.mpos ))
        if self.button.hover:
            if Print:
                print('clicked')
            self.button.clicked = True
            # self.button1.follow = True
        else:
            self.button.clicked = False
            # self.button1.follow = False

    def button_events_mouseup(self, button_id):

        self.button = button_id
        self.button.clicked = False

    def button_is_clicked(self, button_id):
        self.button = button_id

        # print('mouse button down at ' + str(self.game.mpos ))
        if self.button.hover:
            # print('clicked')
            return True
        else:
            # print('miss')
            return False

    def button_is_unclicked(self, button_id):

        self.button = button_id
        self.button.clicked = False


def button_trajectory_support(x, y):
    a = []
    a.append(x)
    a.append(y)
    return a


def button_trajectory(pos, mouse_click, speed):
    if mouse_click:
        mouse_pos = pygame.mouse.get_pos()
        # print(str(pos[0]),str(pos[1]))
        # print(str(mouse_pos[0]),str(mouse_pos[1]))
        a = trajectory(pos[0], mouse_pos[0], pos[1], mouse_pos[1], speed)
        mouse_click = False
        # print(str(a))
        return a


###################################################################################
def Game_time_support():
    a = bool_loop()
    b = 0
    c = [a, b]
    return c


def Game_time_use(game_time_support, print_it=False, use0=True):
    game_time_support[0].flux()
    if game_time_support[0].Bool:
        game_time_support[1] += 1
        return game_time_support[1]
    if game_time_support[1] != 0:
        # print(str(game_time_support[1]))
        pass
    if use0:
        return 0
    else:
        return game_time_support[1]


def Game_time_full(game_time_support):
    a = Game_time_use(game_time_support)
    b = Game_time_use(game_time_support, False, False)
    return [a, b]


def if_Game_time_(Game_time_use, if_time):
    if Game_time_use == if_time:
        return True
    else:
        return False


def if_Game_time_slice(Game_time_use, start_time, end_time):
    if Game_time_use >= start_time and Game_time_use <= end_time:
        return True
    else:
        return False


def if_Game_time_greater(Game_time_use, start_time):
    if Game_time_use >= start_time:
        return True
    else:
        return False


def if_Game_time_flux(Game_time_use, start_time_var, flux_step):
    if Game_time_use > start_time_var + flux_step:
        start_time_var += flux_step
        return True
    else:
        return False


def if_Game_time_flux_version_3(Game_time_use, start_time, flux, times_to_flux):
    var = flux * times_to_flux
    if Game_time_use != 0 and Game_time_use <= var:
        for i in range(Game_time_use):
            if start_time == Game_time_use:
                return True
            elif start_time + flux == Game_time_use:
                return True
            elif Game_time_use > start_time + flux:
                start_time += flux
            else:
                return False
    else:
        return False


################################################################################

def runone_solution(as_needed=100, bool_prefrence=True):
    thislist = []
    for i in range(as_needed):
        has_run = bool_prefrence
        thislist.append(has_run)
    return thislist


def display_time(time1=' '):
    time2 = time.strftime('%I:%M:%S')

    if time2 != time1:
        time1 = time2

    return str(time1)


#################################################################################
def Multi_Bool_loops(amount, loop_length):
    a = []
    for i in range(amount):
        b = bool_loop(0, loop_length)
        a.append(b)
    return a


class bool_loop:
    def __init__(self, last_up=0, mili_ticks=1000):
        self.last_update = last_up
        self.current_time = mili_ticks
        self.runoutcount = 1
        self.fenix_feather = True
        self.run_just_once_bool = True
        self.count = 0
        self.advance_ani_end = True
        self.random_list = random_list_generator()

    def flux(self, start_True=False):  # call this in your update ###                           --example--
        self.Bool = start_True  # you can change the default starting boolian  ####   #  mybool_loop.flux()
        now = pygame.time.get_ticks()  # --the default is False---------------####
        if now - self.last_update > self.current_time:  # now for the if statement
            self.last_update = now  # if mybool_loop.Bool:
            # your code here will only run once :)
            self.Bool = True  # if your fps is 60, then once the amount of
        else:  # ticks imputed in the parent classes argument
            self.Bool = False  # take, this will run the function again.  And again
            # for as long as it is updated

    def advance_mode(self, list_of_bool_counts=None, start_true=False, repeat=True):
        self.Bool = start_true

        now = pygame.time.get_ticks()
        if self.run_just_once_bool:
            if list_of_bool_counts == None:
                list_of_bool_counts = random_list_generator()
            self.current_time = list_of_bool_counts[self.count]
            self.run_just_once_bool = False
        if now - self.last_update > self.current_time and self.advance_ani_end:
            self.last_update = now  # --------------------------------------------------------
            self.count = (self.count + 1) % len(list_of_bool_counts)
            self.current_time = list_of_bool_counts[self.count]
            self.Bool = True
        else:
            self.Bool = False
        if repeat:
            if self.count >= len(list_of_bool_counts) - 1:
                self.count = 0
        else:
            if self.count >= len(list_of_bool_counts) - 1:
                self.count = len(list_of_bool_counts) - 1
                self.advance_ani_end = False

    def run_out_flux(self, times_to_run=1, run_time=1000, bool=False):  # This  was a late night lol.--example--
        self.limitBool = bool  # run function --mybool_loop.run_out_flux(10,5000)
        now = pygame.time.get_ticks()  # then the if statement--
        if self.runoutcount != 0:  # if mybool_loop.limitBool:
            # you code here
            # print('running False')                                                      #this code with the current argument will run
            if now - self.last_update > run_time:  # once every 5000 miliseconds(5seconds), for exactly
                if self.last_update == 0:  # 10 intervals
                    self.runoutcount = times_to_run
                self.last_update = now
                self.runoutcount -= 1
                self.limitBool = True
                # print('hit True')

    def fenix_flux(self):
        if self.fenix_feather == True:
            self.last_update = 0
            self.runoutcount = 1
            self.fenix_feather = False


#################################################################################
class Pause:
    def __init__(self):
        self.running = True

    def see_thru_pause(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.KEYUP:
                    self.running = False
                    # pygame.display.flip()

    def black_out_pause(self, game):
        while self.running:
            game.screen.fill(black)
            for e in pygame.event.get():
                if e.type == pygame.KEYUP:
                    self.running = False
            pygame.display.flip()


def ezpause(g):
    runthis = True
    a = pygame.image.load('Images\\pause.png')
    while runthis:
        g.screen.blit(a, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    runthis = False

        pygame.display.flip()


###############################################################################

class Scene:  # this is primarery used for backround animation , or whole screen animation
    def __init__(self, game, animation_list, tile_size=TILESIZE):
        self.game = game
        self.tile_size = TILESIZE
        self.size = (self.tile_size, self.tile_size)
        self.last_update = 0
        self.last_update2 = 0
        self.current_frame = 0
        self.did_loop = 0
        self.p = Pause
        self.list = animation_list
        self.last_in_list = len(self.list) - 1
        self.re_image = self.last_in_list
        self.did_run = False
        self.did_run_e = False
        self.frame_update = 0
        # more init stuff
        self.go = True
        self.e1 = 100
        self.do_p = True
        self.angle = 0
        self.shrinkx = wth
        self.shrinky = hgt
        self.done_s = False
        self.ux = 0
        self.uy = 0

    def page_turner(self, times_loop=1, scenex=0, sceney=0, fit_to_screen=True, built_in_effect=1):
        self.scenex = scenex
        self.sceney = sceney
        if self.go:
            now = pygame.time.get_ticks()
            if now - self.last_update > 10:
                self.last_update = now
                if not self.did_run:
                    # print('frame 0')
                    self.frame_update += 1
                    self.image = self.list[0]
                    if fit_to_screen:
                        self.image = pygame.transform.scale(self.image, (wth, hgt))
                    if self.frame_update > 1:
                        self.did_run = True
                if self.did_run:
                    self.current_frame = (self.current_frame + 1) % len(self.list)
                    # Pause.see_thru_pause(self)
                    self.image = self.list[self.current_frame]
                    if fit_to_screen:
                        self.image = pygame.transform.scale(self.image, (wth, hgt))
                    if self.do_p:
                        self.p.see_thru_pause(self)
                    # print(str(self.current_frame))
                    if self.current_frame == len(self.list) - 1:
                        self.did_loop += 1
                        # print('time it looped is ' + str(self.did_loop))
                        # self.current_frame = 0

            if self.did_loop < times_loop:

                self.game.screen.blit(self.image, (self.scenex, self.sceney))
            elif self.did_loop >= times_loop:
                if built_in_effect == 1:
                    self.do_p = False
                    now = pygame.time.get_ticks()
                    if now - self.last_update2 > 5:
                        self.last_update = now
                        self.Spin_out_end_effect()
                        self.ux += 5
                        self.uy += 5

                    if self.go:
                        self.game.screen.blit(self.image, (self.ux, self.uy))

    def running(self, time=1000, scenex=0, sceney=0, fit_to_screen=True, use_tiles=False, spin=False, size=None):
        now = pygame.time.get_ticks()
        a, b = wth // 2, hgt // 2
        if now - self.last_update > time:
            self.last_update = now
            # print(str(self.current_frame))

            if not self.did_run:

                self.image = self.list[0]

                self.rect = self.image.get_rect()
                if spin:
                    self.rect.center = (a, b)
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image, (wth, hgt))
                if use_tiles:
                    self.image = pygame.transform.scale(self.image, self.size)
                if size != None:
                    self.image = pygame.transform.scale(self.image, size)
                self.frame_update += 1
                if self.frame_update > 0:
                    self.did_run = True
            else:
                self.current_frame = (self.current_frame + 1) % len(self.list)
                self.image = self.list[self.current_frame]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image, (wth, hgt))
                if use_tiles:
                    self.image = pygame.transform.scale(self.image, self.size)
                if size != None:
                    self.image = pygame.transform.scale(self.image, size)
            if self.current_frame == len(self.list):
                self.current_frame = 0
        if self.last_update != 0:

            if spin:
                self.rect.center = (a, b)
                self.game.screen.blit(self.image, self.rect.center)
                self.image = pygame.transform.rotate(self.image, self.ux)
                self.ux += 1
            else:
                self.game.screen.blit(self.image, (scenex, sceney))

            if self.ux >= 360:
                self.ux = 0

    def button_page_turner(self, scenex=0, sceney=0, fit_to_screen=True):
        self.x = scenex
        self.y = sceney
        self.did_run = False
        if not self.did_run:
            if not self.did_run_e:
                self.image = self.list[0]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image, (wth, hgt))
            else:
                self.current_frame = (self.current_frame + 1) % len(self.list)
                self.image = self.list[self.current_frame]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image, (wth, hgt))

        # self.game.screen.blit(self.image,(scenex,sceney))
        self.did_run_e = True
        self.did_run = True
        self.game.button1.clicked = False

    def button_running(self):
        pass

    def Spin_out_end_effect(self, spin=100, test=True):
        # add this to your code in update after you call a page_turner
        # in new()
        # this will make the last image do a special effect - spin and shrink -
        self.angle += 1
        self.shrinkx -= 10
        self.shrinky -= 10

        aa = 1
        # print('effect has run ')
        # print('angle is ' + str(aa))
        if self.go:
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.image = pygame.transform.scale(self.image, (self.shrinkx, self.shrinky))

            # print(str(self.scenex)+ '   ' +str(self.sceney))
        if self.shrinkx < 1:
            self.shrinkx = 1
            self.go = False

        if self.shrinky < 1:
            self.shrinky = 1
            self.go = False
            # self.image  = self.re_image = pygame.transform.rotate(self.image, aa)
            # self.image = pygame.transform.scale(self.image,(wth + 5,hgt + 5))
            # self.iamge = self.re_image = pygame.transform.scale(self.image,(wth + 5,hgt + 5 ))

    def make_tile_from_list(self, use_index):

        self.image = self.list[use_index]
        self.image = pygame.transform.scale(self.image, self.size)
        return self.image


def ezscene_ani(g, animation_list, runtime):
    running = True
    scene = Scene(g, animation_list)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                running = False
        scene.running(runtime)
        pygame.display.flip()


def ezscene_fixed(g, img, text, kill_time):
    running = True
    timer = Game_time_support()
    while running:
        g.screen.blit(img, (0, 0))
        time = Game_time_full(timer)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYUP:
                running = False
        img = pygame.transform.scale(img, (wth, hgt))
        screen_text_flex(text, g.tsupport, 300, 300)
        if if_Game_time_(time[0], kill_time):
            running = False

        pygame.display.flip()


class Surf(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width=TILESIZE, hieght=TILESIZE):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.size = (width, hieght)
        self.image = pygame.Surface(self.size)
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.image.blit(self.image,(0,0))

    def update(self):
        pass


##################################################################################
class Sheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)
        self.rando = random.randrange(1, 10)
        self.rando2 = random.randrange(1, 3)

    # each appendage will scale image accordingly,
    # get_image10, allows for you to import the scale yourself
    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * 2, h * 2))
        return image

    def get_image2(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // 4, h // 4))
        return image

    def get_image3(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        return image

    def get_image4(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // self.rando, h // self.rando))
        return image

    def get_image5(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * self.rando2, h * self.rando2))
        return image

    def get_image6(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        return image

    def get_image7(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * 2, w * 2))
        return image

    def get_image8(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // 2, h // 2))
        return image

    def get_image9(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * 2, h))
        return image

    def get_image10(self, x, y, w, h, scale_width, scale_hieght):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (scale_width, scale_height))
        return image


##################################################################################
class tester(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        d = random.randrange(1, 5)
        color = random.choice(all_color_list)
        self.image = pygame.Surface((d, d))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        a = random.randrange(1, 500)
        b = random.randrange(1, 500)
        c = random.randrange(10, 200)
        cc = random.randrange(2, 10)
        f = random.randrange(1, 5)
        h = random.choice([True, False, True, False, False, True, True, False, True])
        self.course = random.choice(
            [trajectory_rect(a, b, c, f, h), trajectory_octagon(a, b, c, cc, h), trajectory_triangle(a, b, c, cc, h),
             trajectory_traverseing_circle(a, b, c, cc, f, h)])
        # print('course'+str(self.course))
        self.counter = 0
        self.rect.topleft = self.course[self.counter]
        g = random.randrange(5, 300)
        self.flux = bool_loop(0, 5)
        self.countTrue = True

    def update(self):
        self.flux.flux()
        if self.flux.Bool and self.countTrue:
            self.rect.topleft = self.course[self.counter]
            # print('pos: '+str(self.rect.topleft),'place: '+str(self.counter))
            self.counter += 1

            # if self.counter >= len(self.course) - 1:
            # self.counter = 1

        if self.counter >= len(self.course) - 1:
            # self.countTrue = False
            self.counter = 0


####outdated -vvv-########but########still fuctional#########################################
class Text:
    def __init__(self, game):
        self.game = game
        self.renders()

    def draw_text(self, font, text, size, color, x, y):
        # standered text to screen, flexable
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.game.screen.blit(text_surface, text_rect)

    def draw_text2(self, font, text, color, x, y):
        # less flexable way to text to screen
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.game.screen.blit(text_surface, text_rect)

    def draw_text3(self, font, text, size, color, x, y):
        # the paced in pos is top left allowing for user to line up each line
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.game.screen.blit(text_surface, text_rect)

    def renders(self):
        self.default = pygame.font.Font(None, 40)

    def ask(self, question):
        word = ""
        Text(self.game).draw_text2(self.default, question, green, wth // 2, 50)  # example asking name
        pygame.display.flip()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        word += str(chr(event.key))
                    if event.key == pygame.K_b:
                        word += chr(event.key)
                    if event.key == pygame.K_c:
                        word += chr(event.key)
                    if event.key == pygame.K_d:
                        word += chr(event.key)
                    if event.key == pygame.K_RETURN:
                        done = False
                        # events...
        return Text(self.game).draw_text2(self.default, word, green, wth // 2, 100)


def simple_pretext():
    font = pygame.font.Font(None, 30)
    return font


def simple_display_text(text, color, simplepretext, surface, x, y):
    text_surface = simplepretext.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


##############new and improved -vvv-#######################################################################################################
def screen_text_support(color, surface, Font=None, size=40):
    default = pygame.font.Font(Font, size)
    b = runone_solution(100)
    d = []
    for i in range(100):
        c = 0
        d.append(c)
    a = [default, color, surface, b, d]
    return a


def screen_text_render(size, color, text):
    font = screen_text_fonts(size)
    text_surface = font.render(text, True, color)
    return text_surface


######################################################################################################################
def screen_text_solid(text_surface, surface, x, y):
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#


###########this is the main addition to text##########################################
def screen_text_flex(text, support, x, y, paste_in='midtop', step_360=1, i_d=0, surface_tag=None, colortag=None):
    if paste_in != 'flash':
        if colortag == None:
            color = support[1]
        else:
            color = colortag
    else:
        color = random.choice(all_color_list)
    if paste_in != 'flip_left' and paste_in != 'flip_right' and paste_in != 'tilt_right' and paste_in != 'tilt_left' and paste_in != '360_right' and paste_in != '360_left' and paste_in != '360_bounce' and paste_in != '360_flex':
        # ('no')
        text_surface = support[0].render(text, True, color)
        text_rect = text_surface.get_rect()
    else:
        # print('yes')

        if paste_in == 'flip_left':
            flip = 90
        if paste_in == 'flip_right':
            flip = -90
        if paste_in == 'tilt_right':
            flip = -45
        if paste_in == 'tilt_left':
            flip = 45
        if paste_in == '360_left' or paste_in == '360_right' or paste_in == '360_bounce' or paste_in == '360_flex':
            flip = support[4][0]
            step = step_360
            text_surface = support[0].render(text, True, color)
            text_rect = text_surface.get_rect()
            x_flex, y_flex = text_rect.width, text_rect.height

        if paste_in == '360_left':
            support[4][i_d] += step
            if support[4][i_d] > 360:
                support[4][i_d] = 0
        if paste_in == '360_right' or paste_in == '360_bounce' or paste_in == '360_flex':
            support[4][i_d] -= step
            if support[4][i_d] < -360:
                support[4][i_d] = 0

        # print(paste_in)
        text_surface = support[0].render(text, True, color)
        text_surface = pygame.transform.rotate(text_surface, flip)
        if paste_in == '360_flex':
            text_surface = pygame.transform.scale(text_surface, (x_flex, y_flex))
            x_flex += 1
            y_flex += 1
            if x_flex > text_rect.width + 300:
                x_flex = 1
            if y_flex > text_rect.height + 300:
                y_flex = 1

        text_rect = text_surface.get_rect()
        if paste_in != '360_bounce':
            text_rect.center = (x, y)
        else:
            text_rect.midbottom = (x, y)

    if paste_in == 'midtop':
        text_rect.midtop = (x, y)
        # print('here')
    elif paste_in == 'topleft':
        text_rect.topleft = (x, y)
    elif paste_in == 'topright':
        text_rect.topright = (x, y)
    elif paste_in == 'swirl':
        one = (x + 2, y + 2)
        two = (x - 2, y - 2)
        three = (x - 2, y + 2)
        four = (x + 2, y - 2)
        text_rect.midtop = random.choice([(x, y), one, two, three, four])
    elif paste_in == 'flash':
        text_rect.midtop = (x, y)

    if surface_tag == None:
        support[2].blit(text_surface, text_rect)

    else:
        surface_tag.blit(text_surface, text_rect)


def string_support(g):
    loop = bool_loop(0, 50)
    a = [loop, 0, '', False,all_color_list,0]
    return a


def building_strings(string):
    counter = 0
    new_string = []
    for i in string:
        i = string[counter]
        counter += 1
        new_string.append(i)
        # print(i)
        # print(str(new_string))
    return new_string


def display_timed_string(g, list, support,text_support, paste_in='midtop',fun_color = False):
    if not fun_color:
        screen_text_flex(support[2], text_support, 300, 300, paste_in=paste_in)
    else:
        screen_text_flex(support[2], text_support, 300, 300, paste_in=paste_in,colortag=support[4][support[5]])

    support[0].flux()
    if support[0].Bool and not support[3]:
        support[2] += list[support[1]]
        support[1] += 1
        support[5] +=1
        if support[5] >= len(support[4]):
            support[5] = random.randrange(0,len(support[4]))
        if support[1] == len(list):
            support[1] = len(list)
            support[3] = True


###########this is for making txt windows ez and easy screen clean up###########################################################################################################
def text_window_setup(back='Images\\text_surf.png'):
    thislist = []
    bool_1 = True
    thislist.append(bool_1)
    text_surf = pygame.image.load(back)
    text_surf_rect = text_surf.get_rect()

    thislist.append(text_surf)
    thislist.append(text_surf_rect)
    a = bool_loop()
    thislist.append(a)
    '''[0=a bool set to true]^^^[1=text_backround]****[2=text_surf_rect]^^^^[3=misc.bool_loop_function]'''
    return thislist


def text_window_setup_packs(amount, back='Images\\text_surf.png'):
    thislist = []
    for i in range(amount):
        a = text_window_setup(back)
        thislist.append(a)

    '''this allows for infinite text_windows'''

    return thislist


def text_window_basic(text, support, x, y, text_window_setup, display_time=5, type='basic', tag_display=''):
    b = text_window_setup[1]
    c = support[1]
    d = support[0]
    e = [d, c, b]
    if tag_display != 'fixed':
        text_window_setup[3].run_out_flux(1, display_time * 1000)
        if text_window_setup[3].limitBool:
            # print('False')
            text_window_setup[0] = False
        if text_window_setup[0]:
            text_window_setup[1]

            text_window_setup[2].midtop = (x, y)
            if type == 'basic':
                screen_text_flex(text, e, text_window_setup[2].width // 2, 10, 'midtop')
            if type == 'flash':
                screen_text_flex(text, e, text_window_setup[2].width // 2, 10, 'flash')
        if text_window_setup[0]:
            support[2].blit(text_window_setup[1], text_window_setup[2])
    else:
        text_window_setup[1]

        text_window_setup[2].midtop = (x, y)
        if type == 'basic':
            screen_text_flex(text, e, text_window_setup[2].width // 2, 10, 'midtop')
        if type == 'flash':
            screen_text_flex(text, e, text_window_setup[2].width // 2, 10, 'flash')
        support[2].blit(text_window_setup[1], text_window_setup[2])


def text_window_stack(text1, text2, text3, support, x, y, text_window_setup1, text_window_setup2, text_window_setup3,
                      display_time=5, type='basic'):
    a = 50
    text_window_basic(text1, support, x, y, text_window_setup1, display_time, type,
                      tag_display='fixed')  # text,support,x,y,text_window_setup,display_time=5
    text_window_basic(text2, support, x, y + 50, text_window_setup2, display_time + 1, type, tag_display='fixed')
    text_window_basic(text3, support, x, y + 100, text_window_setup3, display_time + 2, type, tag_display='fixed')


def text_window_page(text_list, support, x, starty, wlist):
    starting_y = starty
    counter = 0
    counter2 = 0
    last_update = 50
    for i in range(len(text_list)):
        text_window_basic(text_list[counter], support, x, starting_y, wlist[counter2], display_time=10000000,
                          tag_display='fixed')
        counter += 1
        starting_y += last_update
        counter2 += 1


###############################################################################
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)

        self.tilewht = len(self.data[0])
        self.tilehgt = len(self.data)
        self.wth = self.tilewht * tilesize
        self.hgt = self.tilehgt * tilesize


#################################################################################
class Grid:
    def __init__(self, game, tile_size=TILESIZE, txt_file=None):
        self.game = game
        self.tile_size = tile_size
        self.txt_file = txt_file
        try:
            self.framing1 = txt_file
        except:
            pass
        # seperater
        self.xlist = []
        self.ylist = []

        self.filler = []
        self.filler_holder = []
        self.ingrid = False

        self.xtile = []
        self.ytile = []

    def draw_grid(self, x_space=0, y_space=0):

        for i in range(x_space, wth + self.tile_size // 2, self.tile_size):
            pygame.draw.line(self.game.screen, blue, (i, x_space), (i, hgt))
        for i in range(y_space, hgt + self.tile_size // 2, self.tile_size):
            pygame.draw.line(self.game.screen, red, (y_space, i), (wth, i))

    def create_grid_cords(self, x_spacer=0, y_spacer=0):

        for i in range(x_spacer, wth, self.tile_size):
            x = i
            self.xlist.append(x)
        for i in range(y_spacer, hgt, self.tile_size):
            y = i
            self.ylist.append(y)
        self.x_space = x_spacer
        self.y_space = y_spacer
        self.set_up_pos()

    def mouse_to_grid_check(self):
        self.check = True
        for row in self.xlist:  # this is the x of the q
            for col in self.ylist:  # this is the y of the q
                if row + self.tile_size > self.game.mpos[0] > row and col + self.tile_size > self.game.mpos[1] > col:
                    self.r = (row) // (self.tile_size)
                    self.c = (col) // (self.tile_size)
                    self.xpos = self.r - 2
                    self.ypos = self.c - 2
        if self.x_space + (self.tile_size * 14) > self.game.mpos[0] > self.x_space and self.y_space + (
            self.tile_size * 4) > self.game.mpos[1] > self.y_space:
            # print('you have entered the grid')
            self.ingrid = True
        else:
            # print('Not in grid')
            self.ingrid = False

    def set_up_pos(self):
        for row in self.xlist:  # this is the x of the q
            r = row
            xpos = r + 1
            self.xtile.append(xpos)
        for col in self.ylist:  # this is the y of the q
            c = col
            ypos = c + 1
            self.ytile.append(ypos)
            # print('x:' + str(self.xtile))
            # print('y:' + str(self.ytile))

    def print_mousepos_grid(self):

        print(self.r // self.tile_size, self.c // self.tile_size)

    def color_a_block_with_click(self):
        self.r = self.r * self.tile_size
        self.c = self.c * self.tile_size
        self.filler.append((self.r, self.c, self.tile_size, self.tile_size))
        print(self.filler)

    def fill(self, color):
        for i in self.filler:
            pygame.draw.rect(self.game.screen, color, i)

    def test_blocks(self, color, length_x, length_y, total, block_x, block_y, fill=False):

        for i in range(total):
            if not fill:
                pygame.draw.rect(self.game.screen, color,
                                 (block_x * self.tile_size, block_y * self.tile_size, self.tile_size, self.tile_size),
                                 5)
                block_x += length_x
                block_y += length_y
            else:
                pygame.draw.rect(self.game.screen, color,
                                 (block_x * self.tile_size, block_y * self.tile_size, self.tile_size, self.tile_size))
                block_x += length_x
                block_y += length_y

    def active(self, Print=False):
        '''self.check = True
         for row in self.xlist:#this is the x of the q
             for col in self.ylist:#this is the y of the q
                 if row +self.tile_size > self.game.mpos[0] > row and col + self.tile_size > self.game.mpos[1] > col:
                    self.r = row
                    self.c = col'''
        self.mouse_to_grid_check()  # the above code is ####mousetogridcheck####
        if Print:
            if self.ingrid:
                print(self.xpos, self.ypos)


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, tile_size, img=None, color=white, does_collide=False, collider_group=None,
                 do_kill=False):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.tile_size = tile_size
        # Make a BLUE wall, of the size specified in the parameters
        if img == None:
            self.image = pygame.Surface((self.tile_size, self.tile_size))
            self.image.fill(color)
            self.color = color
        else:
            try:
                self.image = pygame.image.load(img)
                self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
            except:
                self.image = pygame.Surface((self.tile_size, self.tile_size))
                self.image.fill(color)
                self.color = color

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = self.y * self.tile_size
        self.rect.x = self.x * self.tile_size
        self.do_collide = does_collide
        self.collider_group = collider_group
        self.wallx = self.rect.x
        self.wally = self.rect.y

    def update(self):
        if self.do_collide:
            hits = pygame.sprite.spritecollide(self, self.collider_group, Bool)
            if hits:
                print('wall has had a collizion')

    def Room(self):

        '''for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):'''
        pass


class build_wall:
    def __init__(self, game, x, y, x_to, y_to, length, tile_size=TILESIZE, img=None, color=black, does_collide=False,
                 collider_group=None, do_kill=False):
        self.game = game
        endx = 0
        endy = 0
        self.img = img
        for i in range(length):
            if self.img == None:
                w = Wall(self.game, x, y, tile_size, None, color)
            else:
                try:
                    w = Wall(self.game, x, y, tile_size, self.img)
                except:
                    w = Wall(self.game, x, y, tile_size, None, color)

            self.game.all_sprites.add(w)
            if endx < x_to:
                endx += 1
                x += 1
            if endy < y_to:
                endy += 1
                y += 1


class build_with_click:
    def __init__(self, game, tilesize=TILESIZE, scene=None):
        self.game = game
        self.s = scene
        self.tile_size = tilesize
        self.xlist = []
        self.ylist = []

        self.filler = []
        self.filler_holder = []

        self.var_for_fill = 0
        for i in range(0, wth, self.tile_size):
            x = i
            self.xlist.append(x)

        for i in range(0, hgt, self.tile_size):
            y = i
            self.ylist.append(y)
        print(self.xlist)
        print(self.ylist)

    def update(self):

        # print('updateing....')
        for row in self.xlist:  # this is the x of the q
            for col in self.ylist:  # this is the y of the q
                if row + self.tile_size > self.game.mpos[0] > row and col + self.tile_size > self.game.mpos[1] > col:
                    self.r = row // self.tile_size
                    # print('getting erritated...')
                    self.c = col // self.tile_size
                    # print(self.r // self.tile_size,self.c//self.tile_size)

    def place_tile_sprite(self, img=None, color=green):
        self.update()
        if self.game.click_check:
            if self.s == None:
                print('appending to filler at ' + str(self.r), str(self.c))
                w = Wall(self.game, self.r, self.c, self.tile_size, self.game.aa)
                self.game.all_sprites.add(w)
                print(self.game.all_sprites)
            else:

                print('next')
                s = self.s
                self.filler.append(s)

                # print(self.filler)

                # self.game.all_sprites.add(w)
                # self.game.all_sprites.draw(self.game.screen)
                # print(self.filler)

    def fill(self, image=0):

        if self.game.click_check:
            if self.s == None:
                for i in self.filler:
                    # print(i)
                    self.game.all_sprites.add(self.w)
            else:
                print('fill')
                ax = self.r
                ay = self.r
                x = self.r * self.tile_size
                y = self.c * self.tile_size

                self.update()
                self.view = self.filler[self.var_for_fill].make_tile_from_list(image)
                # self.filler[self.var_for_fill].running(5,x,y,False,True)
                surf = Surf(self.game, self.view, x, y)
                self.game.all_sprites.add(surf)

                self.var_for_fill += 1
                print(self.r, self.c)

            self.game.click_check = False


##misc####useful functions for as neededed#####misc##################################################################
def reverse_list(list):
    a = list
    b = 0
    cnt = len(a) - 1
    for i in range(len(a) - 1):
        e = a.pop(cnt)
        a.insert(b, e)
        b += 1
    return a


def Turn_polarity(number):
    if number < 0:
        number = number - (number + number)
    elif number > 0:
        number = number - (number * 2)

    return number


def random_list_generator(start_int=0, end_int=3000, length_of_list=5, step=1):
    randomlist = []
    for i in range(length_of_list):
        a = random.randrange(start_int, end_int, step)
        randomlist.append(a)
    # print(str(randomlist))
    return randomlist


# random_list = random_list_generator()
#####trajectory############possible some of the most useful functions here###########################################################
# a way to tell s sprite to travel in a contained way
def trajectory(starting_xpos=0, ending_xpos=100, starting_ypos=0, ending_ypos=100, speed=1):
    xneg = False
    yneg = False
    x_var = ending_xpos - starting_xpos
    y_var = ending_ypos - starting_ypos
    if x_var < 0:
        xneg = True

        x_var = Turn_polarity(x_var)

    if y_var < 0:
        yneg = True

        y_var = Turn_polarity(y_var)

    xp = starting_xpos
    xpy = starting_ypos

    endx = ending_xpos
    endy = ending_ypos
    if xp == ending_xpos:
        ending_xpos += 1
    if xpy == ending_ypos:
        ending_ypos += 1
    xlist = []
    ylist = []
    xylist = []
    xup = 0
    yup = 0
    for i in range(x_var):
        if not xneg:
            if xp <= ending_xpos:
                x = xp
                xlist.append(x)
                xp += speed
        else:
            if xp >= endx:
                x = xp
                xlist.append(x)
                # print(str(ylist))
                xp -= speed
    # print('yvar' + str(y_var))
    for i in range(y_var):
        if not yneg:
            if xpy <= ending_ypos:
                y = xpy
                ylist.append(y)
                xpy += speed
        else:
            if xpy >= endy:
                y = xpy
                ylist.append(y)
                # print(str(ylist))
                xpy -= speed
    # print('x: '+str(xlist))
    # print('y: '+str(ylist))
    xlen = len(xlist)
    ylen = len(ylist)
    listsize = max([xlen, ylen])
    # print('listsize: '+str(listsize))

    for i in xlist:
        for i in ylist:
            if xup <= len(xlist) - 1 and xup <= listsize:
                xx = xlist[xup]
            else:
                xx = xlist[len(xlist) - 1]
            if yup <= len(ylist) - 1 and yup <= listsize:
                yy = ylist[yup]
            else:
                yy = ylist[len(ylist) - 1]
            if xup <= listsize and yup <= listsize:
                xylist.append((xx, yy))
                xup += 1
                yup += 1
    # print('xy: '+str(xylist))
    return xylist


a = trajectory(0, 100, 0, 100, 10)
b = trajectory(100, 200, 100, 50, 10)
c = trajectory(200, 200, 50, 0, 25)
d = trajectory(200, 300, 0, 150, 5)
e = trajectory(300, 100, 150, 100, 10)
f = trajectory(100, 300, 100, 100, 1)
g = trajectory(300, 500, 100, 500, 10)
h = trajectory(500, 0, 500, 0, 10)

threelist = [a, b, c, d, e, f, g, h]


def multi_trajectory(list_of_lists=threelist):
    # print(list_of_lists)
    multi_list = []
    list_appender = 0
    list_appender2 = 0
    for i in range(len(list_of_lists)):
        # print(str(len(list_of_lists)))
        for i in list_of_lists[list_appender]:
            a1 = list_of_lists[list_appender][list_appender2]
            multi_list.append(a1)
            list_appender2 += 1
        list_appender += 1
        list_appender2 = 0

    # print('multi: '+str(multi_list))
    return multi_list


def trajectory_cirlce_testfunction(start_x=6, start_y=0, rad=13):
    allx = []
    ally = []
    allxy = []
    up = 0

    xl = [6, 7, 8, 9, 10, 11, 12, 12, 13, 13, 12, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0, 0, 1, 1, 2, 3, 4, 5]
    yl = [0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 13, 12, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    for i in range(len(xl)):
        x = xl[up]
        y = yl[up]

        allxy.append((x, y))
        up += 1

    # print('cirlce'+str(allxy))
    return allxy


def trajectory_octagon(startx, starty, size, step=1, clockwise=True):
    x = startx
    y = starty
    s = size

    a = trajectory(x, x + s, y, y + 1, step)
    x1 = x + s
    # print('a'+ str(a))

    b = trajectory(x1 + 1, x1 + s, y + 1, y + s, step)
    # print('b' + str(b))
    x2 = x1 + s
    y1 = y + s

    c = trajectory(x2, x2 + 1, y1 + 1, y1 + s, step)
    # print('c' + str(c))
    y2 = y1 + s

    d = trajectory(x2 - 1, x2 - s, y2 + 1, y2 + s, step)
    # print('d' + str(d))
    x3 = x2 - s
    y3 = y2 + s

    e = trajectory(x3 - 1, x3 - s, y3, y3 + 1, step)
    # print('e' + str(e))
    x4 = x3 - s

    f = trajectory(x4 - 1, x4 - s, y3 - 1, y3 - s, step)
    # print('f' + str(f))
    x5 = x4 - s
    y4 = y3 - s

    g = trajectory(x5, x5 + 1, y4 + 1, y4 - s, step)
    # print('g' + str(g))
    y5 = y4 - s

    h = trajectory(x5 + 1, x5 + s, y5 - 1, y5 - s, step)
    # print('h' + str(h))




    if clockwise:
        circle_list = [a, b, c, d, e, f, g, h]
    else:
        circle_list = [a, h, g, f, e, d, c, b]
        for i in circle_list:
            i = reverse_list(i)
            # print(i)

    create_it = multi_trajectory(circle_list)
    # print('its alive'+str(create_it))

    return create_it


def trajectory_triangle(startx, starty, size, step=1, clockwise=True):
    x = startx
    y = starty
    s = size

    a = trajectory(x, x + s, y, y + s, step)
    newx = x + size
    newy = y + size
    # print('a'+ str(a))
    b = trajectory(newx, newx - (s + s), newy, newy + 1, step)
    newxx = newx - (s + s)

    # print('b' + str(b))
    c = trajectory(newxx, x - 1, newy, y - 1, step)
    # print('c' + str(c))
    if clockwise:
        tri_list = [a, b, c]
    else:
        tri_list = [c, b, a]
        for i in tri_list:
            i = reverse_list(i)
            # print(i)
    create_it = multi_trajectory(tri_list)
    # print('its alive'+str(create_it))

    return create_it


def trajectory_rect(startx, starty, size, step=1, clockwise=True):
    x = startx
    y = starty
    s = size

    a = trajectory(x, x + s, y, y + 1, step)
    nx = x + s

    b = trajectory(nx, nx - 1, y, y + s, step)
    ny = y + s

    c = trajectory(nx, x, ny, ny - 1, step)

    d = trajectory(x, x + 1, ny, ny - s, step)

    if clockwise:
        rect_list = [a, b, c, d]
    else:
        rect_list = [a, d, c, b]
        for i in rect_list:
            i = reverse_list(i)
            # print(i)
    create_it = multi_trajectory(rect_list)
    # print('its alive'+str(create_it))

    return create_it


def trajectory_traverseing_circle(startx, starty, size, lengthTO=10, step=1, clockwise=True):
    x = startx
    y = starty
    s = size
    print_test_count = 1
    run_one = True
    list1 = []
    if clockwise:
        for num in range(lengthTO):
            a = trajectory(x, x + s, y, y + 1, step)
            x1 = x + s
            # print('a'+ str(a))

            b = trajectory(x1 + 1, x1 + s, y + 1, y + s, step)
            # print('b' + str(b))
            x2 = x1 + s
            y1 = y + s

            c = trajectory(x2, x2 + 1, y1 + 1, y1 + s, step)
            # print('c' + str(c))
            y2 = y1 + s

            d = trajectory(x2 - 1, x2 - s, y2 + 1, y2 + s, step)
            # print('d' + str(d))
            x3 = x2 - s
            y3 = y2 + s

            e = trajectory(x3 - 1, x3 - s, y3, y3 + 1, step)
            # print('e' + str(e))
            x4 = x3 - s

            f = trajectory(x4 - 1, x4 - s, y3 - 1, y3 - s, step)
            # print('f' + str(f))
            x5 = x4 - s
            y4 = y3 - s

            g = trajectory(x5, x5 + 1, y4 + 1, y4 - s, step)
            # print('g' + str(g))
            y5 = y4 - s

            h = trajectory(x5 + 1, x5 + s, y5 - 1, y5 - s, step)
            # print('h' + str(h))

            i = a
            var1 = x + s
            j = trajectory(x1, var1, y, y + 1)

            list1.append(a)
            list1.append(b)
            list1.append(c)
            list1.append(d)
            list1.append(e)
            list1.append(f)
            list1.append(g)
            list1.append(h)
            list1.append(i)
            list1.append(j)
            # print('broken' + str(list1))
            x = var1
    else:
        # print('reverse')
        for num in range(lengthTO):
            a = trajectory(x, x + s, y, y + 1, step)
            x1 = x + s
            # print('a'+ str(a))
            a.reverse()
            # print('a' + str(a))
            b = trajectory(x1 + 1, x1 + s, y + 1, y + s, step)
            # print('b' + str(b))
            x2 = x1 + s
            y1 = y + s
            b.reverse()
            c = trajectory(x2, x2 + 1, y1 + 1, y1 + s, step)
            # print('c' + str(c))
            y2 = y1 + s
            c.reverse()
            d = trajectory(x2 - 1, x2 - s, y2 + 1, y2 + s, step)
            # print('d' + str(d))
            x3 = x2 - s
            y3 = y2 + s
            d.reverse()
            e = trajectory(x3 - 1, x3 - s, y3, y3 + 1, step)
            # print('e' + str(e))
            x4 = x3 - s
            e.reverse()
            f = trajectory(x4 - 1, x4 - s, y3 - 1, y3 - s, step)
            # print('f' + str(f))
            x5 = x4 - s
            y4 = y3 - s
            f.reverse()
            g = trajectory(x5, x5 + 1, y4 + 1, y4 - s, step)
            # print('g' + str(g))
            y5 = y4 - s
            g.reverse()
            h = trajectory(x5 + 1, x5 + s, y5 - 1, y5 - s, step)
            # print('h' + str(h))
            h.reverse()
            i = a
            var1 = x - (s * 2)
            i.reverse()
            j = trajectory(x1, var1, y, y + 1)
            j.reverse()
            list1.append(a)
            list1.append(h)
            list1.append(g)
            list1.append(f)
            list1.append(e)
            list1.append(d)
            list1.append(c)
            list1.append(b)
            '''if run_one:
                list1.append(a)
                run_one = False'''
            # list1.append(i)
            list1.append(j)
            x = var1
    if not clockwise:
        for i in list1:
            i = i.reverse()

    create_it = multi_trajectory(list1)
    # print(str(create_it))
    return create_it


    # k = trajectory_octagon(var1,y,s,step,clockwise)


######################################################################################################################
import re

txt = 'rules'


def auto_save(fileDir, text):
    print('game,saved')
    saveFile = open(fileDir, 'w')
    saveFile.write(text)
    saveFile.close()


def auto_load(fileDir):
    readMe = open(fileDir).read()
    print(readMe)
    return readMe


def appendfile(fileDir, toWrite):
    appendme = open(fileDir, 'a')
    appendme.write(toWrite)
    appendme.close()


def load_support(exampleString):
    s = re.findall(r'\d{1,3}', exampleString)
    print(s)
    return s


def Load(auto_load, fileDir):
    letters = []

    obj = load_support(auto_load)
    for a in obj:
        letters.append(a)
    print(str(letters))
    return letters


def example():
    auto_save('save.txt', '99 9')
    loadd = auto_load('save.txt')
    Load(loadd, 'save.txt')


#######################################################################################################################
def black_fill_back():
    a = pygame.Surface((wth, hgt))
    a.fill(black)
    return a


#######################################################################################################################
def easybutton_support(g,support, x, y, sizex, sizey, text):
    a = pygame.Surface((sizex, sizey))
    a_rect = a.get_rect()
    a_rect.topleft = (x, y)
    w = a_rect.width
    h = a_rect.height
    flux = bool_loop(0, 10)
    screen_text_flex(text, support, 3, 3, paste_in='topleft', surface_tag=a)
    sx = a_rect.topleft[0]
    sy = a_rect.topleft[1]
    c = random.choice(all_color_list)
    cc = random.choice(all_color_list)
    ccc = random.choice(all_color_list)
    cccc = random.choice(all_color_list)
    pygame.draw.line(a, c, (0, 0), (a_rect.width, 0), 5)
    pygame.draw.line(a, cc, (a_rect.width, 0), (a_rect.width, a_rect.height), 5)
    pygame.draw.line(a, ccc, (a_rect.width, a_rect.height), (0, a_rect.height), 5)
    pygame.draw.line(a, cccc, (0, a_rect.height), (0, 0), 5)

    todo = False
    mylist = [(sx, sy), (sx + 5, sy + 5)]
    runone = False

    return [a, a_rect.topleft, w, h, flux, mylist, runone, todo]


def easybutton_support_update(g, support, bool, button, ):
    if bool:

        if button:
            support[7] = True
            g.screen.blit(support[0], support[5][0])



        else:
            g.screen.blit(support[0], support[5][1])
            support[7] = False
    else:

        g.screen.blit(support[0], support[5][1])
        # support[6] = False
        support[7] = False


def button_todo(support):
    if support[7]:
        return True
    else:
        return False


def if_easybutton_clicked(g, support, bool):
    if bool:
        a = Mouse_hit_box_for_image(g, support)
        return a
    else:
        return False


#######################################################################################################################

def Mouse_hit_box_basic(g, rect, width, height):
    if rect[0] + width > g.mpos[0] > rect[0] and rect[1] + height > g.mpos[1] > rect[1]:
        return True
    else:
        return False


def Mouse_hit_box_for_image(g, support):
    a = Mouse_hit_box_basic(g, support[1], support[2], support[3])
    return a


######################################################################################################################
def key_input(g, support,question_txt):
    running = True

    while running:
        g.screen.fill(black)
        screen_text_flex(question_txt, support, 300, 200)
        pygame.draw.line(g.screen, white, (100, 280), (500, 280))
        pygame.draw.line(g.screen, white, (500, 280), (500, 380))
        pygame.draw.line(g.screen, white, (500, 380), (100, 380))
        pygame.draw.line(g.screen, white, (100, 380), (100, 280))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                running = False
                var = e.key
                return var

        pygame.display.flip()
        ###########################################################


def savecontrols(akey, jkey, ikey, i2key, pkey, information, leftkey, rightkey, upkey):
    with open('settings\\controls\\b_action.txt', 'w') as file:
        file.write(str(akey))
    with open('settings\\controls\\b_jump.txt', 'w') as file:
        file.write(str(jkey))
    with open('settings\\controls\\b_interact.txt', 'w') as file:
        file.write(str(ikey))
    with open('settings\\controls\\b_interact2.txt', 'w') as file:
        file.write(str(i2key))
    with open('settings\\controls\\b_pause.txt', 'w') as file:
        file.write(str(pkey))
    with open('settings\\controls\\b_information.txt', 'w') as file:
        file.write(str(information))
    with open('settings\\controls\\b_left.txt', 'w') as file:
        file.write(str(leftkey))
    with open('settings\\controls\\b_right.txt', 'w') as file:
        file.write(str(rightkey))
    with open('settings\\controls\\b_up.txt', 'w') as file:
        file.write(str(upkey))


def load_controls():
    a = []
    with open('settings\\controls\\b_action.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_jump.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_interact.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_interact2.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_pause.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_information.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_left.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_right.txt', 'r') as file:
        a.append(int(file.read()))
    with open('settings\\controls\\b_up.txt', 'r') as file:
        a.append(int(file.read()))
    return a


def settings_loop(g):
    running = True
    clicked = False
    sclick1 = easybutton_support(g, 10, 10, 150, 50, 'action')
    sclick2 = easybutton_support(g, 10, 50, 150, 50, 'jump')
    sclick3 = easybutton_support(g, 10, 100, 150, 50, 'interact')
    sclick4 = easybutton_support(g, 10, 150, 150, 50, 'interactb')
    sclick5 = easybutton_support(g, 10, 200, 150, 50, 'pause')
    sclick6 = easybutton_support(g, 10, 250, 150, 50, 'information')
    sclick7 = easybutton_support(g, 10, 300, 150, 50, 'left')
    sclick8 = easybutton_support(g, 10, 350, 150, 50, 'right')
    sclick9 = easybutton_support(g, 10, 400, 150, 50, 'up')

    sclick_exit = easybutton_support(g, 450, 500, 150, 50, 'exit')
    while running:
        g.screen.fill(black)
        easybutton_support_update(g, sclick1, clicked, if_easybutton_clicked(g, sclick1, clicked))
        easybutton_support_update(g, sclick2, clicked, if_easybutton_clicked(g, sclick2, clicked))
        easybutton_support_update(g, sclick3, clicked, if_easybutton_clicked(g, sclick3, clicked))
        easybutton_support_update(g, sclick4, clicked, if_easybutton_clicked(g, sclick4, clicked))
        easybutton_support_update(g, sclick5, clicked, if_easybutton_clicked(g, sclick5, clicked))
        easybutton_support_update(g, sclick6, clicked, if_easybutton_clicked(g, sclick6, clicked))
        easybutton_support_update(g, sclick7, clicked, if_easybutton_clicked(g, sclick7, clicked))
        easybutton_support_update(g, sclick8, clicked, if_easybutton_clicked(g, sclick8, clicked))
        easybutton_support_update(g, sclick9, clicked, if_easybutton_clicked(g, sclick9, clicked))

        easybutton_support_update(g, sclick_exit, clicked, if_easybutton_clicked(g, sclick_exit, clicked))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                g.running = False
                g.playing = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                g.mpos = pygame.mouse.get_pos()
            if e.type == pygame.MOUSEBUTTONUP:
                clicked = False
        if button_todo(sclick_exit):
            savecontrols(g.action_key, g.jump_key, g.interact_a_key, g.interact_b_key, g.pause_key,
                         g.information_key, g.move_left_key, g.move_right_key, g.set_up_key)
            running = False
            clicked = False
        if button_todo(sclick1):
            g.action_key = key_input(g, 'Type your action/attack key now')
            clicked = False
        if button_todo(sclick2):
            g.jump_key = key_input(g, 'Type your jump key now')
            clicked = False
        if button_todo(sclick3):
            g.interact_a_key = key_input(g, 'Type your interact-a key now')
            clicked = False
        if button_todo(sclick4):
            g.interact_b_key = key_input(g, 'Type your interact-b key now')
            clicked = False
        if button_todo(sclick5):
            g.pause_key = key_input(g, 'Type your pause key now')
            clicked = False
        if button_todo(sclick6):
            g.information_key = key_input(g, 'Type your information key now')
            clicked = False
        if button_todo(sclick7):
            g.move_left_key = key_input(g, 'Type your move left key now')
            clicked = False
        if button_todo(sclick8):
            g.move_right_key = key_input(g, 'Type your move right key now')
            clicked = False
        if button_todo(sclick9):
            g.set_up_key = key_input(g, 'Type your set up direction key now')
            clicked = False

        pygame.display.flip()


########################################################################
def txt_input(g,support ,question_txt, save_to_file):
    running = True

    Name = []
    stringthis = ''
    while running:
        g.screen.fill(black)
        screen_text_flex(question_txt, support, 300, 200)
        pygame.draw.line(g.screen, white, (100, 280), (500, 280))
        pygame.draw.line(g.screen, white, (500, 280), (500, 380))
        pygame.draw.line(g.screen, white, (500, 380), (100, 380))
        pygame.draw.line(g.screen, white, (100, 380), (100, 280))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if len(stringthis) < 8:
                    if e.key == pygame.K_a:
                        Name.append('a')
                        stringthis += 'a'
                    if e.key == pygame.K_b:
                        Name.append('b')
                        stringthis += 'b'
                    if e.key == pygame.K_c:
                        Name.append('c')
                        stringthis += 'c'
                    if e.key == pygame.K_d:
                        Name.append('d')
                        stringthis += 'd'
                    if e.key == pygame.K_e:
                        Name.append('e')
                        stringthis += 'e'
                    if e.key == pygame.K_f:
                        Name.append('f')
                        stringthis += 'f'
                    if e.key == pygame.K_g:
                        Name.append('g')
                        stringthis += 'g'
                    if e.key == pygame.K_h:
                        Name.append('h')
                        stringthis += 'h'
                    if e.key == pygame.K_i:
                        Name.append('i')
                        stringthis += 'i'
                    if e.key == pygame.K_j:
                        Name.append('j')
                        stringthis += 'j'
                    if e.key == pygame.K_k:
                        Name.append('k')
                        stringthis += 'k'
                    if e.key == pygame.K_l:
                        Name.append('l')
                        stringthis += 'l'
                    if e.key == pygame.K_m:
                        Name.append('m')
                        stringthis += 'm'
                    if e.key == pygame.K_n:
                        Name.append('n')
                        stringthis += 'n'
                    if e.key == pygame.K_o:
                        Name.append('o')
                        stringthis += 'o'
                    if e.key == pygame.K_p:
                        Name.append('p')
                        stringthis += 'p'
                    if e.key == pygame.K_q:
                        Name.append('q')
                        stringthis += 'q'
                    if e.key == pygame.K_r:
                        Name.append('r')
                        stringthis += 'r'
                    if e.key == pygame.K_s:
                        Name.append('s')
                        stringthis += 's'
                    if e.key == pygame.K_t:
                        Name.append('t')
                        stringthis += 't'
                    if e.key == pygame.K_u:
                        Name.append('u')
                        stringthis += 'u'
                    if e.key == pygame.K_v:
                        Name.append('v')
                        stringthis += 'v'
                    if e.key == pygame.K_w:
                        Name.append('w')
                        stringthis += 'w'
                    if e.key == pygame.K_x:
                        Name.append('x')
                        stringthis += 'x'
                    if e.key == pygame.K_y:
                        Name.append('y')
                        stringthis += 'y'
                    if e.key == pygame.K_z:
                        Name.append('z')
                        stringthis += 'z'
                    if e.key == pygame.K_SPACE:
                        Name.append(' ')
                        stringthis += ' '
                if e.key == pygame.K_BACKSPACE:
                    stringthis = ' '
                if e.key == pygame.K_RETURN:
                    file = open(save_to_file, 'w')
                    file.write(stringthis)
                    file.close()
                    running = False

        newstring = stringthis
        screen_text_flex(newstring, support, 300, 300)

        pygame.display.flip()


def Y_N_O_box(g,support, question, yes_option, no_option):
    running = True
    supportclick = easybutton_support(g,g.tsupport ,350, 400, 250, 50, yes_option)
    supportclick1 = easybutton_support(g,g.tsupport, 355, 450, 250, 50, no_option)
    clicked = False
    while running:
        g.screen.fill(black)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                g.playing = False
                g.running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                g.mpos = pygame.mouse.get_pos()

            if e.type == pygame.MOUSEBUTTONUP:
                clicked = False
        #easybutton_support_update(g, supportclick, clicked, if_easybutton_clicked(g, supportclick, clicked))
        #easybutton_support_update(g, supportclick1, clicked, if_easybutton_clicked(g, supportclick1, clicked))
        if easybutton_support__v_2(g, supportclick, clicked):
            running = False
            return True
        if easybutton_support__v_2(g, supportclick1, clicked):
            running = False
            return False

        screen_text_flex(question, support, 300, 100)
        pygame.display.flip()

def easybutton_support__v_2(g, support, clicked_bool):
    easybutton_support_update(g, support, clicked_bool, if_easybutton_clicked(g, support, clicked_bool))
    if button_todo(support):
        return True
    else:
        return False

def sprite_lift_support():
    flux = bool_loop(0, 100)
    update = 0
    thisbool = False
    thatbool = False
    return [flux, update, thisbool, thatbool]


def sprite_lift(g, player, sprite, sup):
    if player.is_att2:
        player.pick_it_up = False
        sup[2] = False
        player.put_it_down = False
        sup[3] = False
        player.is_att2 = False
    hits = pygame.sprite.spritecollide(sprite, g.playerg, False)
    if hits:
        if player.pick_it_up:
            sup[2] = True
    else:
        player.pick_it_up = False
    if sup[2]:
        sprite.rect.bottom = player.rect.top
        sprite.rect.left = player.rect.left

        if player.put_it_down:
            sup[2] = False
            sup[3] = True
            player.pick_it_up = False
    if sup[3]:
        if g.att_left:
            sprite.rect.left = player.rect.left
        else:
            sprite.rect.right = player.rect.right
        sprite.rect.bottom = player.rect.bottom
        sup[3] = False
        player.put_it_down = False


def textPageloop(g,support, textlist, kill_time_in_secs):
    running = True

    timer = Game_time_support()
    textlist1 = textlist
    while running:
        time = Game_time_full(timer)
        g.clock.tick(60)
        g.screen.fill(black)
        for e in pygame.event.get():
            if e.type == pygame.KEYUP:
                if if_Game_time_greater(time[1], 2):
                    running = False
        counter = 0
        last_update = 50
        y = 10

        basic_open_events(g)
        for i in range(len(textlist1)):
            screen_text_flex(textlist1[counter], support, wth // 2, y)
            # print(textlist[counter])
            counter += 1
            y += last_update

        if if_Game_time_(time[0], kill_time_in_secs):
            running = False

        pygame.display.flip()


def basic_open_events(g):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            g.playing = False
            g.running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            g.mpos = pygame.mouse.get_pos()

        if e.type == pygame.MOUSEBUTTONUP:
            clicked = False


def physics(acc=0.9, friction=-0.1, grav=0.9, jump=20):
    a = [acc, friction, grav, jump]
    return a


class Fooliery_sprite__init__:
    def __init__(self, SPRITE, hp, speed=1, acc=0.9, friction=-0.01, grav=0.9, jump=20):
        self.sprite = SPRITE
        self.sprite.hp = hp
        self.phy = physics(acc, friction, grav, jump)
        self.sprite.vel = vec(0, 0)
        self.sprite.acc = vec(0, 0)
        self.speed = speed
        jumps = random.randrange(250, 750)
        self.sprite.jump_flux = bool_loop(0, jumps)
        self.sprite.jump_counter = 0
        #########bools and vars for -fall and flux-############
        a_flux = random.randrange(2750, 4000)
        self.fnf_flux = bool_loop(0, a_flux)
        b_flux = random.randrange(4000, 6000)
        self.fnf_flux2 = bool_loop(0, b_flux)
        self.fnf_speed = 1

        if random.choice([True, False]):
            self.fnf_left = True
            self.fnf_right = False
        else:
            self.fnf_left = False
            self.fnf_right = True
            ##########jump vars##################################
            self.j_counter = 0
            self.do_j = False
        ##########detector bools and vars###################
        ########game time stuff###########
        self.timer = Game_time_support()
        ####move vec flux####################
        self.isvec = False

        self.mvff_counter = 1
        ####animation stuff ###################
        self.ani_counter = 0
        self.current_frame = 0
        self.ani_flux = bool_loop(0, 250)
        self.can_jump = True
        self.jump_counter = 0
        pygame.sprite.Sprite.__init__(self.sprite)

    def animation_support(self, mili_ticks, loader, flip=True, front=None):
        self.loader(loader)
        self.ani_counter = 0
        self.current_frame = 0
        self.ani_flux = bool_loop(0, mili_ticks)
        self.right_face = self.sprite.list
        self.left_face = []

        self.c2px_flux = bool_loop(0, 500)
        self.c2px_counter = 0
        self.c2px_counter_b = 0
        if flip:
            for i in self.sprite.list:
                i = pygame.transform.flip(i, True, False)
                self.left_face.append(i)
                i = pygame.transform.flip(i, True, False)
        else:
            self.left_face = self.right_face
        self.ani_direction = self.left_face

        self.front = front

    def time(self):
        time = Game_time_full(self.timer)
        return time

    def hits(self, hit_group, do_kill=False, use_mask=True):
        if use_mask:
            if do_kill:
                hit = pygame.sprite.spritecollide(self.sprite, hit_group, True, pygame.sprite.collide_mask)
                if hit:
                    return True
                else:
                    return False
            else:
                hit = pygame.sprite.spritecollide(self.sprite, hit_group, False, pygame.sprite.collide_mask)
                if hit:
                    return True
                else:
                    return False
        else:
            if do_kill:
                hit = pygame.sprite.spritecollide(self.sprite, hit_group, True)
                if hit:
                    return True
                else:
                    return False
            else:
                hit = pygame.sprite.spritecollide(self.sprite, hit_group, False)
                if hit:
                    return True
                else:
                    return False

    def stay_in_screen_x(self, loop=False):
        if not loop:
            if self.sprite.rect.right <= 0:
                self.sprite.rect.right = 0
            if self.sprite.rect.left >= wth:
                self.sprite.rect.left = wth
        else:
            if self.sprite.rect.right <= -1:
                self.sprite.rect.left = wth
            elif self.sprite.rect.left >= wth + 1:
                self.sprite.rect.right = 0

    def vec_stay_in_screen_x(self, loop=False):

        if not loop:
            if self.sprite.rect.left <= 0:
                if self.sprite.vel.x < 0:
                    self.move_vec_right()
            if self.sprite.rect.right >= wth:
                if self.sprite.vel.x > 0:
                    self.move_vec_left()
        else:
            if self.sprite.rect.left <= -1:
                self.sprite.rect.right = wth
            if self.sprite.rect.left >= wth + 1:
                self.sprite.rect.right = 0

    def fall_and_flux(self, dubble_flux=True):

        self.sprite.rect.x += self.fnf_speed
        if self.sprite.rect.right <= -1:
            self.fnf_speed = Turn_polarity(self.fnf_speed)
        if self.sprite.rect.left >= wth + 1:
            self.fnf_speed = Turn_polarity(self.fnf_speed)

        if dubble_flux:
            self.fnf_flux.flux()
            self.fnf_flux2.flux()
            if self.fnf_flux.Bool:
                self.fnf_speed = Turn_polarity(self.fnf_speed)
            if self.fnf_flux2.Bool:
                self.fnf_speed = Turn_polarity(self.fnf_speed)

    def jump(self, jump_force):
        if self.do_j:
            self.sprite.rect.bottom -= jump_force
            self.j_counter += 1
        if self.j_counter > 25:
            self.j_counter = 0
            self.do_j = False

    def vec_jump(self):
        self.sprite.rect.x += 1
        hits = pygame.sprite.spritecollide(self.sprite, self.sprite.g.platforms, False)
        self.sprite.rect.x -= 1
        if hits:
            # print('111111')
            if self.sprite.rect.bottom >= hits[0].rect.top:
                self.sprite.vel.y = -self.phy[3]  # acc,friction,grav,jump
                # print('22222222')

    def detector_x(self, group):
        for i in group:

            if i.rect.left + i.rect.width > self.sprite.rect.left > i.rect.left:
                return True
            else:
                return False

    def detector_y(self, group):
        for i in group:
            if i.rect.top + i.rect.height > self.sprite.rect.center[0] > i.rect.top:
                return True
            else:
                return False

    def hp_display(self):
        screen_text_flex(str(self.sprite.hp), self.sprite.g.tsupport, self.sprite.rect.midtop[0],
                         self.sprite.rect.midtop[1] - 30, )

    def detector_x_player(self, player):

        if self.sprite.rect.left + self.sprite.rect.width > player.rect.center[0] > self.sprite.rect.left:
            return True
        else:
            return False

    def detector_y_player(self, player):
        if self.sprite.rect.top + self.sprite.rect.height >= player.rect.center[1] > self.sprite.rect.top:
            return True
        else:
            return False

    def contact_x(self, sprite, x, to_x):
        if sprite.rect.center[0] > x and sprite.rect.center[0] < to_x:
            return True
        else:
            return False

    def use_vec(self, x, y, c_flux, d_flux):
        flux = random.randrange(c_flux, d_flux)
        self.sprite.rect.center = (x, y)
        self.sprite.pos = vec(x, y)
        self.move_vec_flux_flux = bool_loop(0, flux)
        self.isvec = True

    def vec_update(self):
        self.sprite.acc = vec(0, self.phy[2])
        if self.sprite.vel.x >= 0 and self.sprite.vel.x <= 0.1:
            self.sprite.vel.x = 0
        if self.sprite.vel.x <= 0 and self.sprite.vel.x >= -0.1:
            self.sprite.vel.x = 0
        self.sprite.acc += self.sprite.vel * self.phy[1]  # acc,friction,grav,jump
        self.sprite.vel += self.sprite.acc
        self.sprite.pos += self.sprite.vel + 0.5 * self.sprite.acc
        self.sprite.rect.midbottom = self.sprite.pos
        self.plathits = pygame.sprite.spritecollide(self.sprite, self.sprite.g.platforms, False)
        if self.plathits:
            if self.sprite.rect.bottom > self.plathits[0].rect.top > self.sprite.rect.bottom - 25:
                self.sprite.pos.y = self.plathits[0].rect.top
                self.sprite.vel.y = 0

    def move_vec_left(self):
        self.sprite.vel.x = -self.phy[0]

    def move_vec_right(self):
        self.sprite.vel.x = self.phy[0]

    def move_x_left(self):
        if self.speed > 0:
            self.speed = Turn_polarity(self.speed)
            self.sprite.rect.x += self.speed

    def move_x_right(self):
        if self.speed < 0:
            self.speed = Turn_polarity(self.speed)
            self.sprite.rect.x += self.speed

    def move_vec_flux(self):
        self.move_vec_flux_flux.flux()
        if self.move_vec_flux_flux.Bool:
            self.mvff_counter = Turn_polarity(self.mvff_counter)
        if self.mvff_counter > 0:
            self.move_vec_right()
        else:
            self.move_vec_left()

    def vec_wth_check_left_out(self, player, wth_check=200):
        if self.sprite.rect.center[0] >= player.rect.center[0] + wth_check:
            return True
        else:
            return False

    def vec_wth_check_right_out(self, player, wth_check=200):
        if self.sprite.rect.center[0] <= player.rect.center[0] - wth_check:
            return True
        else:
            return False

    def vec_wth_check_left_in(self, player, wth_check=200):
        if self.sprite.rect.center[0] >= player.rect.center[0] + wth_check:
            return True
        else:
            return False

    def vec_wth_check_right_in(self, player, wth_check=200):
        if self.sprite.rect.center[0] <= player.rect.center[0] - wth_check:
            return True
        else:
            return False

    def loader(self, loader):
        self.sprite.list = loader

    def animate_it(self, switch=False, xflip=True):
        self.ani_flux.flux()
        if xflip:
            if self.sprite.vel.x < 0:
                if not switch:
                    self.ani_direction = self.right_face
                else:
                    self.ani_direction = self.left_face
            else:
                if not switch:
                    self.ani_direction = self.left_face
                else:
                    self.ani_direction = self.right_face
            if self.ani_flux.Bool:
                if self.front != None:
                    if self.check_vel(0.8):
                        self.ani_direction = self.front
                self.sprite.image = self.ani_direction[self.current_frame]
                self.current_frame += 1
        if self.current_frame > len(self.sprite.list) - 1:
            self.current_frame = 0

    def check_vel(self, check=0.2):
        if self.sprite.vel.x <= check and self.sprite.vel.x >= -check:
            return True

    def vec_at_end_of_plat_left(self, group):
        for i in group:
            if self.plathits:
                if self.sprite.rect.left <= i.rect.left + 10 and self.sprite.rect.left >= i.rect.left:
                    return True

            else:
                return False

    def vec_at_end_of_plat_right(self, group):
        for i in group:
            if self.plathits:
                if self.sprite.rect.right >= i.rect.right - 10 and self.sprite.rect.right <= i.rect.right:
                    return True

            else:
                return False

    def chase_player_up_plat(self):
        if self.sprite.g.player.rect.bottom < self.sprite.rect.top:
            if self.vec_at_end_of_plat_left(self.sprite.g.platforms2):

                self.move_vec_right()
                self.sprite.jump_flux.flux()
                if self.sprite.jump_flux.Bool:
                    self.jump_counter += 1
                if self.jump_counter == 3:
                    self.jump_counter = 0
                    self.can_jump = True
            if self.vec_at_end_of_plat_right(self.sprite.g.platforms2):

                self.move_vec_left()
                self.sprite.jump_flux.flux()
                if self.sprite.jump_flux.Bool:
                    self.jump_counter += 1
                if self.jump_counter == 3:
                    self.jump_counter = 0
                    self.can_jump = True

    def hp_death(self, dokill=True):
        if self.sprite.hp <= 0:
            if dokill:
                self.sprite.kill()
            return True
        else:
            return False

    def player_hits_sprite(self):
        self.sprite.hp -= self.sprite.g.player.damage

    def chase_player__platx(self, check_left=200, check_right=200):
        if not self.detector_x_player(self.sprite.g.player):
            if self.can_jump:
                if self.detector_x(self.sprite.g.platforms2):
                    self.vec_jump()
                    self.can_jump = False
            else:
                self.sprite.jump_flux.flux()
                if self.sprite.jump_flux.Bool:
                    self.jump_counter += 1
                if self.jump_counter == 3:
                    self.jump_counter = 0
                    self.can_jump = True
        else:
            if self.vec_wth_check_left_out(self.sprite.g.player, check_left):
                self.move_vec_left()

            if self.vec_wth_check_right_out(self.sprite.g.player, check_right):
                self.move_vec_right()

    def chase_player__platy(self, checkleft=100, checkright=100):
        if not self.detector_y_player(self.sprite.g.player):
            if self.can_jump:
                if self.detector_x(self.sprite.g.platforms2):
                    self.vec_jump()
                    self.can_jump = False
            else:
                self.sprite.jump_flux.flux()
                if self.sprite.jump_flux.Bool:
                    self.jump_counter += 1
                if self.jump_counter == 3:
                    self.jump_counter = 0
                    self.can_jump = True
        else:

            if self.vec_wth_check_left_out(self.sprite.g.player, checkleft):
                self.move_vec_left()

            elif self.vec_wth_check_right_out(self.sprite.g.player, checkright):
                self.move_vec_right()

    def sprite_choice(self):
        a = random.randrange(0, 1)
        if a == 0:
            return True
        else:
            return False

    def constant_to_player_centerx(self):
        if self.sprite.rect.center[0] >= self.sprite.g.player.rect.center[0]:

            self.move_vec_left()
        else:
            self.move_vec_right()

    def c2px_with_delay(self, delay):

        if self.sprite.rect.center[0] >= self.sprite.g.player.rect.center[0]:
            self.c2px_flux.flux()
            if self.c2px_flux.Bool:
                self.c2px_counter += 1
            if self.c2px_counter >= delay:
                self.c2px_counter_b = 0
                self.move_vec_left()
        else:
            self.c2px_flux.flux()
            if self.c2px_flux.Bool:
                self.c2px_counter_b += 1
            if self.c2px_counter_b >= delay:
                self.c2px_counter = 0
                self.move_vec_right()
            ############################helper sprite ideas#################################################

    def hit_intirperter(self):
        if self.hits(self.sprite.g.goods, False):
            if self.sprite.g.att_left:
                if self.isvec:
                    self.sprite.pos.x -= 4
                    self.sprite.pos.y -= 3
                else:
                    self.sprite.rect.x -= 4
                    self.sprite.rect.y -= 3
            if self.sprite.g.att_right:
                if self.isvec:
                    self.sprite.pos.x += 4
                    self.sprite.pos.y -= 3
                else:
                    self.sprite.rect.x += 4
                    self.sprite.rect.y -= 3
            if self.sprite.g.player.att_up:
                if self.isvec:
                    self.sprite.pos.y -= 3
                    self.sprite.vel.y -= self.sprite.acc.y
                else:
                    self.sprite.rect.y -= 1
                    self.sprite.rect.x += random.choice([-1, 1])
                    # print(str(self.hp))
            self.player_hits_sprite()
            print('good hit')
        if self.hits(self.sprite.g.hit_tottums, False):
            self.sprite.hp -= 10
            print('tottum hit')


#####################################################################################################33
def txt_input_with_return(g,support,question_txt):
    running = True
    runone = False
    Name = []
    startx = 300
    stringthis = ''
    while running:
        g.screen.fill(black)
        screen_text_flex(question_txt, support, 300, 200)
        pygame.draw.line(g.screen, white, (100, 280), (500, 280))
        pygame.draw.line(g.screen, white, (500, 280), (500, 380))
        pygame.draw.line(g.screen, white, (500, 380), (100, 380))
        pygame.draw.line(g.screen, white, (100, 380), (100, 280))
        for e in pygame.event.get():
            k = pygame.key.get_pressed()
            if k[pygame.K_LSHIFT] or k[pygame.K_RSHIFT]:
                c = True
                print('caps')
            else:
                c = False

            if e.type == pygame.KEYDOWN:
                if len(stringthis) < 1000:
                    if e.key == pygame.K_a:
                        if not c:
                            stringthis += 'a'
                        else:
                            stringthis += 'A'
                    if e.key == pygame.K_b:
                        if not c:
                            stringthis += 'b'
                        else:
                            stringthis += 'B'
                    if e.key == pygame.K_c:
                        if not c:
                            stringthis += 'c'
                        else:
                            stringthis += 'C'
                    if e.key == pygame.K_d:
                        if not c:
                            stringthis += 'd'
                        else:
                            stringthis += 'D'
                    if e.key == pygame.K_e:
                        if not c:
                            stringthis += 'e'
                        else:
                            stringthis += 'E'
                    if e.key == pygame.K_f:
                        if not c:
                            stringthis += 'f'
                        else:
                            stringthis += 'F'
                    if e.key == pygame.K_g:
                        if not c:
                            stringthis += 'g'
                        else:
                            stringthis += 'G'
                    if e.key == pygame.K_h:
                        if not c:
                            stringthis += 'h'
                        else:
                            stringthis += 'H'
                    if e.key == pygame.K_i:
                        if not c:
                            stringthis += 'i'
                        else:
                            stringthis += 'I'
                    if e.key == pygame.K_j:
                        if not c:
                            stringthis += 'j'
                        else:
                            stringthis += 'J'
                    if e.key == pygame.K_k:
                        if not c:
                            stringthis += 'k'
                        else:
                            stringthis += 'K'
                    if e.key == pygame.K_l:
                        if not c:
                            stringthis += 'l'
                        else:
                            stringthis += 'L'
                    if e.key == pygame.K_m:
                        if not c:
                            stringthis += 'm'
                        else:
                            stringthis += 'M'
                    if e.key == pygame.K_n:
                        if not c:
                            stringthis += 'n'
                        else:
                            stringthis += 'N'
                    if e.key == pygame.K_o:
                        if not c:
                            stringthis += 'o'
                        else:
                            stringthis += 'O'
                    if e.key == pygame.K_p:
                        if not c:
                            stringthis += 'p'
                        else:
                            stringthis += 'P'
                    if e.key == pygame.K_q:
                        if not c:
                            stringthis += 'q'
                        else:
                            stringthis += 'Q'
                    if e.key == pygame.K_r:
                        if not c:
                            stringthis += 'r'
                        else:
                            stringthis += 'R'
                    if e.key == pygame.K_s:
                        if not c:
                            stringthis += 's'
                        else:
                            stringthis += 'S'
                    if e.key == pygame.K_t:
                        if not c:
                            stringthis += 't'
                        else:
                            stringthis += 'T'
                    if e.key == pygame.K_u:
                        if not c:
                            stringthis += 'u'
                        else:
                            stringthis += 'U'
                    if e.key == pygame.K_v:
                        if not c:
                            stringthis += 'v'
                        else:
                            stringthis += 'V'
                    if e.key == pygame.K_w:
                        if not c:
                            stringthis += 'w'
                        else:
                            stringthis += 'W'
                    if e.key == pygame.K_x:
                        if not c:
                            stringthis += 'x'
                        else:
                            stringthis += 'X'
                    if e.key == pygame.K_y:
                        if not c:
                            stringthis += 'y'
                        else:
                            stringthis += 'Y'
                    if e.key == pygame.K_z:
                        if not c:
                            stringthis += 'z'
                        else:
                            stringthis += 'Z'
                    if e.key == pygame.K_1:
                        stringthis += '1'
                    if e.key == pygame.K_2:
                        stringthis += '2'
                    if e.key == pygame.K_3:
                        stringthis += '3'
                    if e.key == pygame.K_4:
                        stringthis += '4'
                    if e.key == pygame.K_5:
                        stringthis += '5'
                    if e.key == pygame.K_6:
                        stringthis += '6'
                    if e.key == pygame.K_7:
                        stringthis += '7'
                    if e.key == pygame.K_8:
                        stringthis += '8'
                    if e.key == pygame.K_9:
                        stringthis += '9'
                    if e.key == pygame.K_0:
                        stringthis += '0'

                    if e.key == pygame.K_COMMA:
                        stringthis += ','

                    if e.key == pygame.K_PERIOD:
                        stringthis += '.'

                    if e.key == pygame.K_MINUS:
                        if not c:
                            stringthis += '-'
                        else:
                            stringthis += '_'

                    if e.key == pygame.K_SPACE:
                        Name.append(' ')
                        stringthis += ' '
                if e.key == pygame.K_BACKSPACE:
                    stringthis = ' '
                if e.key == pygame.K_RETURN:
                    return newstring
        if len(stringthis) == 20:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 40:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 60:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 80:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 100:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 120:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 140:
            stringthis += '\n'
            startx -= 130
        if len(stringthis) == 160:
            stringthis += '\n'
            startx -= 130
        newstring = stringthis
        screen_text_flex(newstring, support, startx, 300)
        runone = True
        pygame.display.flip()
