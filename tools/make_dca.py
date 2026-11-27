#!/usr/bin/env python3
"""Builds dca.html (Disney California Adventure) from index.html (Disneyland Park).
Run from the repo root after changing index.html:  python3 tools/make_dca.py
Only the park data, names, storage keys and plan-code prefix differ. Everything else is shared."""
import json, re, sys

src = open('index.html', encoding='utf-8').read()
out = src

def sub1(pattern, repl, flags=re.S):
    global out
    new, n = re.subn(pattern, lambda m: repl, out, count=1, flags=flags)
    if n != 1: sys.exit('pattern not found: ' + pattern[:60])
    out = new

def rep1(old, new):
    global out
    if out.count(old) != 1: sys.exit('expected exactly one: ' + old[:70] + ' got %d' % out.count(old))
    out = out.replace(old, new)

# ---- park data -------------------------------------------------------------
# 0 name, 1 land, 2 age, 3 minHeight(in), 4 pixar, 5 gentle, 6 note, 7 icon, 8 default wait, 9 length (min), 10 youtube id, 11 video note, 12 kind
R = [
 ["Radiator Springs Racers","Cars Land","Ages 6+",40,True,False,"Cars-themed dark ride that ends in a high-speed race. Single Pass only, so it is not on Multi Pass.","car",80,5,"","","ride"],
 ["Luigi's Rollickin' Roadsters","Cars Land","Little kids and up",32,True,True,"Cars bounce and sway to music. The holiday version is Luigi's Joy to the Whirl.","car",20,3,"","","ride"],
 ["Mater's Junkyard Jamboree","Cars Land","Little kids and up",32,True,True,"Tractors whip around on a short tether. The holiday version is Mater's Jingle Jamboree.","spinner",15,3,"","","ride"],
 ["Meet the Residents of Radiator Springs in Cars Land","Cars Land","All ages",0,True,True,"Characters walk around Cars Land. Check the app for times.","play",0,10,"","","meet"],
 ["Incredicoaster","Pixar Pier","Ages 8+",48,True,False,"Fast coaster with a launch and loops. The tallest height rule in the park.","coaster",40,3,"","","ride"],
 ["Toy Story Midway Mania!","Pixar Pier","Little kids and up",0,True,True,"Shoot targets in a 4D carnival game. A good fit for 6 year olds.","sim",50,6,"","","ride"],
 ["Inside Out Emotional Whirlwind","Pixar Pier","Little kids and up",0,True,True,"Spinning ride with the Inside Out emotions.","spinner",18,3,"","","ride"],
 ["Pixar Pal-A-Round - Swinging","Pixar Pier","Ages 6+",0,True,False,"Big Ferris wheel with swinging gondolas. There is also a non-swinging line.","spinner",30,8,"","","ride"],
 ["Jessie's Critter Carousel","Pixar Pier","All ages",0,True,True,"Carousel with Toy Story critters.","carousel",6,3,"","","ride"],
 ["Jumpin' Jellyfish","Pixar Pier","Little kids and up",40,True,True,"Gentle parasail-style drop.","spinner",10,2,"","","ride"],
 ["Games of Pixar Pier","Pixar Pier","All ages",0,True,True,"Midway-style games. Paid, and they take as long as you like.","play",0,15,"","","play"],
 ["Operation: Playtime! - featuring the Green Army Patrol","Pixar Pier","All ages",0,True,True,"Live show with the Green Army Men. Check the app for times.","show",10,15,"","","show"],
 ["Goofy's Sky School","Paradise Gardens Park","Ages 6+",42,False,False,"Small coaster with sharp turns.","coaster",35,2,"","","ride"],
 ["Silly Symphony Swings","Paradise Gardens Park","Little kids and up",40,False,True,"Swing ride. Tandem swings need 40 inches; a single swing needs 48.","spinner",12,3,"","","ride"],
 ["Golden Zephyr","Paradise Gardens Park","All ages",0,False,True,"Rocket-shaped swings.","spinner",10,3,"","","ride"],
 ["The Little Mermaid - Ariel's Undersea Adventure","Paradise Gardens Park","All ages",0,False,True,"Gentle dark ride through the movie.","car",22,6,"","","ride"],
 ["World of Color","Paradise Gardens Park","All ages",0,False,True,"Evening water, light and projection show. Seasonal editions change the name. Check the app for times and viewing options.","show",20,22,"","","show"],
 ["Soarin' Across America","Grizzly Peak","Little kids and up",40,False,True,"Flying-theater ride over American landscapes. New in 2026, so there is no wait history yet.","sim",45,6,"","","ride"],
 ["Grizzly River Run","Grizzly Peak","Ages 6+",42,False,False,"River rapids raft ride. You will get wet.","boat",30,5,"","","ride"],
 ["Redwood Creek Challenge Trail","Grizzly Peak","Ages 6+",42,False,True,"Climbing and zip line trail. The rock wall and zip line need 42 inches.","play",0,30,"","","play"],
 ["Monsters, Inc. Mike & Sulley to the Rescue!","Hollywood Land","Little kids and up",0,True,True,"Dark ride through Monstropolis. A few dark scenes.","car",30,6,"","","ride"],
 ["Mickey's PhilharMagic","Hollywood Land","All ages",0,False,True,"3D movie show with Disney songs. A cool seat in the shade.","show",10,12,"","","show"],
 ["Turtle Talk with Crush","Hollywood Land","All ages",0,True,True,"Crush answers kids' questions live on screen.","show",10,15,"","","show"],
 ["Animation Academy","Hollywood Land","Little kids and up",0,False,True,"Learn to draw a character. Classes are first come, first served.","play",0,30,"","","play"],
 ["Sorcerer's Workshop","Hollywood Land","All ages",0,False,True,"Interactive Disney exhibit.","play",0,15,"","","play"],
 ["Disney Jr. Mickey Mouse Clubhouse Live!","Hollywood Land","Toddlers and up",0,False,True,"Live stage show for younger kids. Check the app for times.","show",10,20,"","","show"],
 ["Guardians of the Galaxy - Mission: BREAKOUT!","Avengers Campus","Ages 8+",40,False,False,"Drop ride in the dark with loud effects.","sim",70,3,"","","ride"],
 ["WEB SLINGERS: A Spider-Man Adventure","Avengers Campus","Little kids and up",0,False,True,"Shoot webs at targets. No height rule.","sim",40,5,"","","ride"],
 ["Warriors of Wakanda: The Disciplines of the Dora Milaje","Avengers Campus","All ages",0,False,True,"Live performance with the Dora Milaje. Check the app for times.","show",10,15,"","","show"],
 ["Avengers Headquarters","Avengers Campus","All ages",0,False,True,"Meet Marvel heroes. Check the app for times.","play",0,10,"","","meet"],
 ["The Bakery Tour","Pacific Wharf","All ages",0,False,True,"Short bread-making tour with a sample.","play",0,15,"","","walk"],
 ["Five & Dime","Buena Vista Street","All ages",0,False,True,"Musical street show on Buena Vista Street. Check the app for times.","show",0,15,"","","show"],
 ["Meet Disney Pals on Buena Vista Street","Buena Vista Street","All ages",0,False,True,"Meet characters near the entrance. Check the app for times.","play",0,10,"","","meet"],
]
rides_js = "const RIDES = [\n" + ",\n".join(" " + json.dumps(r, ensure_ascii=False, separators=(',', ':')) for r in R) + "\n];"
sub1(r"const RIDES = \[.*?\n\];", rides_js)

