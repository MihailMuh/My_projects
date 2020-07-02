import pygame
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
import random
import os
import sys
from PIL import ImageTk
import time
from scriptspy import inventar, icons, support, button, explosions, functions, loading, shoots, character, heart, boss_game, opponents, meteor, achievment

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(5000)

x = 1370
y = 800

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'scriptspy\images')
snd_folder = os.path.join(game_folder, 'scriptspy\sounds')

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
drobs = pygame.sprite.Group()
drobs_boss = pygame.sprite.Group()
bosses = pygame.sprite.Group()
vaders_group = pygame.sprite.Group()

score = 0
health_boss = 30
sprites = False
jelly = False
putin = False
virus = False
vaders = True
death = False
ship_player = True
ship_gunner = False
for_file = []
key_btn = 0
mouse_btn = 1
count_bosses = 0
font_name = pygame.font.match_font('Segoe Script')
sh = 0
ju = 1
equip = 0
speed_enem = 4
max_score = 0


def game():
    global menu_sound
    global health_boss
    global ju, sh, equip
    global all_sprites, bullets, drobs, drobs_boss, bosses
    global score, count_bosses
    global waiting

    def pause():
        global waiting
        waiting = False
        btn_start.kill()
        btn_quit.kill()
        return waiting

    def best_score():
        global max_score
        with open('scriptspy\papers\score.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                list = lines[0].split(' ')
                for i in list:
                    if i != '':
                        for_file.append(int(i))
                max_score = max(for_file)
        return max_score

    if functions.hardmode:
        pygame.mixer.music.load(os.path.join(snd_folder, 'fight.mp3'))
    else:
        pygame.mixer.music.load(os.path.join(snd_folder, 'pirate.mp3'))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    loading.menu_sound.stop()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-50),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)

    gameover_bg = pygame.image.load(os.path.join(img_folder, 'gameover.jpg'))
    gameover_bg = pygame.transform.scale(gameover_bg, (x, y))
    gameover_rect = gameover_bg.get_rect()

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']

    for img in background_list:
        if img == 'background1.jpg':
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x + 100, y))
            background_images.append(bd)
        else:
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x, y))
            background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    all_sprites = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    shotgun_fly = pygame.sprite.Group()
    vaders_group = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    drobs_boss = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    drobs = pygame.sprite.Group()
    hearts = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    fire = pygame.sprite.Group()
    factories = pygame.sprite.Group()
    minions = pygame.sprite.Group()
    player_gunner_npc_group = pygame.sprite.Group()

    if ship_gunner:
        player = character.Gunner(all_sprites, bullets)
    elif ship_player:
        player = character.Player(sprites, key_btn, mouse_btn, ju, sh, equip, all_sprites, bullets, drobs)
    inv = inventar.Inventar()
    shotgun = icons.Icon_sh()
    shotgun_big = icons.Icon_sh_big()
    rifle = icons.Icon_ju()
    rifle_big = icons.Icon_ju_big()
    heart1 = heart.Heart(loading.ful_heart, 165, 310)
    heart2 = heart.Heart(loading.ful_heart, 165 + 75, 310)
    heart3 = heart.Heart(loading.ful_heart, 165 + 150, 310)
    heart4 = heart.Heart(loading.ful_heart, 165 + 225, 310)
    heart5 = heart.Heart(loading.ful_heart, 165 + 300, 310)
    hearts.add(heart1)
    hearts.add(heart2)
    hearts.add(heart3)
    hearts.add(heart4)
    hearts.add(heart5)

    clock = pygame.time.Clock()
    count_bosses = 0
    hits = 0
    sh = 0
    ju = 1
    equip = 0
    heal = False
    sh_fly = False
    score = 0
    gameover = False
    player_gunner_npc = False
    health_boss2 = health_boss
    if functions.hardmode:
        enemy_vaders = 20
        enemy_meteors = 8
    else:
        enemy_vaders = 17
        enemy_meteors = 0
    boss_time = 50000
    last_boss = pygame.time.get_ticks()
    waiting = False
    FPS = 60

    all_sprites.add(player)

    for i in range(enemy_vaders):
        if random.random() > loading.chanse_triple_fighter:
            imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses, speed_enem,
                                    count_bosses, all_sprites)
            all_sprites.add(imp)
            vaders_group.add(imp)
        else:
            imp = opponents.TripleFighter(sprites, bosses, speed_enem, all_sprites, drobs_boss,
                                          player.rect.center[0], player.rect.center[1])
            all_sprites.add(imp)
            vaders_group.add(imp)
    for i in range(enemy_meteors):
        m = meteor.Meteor(bosses, speed_enem, count_bosses)
        all_sprites.add(m)
        meteors.add(m)

    attention = opponents.Attention(fire)
    attention.hide()
    fire.add(attention)

    rocket = opponents.Rocket(sprites, all_sprites)
    fire.add(rocket)

    all_sprites.add(inv)
    all_sprites.add(rifle_big)
    all_sprites.add(heart1)
    all_sprites.add(heart2)
    all_sprites.add(heart3)
    all_sprites.add(heart4)
    all_sprites.add(heart5)
    all_sprites.add(hearts)

    best_score()
    loading.ready.play()
    for i in [3, 2, 1, 0]:
        screen.blit(random_background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        draw_text(screen, str(max_score), 30, x - 200, 40)
        draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
        if i == 0:
            draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
        else:
            draw_text(screen, str(i), 500, x // 2, 70)
        pygame.display.flip()
        time.sleep(1)

    pygame.event.clear()

    while True:
        clock.tick(FPS)
        nowboss = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        if (key[pygame.K_DOWN]) and (FPS >= 2):
            FPS -= 1
        if key[pygame.K_UP]:
            FPS += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_score()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    loading.pause_snd.play(-1)

                    btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                    btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
                    btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                    buttons.add(btn_quit)
                    buttons.add(btn_menu)
                    buttons.add(btn_start)

                    waiting = True
                    while waiting:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    waiting = False
                        buttons.update()
                        buttons.draw(screen)
                        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2, btn_quit.rect.y)
                        draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2, btn_menu.rect.y)
                        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2, btn_start.rect.y)
                        pygame.display.flip()
                        pygame.display.update()

                    loading.pause_snd.stop()
                    pygame.mixer.music.unpause()

                elif event.key == pygame.K_g:
                    functions.god()

                if key_btn == 1 and mouse_btn == 0:
                    if event.key == pygame.K_2:
                        if equip == 1:
                            if sh != 1:
                                random.choice(loading.reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)
                    elif event.key == pygame.K_1:
                        if equip == 1:
                            if ju != 1:
                                random.choice(loading.reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_btn == 1 and key_btn == 0:
                    if event.button == 4:
                        if equip == 1:
                            if ju != 1:
                                random.choice(loading.reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)
                    elif event.button == 5:
                        if equip == 1:
                            if sh != 1:
                                random.choice(loading.reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)

        for i in vaders_group:
            if i.radius == 70:
                i.sufferx, i.suffery = player.rect.center[0], player.rect.center[1]
                distance = functions.rect_distance(player.rect, i.rect)
                if distance <= 200:
                    i.shoot()

        for i in minions:
            i.sufferx, i.suffery = player.rect.center[0], player.rect.center[1]
            i.shoot()

        if (nowboss - last_boss > boss_time) and not bosses:
            last_boss = nowboss
            health_boss += 10
            health_boss2 = health_boss
            if random.random() > loading.chanse_dead_boss:
                boss = boss_game.Boss(jelly, putin, virus, vaders, death, sprites, all_sprites, drobs_boss)
            else:
                boss = boss_game.Dead(sprites, all_sprites, drobs_boss)
            if functions.hardmode:
                boss.hard()
            all_sprites.add(boss)
            bosses.add(boss)

        if random.random() > loading.chanse_heal:
            if not powerups:
                heal = support.Health()
                all_sprites.add(heal)
                powerups.add(heal)

        if score >= 50:
            if random.random() > loading.chanse_shotgun:
                if not shotgun_fly and equip != 1:
                    sh_fly = support.Fly_sh()
                    all_sprites.add(sh_fly)
                    shotgun_fly.add(sh_fly)

        if (score >= 100) and (functions.newgunner == 0) and (not player_gunner_npc_group) and (functions.newgunner == 0):
            player_gunner_npc = opponents.NewPlayer(sprites)
            all_sprites.add(player_gunner_npc)
            player_gunner_npc_group.add(player_gunner_npc)
            functions.spawnsplayer()
            functions.newplayer()

        if random.random() > loading.chanse_rocket:
            rocket.start()
            attention.visible(rocket.rect.centerx)

        if rocket.rect.y >= -35:
            attention.hide()

        if (random.random() > loading.chanse_factory) and not factories:
            f = opponents.Factory(all_sprites, sprites, bosses, drobs_boss, minions, player.rect.center[0], player.rect.center[1])
            all_sprites.add(f)
            factories.add(f)

        if sh_fly and (player.radius == 40):
            boom_sh_fly = pygame.sprite.spritecollide(player, shotgun_fly, True, pygame.sprite.collide_circle)
            if boom_sh_fly:
                random.choice(loading.reload_sounds).play()
                equip = 1
                ju = 0
                sh = 1
                all_sprites.add(shotgun_big)
                all_sprites.remove(shotgun)
                all_sprites.remove(rifle_big)
                all_sprites.add(rifle)
        elif sh_fly and (player.radius > 40):
            boom_sh_fly = pygame.sprite.groupcollide(shotgun_fly, bullets, False, True, pygame.sprite.collide_circle)
            for i in boom_sh_fly:
                loading.boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = explosions.Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = explosions.Explosion(i.rect.center, 'lg', 2)
                    all_sprites.add(expl)
            sh_fly.kill()

        if heal:
            boom_heal = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
            if boom_heal:
                hits = 0
                heart5.change(loading.ful_heart, 165 + 300, 310)
                heart4.change(loading.ful_heart, 165 + 225, 310)
                heart3.change(loading.ful_heart, 165 + 150, 310)
                heart2.change(loading.ful_heart, 165 + 75, 310)
                heart1.change(loading.ful_heart, 165, 310)
                loading.heal_sound.play()

        if player_gunner_npc:
            boom_player_gunner_npc = pygame.sprite.spritecollide(player, player_gunner_npc_group,
                                                                 True, pygame.sprite.collide_circle)
            if boom_player_gunner_npc:
                functions.unlockplayer()
                functions.newplayer()

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True, pygame.sprite.collide_circle)
        boom_sh = pygame.sprite.groupcollide(vaders_group, drobs, False, True)
        boom = pygame.sprite.spritecollide(player, vaders_group, False, pygame.sprite.collide_circle)
        boom_m = pygame.sprite.spritecollide(player, meteors, False, pygame.sprite.collide_circle)
        boom_bullet_boss = pygame.sprite.spritecollide(player, drobs_boss, True, pygame.sprite.collide_circle)
        boom_rocket = pygame.sprite.spritecollide(player, fire, False, pygame.sprite.collide_circle)
        boom_factory = pygame.sprite.groupcollide(factories, bullets, False, True)
        boom_factory_sh = pygame.sprite.groupcollide(factories, drobs, False, True)
        boom_minion = pygame.sprite.groupcollide(minions, bullets, False, True, pygame.sprite.collide_circle)
        boom_minion_sh = pygame.sprite.groupcollide(minions, drobs, False, True, pygame.sprite.collide_circle)
        boom_minion_pl = pygame.sprite.spritecollide(player, minions, False, pygame.sprite.collide_circle)

        for i in bosses:
            boom_boss = pygame.sprite.groupcollide(bullets, bosses, True, False)
            boom_boss_drob = pygame.sprite.groupcollide(drobs, bosses, True, False)

            for _ in boom_boss:
                if functions.godmode:
                    health_boss2 -= 10
                elif i.rect.y < -200:
                    health_boss2 = health_boss
                else:
                    health_boss2 -= 0.5

            for _ in boom_boss_drob:
                if functions.godmode:
                    health_boss2 -= 10
                elif i.rect.y < -200:
                    health_boss2 = health_boss
                elif functions.hardmode:
                    health_boss2 -= 1
                else:
                    health_boss2 -= 1.5

            if health_boss2 <= 0:
                i.kill()
                for j in drobs_boss:
                    if random.randint(1, 2) == 1:
                        expl = explosions.Explosion(j.rect.center, 'sm')
                        all_sprites.add(expl)
                    else:
                        expl = explosions.Explosion(j.rect.center, 'sm', 2)
                        all_sprites.add(expl)
                    j.kill()
                score += 50
                loading.boom_snd.play()
                expl = explosions.Explosion(i.rect.center, 'hu')
                all_sprites.add(expl)
                count_bosses += 3
                for _ in range(enemy_vaders):
                    if random.random() > loading.chanse_triple_fighter:
                        imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses, speed_enem,
                                                count_bosses, all_sprites)
                        all_sprites.add(imp)
                        vaders_group.add(imp)
                    else:
                        imp = opponents.TripleFighter(sprites, bosses, speed_enem, all_sprites, drobs_boss,
                                                      player.rect.center[0], player.rect.center[1])
                        all_sprites.add(imp)
                        vaders_group.add(imp)
                for _ in range(enemy_meteors):
                    m = meteor.Meteor(bosses, speed_enem, count_bosses)
                    all_sprites.add(m)
                    meteors.add(m)

        for hit in boom_factory:
            if player.radius == 40:
                hit.damage('small')
            else:
                hit.damage('mini')
            if hit.health <= 0:
                score += 10

        for hit in boom_factory_sh:
            hit.damage()
            if hit.health <= 0:
                score += 10

        for i in boom_minion:
            if player.radius == 40:
                i.damage('small')
            else:
                i.damage('mini')

        for i in boom_minion_sh:
            i.damage()

        for i in boom_minion_pl:
            if not functions.godmode:
                if player.radius == 40:
                    hits += 1
                else:
                    hits += 0.5
            loading.metal.play()
            expl = explosions.Explosion(i.rect.center, 'sm', 2)
            all_sprites.add(expl)
            i.kill()

        for i in boom_bullet_boss:
            if not functions.godmode:
                hits += 0.5
            expl = explosions.Explosion(i.rect.center, 'sm', 2)
            all_sprites.add(expl)

        for i in boom_rocket:
            if i != attention:
                if not functions.godmode:
                    hits += 100
                rocket.damage()

        for hit3 in boom_m:
            loading.metal.play()
            if not functions.godmode:
                if player.radius == 40:
                    hits += 1
                else:
                    hits += 0.5
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit3.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit3.rect.center, 'sm', 2)
                all_sprites.add(expl)
            hit3.rect.x = random.randrange(50, x - 70)
            hit3.rect.y = random.randrange(-100, -30)
            hit3.speedy = random.randrange(speed_enem // 2 + 1 + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit3.rot_speed = random.randrange(-10, 10)

        for hit in boom_b:
            if player.radius == 40:
                hit.damage('small')
            else:
                hit.damage('mini')
            if hit.health <= 0:
                if hit.radius == 70:
                    score += 2
                else:
                    score += 1

        for hit2 in boom_sh:
            hit2.damage('big')
            if hit2.health <= 0:
                if hit2.radius == 70:
                    score += 2
                else:
                    score += 1

        for hit4 in boom:
            loading.metal.play()
            if not functions.godmode:
                if hit4.radius == 70:
                    if player.radius == 40:
                        hits += 3
                    else:
                        hits += 1
                else:
                    if player.radius == 40:
                        hits += 2
                    else:
                        hits += 1
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit4.rect.center, 'sm', 2)
                all_sprites.add(expl)
            if not bosses:
                hit4.rect.x = random.randrange(50, x - 70)
                hit4.rect.y = random.randrange(-100, -30)
                hit4.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
                hit4.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
                hit4.rot_speed = random.randrange(-20, 20)
            else:
                hit4.kill()

        if gameover:
            current_score()
            achievment.deathes()
            best_score()

            for i in all_sprites:
                key = pygame.key.get_pressed()
                if (key[pygame.K_DOWN]) and (FPS >= 2):
                    FPS -= 1
                if key[pygame.K_UP]:
                    FPS += 1
                if i not in hearts:
                    loading.boom_snd.play()
                    if (i == player) or (i == rocket) or (i in factories):
                        if random.randint(1, 2) == 1:
                            expl = explosions.Explosion(i.rect.center, 'hu')
                            all_sprites.add(expl)
                        else:
                            expl = explosions.Explosion(i.rect.center, 'hu', 2)
                            all_sprites.add(expl)
                    else:
                        if random.randint(1, 2) == 1:
                            expl = explosions.Explosion(i.rect.center, 'lg')
                            all_sprites.add(expl)
                        else:
                            expl = explosions.Explosion(i.rect.center, 'lg', 2)
                            all_sprites.add(expl)
                    screen.blit(gameover_bg, gameover_rect)
                    all_sprites.update()
                    i.kill()
                    all_sprites.draw(screen)
                    draw_text(screen, 'Счёт:', 30, x // 2, 10)
                    draw_text(screen, str(score), 30, x // 2, 40)
                    draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                    draw_text(screen, str(max_score), 30, x - 200, 40)
                    draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.mixer.music.pause()
                                loading.pause_snd.play(-1)

                                btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                                btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
                                btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                                buttons.add(btn_quit)
                                buttons.add(btn_menu)
                                buttons.add(btn_start)

                                waiting = True
                                while waiting:
                                    clock.tick(10)
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_ESCAPE:
                                                waiting = False
                                    buttons.update()
                                    buttons.draw(screen)
                                    draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                              btn_quit.rect.y)
                                    draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                              btn_menu.rect.y)
                                    draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                              btn_start.rect.y)
                                    pygame.display.flip()
                                    pygame.display.update()

                                loading.pause_snd.stop()
                                pygame.mixer.music.unpause()
                    pygame.display.flip()

            loading.gameover_phrase.play()
            while gameover:
                clock.tick(FPS)
                key = pygame.key.get_pressed()
                if (key[pygame.K_DOWN]) and (FPS >= 2):
                    FPS -= 1
                if key[pygame.K_UP]:
                    FPS += 1
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.pause()
                            loading.pause_snd.play(-1)

                            btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
                            btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            loading.pause_snd.stop()
                            pygame.mixer.music.unpause()
                        elif event.key == pygame.K_TAB:
                            gameover = False

                screen.blit(gameover_bg, gameover_rect)
                draw_text(screen, 'Нажмите "TAB", чтобы продолжить', x // 30, x // 2, y - 300)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                draw_text(screen, str(max_score), 30, x - 200, 40)
                draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                all_sprites.update()
                all_sprites.draw(screen)
                pygame.display.flip()

            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)

            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            bosses = pygame.sprite.Group()
            drobs_boss = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            hearts = pygame.sprite.Group()
            meteors = pygame.sprite.Group()
            buttons = pygame.sprite.Group()
            fire = pygame.sprite.Group()
            factories = pygame.sprite.Group()
            minions = pygame.sprite.Group()

            if ship_gunner:
                player = character.Gunner(all_sprites, bullets)
            elif ship_player:
                player = character.Player(sprites, key_btn, mouse_btn, ju, sh, equip, all_sprites, bullets, drobs)
            inv = inventar.Inventar()
            shotgun = icons.Icon_sh()
            shotgun_big = icons.Icon_sh_big()
            rifle = icons.Icon_ju()
            rifle_big = icons.Icon_ju_big()
            heart1 = heart.Heart(loading.ful_heart, 165, 310)
            heart2 = heart.Heart(loading.ful_heart, 165 + 75, 310)
            heart3 = heart.Heart(loading.ful_heart, 165 + 150, 310)
            heart4 = heart.Heart(loading.ful_heart, 165 + 225, 310)
            heart5 = heart.Heart(loading.ful_heart, 165 + 300, 310)
            hearts.add(heart1)
            hearts.add(heart2)
            hearts.add(heart3)
            hearts.add(heart4)
            hearts.add(heart5)

            clock = pygame.time.Clock()
            count_bosses = 0
            hits = 0
            sh = 0
            ju = 1
            equip = 0
            heal = False
            sh_fly = False
            score = 0
            gameover = False
            health_boss2 = health_boss
            if functions.hardmode:
                enemy_vaders = 20
                enemy_meteors = 8
            else:
                enemy_vaders = 17
                enemy_meteors = 0
            waiting = False
            FPS = 60

            all_sprites.add(player)

            for i in range(enemy_vaders):
                if random.random() > loading.chanse_triple_fighter:
                    imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses, speed_enem,
                                            count_bosses, all_sprites)
                    all_sprites.add(imp)
                    vaders_group.add(imp)
                else:
                    imp = opponents.TripleFighter(sprites, bosses, speed_enem, all_sprites, drobs_boss,
                                                  player.rect.center[0], player.rect.center[1])
                    all_sprites.add(imp)
                    vaders_group.add(imp)
            for i in range(enemy_meteors):
                m = meteor.Meteor(bosses, speed_enem, count_bosses)
                all_sprites.add(m)
                meteors.add(m)

            attention = opponents.Attention(fire)
            attention.hide()
            fire.add(attention)

            rocket = opponents.Rocket(sprites, all_sprites)
            fire.add(rocket)

            all_sprites.add(inv)
            all_sprites.add(rifle_big)
            all_sprites.add(heart1)
            all_sprites.add(heart2)
            all_sprites.add(heart3)
            all_sprites.add(heart4)
            all_sprites.add(heart5)
            all_sprites.add(hearts)

            best_score()
            loading.ready.play()
            for i in [3, 2, 1, 0]:
                screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                draw_text(screen, str(max_score), 30, x - 200, 40)
                draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                if i == 0:
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()
            boss_time = 50000
            last_boss = pygame.time.get_ticks()

        if hits == 1:
            heart5.change(loading.half_heart, 165 + 300, 310)
        elif hits == 2:
            heart5.change(loading.non_heart, 165 + 300, 310)
        elif hits == 3:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.half_heart, 165 + 225, 310)
        elif hits == 4:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
        elif hits == 5:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
            heart3.change(loading.half_heart, 165 + 150, 310)
        elif hits == 6:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
            heart3.change(loading.non_heart, 165 + 150, 310)
        elif hits == 7:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
            heart3.change(loading.non_heart, 165 + 150, 310)
            heart2.change(loading.half_heart, 165 + 75, 310)
        elif hits == 8:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
            heart3.change(loading.non_heart, 165 + 150, 310)
            heart2.change(loading.non_heart, 165 + 75, 310)
        elif hits == 9:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
            heart3.change(loading.non_heart, 165 + 150, 310)
            heart2.change(loading.non_heart, 165 + 75, 310)
            heart1.change(loading.half_heart, 165, 310)
        elif hits >= 10:
            heart5.change(loading.non_heart, 165 + 300, 310)
            heart4.change(loading.non_heart, 165 + 225, 310)
            heart3.change(loading.non_heart, 165 + 150, 310)
            heart2.change(loading.non_heart, 165 + 75, 310)
            heart1.change(loading.non_heart, 165, 310)
            gameover = True

        screen.blit(random_background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        draw_text(screen, str(max_score), 30, x - 200, 40)
        draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
        if bosses:
            functions.draw_health_bar_boss(screen, 30, 100, health_boss2, health_boss)
        fire.update()
        fire.draw(screen)
        pygame.display.flip()
    return


def kill_or_die():
    global menu_sound
    global ju, sh, equip
    global all_sprites, drobs, bullets
    global waiting

    def pause():
        global waiting
        waiting = False
        btn_start.kill()
        btn_quit.kill()
        return waiting

    def best_score():
        global max_score
        with open('scriptspy\papers\score.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                list = lines[0].split(' ')
                for i in list:
                    if i != '':
                        for_file.append(int(i))
                max_score = max(for_file)
        return max_score

    loading.menu_sound.stop()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-50),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    gameover_bg = pygame.image.load(os.path.join(img_folder, 'gameover.jpg'))
    gameover_bg = pygame.transform.scale(gameover_bg, (x, y))
    gameover_rect = gameover_bg.get_rect()

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']
    for img in background_list:
        if img == 'background1.jpg':
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x + 100, y))
            background_images.append(bd)
        else:
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x, y))
            background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    all_sprites = pygame.sprite.Group()
    shotgun_fly = pygame.sprite.Group()
    vaders_group = pygame.sprite.Group()
    drobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    buttons = pygame.sprite.Group()

    if ship_gunner:
        player = character.Gunner(all_sprites, bullets)
    elif ship_player:
        player = character.Player(sprites, key_btn, mouse_btn, ju, sh, equip, all_sprites, bullets, drobs)
    inv = inventar.Inventar()
    shotgun = icons.Icon_sh()
    shotgun_big = icons.Icon_sh_big()
    rifle = icons.Icon_ju()
    rifle_big = icons.Icon_ju_big()
    all_sprites.add(player)
    for i in range(28):
        imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses, speed_enem,
                                count_bosses, all_sprites)
        all_sprites.add(imp)
        vaders_group.add(imp)
    sh = 0
    ju = 1
    sh_fly = False
    score = 0
    a = True
    count = 700
    count_loose = 0
    count_win = 1
    equip = 0
    gameover = False
    waiting = False
    FPS = 60

    all_sprites.add(inv)
    all_sprites.add(rifle_big)

    loading.ready.play()
    for i in [3, 2, 1, 0]:
        screen.blit(random_background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        draw_text(screen, str(max_score), 30, x - 200, 40)
        draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
        if i == 0:
            pygame.mixer.music.load(os.path.join(snd_folder, 'speed.mp3'))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
            draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
        else:
            draw_text(screen, str(i), 500, x // 2, 70)
        pygame.display.flip()
        time.sleep(1)

    pygame.event.clear()

    def stop():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    loading.pause_snd.play(-1)

                    btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                    btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
                    btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                    buttons.add(btn_quit)
                    buttons.add(btn_menu)
                    buttons.add(btn_start)

                    waiting = True
                    while waiting:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    waiting = False
                        buttons.update()
                        buttons.draw(screen)
                        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                  btn_quit.rect.y)
                        draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                  btn_menu.rect.y)
                        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                  btn_start.rect.y)
                        pygame.display.flip()
                        pygame.display.update()

                    loading.pause_snd.stop()
                    pygame.mixer.music.unpause()

    while a:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if (key[pygame.K_DOWN]) and (FPS >= 2):
            FPS -= 1
        if key[pygame.K_UP]:
            FPS += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_score()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

                    pygame.mixer.music.pause()
                    loading.pause_snd.play(-1)

                    btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                    btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
                    btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                    buttons.add(btn_quit)
                    buttons.add(btn_menu)
                    buttons.add(btn_start)

                    waiting = True
                    while waiting:
                        clock.tick(10)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    waiting = False
                        buttons.update()
                        buttons.draw(screen)
                        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                  btn_quit.rect.y)
                        draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                  btn_menu.rect.y)
                        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                  btn_start.rect.y)
                        pygame.display.flip()
                        pygame.display.update()

                    loading.pause_snd.stop()
                    pygame.mixer.music.unpause()

                elif event.key == pygame.K_g:
                    functions.god()

                if key_btn == 1 and mouse_btn == 0:
                    if event.key == pygame.K_2:
                        if equip == 1:
                            if sh != 1:
                                random.choice(loading.reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)
                    elif event.key == pygame.K_1:
                        if equip == 1:
                            if ju != 1:
                                random.choice(loading.reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_btn == 1 and key_btn == 0:
                    if event.button == 4:
                        if equip == 1:
                            if ju != 1:
                                random.choice(loading.reload_sounds).play()
                                ju = 1
                                sh = 0
                                all_sprites.add(shotgun)
                                all_sprites.remove(shotgun_big)
                                all_sprites.add(rifle_big)
                                all_sprites.remove(rifle)
                    elif event.button == 5:
                        if equip == 1:
                            if sh != 1:
                                random.choice(loading.reload_sounds).play()
                                sh = 1
                                ju = 0
                                all_sprites.add(shotgun_big)
                                all_sprites.remove(shotgun)
                                all_sprites.remove(rifle_big)
                                all_sprites.add(rifle)

        count -= 1
        draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
        pygame.display.flip()

        if gameover:
            current_score()
            achievment.deathes()
            best_score()

            for i in vaders_group:
                key = pygame.key.get_pressed()
                if (key[pygame.K_DOWN]) and (FPS >= 2):
                    FPS -= 1
                if key[pygame.K_UP]:
                    FPS += 1
                loading.boom_snd.play()
                if random.randint(1, 2) == 1:
                    expl = explosions.Explosion(i.rect.center, 'lg')
                    all_sprites.add(expl)
                else:
                    expl = explosions.Explosion(i.rect.center, 'lg', 2)
                    all_sprites.add(expl)
                screen.blit(gameover_bg, gameover_rect)
                all_sprites.update()
                i.kill()
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                draw_text(screen, str(max_score), 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                stop()
                pygame.display.flip()

            loading.boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(player.rect.center, 'hu')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(player.rect.center, 'hu', 2)
                all_sprites.add(expl)
            all_sprites.update()
            player.kill()
            all_sprites.draw(screen)
            draw_text(screen, 'Счёт:', 30, x // 2, 10)
            draw_text(screen, str(score), 30, x // 2, 40)
            draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
            draw_text(screen, str(max_score), 30, x - 200, 40)
            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
            draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
            all_sprites.update()
            stop()

            while gameover:
                clock.tick(FPS)
                key = pygame.key.get_pressed()
                if (key[pygame.K_DOWN]) and (FPS >= 2):
                    FPS -= 1
                if key[pygame.K_UP]:
                    FPS += 1
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:

                            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

                            pygame.mixer.music.pause()
                            loading.pause_snd.play(-1)

                            btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
                            btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
                            btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Продолжить', pause)
                            buttons.add(btn_quit)
                            buttons.add(btn_menu)
                            buttons.add(btn_start)

                            waiting = True
                            while waiting:
                                clock.tick(10)
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            waiting = False
                                buttons.update()
                                buttons.draw(screen)
                                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                                          btn_quit.rect.y)
                                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                                          btn_menu.rect.y)
                                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                                          btn_start.rect.y)
                                pygame.display.flip()
                                pygame.display.update()

                            loading.pause_snd.stop()
                            pygame.mixer.music.unpause()
                        elif event.key == pygame.K_TAB:
                            gameover = False

                screen.blit(gameover_bg, gameover_rect)
                draw_text(screen, 'Нажмите "TAB", чтобы продолжить', x // 30, x // 2, y - 300)
                all_sprites.update()
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                draw_text(screen, str(max_score), 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                pygame.display.flip()

            pygame.mixer.music.stop()

            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            buttons = pygame.sprite.Group()

            if ship_gunner:
                player = character.Gunner(all_sprites, bullets)
            elif ship_player:
                player = character.Player(sprites, key_btn, mouse_btn, ju, sh, equip, all_sprites, bullets, drobs)
            inv = inventar.Inventar()
            shotgun = icons.Icon_sh()
            shotgun_big = icons.Icon_sh_big()
            rifle = icons.Icon_ju()
            rifle_big = icons.Icon_ju_big()
            all_sprites.add(player)
            for i in range(28):
                imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses,
                                        speed_enem, count_bosses, all_sprites)
                all_sprites.add(imp)
                vaders_group.add(imp)
            sh = 0
            ju = 1
            sh_fly = False
            score = 0
            a = True
            count = 700
            count_loose = 0
            count_win = 1
            equip = 0
            gameover = False
            waiting = False
            FPS = 60

            all_sprites.add(inv)
            all_sprites.add(rifle_big)

            loading.ready.play()
            for i in [3, 2, 1, 0]:
                screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                draw_text(screen, str(max_score), 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                if i == 0:
                    pygame.mixer.music.load(os.path.join(snd_folder, 'speed.mp3'))
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()

        if count == 0 and score < 200 * count_win:
            gameover = True

        elif count == 0 and score >= 200 * count_win:
            count_win += 1
            count_loose += 1
            count = 700 - (100 * count_loose)
            pygame.display.flip()

        if count_loose == 7 and score >= 1400:
            pygame.mixer.music.stop()
            current_score()
            best_score()

            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
            draw_text(screen, 'Поздравляем! Вы ВЫИГРАЛИ!!!', x // 23, x // 2, y // 2)
            pygame.display.flip()

            loading.win.play(-1)
            draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)

            pygame.mixer.music.pause()

            btn_quit = button.Buttonpy(x // 2 - 84, 468, 170, 70, screen, 'Выход', super_break)
            btn_menu = button.Buttonpy(x // 2 - 150, 378, 300, 70, screen, 'В меню', preview)
            btn_start = button.Buttonpy(x // 2 - 180, 288, 360, 70, screen, 'Рестарт', pause)
            buttons.add(btn_quit)
            buttons.add(btn_menu)
            buttons.add(btn_start)

            waiting = True
            while waiting:
                clock.tick(FPS)
                key = pygame.key.get_pressed()
                if (key[pygame.K_DOWN]) and (FPS >= 2):
                    FPS -= 1
                if key[pygame.K_UP]:
                    FPS += 1
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            waiting = False
                buttons.update()
                buttons.draw(screen)
                draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2,
                            btn_quit.rect.y)
                draw_text(screen, btn_menu.text, 40, btn_menu.rect.x + btn_menu.width // 2,
                            btn_menu.rect.y)
                draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2,
                            btn_start.rect.y)
                pygame.display.flip()
                pygame.display.update()

            loading.win.stop()

            random_background = random.choice(background_images)

            all_sprites = pygame.sprite.Group()
            shotgun_fly = pygame.sprite.Group()
            vaders_group = pygame.sprite.Group()
            drobs = pygame.sprite.Group()
            buttons = pygame.sprite.Group()

            if ship_gunner:
                player = character.Gunner(all_sprites, bullets)
            elif ship_player:
                player = character.Player(sprites, key_btn, mouse_btn, ju, sh, equip, all_sprites, bullets, drobs)
            inv = inventar.Inventar()
            shotgun = icons.Icon_sh()
            shotgun_big = icons.Icon_sh_big()
            rifle = icons.Icon_ju()
            rifle_big = icons.Icon_ju_big()
            all_sprites.add(player)
            for i in range(28):
                imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses,
                                        speed_enem, count_bosses, all_sprites)
                all_sprites.add(imp)
                vaders_group.add(imp)
            sh = 0
            ju = 1
            sh_fly = False
            score = 0
            a = True
            count = 700
            count_loose = 0
            count_win = 1
            equip = 0
            gameover = False
            waiting = False

            all_sprites.add(inv)
            all_sprites.add(rifle_big)

            loading.ready.play()
            for i in [3, 2, 1, 0]:
                screen.blit(random_background, background_rect)
                all_sprites.draw(screen)
                draw_text(screen, 'Счёт:', 30, x // 2, 10)
                draw_text(screen, str(score), 30, x // 2, 40)
                draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
                draw_text(screen, str(max_score), 30, x - 200, 40)
                draw_text(screen, 'Таймер: ' + str(count), 30, 150, 20)
                draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
                if i == 0:
                    pygame.mixer.music.load(os.path.join(snd_folder, 'speed.mp3'))
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    draw_text(screen, 'Стреляй!', x // 6, x // 2, 250)
                else:
                    draw_text(screen, str(i), 500, x // 2, 70)
                pygame.display.flip()
                time.sleep(1)

            pygame.event.clear()

        if score >= 50:
            if random.random() > 0.99:
                if not shotgun_fly and equip != 1:
                    sh_fly = support.Fly_sh()
                    all_sprites.add(sh_fly)
                    shotgun_fly.add(sh_fly)

        if sh_fly:
            boom_sh_fly = pygame.sprite.spritecollide(player, shotgun_fly, True, pygame.sprite.collide_circle)
            if boom_sh_fly:
                random.choice(loading.reload_sounds).play()
                equip = 1
                ju = 0
                sh = 1
                all_sprites.add(shotgun_big)
                all_sprites.remove(shotgun)
                all_sprites.remove(rifle_big)
                all_sprites.add(rifle)

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True)
        boom_sh = pygame.sprite.groupcollide(vaders_group, drobs, False, False)
        boom = pygame.sprite.spritecollide(player, vaders_group, False, pygame.sprite.collide_circle)

        for hit in boom_b:
            score += 1
            loading.boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit.rect.center, 'lg', 2)
                all_sprites.add(expl)
            hit.rect.x = random.randrange(50, x - 70)
            hit.rect.y = random.randrange(-100, -30)
            hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit.rot_speed = random.randrange(-20, 20)

        for hit2 in boom_sh:
            score += 1
            loading.boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit2.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit2.rect.center, 'lg', 2)
                all_sprites.add(expl)
            hit2.rect.x = random.randrange(50, x - 70)
            hit2.rect.y = random.randrange(-100, -30)
            hit2.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit2.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit2.rot_speed = random.randrange(-20, 20)

        for hit4 in boom:
            loading.metal.play()
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit4.rect.center, 'sm', 2)
                all_sprites.add(expl)
            hit4.rect.x = random.randrange(50, x - 70)
            hit4.rect.y = random.randrange(-100, -30)
            hit4.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit4.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit4.rot_speed = random.randrange(-20, 20)

        screen.blit(random_background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        draw_text(screen, 'Счёт:', 30, x // 2, 10)
        draw_text(screen, str(score), 30, x // 2, 40)
        draw_text(screen, 'Лучший результат:', 30, x - 200, 10)
        draw_text(screen, str(max_score), 30, x - 200, 40)
        draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))
        pygame.display.flip()
    return


def preview():
    functions.hardmode = False
    achievment.success()
    functions.newplayer()
    global all_sprites, drobs, bullets, vaders_group, bosses

    loading.pause_snd.play(-1)
    loading.pause_snd.stop()

    loading.menu_sound.play(-1)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((x, y-27),pygame.HWSURFACE|pygame.DOUBLEBUF)

    background_images = []
    background_list = ['background1.jpg', 'background2.jpg', 'background3.jpg']
    for img in background_list:
        if img == 'background1.jpg':
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x + 100, y))
            background_images.append(bd)
        else:
            bd = pygame.image.load(os.path.join(img_folder, img))
            bd = pygame.transform.scale(bd, (x, y))
            background_images.append(bd)
    for img in background_images:
        background_rect = img.get_rect()

    random_background = random.choice(background_images)

    def player_player():
        global ship_player, ship_gunner
        ship_player = True
        ship_gunner = False
        start()

    def player_gunner():
        global ship_player, ship_gunner
        ship_player = False
        ship_gunner = True
        start()

    def characters():
        btn_player.change(x // 3, y // 2, 'ВЫББЕРИТЕ ПЕРСОНАЖА', player_player)
        if (functions.newgunner == 0) or (functions.newgunner == 1):
            btn_gunner.change(x // 2, y // 2, 'ВЫББЕРИТЕ ПЕРСОНАЖА')
        elif functions.newgunner == 2:
            btn_gunner.change(x // 2, y // 2, 'ВЫББЕРИТЕ ПЕРСОНАЖА', player_gunner)

    def start():
        def changes():
            btn_start.function = functions.hardgame(game)

        btn_player.change(x + 1000, y // 2, ' ')
        btn_gunner.change(x + 1000, y // 2, ' ')
        btn_start.change(0, 0, 440)
        btn_start.change(x // 2 - btn_start.width // 2, y - 120, 440, 70, 'Сложный режим', changes)
        btn_option.change(btn_start.rect.x + btn_start.width, y - 120, 440, 70, 'Режим таймера', kill_or_die)
        btn_quit.change(btn_start.rect.x - btn_start.width, y - 120, 440, 70, 'Лёгкий режим', game)

    def back():
        btn_player.change(x + 1000, y // 2, ' ')
        btn_gunner.change(x + 1000, y // 2, ' ')
        btn_quit.change(x // 4, y - 120, 170, 70, 'Выход', super_break)
        btn_start.change(btn_quit.rect.x + btn_quit.width, y - 120, 300, 70, 'Старт', characters)
        btn_option.change(btn_quit.rect.x + btn_quit.width + btn_start.width, y - 120, 190, 70, 'Опции', settings)

    vaders_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    for i in range(25):
        imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses, speed_enem, count_bosses, all_sprites)
        all_sprites.add(imp)
        vaders_group.add(imp)

    npc = character.Npc(all_sprites, bullets, sprites)

    btn_quit = button.Buttonpy(x // 4, y - 120, 170, 70, screen, 'Выход', super_break)
    btn_start = button.Buttonpy(btn_quit.rect.x + btn_quit.width, y - 120, 300, 70, screen, 'Старт', characters)
    btn_option = button.Buttonpy(btn_quit.rect.x + btn_quit.width + btn_start.width, y - 120, 190, 70, screen, 'Опции',
                                 settings)
    btn_player = button.ButtonPlayer(x + 1000, y // 2, screen, 'player', ' ', start)
    btn_gunner = button.ButtonPlayer(x + 1000, y // 2, screen, 'gunner', ' ', start)
    all_sprites.add(btn_player)
    all_sprites.add(btn_gunner)

    all_sprites.add(npc)

    all_sprites.add(btn_quit)
    all_sprites.add(btn_start)
    all_sprites.add(btn_option)
    all_sprites.add(btn_player)
    all_sprites.add(btn_gunner)

    clock = pygame.time.Clock()

    FPS = 60

    while True:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if (key[pygame.K_DOWN]) and (FPS >= 2):
            FPS -= 1
        if key[pygame.K_UP]:
            FPS += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                    return
                if event.key == pygame.K_e:
                    pygame.time.delay(200)
                    back()
                if event.key == pygame.K_q:
                    achievment.achievements()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    for i in vaders_group:
                        loading.boom_snd.play()
                        if random.randint(1, 2) == 1:
                            expl = explosions.Explosion(i.rect.center, 'lg')
                            all_sprites.add(expl)
                        else:
                            expl = explosions.Explosion(i.rect.center, 'lg', 2)
                            all_sprites.add(expl)
                        i.rect.x = random.randrange(50, x - 70)
                        i.rect.y = random.randrange(-100, -30)
                        i.speedy_imp = random.randrange(speed_enem + count_bosses // 3,
                                                        speed_enem * 3 + count_bosses // 2)
                        i.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3,
                                                        speed_enem + count_bosses // 3)
                        i.rot_speed = random.randrange(-20, 20)
                    loading.boom_snd.play()
                    bullets = pygame.sprite.Group()
                    npc.kill()
                    if random.randint(1, 2) == 1:
                        expl = explosions.Explosion(npc.rect.center, 'hu')
                        all_sprites.add(expl)
                    else:
                        expl = explosions.Explosion(npc.rect.center, 'hu', 2)
                        all_sprites.add(expl)
                    npc = character.Npc(all_sprites, bullets, sprites)
                    all_sprites.add(npc)

        boom_b = pygame.sprite.groupcollide(vaders_group, bullets, False, True, pygame.sprite.collide_circle)
        boom = pygame.sprite.spritecollide(npc, vaders_group, False, pygame.sprite.collide_circle)

        for hit in boom_b:
            loading.boom_snd.play()
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit.rect.center, 'lg', 2)
                all_sprites.add(expl)
            hit.rect.x = random.randrange(50, x - 70)
            hit.rect.y = random.randrange(-100, -30)
            hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit.rot_speed = random.randrange(-20, 20)

        for hit4 in boom:
            loading.metal.play()
            if random.randint(1, 2) == 1:
                expl = explosions.Explosion(hit4.rect.center, 'sm')
                all_sprites.add(expl)
            else:
                expl = explosions.Explosion(hit4.rect.center, 'sm', 2)
                all_sprites.add(expl)
            hit4.rect.x = random.randrange(50, x - 70)
            hit4.rect.y = random.randrange(-100, -30)
            hit.speedy_imp = random.randrange(speed_enem + count_bosses // 3, speed_enem * 3 + count_bosses // 2)
            hit.speedx_imp = random.randrange(-speed_enem * 2 - count_bosses // 3, speed_enem + count_bosses // 3)
            hit4.rot_speed = random.randrange(-20, 20)

        screen.blit(random_background, background_rect)

        all_sprites.update()
        all_sprites.draw(screen)

        draw_text(screen, btn_quit.text, 40, btn_quit.rect.x + btn_quit.width // 2, btn_quit.rect.y)
        draw_text(screen, btn_start.text, 40, btn_start.rect.x + btn_start.width // 2, btn_start.rect.y)
        draw_text(screen, btn_option.text, 40, btn_option.rect.x + btn_option.width // 2, btn_option.rect.y)
        draw_text(screen, btn_gunner.text, 50, x // 2, y // 3)

        draw_text(screen, '"ESC": выход', 20, x - 100, 70)
        draw_text(screen, '"E": назад', 20, 100, 70)
        draw_text(screen, '"Q": достижения', 20, 110, 130)

        draw_text(screen, 'FPS: ' + str(FPS), 30, x - 100, 130, (255, 0, 0))

        pygame.display.flip()
        pygame.display.update()
    return


def draw_text(surf, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def current_score():
    with open('scriptspy\papers\score.txt', 'a') as file:
        file.write(str(score) + ' ')


def delete_cash(arg_score, arg_death, arg_player):
    if arg_score == score:
        with open('scriptspy\papers\score.txt', 'wb'):
            pass
    if arg_death == achievment.gameovers:
        with open('scriptspy\papers\deathes.txt', 'wb'):
            pass
    if arg_player == functions.newgunner:
        with open('scriptspy\papers\gunner.txt', 'wb'):
            pass


def super_break():
    current_score()
    pygame.quit()
    sys.exit()


count1 = 1


def sprite():
    loading.spacebar_snd.play()
    global sprites
    global count1
    global button_sprites

    count1 += 1
    if count1 % 2 == 0 and count1 != 0:
        button_sprites['text'] = 'Да'
        sprites = True
    else:
        button_sprites['text'] = 'Нет'
        sprites = False

    return sprites, button_sprites


def keyboard():
    loading.spacebar_snd.play()
    global mouse_btn
    global key_btn
    key_btn = 1
    mouse_btn = 0
    return key_btn, mouse_btn


def mouse():
    loading.spacebar_snd.play()
    global mouse_btn
    global key_btn
    key_btn = 0
    mouse_btn = 1
    return key_btn, mouse_btn


def speed():
    global speed_enem
    speed_enem = int(scale1.get())
    return speed_enem


def skins():
    loading.spacebar_snd.play()
    global jelly, putin, virus, vaders, death

    if var.get() == 0:
        vaders = False
        jelly = True
        virus = False
        putin = False
        death = False
    elif var.get() == 1:
        vaders = False
        putin = True
        virus = False
        jelly = False
        death = False
    elif var.get() == 2:
        vaders = False
        virus = True
        putin = False
        jelly = False
        death = False
    elif var.get() == 3:
        vaders = True
        jelly = False
        virus = False
        putin = False
        death = False
    elif var.get() == 4:
        death = True
        vaders = False
        jelly = False
        virus = False
        putin = False
    return vaders, virus, putin, jelly, death


def reset():
    global vaders_group, all_sprites
    for i in vaders_group:
        i.kill()
    for i in range(25):
        imp = opponents.Imperia(jelly, putin, virus, vaders, death, sprites, bosses,
                                speed_enem, count_bosses, all_sprites)
        all_sprites.add(imp)
        vaders_group.add(imp)


def moving():
    loading.spacebar_snd.play()
    if key_btn == 1:
        messagebox.showinfo('Меню игры STAR WARS - THE JOKE',
                            'УПРАВЛЕНИЕ: \n W - вверх \n S - вниз \n A - влево \n D - вправо \n ПРОБЕЛ - стрелять \n "1" - переключить на первое оружие \n "2" - переключить на второе оружие \n "ESC" - пауза')
    elif mouse_btn == 1:
        messagebox.showinfo('Меню игры STAR WARS - THE JOKE',
                            'УПРАВЛЕНИЕ: \n Передвижение мышкой \n ЛЕВАЯ кнопка мыши - стрелять \n Переключать оружия КОЛЁСИКОМ мыши \n "ESC" - поставить / убрать паузу')
    return


def settings():
    global scale1
    global button_sprites
    global var

    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()+10, root.winfo_screenheight()+10))

    def destroy():
        speed()
        skins()
        reset()
        root.destroy()

    img_ram2 = ImageTk.PhotoImage(loading.img_ram, master=root)
    img_skull2 = ImageTk.PhotoImage(loading.img_skull2)
    img_keyb = ImageTk.PhotoImage(loading.img_key)
    img_keym = ImageTk.PhotoImage(loading.img_mouse)
    img_option2 = ImageTk.PhotoImage(loading.img_option)
    img_vader4 = ImageTk.PhotoImage(loading.img1)
    img_putin = ImageTk.PhotoImage(loading.putin1)
    img_virus = ImageTk.PhotoImage(loading.virus1)
    img_vaders = ImageTk.PhotoImage(loading.img_vader_tk)

    canvas = Canvas(root, width=x+10, height=y+10, bg='black')
    canvas.pack()

    canvas.create_image(x//2, y//2-25, image=img_ram2)

    text = canvas.create_text(270, 20, font=("Comic Sans MS", 15), text="Минимальная скорость врагов(по умолчанию 4)", fill="#dceca4")
    scale1 = Scale(canvas, orient=HORIZONTAL, length=700, from_=1, to=25, tickinterval=1, resolution=1, bg='black', fg='#dceca4')
    scale1.place(x=0, y=35)
    canvas.create_image(17, 20, image=img_option2)

    text = canvas.create_text(190, 140, font=("Comic Sans MS", 15), text="Включать прорисовку спрайтов", fill="#dceca4")
    if sprites:
        button_sprites = Button(text="Да", command=sprite)
        button_sprites.place(x=350, y=130)
        button_sprites['bg'] = '#dceca4'
        button_sprites['activebackground'] = 'black'
        button_sprites['fg'] = 'black'
        button_sprites['activeforeground'] = '#dceca4'
    else:
        button_sprites = Button(root, text='Нет', command=sprite)
        button_sprites.place(x=350, y=130)
        button_sprites['bg'] = '#dceca4'
        button_sprites['activebackground'] = 'black'
        button_sprites['fg'] = 'black'
        button_sprites['activeforeground'] = '#dceca4'
    canvas.create_image(17, 140, image=img_option2)

    text = canvas.create_text(160, 220, font=("Comic Sans MS", 15), text="Изображения для врагов", fill="#dceca4")
    canvas.create_image(17, 220, image=img_option2)
    canvas.create_image(60, 280, image=img_vader4)
    canvas.create_image(148, 280, image=img_putin)
    canvas.create_image(238, 280, image=img_virus)
    canvas.create_image(326, 280, image=img_vaders)
    if achievment.gameovers >= 50:
        canvas.create_image(420, 280, image=img_skull2)
    var = IntVar()
    var.set(3)
    radio = Radiobutton(root, variable=var, value=0)
    radio.place(x=45, y=325)
    radio = Radiobutton(root, variable=var, value=1)
    radio.place(x=135, y=325)
    radio = Radiobutton(root, variable=var, value=2)
    radio.place(x=225, y=325)
    radio = Radiobutton(root, variable=var, value=3)
    radio.place(x=315, y=325)
    if achievment.gameovers >= 50:
        radio = Radiobutton(root, variable=var, value=4)
        radio.place(x=404, y=325)

    text = canvas.create_text(135, 410, font=("Comic Sans MS", 15), text="Способ управления", fill="#dceca4")
    canvas.create_image(17, 410, image=img_option2)
    buttonkey = Button(command=keyboard, image=img_keyb)
    buttonkey.place(x=30, y=460)
    buttonmouse = Button(command=mouse, image=img_keym)
    buttonmouse.place(x=140, y=460)

    text = canvas.create_text(270, 610, font=("Comic Sans MS", 15), text="Здесь можно посмотреть текущее управление", fill="#dceca4")
    canvas.create_image(17, 610, image=img_option2)
    button = Button(text="Здесь", command=moving, font=("Comic Sans MS", 10))
    button.place(x=55, y=630)
    button['bg'] = '#dceca4'
    button['activebackground'] = 'black'
    button['fg'] = 'black'
    button['activeforeground'] = '#dceca4'

    d = Button(text="Подтведить эти изменения", command=destroy, font=("Comic Sans MS", 14))
    d.place(x=20, y=y-100)
    d['bg'] = '#dceca4'
    d['activebackground'] = 'black'
    d['fg'] = 'black'
    d['activeforeground'] = '#dceca4'

    root.overrideredirect(1)
    root.attributes("-topmost", True)
    root.update()
    root.deiconify()
    root.mainloop()
    return


def windows():
    global x, y
    window = Tk()
    x = window.winfo_screenwidth()
    y = window.winfo_screenheight() + 50
    window.destroy()


windows()
preview()
