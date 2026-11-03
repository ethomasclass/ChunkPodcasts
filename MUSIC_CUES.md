# Music Cues (simplified plan)

This plan replaces the full M1–M21 cue lists in each episode's `script.md`. Each episode gets **4 music placements**, and the rest is narration with sound effects only. Every Suno prompt is instrumental. Each track has a **style prompt** and a **lyrics box** entry. The lyrics box holds only bracketed structure tags, with no words to sing. The "length needed" is how much of the track you'll use, so trim the Suno output to that length, with the fade included.

## Series theme (make once, use in every episode)
**T1 Main theme**
`slow cinematic americana, fingerpicked acoustic guitar, warm cello, light harmonica, soft steady pulse, reflective and grounded, documentary theme, instrumental`

Lyrics box:
```
[Intro: solo fingerpicked acoustic guitar]
[Instrumental: cello joins, light harmonica melody]
[Build: soft steady pulse]
[Outro: guitar and cello, gentle ritardando]
[Fade Out]
[End]
```
- Intro: **15 sec**. Swell for 5 sec, duck under "This is Chunk History Shorts…", then fade out over 3 sec.
- Outro: **40 sec**. Low under the final narration block, then let it rise for about 8 sec at the end.

**T1b Somber theme variation (Episode 3 only)**
`slow somber cinematic americana, solo cello and sparse piano, fingerpicked acoustic guitar, minor key, no drums, reverent and still, documentary, instrumental`

Lyrics box:
```
[Intro: solo cello, slow]
[Instrumental: sparse piano and fingerpicked guitar, minor key]
[Outro: cello sustains, piano fades]
[Fade Out]
[End]
```
- Intro: **15 sec**. Outro: **35 sec**.

## Episode 1: Boom, Bust, and Barbed Wire
| # | Where | Track | Length needed |
|---|---|---|---|
| 1 | Intro, VO 3 | T1 | 15 sec |
| 2 | Cattle and cowboys, VO 8–9 | E1-A | 1 min 50 sec |
| 3 | Nuevomexicanos and Las Gorras Blancas, VO 12–13 | E1-B | 1 min 40 sec |
| 4 | Outro, VO 14 | T1 | 40 sec |

**E1-A Cattle trail**
`laid-back western trail instrumental, loping mid-tempo rhythm, strummed acoustic guitar, gentle fiddle, upright bass, open prairie, steady and unhurried, instrumental`

Lyrics box:
```
[Intro: strummed acoustic guitar, loping rhythm]
[Instrumental: gentle fiddle melody, upright bass]
[Instrumental: steady trail groove, no build]
[Outro: fiddle fades]
[End]
```

**E1-B New Mexico**
`slow northern new mexico folk, nylon string spanish guitar, solo violin, melancholy but determined, sparse, night, instrumental`

Lyrics box:
```
[Intro: solo nylon string guitar]
[Instrumental: solo violin enters, slow]
[Instrumental: guitar and violin, sparse]
[Outro: guitar alone]
[Fade Out]
[End]
```

No music: the cold open, boomtowns, mining and barbed wire (sound effects only).

## Episode 2: Sodbusters
| # | Where | Track | Length needed |
|---|---|---|---|
| 1 | Intro, VO 3 | T1 | 15 sec |
| 2 | Sod houses, VO 7–8 | E2-A | 1 min |
| 3 | Children's Blizzard, VO 10 | E2-B | 40 sec |
| 4 | Outro, VO 12 | T1 | 35 sec |

**E2-A Homestead life**
`gentle folksy homestead instrumental, banjo, soft fiddle, upright bass, 1880s prairie, simple and calm, instrumental`

Lyrics box:
```
[Intro: gentle banjo]
[Instrumental: soft fiddle and upright bass, simple melody]
[Outro: banjo alone]
[End]
```

**E2-B Blizzard**
`cold tense winter underscore, sustained high strings, low cello pulse, airy wind-like textures, slow build, instrumental`

Lyrics box:
```
[Intro: airy wind-like textures]
[Instrumental: sustained high strings, low cello pulse]
[Build: slow tension rise]
[Outro: strings hold, cut to silence]
[End]
```

No music: the cold open (blizzard sound effects only), the Great American Desert, the Homestead Act, the Exodusters, hard times and Turner.

## Episode 3: The Road to Wounded Knee
| # | Where | Track | Length needed |
|---|---|---|---|
| 1 | Intro, VO 3 | T1b | 15 sec |
| 2 | Plains nations and the buffalo, VO 4 | E3-A | 40 sec |
| 3 | Nez Perce and Chief Joseph, VO 10 | E3-B | 40 sec |
| 4 | Outro, Black Elk, VO 16 | T1b | 35 sec |

**E3-A Plains nations**
`spacious reverent instrumental, warm low strings, soft sustained piano, gentle frame drum heartbeat, wide open plains at dawn, calm, instrumental`

Lyrics box:
```
[Intro: soft sustained piano]
[Instrumental: warm low strings, gentle frame drum heartbeat]
[Outro: strings fade]
[End]
```

**E3-B Nez Perce**
`slow aching cinematic instrumental, solo cello melody over sparse piano, mountain stillness, quiet resolve and loss, instrumental`

Lyrics box:
```
[Intro: sparse piano]
[Instrumental: solo cello melody, slow]
[Outro: cello sustains, fade]
[End]
```

**No music during Wounded Knee (VO 14–15).** Leave only the sound effects and the silence. Music returns with the outro.

## Mix notes
- Keep music about −20 dB under the voice. Let it rise only in the gaps.
- Fade every bed in over about 2 sec and out over about 3 sec.
- Each track only needs to be generated once. Suno makes longer songs, so trim them.