# ---- typical waits by hour (hours 8..23) from Queue-Times 2025 statistics, late hours capped at the 9 PM value
HIST = {
 "Radiator Springs Racers":[90,75,77,80,80,80,79,81,82,81,79,77,72,60,60,60],
 "Guardians of the Galaxy - Mission: BREAKOUT!":[42,53,59,66,69,71,77,80,84,87,86,87,85,82,56,65],
 "WEB SLINGERS: A Spider-Man Adventure":[16,31,37,40,41,42,41,44,45,44,40,37,31,20,8,7],
 "Grizzly River Run":[5,5,9,19,29,36,38,39,36,28,21,13,9,8,8,8],
 "Incredicoaster":[13,22,27,29,33,35,39,41,41,43,45,45,40,31,5,5],
 "Toy Story Midway Mania!":[16,35,40,44,47,49,52,53,54,53,52,47,40,26,12,7],
 "The Little Mermaid - Ariel's Undersea Adventure":[5,6,11,18,22,24,24,24,24,21,18,14,9,6,5,5],
 "Monsters, Inc. Mike & Sulley to the Rescue!":[6,15,30,38,39,41,42,44,44,43,40,35,28,18,9,9],
 "Goofy's Sky School":[6,18,31,38,42,44,47,49,50,49,45,40,36,24,20,20],
 "Golden Zephyr":[5,5,6,8,10,11,11,11,11,11,10,10,10,10,10,10],
 "Silly Symphony Swings":[5,6,7,9,10,11,12,12,13,12,11,11,10,10,10,10],
 "Inside Out Emotional Whirlwind":[5,6,12,16,18,19,20,20,21,21,20,18,15,9,6,7],
 "Jessie's Critter Carousel":[5,5,5,5,5,6,6,6,6,7,7,6,6,6,5,5],
 "Jumpin' Jellyfish":[5,7,9,9,10,11,11,11,11,11,10,12,12,10,7,7],
 "Pixar Pal-A-Round - Swinging":[5,9,21,27,30,34,37,37,38,38,38,37,22,25,25,25],
}
assert all(len(v) == 16 for v in HIST.values())
names = {r[0] for r in R}
assert set(HIST) <= names, set(HIST) - names
sub1(r"const HIST = \{.*?\};\n", "const HIST = " + json.dumps(HIST, ensure_ascii=False, separators=(',', ':')) + ";\n")

