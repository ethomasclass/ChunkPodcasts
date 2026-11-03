# Music Cues

Every track comes from the existing Chunk History music library (`music/cues/` in the `15minhistorystyle` repo), so there's nothing to generate. Copies are in each episode's `audio/music/` folder, keeping their original prefixes so they can be traced back to the library.

**No intro or outro theme.** Each episode has 4 main music placements, plus a few extra beds: a continuous ambience under every cold open, and a couple of very quiet beds where a section needed a little support under specific sections. Everything else is narration and sound effects only.

## Episode 1: Boom, Bust, and Barbed Wire
| # | Where | Track | Use | Notes |
|---|---|---|---|---|
| 0 | Cold open (VO 1–2) | `rc_night_riders` + `sfx/S11_night_crickets_loop` | 0:00 to end of VO 2, 0:47 | A night bed under the whole cold open. The crickets loop keeps the night sound going after the horse effect ends. |
| 1 | Boomtowns (VO 4) | `aw_boomtown_rush` | 0:00–0:44 of the track | Starts with VO 4. Hard-stop the music right after "bust" (43 sec into VO 4) and let the bust line sit in silence. |
| 2 | Hydraulic mining (VO 7) | `aw_boomtown_hollow` | first 0:35 | Low strings, one sour piano chord. Comes in after the water-cannon SFX. |
| 3 | Cattle and cowboys (VO 8–9) | `aw_long_drive` | first 1:50 | A cattle-trail cue. Fade out on "Then came the wire." |
| 4a | Village life (VO 12) | `sfx/S13_village_sheep` + distant train whistle on "railroad" | SFX | Sheep and a far-off church bell, then the railroad arrives. |
| 4 | Nuevomexicanos (VO 12 into VO 13) | `m_lament` | full track, 1:09 | Borderlands lament on nylon guitar. Fade before "In 1890, they posted a public platform." |

## Episode 2: Sodbusters
| # | Where | Track | Use | Notes |
|---|---|---|---|---|
| 0 | Cold open ambience (VO 1–2) | `sfx/S9_calm_morning_loop` → `sfx/S10_blizzard_wind_loop` | whole cold open | A calm prairie morning that cuts to a howling blizzard on "Then it hits," and a door bursts open on "door." |
| 1 | Blizzard cold open (VO 1–2) | `aw_white_cold` | from "bruised gray" to end of VO 2 | Glassy, wind-like, no melody. It creeps in as the sky turns. |
| 2 | Exodusters (VO 6) | `rc_resolve` | first 0:50 | A dignified hymn with a quiet, determined swell. |
| 3 | Sod houses (VO 7–8) | `rc_jubilo` | first 1:00 | Banjo and fiddle, hopeful but fragile. |
| 3b | Hard times (VO 9, from "Money") | `aw_boomtown_hollow` | about 0:30, kept very low | A quiet, hollow bed under the debt and foreclosure lines. |
| 4 | Children's Blizzard (VO 10) | `aw_white_cold` + `sfx/S10_blizzard_wind_loop` | 0:40, starting about 1:00 into the track | The same cue and storm return, tying back to the cold open. |

## Episode 3: The Road to Wounded Knee
| # | Where | Track | Use | Notes |
|---|---|---|---|---|
| 0 | Cold open ambience (VO 1–2) | `sfx/S14_winter_wind_loop` | whole cold open | Steady winter wind, with an occasional horse snort and harness jingle. |
| 1 | Cold open (VO 1–2) | `j_cold_open` | first 0:45 | Low cello, a frame-drum heartbeat, slow suspense. |
| 2 | Plains nations and the buffalo (VO 4) | `aw_promise_theme` | first 0:40 | Solo piano into warm strings. |
| 3 | Nez Perce and Chief Joseph (VO 10) | `j_grief` | full track, 0:40 | Solo cello. Let it ring out under "I will fight no more forever." |
| 3b | Dawes Act (VO 12) | `rc_codes` | about 0:27, kept very low | Cold and legalistic, with a pocket-watch tick, under the land being split up. |
| 3c | Back to Wounded Knee (VO 14) | `sfx/S14_winter_wind_loop` | from VO 14 to "opened fire" | The cold-open wind returns, then cuts out when the soldiers open fire. |
| 4 | Black Elk's closing (VO 16) | `aw_long_grief` | first 0:35 | Very quiet grieving cello. This is the first music after Wounded Knee. |

**No music during Wounded Knee (VO 14–15).** Leave only the sound effects and the silence.

## Mix notes
- Keep beds well under the voice, roughly −18 to −22 dB. The library cues are mastered to different levels, so most `aw_` cues are already quiet (about −21 to −23 LUFS) and need less turning down than `j_cold_open` or `m_lament`. Set each one by ear.
- Fade in over about 2 sec and out over about 3 sec, except the hard stop on "bust" in Episode 1.
