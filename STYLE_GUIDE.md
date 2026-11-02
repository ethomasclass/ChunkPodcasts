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
- **Avoid `[excited]`.** In Episode 1 it made the delivery sound too excited. Use calmer, engaged tags instead: `[interested]`, `[intrigued]`, `[curious]`, `[confident]`, `[warm]`.
- Go easy on `[playful]` and `[upbeat]` for the same reason.
- Good tags for serious moments: `[serious]`, `[somber]`, `[thoughtful]`, `[reflective]`, `[sad]`, `[determined]`.

## Music (Suno)
- Instrumental only, with no artist names in the prompts.
- Keep it about −18 to −22 dB under the voice and bring it up in the gaps.
