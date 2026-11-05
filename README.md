# Chunk History Shorts

Short, story-driven history podcast episodes for students (6–7 minutes each), narrated by one host.

## Episodes

| # | Title | Topic | Status |
|---|---|---|---|
| 1 | [Boom, Bust, and Barbed Wire](episode-01-boom-bust-barbed-wire/) | Mining, ranching, the open range, Las Gorras Blancas | Narration and SFX recorded; music to add |
| 2 | [Sodbusters](episode-02-sodbusters/) | Homestead Act, Exodusters, farming the Plains, the Children's Blizzard, Turner's Frontier Thesis | Narration and SFX recorded; music to add |
| 3 | [The Road to Wounded Knee](episode-03-road-to-wounded-knee/) | Plains Nations and the Plains Wars, assimilation, the Dawes Act, Wounded Knee | Narration and SFX recorded; music to add |

## What's in each episode folder

- `script.md`: production script with narration blocks, emotion tags, music and SFX cues, Suno prompts, and pronunciation notes.
- `narration.txt`: narration text only, split into the VO blocks.
- `audio/narration/`: one ElevenLabs render per VO block, numbered in order.
- `audio/sfx/`: ElevenLabs sound effects, named to match the cues in the script (S1, S2, ...).
- `audio/narration_preview.mp3`: all narration clips joined with short gaps, without music.

## Production workflow

1. Render each VO block with ElevenLabs (see [STYLE_GUIDE.md](STYLE_GUIDE.md) for the model and settings).
2. Generate the music cues in Suno, using the instrumental prompts in the script.
3. Assemble the clips in an audio editor, layering music and SFX at the cue points.

Music: see [MUSIC_CUES.md](MUSIC_CUES.md). Each episode reuses 4 cues from the Chunk History music library, with no intro or outro theme.

See [STYLE_GUIDE.md](STYLE_GUIDE.md) for voice, tag, and format rules shared by every episode.

## Final mixes

Each episode folder has a finished mix: `Ep<N>_<Title>.mp3` (narration, sound effects and music beds, normalized to −16 LUFS).

To rebuild after changing a clip or a cue, run `python3 tools/build_mixes.py` for all episodes, or `python3 tools/build_mixes.py 2` for just Episode 2. Cue placements live in `tools/build_mixes.py`. Sound effects can be anchored to a spoken word using the word timings in `tools/words/`. If you re-record a clip, refresh its word timings too.