# ---- lightning lane (Disneyland's Lightning Lane passes page, checked Nov 27, 2026)
LANE = {n: "multi" for n in ["Goofy's Sky School","Grizzly River Run","Guardians of the Galaxy - Mission: BREAKOUT!","Incredicoaster","The Little Mermaid - Ariel's Undersea Adventure","Monsters, Inc. Mike & Sulley to the Rescue!","Soarin' Across America","Toy Story Midway Mania!","WEB SLINGERS: A Spider-Man Adventure"]}
LANE["Radiator Springs Racers"] = "single"
assert set(LANE) <= names
sub1(r"const LANE = \{.*?\};\n", "const LANE = " + json.dumps(LANE, ensure_ascii=False, separators=(',', ':')) + ";\n")
rep1("(checked Nov 26, 2026)", "(checked Nov 27, 2026)")

# ---- names that differ between listings and live feeds
sub1(r"const ALIASES = \{.*?\};\n", 'const ALIASES = {"World of Color - Season of Light":"World of Color","World of Color – ONE":"World of Color","Luigi\'s Joy to the Whirl":"Luigi\'s Rollickin\' Roadsters","Mater\'s Jingle Jamboree":"Mater\'s Junkyard Jamboree","Pixar Pal-A-Round – Swinging":"Pixar Pal-A-Round - Swinging"};\n')
rep1("const SYN = [];", "const SYN = [['joy to the whirl','rollickin roadsters'],['jingle jamboree','junkyard jamboree']];")

# ---- map
lands = """const LANDS = {
 "Buena Vista Street":{x:300,y:430,c:"#b9852f"},
 "Hollywood Land":{x:455,y:340,c:"#c0602a"},
 "Avengers Campus":{x:480,y:190,c:"#3b4a6b"},
 "Grizzly Peak":{x:300,y:150,c:"#2e8b57"},
 "Cars Land":{x:110,y:160,c:"#c4302b"},
 "Pacific Wharf":{x:300,y:290,c:"#8a5a2b"},
 "Paradise Gardens Park":{x:115,y:290,c:"#1c8fa8"},
 "Pixar Pier":{x:125,y:415,c:"#2f5bd8"}
};
"""
sub1(r"const LANDS = \{.*?\n\};\n", lands)
rep1("const HUB = {x:300,y:350};", "const HUB = {x:300,y:365};")
out = out.replace("Main Street, U.S.A.", "Buena Vista Street")   # remaining code uses (defaults, map spokes)
rep1(">Castle hub<", ">Park hub<")
sub1(r"const LAND_GUESS = \[.*?\];\n", "const LAND_GUESS = [[/world of color|paradise|mermaid/i,'Paradise Gardens Park'],[/pixar|toy story|incredi|inside out|playtime/i,'Pixar Pier'],[/avengers|spider|guardians|wakanda|marvel/i,'Avengers Campus'],[/cars|radiator|luigi|mater/i,'Cars Land'],[/hollywood|disney jr|animation|monsters|philharmagic/i,'Hollywood Land'],[/grizzly|redwood|soarin/i,'Grizzly Peak'],[/.*/,'Buena Vista Street']];\n")

# ---- live sources
rep1("https://queue-times.com/parks/16/queue_times.json", "https://queue-times.com/parks/17/queue_times.json")
rep1("7340550b-c14d-4def-80bb-acdb51d49a66", "832fcd51-ea19-4e77-85c7-75d5843b127c")

# ---- text, storage, plan codes
rep1("<title>Disneyland Park Planner</title>", "<title>Disney California Adventure Planner</title>")
rep1("<h1>Disneyland Park planner</h1>", "<h1>Disney California Adventure planner</h1>")
rep1('<a href="index.html" aria-current="page">Disneyland Park</a><a href="dca.html">California Adventure</a>', '<a href="index.html">Disneyland Park</a><a href="dca.html" aria-current="page">California Adventure</a>')
rep1("Simplified Disneyland Park map", "Simplified Disney California Adventure map")
rep1("name + ' Disneyland'", "name + ' Disney California Adventure'")
out = out.replace("'dl-plan2'", "'dca-plan1'")
rep1("localStorage.getItem('dca-plan1') || localStorage.getItem('dl-plan')", "localStorage.getItem('dca-plan1')")
rep1("'DL2.' +", "'DC1.' +")
rep1("code.startsWith('DL2.') || code.startsWith('DL1.')", "code.startsWith('DC1.')")
sub1(r"\(2025 for most rides; all years for Tiana's Bayou Adventure, Runaway Railway and Haunted Mansion\)", "(2025 statistics; late-evening values are capped at the 9 PM average)")
open('dca.html', 'w', encoding='utf-8').write(out)
print('dca.html written:', len(R), 'attractions')
