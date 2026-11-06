# Podcast artwork

Two colour options for the "SHORTS" slab. Everything else is identical.

| File | Size | Use |
|---|---|---|
| `cover_A_cream.png` / `cover_B_orange.png` | 3000×3000 | Podcast cover (YouTube podcast playlist, Spotify, Apple) |
| `cover_*_1400.jpg` | 1400×1400 | Smaller copy for upload size limits |
| `wide_A_cream.png` / `wide_B_orange.png` (+ `.jpg`) | 1920×1080 | Still image for an audio-only YouTube video |
| `*.svg` | vector | Source artwork |

The mark and the CHUNK / HISTORY slabs are the channel's own artwork (`brand/chunk-history/final/` in `15minhistorystyle`). The SHORTS slab reuses the custom letters from HISTORY (S, H, O, R, T), so nothing is retyped in a font. The waveform bars use the logo's chamfered-corner shape. The label is IBM Plex Mono.

To rebuild: `python3 tools/brand/cover.py brand && node tools/brand/render.js brand` (needs the `15minhistorystyle` repo cloned next to this one, at `/home/user/ethomasclass/15minhistorystyle`).
