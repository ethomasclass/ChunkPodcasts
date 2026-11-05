# Style Guide

## Format
- Single host, story-driven. Each episode starts with a cold open, rewinds, works through the assigned questions in story order, returns to the cold open, and ends with a short reflection that teases the next episode.
- Target 6–7 minutes, including music. At this voice's pace that is about **950–1,000 words** of narration. Episode 1 ran about 1,170 words and came out around 7:40 of narration alone.
- No show name and no host name anywhere in the audio. Each episode opens straight into the cold open and ends on its final line, with no intro or sign-off.
- The main theme (M1) is reused in every episode.

## ElevenLabs voice
- Model: `eleven_v4`
- Voice ID: `mI4rIAStSQeKeqsz4FwM`
- Stability 0.5, similarity 0.75, speaker boost on.
- Render each VO block as its own clip.

## Emotion tags
- Write tags in square brackets, such as `[serious]`. The model performs them without reading them aloud.
- **Never use quiet, whisper, soft, or hushed tags.** They sound odd with this voice.
- **Keep the energy low-key.** Don't use `[excited]`, `[playful]`, `[upbeat]`, `[amused]` (it can make the voice laugh), `[dramatic]`, `[intense]`, `[intrigued]`, `[confident]`, or `[warm]`. They all made the delivery too upbeat.
- Tags to use instead: `[interested]`, `[curious]`, `[matter-of-fact]`, `[calm]`, `[storytelling]`, `[serious]`, `[somber]`, `[thoughtful]`, `[reflective]`, `[sad]`, `[determined]`, `[ominous]`.

## Music (Suno)
- Instrumental only, with no artist names in the prompts.
- Keep it about −18 to −22 dB under the voice and bring it up in the gaps.
