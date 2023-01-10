import sys
import pygame

if __name__ == "__main__":

    """
    Game of Goats and Cabbages
    Rules equal to ones in Missionaries and Cannibals.
    If Goats outnumber cabbages - rip.
    """
    def getkey():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(window, "game-over.png")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit()
                if event.key in controls:
                    key = controls[event.key]
                    return key

    def ferry(who, step):
        """
        movement of the "boat" and our characters
        """
        done = False
        for actor in who:
            actor["rect"] = actor["rect"].move((step, 0))
            if not arena.contains(actor["rect"]):
                actor["rect"] = actor["rect"].move((-step, 0))
                actor["surf"] = pygame.transform.flip(actor["surf"], True, False)
                done = True
        return done

    def failure():
        """
        Lost game - goats oytnumbered cabbages
        """
        myfont = pygame.font.Font('freesansbold.ttf', 48)
        msg = myfont.render("Failure", True, (255, 0, 0))
        msg_box = msg.get_rect()
        msg_box.center = arena.center
        window.blit(msg, msg_box)
        pygame.display.flip()
        pygame.time.wait(1000)

    def success():
        """
        succesfully finished game
        """
        myfont = pygame.font.Font('freesansbold.ttf', 48)
        msg = myfont.render("Success", True, (0, 0, 255))
        msg_box = msg.get_rect()
        msg_box.center = arena.center
        window.blit(msg, msg_box)
        pygame.display.flip()
        pygame.time.wait(1000)

    pygame.init()
    window = pygame.display.set_mode((640, 480))
    arena = window.get_rect()

    goat0 = {"file": "goat.png"}
    goat1 = {"file": "goat.png"}
    goat2 = {"file": "goat.png"}
    cabb = {"file": "cabb.png"}
    cabb1 = {"file": "cabb.png"}
    cabb2 = {"file": "cabb.png"}
    farm = {"file": "farm.png"}
    cabbages = [cabb, cabb1, cabb2]
    goats = [goat0, goat1, goat2]
    actors = [goat0, goat1, goat2, cabb, cabb1, cabb2, farm]

    """
    Welcome screen and instruction
    """
    black = (0, 0, 0)
    end_it = False
    while (end_it == False):
        window.fill(black)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Welcome to Goats and Cabbages.", 1, (255, 0, 0))
        n1label = myfont.render("Try shipping everything across the screen.", 1, (255, 0, 0))
        n2label = myfont.render("Outnumbered cabbages = you lose.", 1, (255, 0, 0))
        n3label = myfont.render("Press any key to Continue.", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                end_it=True
        window.blit(nlabel,(100,90))
        window.blit(n1label,(10,150))
        window.blit(n2label,(10,190))
        window.blit(n3label,(10,330))
        pygame.display.flip()
    end_it = False
    while (end_it == False): 
        window.fill(black)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Q(1), A(2), Z(3) - single cabbages", 1, (255, 0, 0))
        n1label = myfont.render("W(1), S(2), X(3) - single goats", 1, (255, 0, 0))
        n2label = myfont.render("Y(1,2), H(1,3), N(2,3) - double cabbages", 1, (255, 0, 0))
        n3label = myfont.render("U(1,2), J(1,3), M(2,3) - double goats", 1, (255, 0, 0))
        n4label = myfont.render("E(1,1), D(1,2), C(1,3) - cabbage(1) and a goat", 1, (255, 0, 0))
        n5label = myfont.render("R(2,1), F(2,2), V(2,3) - cabbage(2) and a goat", 1, (255, 0, 0))
        n6label = myfont.render("T(3,1), G(3,1), B(3,3) - cabbage(3) and a goat", 1, (255, 0, 0))
        n7label = myfont.render("Any key to start a game.", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                end_it=True
        window.blit(nlabel,(10,10))
        window.blit(n1label,(10,50))
        window.blit(n2label,(10,90))
        window.blit(n3label,(10,130))
        window.blit(n4label,(10,170))
        window.blit(n5label,(10,210))
        window.blit(n6label,(10,250))
        window.blit(n6label,(10,290))
        window.blit(n7label,(150,380))
        pygame.display.flip()

    for i, actor in enumerate(actors):
        actor["surf"] = pygame.image.load(actor["file"])
        actor["rect"] = actor["surf"].get_rect()
        actor["rect"].midleft = (0, (i+1)*arena.height/8)

    gamegraph = {
                "cccgggf-": {"q": "ccggg-cf", "a": "ccggg-cf", "z": "ccggg-cf",
                    "y": "cggg-ccf", "h": "cggg-ccf", "n": "cggg-ccf",
                    "w": "cccgg-gf", "s": "cccgg-gf", "x": "cccgg-gf",
                    "u": "cccg-ggf", "j": "cccg-ggf", "m": "cccg-ggf",
                    "e": "ccgg-cgf", "d": "ccgg-cgf", "c": "ccgg-cgf",
                    "r": "ccgg-cgf", "f": "ccgg-cgf", "v": "ccgg-cgf",
                    "t": "ccgg-cgf", "g": "ccgg-cgf", "b": "ccgg-cgf"},
                "cccgg-gf": {"w": "cccgggf-", "s": "cccgggf-", "x": "cccgggf-"},
                "ccgg-cgf": {"q": "cccggf-g", "a": "cccggf-g", "z": "cccggf-g",
                    "w": "ccgggf-c", "s": "ccgggf-c", "x": "ccgggf-c",
                    "e": "cccgggf-", "d": "cccgggf-", "c": "cccgggf-",
                    "r": "cccgggf-", "f": "cccgggf-", "v": "cccgggf-",
                    "t": "cccgggf-", "g": "cccgggf-", "b": "cccgggf-"},
                "cccggf-g": {"q": "ccgg-cgf", "a": "ccgg-cgf", "z": "ccgg-cgf",
                    "y": "cgg-ccgf", "h": "cgg-ccgf", "n": "cgg-ccgf",
                    "w": "cccg-ggf", "s": "cccg-ggf", "x": "cccg-ggf",
                    "u": "ccc-gggf", "j": "ccc-gggf", "m": "ccc-gggf",
                    "e": "ccg-cggf", "d": "ccg-cggf", "c": "ccg-cggf",
                    "r": "ccg-cggf", "f": "ccg-cggf", "v": "ccg-cggf",
                    "t": "ccg-cggf", "g": "ccg-cggf", "b": "ccg-cggf"},
                "cccg-ggf": {"w": "cccggf-g", "s": "cccggf-g", "x": "cccggf-g",
                    "u": "cccgggf-", "j": "cccgggf-", "m": "cccgggf-"},
                "ccc-gggf": {"w": "cccgf-gg", "s": "cccgf-gg", "x": "cccgf-gg",
                    "u": "cccggf-g", "j": "cccggf-g", "m": "cccggf-g"},
                "cccgf-gg": {"q": "ccg-cggf", "a": "ccg-cggf", "z": "ccg-cggf",
                    "y": "cg-ccggf", "h": "cg-ccggf", "n": "cg-ccggf",
                    "w": "ccc-gggf", "s": "ccc-gggf", "x": "ccc-gggf",
                    "e": "cc-cgggf", "d": "cc-cgggf", "c": "cc-cgggf",
                    "r": "cc-cgggf", "f": "cc-cgggf", "v": "cc-cgggf",
                    "t": "cc-cgggf", "g": "cc-cgggf", "b": "cc-cgggf"},
                "cg-ccggf": {"q": "ccgf-cgg", "a": "ccgf-cgg", "z": "ccgf-cgg",
                    "y": "cccgf-gg", "h": "cccgf-gg", "n": "cccgf-gg",
                    "w": "cggf-ccg", "s": "cggf-ccg", "x": "cggf-ccg",
                    "u": "cgggf-cc", "j": "cgggf-cc", "m": "cgggf-cc",
                    "e": "ccggf-cg", "d": "ccggf-cg", "c": "ccggf-cg",
                    "r": "ccggf-cg", "f": "ccggf-cg", "v": "ccggf-cg",
                    "t": "ccggf-cg", "g": "ccggf-cg", "b": "ccggf-cg"},
                "ccggf-cg": {"q": "cgg-ccgf", "a": "cgg-ccgf", "z": "cgg-ccgf",
                    "y": "gg-cccgf", "h": "gg-cccgf", "n": "gg-cccgf",
                    "w": "ccg-cggf", "s": "ccg-cggf", "x": "ccg-cggf",
                    "u": "cc-cgggf", "j": "cc-cgggf", "m": "cc-cgggf",
                    "e": "cg-ccggf", "d": "cg-ccggf", "c": "cg-ccggf",
                    "r": "cg-ccggf", "f": "cg-ccggf", "v": "cg-ccggf",
                    "t": "cg-ccggf", "g": "cg-ccggf", "b": "cg-ccggf"},
                "gg-cccgf": {"q": "cggf-ccg", "a": "cggf-ccg", "z": "cggf-ccg",
                    "y": "ccggf-cg", "h": "ccggf-cg", "n": "ccggf-cg",
                    "w": "gggf-ccc", "s": "gggf-ccc", "x": "gggf-ccc",
                    "e": "cgggf-cc", "d": "cgggf-cc", "c": "cgggf-cc",
                    "r": "cgggf-cc", "f": "cgggf-cc", "v": "cgggf-cc",
                    "t": "cgggf-cc", "g": "cgggf-cc", "b": "cgggf-cc"},
                "gggf-ccc": {"w": "gg-cccgf", "s": "gg-cccgf", "x": "gg-cccgf",
                    "u": "g-cccggf", "j": "g-cccggf", "m": "g-cccggf"},
                "g-cccggf": {"q": "cgf-ccgg", "a": "cgf-ccgg", "z": "cgf-ccgg",
                    "y": "ccgf-cgg", "h": "ccgf-cgg", "n": "ccgf-cgg",
                    "w": "ggf-cccg", "s": "ggf-cccg", "x": "ggf-cccg",
                    "u": "gggf-ccc", "j": "gggf-ccc", "m": "gggf-ccc",
                    "e": "cggf-ccg", "d": "cggf-ccg", "c": "cggf-ccg",
                    "r": "cggf-ccg", "f": "cggf-ccg", "v": "cggf-ccg",
                    "t": "cggf-ccg", "g": "cggf-ccg", "b": "cggf-ccg"},
                "cgf-ccgg": {"q": "g-cccggf", "a": "g-cccggf", "z": "g-cccggf",
                    "w": "c-ccgggf", "s": "c-ccgggf", "x": "c-ccgggf",
                    "e": "-cccgggf", "d": "-cccgggf", "c": "-cccgggf",
                    "r": "-cccgggf", "f": "-cccgggf", "v": "-cccgggf",
                    "t": "-cccgggf", "g": "-cccgggf", "b": "-cccgggf"},
                "ggf-cccg": {"w": "g-cccggf", "s": "g-cccggf", "x": "g-cccggf",
                    "u": "-cccgggf", "j": "-cccgggf", "m": "-cccgggf"},
                "ccf-cggg": "failure",
                "ccgf-cgg": "failure",
                "cggf-ccg": "failure",
                "cgggf-cc": "failure",
                "ccgggf-c": "failure",
                "cf-ccggg": "failure",
                "cc-cgggf": "failure",
                "ccg-cggf": "failure",
                "cgg-ccgf": "failure",
                "cggg-ccf": "failure",
                "ccggg-cf": "failure",
                "c-ccgggf": "failure",
                "-cccgggf": "success"}

    gamestate = "cccgggf-"
    controls = {pygame.K_q: "q", pygame.K_a: "a", pygame.K_z: "z",
        pygame.K_w: "w", pygame.K_s: "s", pygame.K_x: "x",
        pygame.K_e: "e", pygame.K_d: "d", pygame.K_c: "c",
        pygame.K_r: "r", pygame.K_f: "f", pygame.K_v: "v",
        pygame.K_t: "t", pygame.K_g: "g", pygame.K_b: "b",
        pygame.K_y: "y", pygame.K_h: "h", pygame.K_n: "n",
        pygame.K_u: "u", pygame.K_j: "j", pygame.K_m: "m"}
    passengers = {"q": [cabb, farm], "a": [cabb1, farm], "z": [cabb2, farm],
        "w": [goat0, farm], "s": [goat1, farm], "x": [goat2, farm],
        "e": [cabb, goat0, farm], "d": [cabb, goat1, farm], "c": [cabb, goat2, farm],
        "r": [cabb1, goat0, farm], "f": [cabb1, goat1, farm], "v": [cabb1, goat2, farm],
        "t": [cabb2, goat0, farm], "g": [cabb2, goat1, farm], "b": [cabb2, goat2, farm],
        "y": [cabb, cabb1, farm], "h": [cabb, cabb2, farm], "n": [cabb1, cabb2, farm],
        "u": [goat0, goat1, farm], "j": [goat0, goat2, farm], "m": [goat1, goat2, farm]}
    ferry_step = -5
    action = "listen"

    fpsClock = pygame.time.Clock()
    """
    main loop
    """
    while True:
        if action == "listen":
            key = getkey()
            if key in gamegraph[gamestate]:
                gamestate = gamegraph[gamestate][key]
                ferry_who = passengers[key]
                ferry_step = -ferry_step
                action = "ferry"

        if action == "ferry":
            done = ferry(ferry_who, ferry_step)
            if done:
                if gamegraph[gamestate] == "failure":
                    action = "failure"
                elif gamegraph[gamestate] == "success":
                    action = "success"
                else:
                    action = "listen"

        if action == "failure":
            failure()
            sys.exit()
        if action == "success":
            success()
            sys.exit()

        window.fill(pygame.Color("green"))
        for actor in actors:
            window.blit(actor["surf"], actor["rect"])

        pygame.display.flip()
        fpsClock.tick(120)
