#!/usr/bin/env python3

#!/usr/bin/env python3

import os, re

class ProcessStrangeNewWorlds:
    def __init__(self):
        self.SNWre1 = re.compile("Star.Trek.Strange.New.Worlds.")
        self.SNWre2 = re.compile("star.trek.strange.new.worlds.")
        self.SNWre3 = re.compile("STAR.TREK.STRANGE.NEW.WORLDS.")
        self.SNWre4 = re.compile("Star Trek Strange New Worlds. ")
        self.SNWre5 = re.compile("star trek strange new worlds. ")
        self.SNWre6 = re.compile("STAR TREK STRANGE NEW WORLDS. ")
        self.SNWcount = len("Star.Trek.Strange.New.Worlds.")

    def scan_file(self, filetup):
        s1 = re.search(self.SNWre1, filetup[1])
        s2 = re.search(self.SNWre2, filetup[1])
        s3 = re.search(self.SNWre3, filetup[1])
        s4 = re.search(self.SNWre4, filetup[1])
        s5 = re.search(self.SNWre5, filetup[1])
        s6 = re.search(self.SNWre6, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        elif s4 != None:
            return True
        elif s5 != None:
            return True
        elif s6 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Star Trek Strange New Worlds " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessObiWanKenobi:
    def __init__(self):
        self.OWKre1 = re.compile("Obi-Wan.Kenobi.")
        self.OWKre2 = re.compile("obi-wan.kenobi.")
        self.OWKre3 = re.compile("OBI-WAN.KENOBI.")
        self.OWKre4 = re.compile("Obi-Wan Kenobi ")
        self.OWKre5 = re.compile("obi-wan kenobi ")
        self.OWKre6 = re.compile("OBI-WAN KENOBI ")
        self.OWKre7 = re.compile("Obi-wan Kenobi ")
        self.OWKcount = len("Obi-Wan.Kenobi.")

    def scan_file(self, filetup):
        s1 = re.search(self.OWKre1, filetup[1])
        s2 = re.search(self.OWKre2, filetup[1])
        s3 = re.search(self.OWKre3, filetup[1])
        s4 = re.search(self.OWKre4, filetup[1])
        s5 = re.search(self.OWKre5, filetup[1])
        s6 = re.search(self.OWKre6, filetup[1])
        s7 = re.search(self.OWKre7, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        elif s4 != None:
            return True
        elif s5 != None:
            return True
        elif s6 != None:
            return True
        elif s7 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.OWKcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Obi-Wan Kenobi " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessOrville:
    def __init__(self):
        self.ORVre1 = re.compile("The.Orville.")
        self.ORVre2 = re.compile("the.orville")
        self.ORVre3 = re.compile("THE.ORVILLE.")
        self.ORVre4 = re.compile("The Orville ")
        self.ORVre5 = re.compile("THE ORVILLE ")
        self.ORVcount = len("The.Orville.")

    def scan_file(self, filetup):
        s1 = re.search(self.ORVre1, filetup[1])
        s2 = re.search(self.ORVre2, filetup[1])
        s3 = re.search(self.ORVre3, filetup[1])
        s4 = re.search(self.ORVre4, filetup[1])
        s5 = re.search(self.ORVre5, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        elif s4 != None:
            return True
        elif s5 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.ORVcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/The Orville " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessMsMarvel:
    def __init__(self):
        self.MMre1 = re.compile("Ms.Marvel.")
        self.MMre2 = re.compile("ms.marvel.")
        self.MMre3 = re.compile("MS.MARVEL.")
        self.MMre4 = re.compile("Ms Marvel ")
        self.MMre5 = re.compile("ms marvel ")
        self.MMre6 = re.compile("MS MARVEL ")
        self.MMcount = len("Ms.Marvel.")

    def scan_file(self, filetup):
        s1 = re.search(self.MMre1, filetup[1])
        s2 = re.search(self.MMre2, filetup[1])
        s3 = re.search(self.MMre3, filetup[1])
        s4 = re.search(self.MMre4, filetup[1])
        s5 = re.search(self.MMre5, filetup[1])
        s6 = re.search(self.MMre6, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        elif s4 != None:
            return True
        elif s5 != None:
            return True
        elif s6 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.MMcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Ms Marvel " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessForAllMankind:
    def __init__(self):
        self.FAMKre1 = re.compile("For.All.Mankind.")
        self.FAMKre2 = re.compile("for.all.mankind.")
        self.FAMKre3 = re.compile("FOR.ALL.MANKIND.")
        self.FAMKre4 = re.compile("For All Mankind ")
        self.FAMKre5 = re.compile("for all mankind ")
        self.FAMKre6 = re.compile("FOR ALL MANKIND ")
        self.FAMKcount = len("For.All.Mankind.")

    def scan_file(self, filetup):
        s1 = re.search(self.FAMKre1, filetup[1])
        s2 = re.search(self.FAMKre2, filetup[1])
        s3 = re.search(self.FAMKre3, filetup[1])
        s4 = re.search(self.FAMKre4, filetup[1])
        s5 = re.search(self.FAMKre5, filetup[1])
        s6 = re.search(self.FAMKre6, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        elif s4 != None:
            return True
        elif s5 != None:
            return True
        elif s6 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.FAMKcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/For All Mankind " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessIAmGroot:
    def __init__(self):
        self.IAGre1 = re.compile("I.Am.Groot.")
        self.IAGre2 = re.compile("i.am.groot.")
        self.IAGcount = len("I.Am.Groot.")

    def scan_file(self, filetup):
        s1 = re.search(self.IAGre1, filetup[1])
        s2 = re.search(self.IAGre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.IAGcount:]
            print(raw)
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/I Am Groot " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessLowerDecks:
    def __init__(self):
        self.SNWre1 = re.compile("Star.Trek.Lower.Decks.")
        self.SNWre2 = re.compile("star.trek.lower.decks.")
        self.SNWcount = len("Star.Trek.Lower.Decks.")

    def scan_file(self, filetup):
        s1 = re.search(self.SNWre1, filetup[1])
        s2 = re.search(self.SNWre2, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Star Trek Lower Decks " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessHouseOfTheDragon:
    def __init__(self):
        self.LDre1 = re.compile("Dragon.")
        self.LDre2 = re.compile("house.of.the.dragon.")
        self.LDre3 = re.compile("HOUSE.OF.THE.DRAGON.")
        self.LDre4 = re.compile("House.of.the.Dragon. ")
        self.SNWcount = len("House.of.the.Dragon.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        s3 = re.search(self.LDre3, filetup[1])
        s4 = re.search(self.LDre4, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        elif s4 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/House Of The Dragon " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessSheHulk:
    def __init__(self):
        self.LDre1 = re.compile("She.Hulk.Attorney.At.Law.")
        self.LDre2 = re.compile("she.hulk.attorney.at.law.")
        self.LDre3 = re.compile("She-Hulk.Attorney.at.Law.")

        self.SNWcount = len("She.Hulk.Attorney.At.Law.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        s3 = re.search(self.LDre3, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/She Hulk Attorney At Law " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessHouseOfTheDragon:
    def __init__(self):
        self.LDre1 = re.compile("House.Of.The.Dragon.")
        self.LDre2 = re.compile("house.of.the.dragon.")
        self.LDre3 = re.compile("House.of.the.Dragon.")

        self.SNWcount = len("House.Of.The.Dragon.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        s3 = re.search(self.LDre3, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/House Of The Dragon " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessTheLordOfTheRingsTheRingsOfPower:
    def __init__(self):
        self.LDre1 = re.compile("The.Lord.Of.The.Rings.The.Rings.Of.Power.")
        self.LDre2 = re.compile("the.lord.of.the.rings.the.rings.of.power.")
        self.LDre3 = re.compile("The.Lord.of.the.Rings.The.Rings.of.Power.")

        self.SNWcount = len("The.Lord.Of.The.Rings.The.Rings.Of.Power.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        s3 = re.search(self.LDre3, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/The Lord Of The Rings The Rings Of Power " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessAndor:
    def __init__(self):
        self.LDre1 = re.compile("Andor.")
        self.LDre2 = re.compile("andor.")

        self.SNWcount = len("Andor.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/Andor " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessStarTrekProdigy:
    def __init__(self):
        self.LDre1 = re.compile("Star.Trek.Prodigy.")
        self.LDre2 = re.compile("star.trek.prodigy.")

        self.SNWcount = len("Star.Trek.Prodigy.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/Star Trek Prodigy " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessNightSky:
    def __init__(self):
        self.LDre1 = re.compile("Night.Sky.")
        self.LDre2 = re.compile("night.sky.")

        self.SNWcount = len("Night.Sky.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            print(season)
            print(episode)
            newstring = filetup[0] + "/Night Sky " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessStarWarsVisions:
    def __init__(self):
        self.LDre1 = re.compile("Star.Wars.Visions.")
        self.LDre2 = re.compile("star.wars.visions.")

        self.SNWcount = len("Star.Wars.Visions.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Star Wars Visions " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessSecretInvasion:
    def __init__(self):
        self.LDre1 = re.compile("Secret.Invasion.")
        self.LDre2 = re.compile("secret.invasion.")

        self.SNWcount = len("Secret.Invasion.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Secret Invasion " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessSilo:
    def __init__(self):
        self.LDre1 = re.compile("Silo.")
        self.LDre2 = re.compile("silo.")

        self.SNWcount = len("Silo.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Silo " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessFoundation:
    def __init__(self):
        self.LDre1 = re.compile("Foundation.")
        self.LDre2 = re.compile("foundation.")

        self.SNWcount = len("Foundation.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Foundation " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessTheContenintal:
    def __init__(self):
        self.LDre1 = re.compile("The.Continental.")
        self.LDre2 = re.compile("the.continental.")

        self.SNWcount = len("The.Continental.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/The Continental " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessAhsoka:
    def __init__(self):
        self.LDre1 = re.compile("Ahsoka.")
        self.LDre2 = re.compile("ahsoka.")

        self.SNWcount = len("Ahsoka.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Ahsoka " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessWheelOfTime:
    def __init__(self):
        self.LDre1 = re.compile("The.Wheel.Of.Time.")
        self.LDre2 = re.compile("The.Wheel.of.Time.")
        self.LDre3 = re.compile("the.wheel.of.time.")

        self.SNWcount = len("The.Wheel.Of.Time.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])
        s3 = re.search(self.LDre3, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        elif s3 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Wheel Of Time " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessOurFlagMeansDeath:
    def __init__(self):
        self.LDre1 = re.compile("Our.Flag.Means.Death.")
        self.LDre2 = re.compile("our.flag.means.death.")

        self.SNWcount = len("Our.Flag.Means.Death.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Our Flag Means Death " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessLoki:
    def __init__(self):
        self.LDre1 = re.compile("Loki.")
        self.LDre2 = re.compile("loki.")

        self.SNWcount = len("Loki.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1])
        s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Loki " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessMonarch:
    def __init__(self):
        self.LDre1 = re.compile("monarch.legacy.of.monsters.")
        # self.LDre2 = re.compile("loki.")

        self.SNWcount = len("monarch.legacy.of.monsters.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())
        # s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Monarch Legacy Of Monsters " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessHalo:
    def __init__(self):
        self.LDre1 = re.compile("halo.")
        # self.LDre2 = re.compile("loki.")

        self.SNWcount = len("halo.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())
        # s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Halo " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessBadBatch:
    def __init__(self):
        self.LDre1 = re.compile("star.wars.the.bad.batch.")
        # self.LDre2 = re.compile("loki.")

        self.SNWcount = len("star.wars.the.bad.batch.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())
        # s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Star Wars The Bad Batch " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessShogun:
    def __init__(self):
        self.LDre1 = re.compile("shogun.2024.")
        # self.LDre2 = re.compile("loki.")

        self.SNWcount = len("shogun.2024.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())
        # s2 = re.search(self.LDre2, filetup[1])

        if s1 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Shogun " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)


class ProcessStarTrekDiscovery:
    def __init__(self):
        self.LDre1 = re.compile("star.trek.discovery.")
        self.LDre2 = re.compile("star\ trek\ discovery\.")

        self.SNWcount = len("star.trek.discovery.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())
        s2 = re.search(self.LDre2, filetup[1].lower())

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Star Trek Discovery " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class Process3BodyProblem:
    def __init__(self):
        self.LDre1 = re.compile("3.body.problem.")
        self.LDre2 = re.compile("3\ body\ problem\.")

        self.SNWcount = len("3.body.problem.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())
        s2 = re.search(self.LDre2, filetup[1].lower())

        if s1 != None:
            return True
        elif s2 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/3 Body Problem " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class ProcessFallout:
    def __init__(self):
        self.LDre1 = re.compile("fallout.")

        self.SNWcount = len("fallout.")

    def scan_file(self, filetup):
        s1 = re.search(self.LDre1, filetup[1].lower())

        if s1 != None:
            return True
        else:
            return False

    def process_file(self, filetup):
        if self.scan_file(filetup) != True:
            pass
        else:
            raw = filetup[1][self.SNWcount:]
            season = raw[:3]
            episode = raw[3:6]
            newstring = filetup[0] + "/Fallout " + season.upper() + episode.upper() + " Episode" + episode[1:] + filetup[2]
            oldstring = filetup[0] + "/" + filetup[1] + filetup[2]
            print(newstring)
            print(oldstring)
            try:
                os.renames(oldstring, newstring)
            except FileNotFoundError:
                print(oldstring, newstring)

class TVSNameClean:
    def __init__(self):
        # self.tvfolder = "/media/charliepi/CHOCOLATE/tvshows"
        self.tvfolder = "/home/teresa/Downloads/tvshows"
        self.tvs = []


    def find_tvs_files(self):
        for (paths, dirs, files) in os.walk(self.tvfolder, followlinks=True):
            for filename in files:
                fnn = os.path.join(paths, filename)
                path, ext = os.path.splitext(fnn)
                dir, file = os.path.split(path)

                if ext == ".mkv" or ext == ".mp4":
                    parts = (dir, file, ext)
                    self.tvs.append(parts)
        # print(self.tvs)
        return self.tvs



if __name__ == "__main__":
    TVC = TVSNameClean()
    PSNW = ProcessStrangeNewWorlds()
    POWK = ProcessObiWanKenobi()
    FAMK = ProcessForAllMankind()
    ORV = ProcessOrville()
    MM = ProcessMsMarvel()
    IAG = ProcessIAmGroot()
    STLD = ProcessLowerDecks()
    HOTD = ProcessHouseOfTheDragon()
    SH = ProcessSheHulk()
    TLOTRTROP = ProcessTheLordOfTheRingsTheRingsOfPower()
    ANDOR = ProcessAndor()
    STP = ProcessStarTrekProdigy()
    NS = ProcessNightSky()
    TOTJ = ProcessStarWarsVisions()
    SI = ProcessSecretInvasion()
    SL = ProcessSilo()
    FDN = ProcessFoundation()
    TC = ProcessTheContenintal()
    PA = ProcessAhsoka()
    WOT = ProcessWheelOfTime()
    OFMD = ProcessOurFlagMeansDeath()
    PL = ProcessLoki()
    MLOM = ProcessMonarch()
    SWBB = ProcessBadBatch()
    HALO = ProcessHalo()
    SHO = ProcessShogun()
    STD = ProcessStarTrekDiscovery()
    TBP = Process3BodyProblem()
    FAL = ProcessFallout()

    tvfiles = TVC.find_tvs_files()
    for tv in tvfiles:
        PSNW.process_file(tv)
        POWK.process_file(tv)
        ORV.process_file(tv)
        FAMK.process_file(tv)
        MM.process_file(tv)
        IAG.process_file(tv)
        STLD.process_file(tv)
        HOTD.process_file(tv)
        SH.process_file(tv)
        HOTD.process_file(tv)
        TLOTRTROP.process_file(tv)
        ANDOR.process_file(tv)
        STP.process_file(tv)
        NS.process_file(tv)
        TOTJ.process_file(tv)
        SI.process_file(tv)
        SL.process_file(tv)
        FDN.process_file(tv)
        TC.process_file(tv)
        PA.process_file(tv)
        WOT.process_file(tv)
        OFMD.process_file(tv)
        PL.process_file(tv)
        MLOM.process_file(tv)
        SWBB.process_file(tv)
        HALO.process_file(tv)
        SHO.process_file(tv)
        STD.process_file(tv)
        TBP.process_file(tv)
        FAL.process_file(tv)
