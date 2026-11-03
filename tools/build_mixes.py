"""Cue layout for every Chunk History Shorts episode. Run: python3 tools/build_mixes.py [1 2 3]

seq:      the running order. ('vo', n) places a narration clip, ('gap', s) adds silence, and
          ('sfx', name, 'clear'|'under', advance) starts a sound effect at the current time, then moves on by `advance` seconds.
anchored: (sfx name, anchor[, target LUFS]) puts a sound effect on a spoken word.
music:    (track, start anchor, end anchor, offset into track, fade in, fade out[, target LUFS]).
          Names starting with 'sfx/' are ambience loops laid down as a bed.
anchors:  ('vo', n, 'start'|'end', shift), ('word', n, 'word', 'start'|'end', shift[, nth]) or ('t', seconds).
"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mix import build
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'
V=lambda n:('vo',n); G=lambda s:('gap',s)
AMB=-32   # ambience beds
which=sys.argv[1:] or ['1','2','3']

if '1' in which:
 ep='episode-01-boom-bust-barbed-wire'
 seq=[('sfx','S1_night_grassland','under',2.5),V(1),G(.4),('sfx','S2_wire_snip','clear'),G(.3),V(2),G(1.0),V(3),G(.6),
  ('sfx','S3_pickaxe','clear',2.0),V(4),G(.7),V(5),G(.5),V(6),G(.3),('sfx','S6_water_cannon','clear',3.5),V(7),G(.8),
  ('sfx','S7_cattle_herd','under',2.5),V(8),G(.6),V(9),G(.3),('sfx','S12_wire_stretch','clear',3.0),V(10),G(.6),V(11),G(.8),
  ('sfx','S13_village_sheep','under',2.5),V(12),G(.6),V(13),G(1.0),V(14),G(2.5)]
 anch=[('S4_frontier_street',('word',4,'Virginia','start',-0.5)),('S5_gold_pan',('word',5,'placer','start',-0.3)),
  ('S8_steam_train',('word',8,'railroad','start',-0.3)),('S9_blizzard',('word',10,'nature','start',-0.3)),
  ('S8_steam_train',('word',12,'railroad','start',-0.3),-34),
  ('S10_horses_gallop',('word',13,'masks','end',0.2))]
 mus=[('rc_night_riders',('t',0),('vo',2,'end',1.5),0,2.0,3.0),
  ('sfx/S11_night_crickets_loop',('t',0),('vo',2,'end',1.5),0,1.5,3.0,AMB),
  ('aw_boomtown_rush',('vo',4,'start',-0.5),('word',4,'bust','end',0.15),0,1.0,0.25),
  ('aw_boomtown_hollow',('vo',7,'start',-1.0),('vo',7,'end',1.5),0,1.5,2.5),
  ('aw_long_drive',('vo',8,'start',-2.5),('word',9,'wire','end',1.2),0,2.0,3.0),
  ('m_lament',('vo',12,'start',-2.0),('word',13,'posted','start',-1.0),0,2.0,3.0),
  ('sfx/S11_night_crickets_loop',('vo',13,'start',-0.5),('word',13,'posted','start',-0.5),20,2.0,3.0,AMB)]
 build(ep,seq,anch,mus,R+ep+'/Chunk_History_Shorts_Ep1_Boom_Bust_and_Barbed_Wire.mp3')

if '2' in which:
 ep='episode-02-sodbusters'
 seq=[G(2.0),V(1),G(.6),V(2),G(1.0),V(3),G(.8),('sfx','S2_prairie_wind','under',2.0),V(4),G(.4),
  ('sfx','S3_quill_pen','clear'),G(.2),V(5),G(.5),V(6),G(.5),V(7),G(.3),('sfx','S6_plow_sod','clear',3.0),V(8),G(.8),V(9),G(.8),
  V(10),G(.8),('sfx','S8_worlds_fair','under',2.0),V(11),G(1.0),V(12),G(2.5)]
 anch=[('S11_door_burst',('word',1,'door','start',-0.1),-22),
  ('S4_steamboat',('word',6,'west','end',0.1)),('S5_camera_flash',('word',7,'camera','end',0.1)),
  ('S7_grasshopper_swarm',('word',9,'grasshoppers','start',-0.3)),('S12_wagon_creak',('word',9,'wagons','start',-0.5))]
 mus=[('sfx/S9_calm_morning_loop',('t',0),('word',1,'hits','start',0.0),0,1.5,0.6,AMB),
  ('sfx/S10_blizzard_wind_loop',('word',1,'hits','start',-0.3),('vo',2,'end',1.5),0,0.4,3.0,-28),
  ('aw_white_cold',('word',1,'gray','start',-1.0),('vo',2,'end',1.5),0,2.0,3.0),
  ('rc_resolve',('vo',6,'start',-1.0),('vo',6,'end',1.5),0,1.5,3.0),
  ('rc_jubilo',('vo',7,'start',-0.5),('vo',8,'end',1.5),0,1.5,3.0),
  ('aw_boomtown_hollow',('word',9,'Money','start',-1.0),('vo',9,'end',1.5),0,2.0,3.0,-37),
  ('sfx/S10_blizzard_wind_loop',('vo',10,'start',-2.0),('vo',10,'end',1.5),30,2.0,3.0,AMB),
  ('aw_white_cold',('vo',10,'start',-3.0),('vo',10,'end',1.5),60,2.0,3.0)]
 build(ep,seq,anch,mus,R+ep+'/Chunk_History_Shorts_Ep2_Sodbusters.mp3')

if '3' in which:
 ep='episode-03-road-to-wounded-knee'
 seq=[('sfx','S1_blizzard_cavalry','under',3.0),V(1),G(.6),V(2),G(1.0),V(3),G(.6),('sfx','S2_buffalo_herd','clear',4.0),V(4),G(.6),
  ('sfx','S3_dry_cornstalks','under',2.0),V(5),G(.5),('sfx','S4_gold_pan','under',2.0),V(6),G(.6),('sfx','S5_treaty_tent','under',2.0),V(7),G(.4),
  ('sfx','S6_pickaxe_pines','clear',2.5),V(8),G(.3),('sfx','S7_horses_gallop','clear',3.5),V(9),G(.6),('sfx','S8_mountain_trail','under',2.5),V(10),G(2.0),
  ('sfx','S9_school_bell_scissors','clear',4.0),V(11),G(.4),('sfx','S10_surveyor_chain','clear',3.0),V(12),G(.6),
  ('sfx','S11_night_campfire','under',3.0),V(13),G(.8),V(14),G(.5),
  ('sfx','S12_distant_boom','clear',5.0),G(1.0),V(15),G(.5),('sfx','S13_blizzard_settling','clear',5.0),V(16),G(3.0)]
 mus=[('sfx/S14_winter_wind_loop',('t',0),('vo',2,'end',1.5),0,1.5,3.0,AMB),
  ('j_cold_open',('t',0),('vo',2,'end',1.5),0,2.0,3.0),
  ('aw_promise_theme',('vo',4,'start',-1.0),('vo',4,'end',1.5),0,1.5,3.0),
  ('j_grief',('vo',10,'start',-1.0),('vo',10,'end',2.0),0,1.5,3.0),
  ('rc_codes',('vo',12,'start',-0.5),('vo',12,'end',1.5),0,1.5,3.0,-37),
  ('sfx/S14_winter_wind_loop',('vo',14,'start',-2.0),('word',14,'fire','end',0.3),30,1.5,0.4,AMB),
  ('aw_long_grief',('vo',16,'start',-2.0),('vo',16,'end',3.0),0,2.0,3.0)]
 build(ep,seq,[],mus,R+ep+'/Chunk_History_Shorts_Ep3_The_Road_to_Wounded_Knee.mp3')
