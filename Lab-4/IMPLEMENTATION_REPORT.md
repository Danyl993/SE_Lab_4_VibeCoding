# Software Engineering Lab 4 - Vibe Coding

## Requirement checklist

- [x] Read the full one-page official handout and the reference repository README.
- [x] Clone the assigned repository locally and inspect the starter code.
- [x] Fix bullet collision handling so adjacent list elements are not skipped and each target scores once.
- [x] Show a final-score game-over screen after a player hit or enemy-grid descent.
- [x] Allow replay with Easy, Medium, or Hard enemy movement/fire settings, or exit.
- [x] Add firing, enemy-destroyed, and game-over sound feedback.
- [x] Add regression tests and document setup/run/test commands.
- [x] Keep changes local. No push, fork, or pull request was created.
- [x] Create four task-labeled local commits for the regression tests; the shared engine implementation is in a preceding implementation commit.
- [ ] Capture a genuine 10-second before gameplay video.
- [ ] Capture a genuine 10-second after gameplay video.
- [x] Export the user/assistant message transcript as a PDF and include the complete Codex conversation share link.
- [ ] Verify four separate local commits, one per task (to be finalized after code verification).

The handout asks for a push to a personal repository. That step is intentionally not performed because the user explicitly prohibited pushing or publishing. The source checkout has the SETAPESU26 reference as its origin; do not push to it.

## Setup and run

From `46_space-invaders`:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Controls: arrows or A/D to move, Space to fire. On the game-over screen, press 1 (Easy), 2 (Medium), or 3 (Hard) to replay; press Q or Esc to exit.

## Test command

```powershell
python -m unittest discover -s tests -v
```

Results: **7 tests passed** on Python 3.11.9 / Pygame 2.6.1. `python -m compileall -q main.py game tests` also passed. A headless startup smoke check posted a window-close event to the actual `main()` loop and verified a clean exit. A live visual gameplay session still needs to be opened for the real before/after videos.

## Required real recordings

Videos must be captured by a person with a screen recorder; no recordings have been fabricated.

### Before video

The untouched starter is available at `recordings/before-source/`. A deterministic demonstration launcher at `recordings/before_collision_demo.py` sets up two simultaneous hits against the unmodified engine; the starter scores only one and visibly leaves the second enemy alive.

1. Open PowerShell in `C:\Users\danyl\Documents\SEM5\SE\lab_4\Lab-4\recordings`.
2. Start the recorder (Windows Snipping Tool screen recording, Xbox Game Bar with `Win+Alt+R`, or another recorder).
3. Run `python before_collision_demo.py` and record at least 10 seconds showing the original game screen and the collision result (`Expected score: 2 | Actual score: 1`).
4. Stop the recording and save it as `recordings/before.mp4`.

The demonstration launcher changes no file in `before-source`; it only prepares a reproducible in-game state for the untouched engine.

### After video

1. Open PowerShell in `C:\Users\danyl\Documents\SEM5\SE\lab_4\46_space-invaders`.
2. Start the recorder, then run `python main.py`.
3. Record at least 10 seconds of gameplay showing movement and shooting. For the feature demonstration, let an enemy bullet hit the player or the enemy grid descend to trigger Game Over, show the final score, press a difficulty key, and show the fresh round. Keep recording until these behaviors are visible (the handout says 10 seconds; a longer clip may be needed to show the full flow).
4. Stop the recording and save it as `recordings/after.mp4`.

Place both saved files in `Lab-4/recordings/`.

## Chat history

`docs/LLM_PROMPT_LOG.md` contains the task prompts and review notes used for the implementation. `docs/Chat_History.pdf` contains the conversation's user/assistant messages and a completion summary. `docs/CHAT_HISTORY_LINK.md` links to the full Codex conversation, including tool traces and command results.

## Local commit history

- `24bfa15` Task 1: add collision regression test
- `50bf698` Task 2: test game-over conditions and screen
- `9a992e5` Task 3: test replay difficulty and reset
- `64188fb` Task 4: test sound effects and silent fallback
- `c5f4a01` Complete Lab 4 gameplay tasks 1-4

The source implementation for the shared game engine is grouped in the `c5f4a01` implementation commit; each task's regression tests are committed separately. The branch is five commits ahead of `origin/main`; nothing has been pushed.
