# Style Guide

## Format
- Single host, story-driven. Each episode starts with a cold open, rewinds, works through the assigned questions in story order, returns to the cold open, and ends with a short reflection that teases the next episode.
- Target 6–7 minutes, including music. At this voice's pace that is about **950–1,000 words** of narration. Episode 1 ran about 1,170 words and came out around 7:40 of narration alone.
- The host is never named. Intro: "This is Chunk History Shorts. Episode [number]: [title]." Outro: "Thanks for listening to Chunk History Shorts."
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
- **The show-name lines match the episode's mood.** The intro ("This is Chunk History Shorts...") uses the cold open's tone, and the outro ("Thanks for listening...") uses the ending's tone. For example, Episode 3 uses `[somber]` for both. Never tag either line upbeat or warm.

## Music (Suno)
- Instrumental only, with no artist names in the prompts.
- Keep it about −18 to −22 dB under the voice and bring it up in the gaps.
