import pygame
pygame.mixer.init()

sounds = {
    "chomp": pygame.mixer.Sound("sound/chomp.ogg"),
    "chop": pygame.mixer.Sound("sound/chop.ogg"),
    "loud_thump": pygame.mixer.Sound("sound/loud_thump.ogg"),
    "squish": pygame.mixer.Sound("sound/squish.ogg"),
    "paper": pygame.mixer.Sound("sound/paper.ogg"),
}

sounds["chop"].set_volume(0.9)
sounds["chop"].set_volume(0.1)
sounds["loud_thump"].set_volume(0.4)
sounds["squish"].set_volume(0.3)
sounds["paper"].set_volume(0.5)


def play(name):
    sounds[name].play()

overtureLoopTime = 25.424 # seconds
END_FLAG = pygame.USEREVENT + 1 # ensures that this flag != any preset one

pygame.mixer.music.load("sound/overture.mp3")
pygame.mixer.music.set_endevent(END_FLAG)
