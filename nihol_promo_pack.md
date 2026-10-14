# Nihol — promotional video pack

Nihol is a Telegram mini app for focus and productivity: start a session, a sapling grows while you stay off your phone, break the session and it withers. ("Nihol" = sapling, pronounced "Nahol".) This pack is the plan for the launch promo.

Status: **Tier A rendered on 2026-10-14.** 1080×1920, about 34 s, English narration, built from the author's screen recordings (in `nihol/footage/`), two illustrated stills and the bot's avatar. Spend: about 8 credits.

Visual rule: all characters, the sapling, and the UI mockups are original. The focus-timer mechanic is a concept, not a brand, so the video never copies another app's art, mascot, colours or wording.

---

## 1. Concept: "Grow something while you grow"

One sitting, one tree. The video follows a single student from distraction to a finished session. Every beat shows the real app screen as the hero, with illustrated moments around it. Tone: calm, warm, slightly playful. Same flat-vector palette family as the IELTS series (teal and mustard), plus a fresh leaf green for Nihol so the brand stands apart.

## 2. Format

| Item | Value |
|---|---|
| Primary cut | 30 s, 9:16 vertical (Telegram posts, Reels, TikTok, Shorts) |
| Secondary cut | 15 s, 1:1 (Telegram channel preview, ads) |
| Resolution | 1080×1920 and 1080×1080 |
| Narration | One voice, same narrator as the IELTS series for channel continuity, or none (music + captions) |
| Language | English master; Uzbek and Russian text-card variants are a 5-minute swap |
| Captions | Burned, top-center |

## 3. Script (30 s, 6 beats × 5 s)

| Beat | Time | Narration | On screen |
|---|---|---|---|
| 1 Hook | 0-5 | "Your phone is the reason your to-do list is still a list." | Illustration: student at desk, phone buzzing, a dozen notification bubbles crowding the frame. Hard cut to black. |
| 2 Reveal | 5-10 | "This is Nihol. Plant a sapling inside Telegram, and it grows every minute you stay focused." (voice spelling: Nihhol) | Real app screen: the home view with the sapling. Phone frame in the centre, soft leaf-green glow. Logo top-left. |
| 3 Mechanic | 10-15 | "Set the time. Pick your plant. Hit Plant, and put the phone down." | Real app screens, three quick taps: task entry, timer dial, start button. Screen-recorded, each held 1.5 s. |
| 4 Stakes | 15-20 | "Leave the app, and your sapling dies. Stay, and one hour becomes a full tree." | Split frame: left, the sapling drooping as a thumb reaches for the phone; right, the sapling in full leaf. Illustration over app UI. |
| 5 Payoff | 20-25 | "Every session goes into your garden. Daily streaks unlock rare plants." | Real app screen: the garden or history view with a week of trees. If the app has streaks or stats, show them here. |
| 6 CTA | 25-30 | "That's Nihol. Inside Telegram. No download, no sign-up." | App icon, the Telegram handle, big "Open in Telegram" button. Text card: "t.me/<bot> — free". |

Narration total is about 60 words, which fits 30 s at a relaxed pace.

## 4. Text overlays (burned)

- 0:05  NIHOL
- 0:10  PICK · SET · PUT IT DOWN
- 0:15  LEAVE EARLY → IT WILTS
- 0:20  7 DAYS = A GARDEN
- 0:25  OPEN IN TELEGRAM  ·  FREE

## 5. Assets needed from the app (you)

1. Screen recording, vertical, of one full flow: open the mini app, create a task, set a timer, start, let it run 10 seconds, finish. 60-90 seconds raw is plenty.
2. Screenshots at full resolution: home with sapling, timer running, the wilted state, the garden/history view, any stats or streak screen.
3. App icon or logo as PNG or SVG, and the brand colours if you have them.
4. The bot link (t.me/...).
5. Which language the first cut should be in.

If a screen doesn't exist yet (for example a garden view), say so and I'll illustrate it as a "coming soon" beat instead of faking UI.

## 6. Assets generated (me)

| Asset | Model | Credits |
|---|---|---|
| Student character sheet (reuse the IELTS student or a new one) | still | 1.25 |
| Beat 1 still: desk, buzzing phone, notification swarm | still | 1.25 |
| Beat 4 still: wilting sapling vs thriving sapling, split | still | 1.25 |
| Sapling growth stages sheet (seed, sprout, sapling, tree, wilted) for overlays | still | 1.25 |
| Beat 1 as a 5-second motion clip (optional) | Seedance 2.0 fast 720p | ~12.5 |
| Beat 4 as a 5-second motion clip (optional) | Seedance 2.0 fast 720p | ~12.5 |
| Narration, 6 lines | voice | 3 |

## 7. Cost tiers

| Tier | What moves | Credits | Fits current balance (12.75)? |
|---|---|---|---|
| A. Stills + your screen recording | App UI (real), stills with zoom/pan, captions | ~8 | Yes |
| B. One motion hero shot | Tier A plus beat 1 animated | ~20 | No, short by ~8 |
| C. Two motion shots | Tier A plus beats 1 and 4 animated | ~33 | No |

Tier A is a genuinely good promo because the real app does the heavy lifting. Motion clips add polish to the illustrated beats only.

## 8. Assembly (free, in the edit sandbox)

1. Phone-frame the screen recording: 9:16 canvas, device bezel, soft shadow, leaf-green gradient background.
2. Stills get the three-cut zoom/pan treatment used on Day 13.
3. Narration centred per beat, music bed if you supply a royalty-free track, captions burned.
4. Export 1080×1920 master, then a 1:1 crop with the phone centred.

## 9. Three alternative hooks, if the first one tests weak

- "Forty minutes. One tree. Zero scrolling."
- "The to-do app that punishes you with a dead plant."
- "You don't need another app. You need to put this one down."

## 10. As built

- Palette switched to the brand: deep green background, orange accents, mint and cream, taken from the bot avatar.
- Phone frame: 540×1172 rounded device with bezel and shadow; the 384×834 recordings scale into it cleanly.
- Footage moments used: timer screen (rec2 24.0 s), dial / plant picker / Plant button (rec1 15.2, 25.4, 32.6 s), garden (rec2 9.6 s), streak rewards (rec1 25.6 s). The two recordings are never joined end to end; each moment sits in its own beat with a crossfade.
- Narration: the author picked one take of the closing line by ear. Because the voice engine pronounces the same spelling differently between takes, the name in line 2 is spliced in from that approved take rather than regenerated. On-screen text keeps "Nihol". The closing take had a 3-second internal pause, which was cut out in the edit.
- Beat lengths are derived from each trimmed narration line plus 0.55 s, so lines never overlap; beats crossfade over 0.3 s.
- Build script: `build.py` in the edit sandbox (re-creatable from this pack). Inputs: rec1.mp4, rec2.mp4, s1.png, s4.png, avatar.jpg, vo1-6.wav.

Known limits: the onboarding tooltips ("Skip / Next") are visible in some app shots because they are in the recording. A re-record with the guide dismissed removes them. The square 1:1 cut was not produced.

## 11. Wordless cut (app-intro style)

Built 2026-10-14 from the same assets plus `nihol/footage/rec3.mp4` (the dial drag from 10:00 to 55:00 with the plant preview growing). No narration, one headline per section, soft placeholder music pad, 28.6 s, 1080×1920. Cost: 0 credits.

| Time | Section | Headline | Source |
|---|---|---|---|
| 0-3.5 | Open | Put the phone aside. | logo on brand green, gentle sway |
| 3.1-8.6 | Mechanic | Set the time. / Watch it grow. | rec3 full, last frame held |
| 8.2-13.2 | Reward | Unlock rare plants. | rec1 25.6 s |
| 12.8-17.8 | Garden | Build your garden. | rec2 9.6 s |
| 17.4-21.4 | Progress | Keep your streak. | rec2 22.2 s |
| 21.0-24.5 | Fit | Uzbek · Russian · English | rec2 5.4 s |
| 24.1-28.6 | Close | NIHOL / Grow while you study. / link | logo card |

Transitions: iris open, slide left, fade, slide up, fade, iris open. Every phone section has a slow 3.5 percent push-in. Headlines slide up and fade in over half a second.

Music: a synthesised pad with a light pluck line, placeholder only, mixed at about -19 LUFS. Replace with a licensed track before publishing. No real-world impact claims anywhere, by the author's instruction.

Build script: `build_wordless.py` in the edit sandbox.

## 12. Promo stills

Built 2026-10-14 in the edit sandbox, 0 credits. Brand green radial background, the bot avatar as logo with "NIHOL" wordmark, headline "Put the phone aside." with sub-line "Your tree grows while you study.", and the real app screen (dial at 60:00 with the full pomegranate tree, from `nihol/footage/rec3.mp4`) in a rounded phone frame that bleeds off the bottom edge. No link on the image, by the author's instruction.

| Size | Use | Phone width |
|---|---|---|
| 1080×1350 (4:5) | Telegram or Instagram post | 480 px, top at 430 |
| 1080×1080 (1:1) | channel preview, ads | 440 px, top at 360 |
| 1080×1920 (9:16) | story | 540 px, top at 620, fully visible |

Script: `promo_img.sh` in the sandbox builds the stage (background, shadow, bezel, masked screen); the text is layered with ImageMagick annotate in Montserrat ExtraBold.
