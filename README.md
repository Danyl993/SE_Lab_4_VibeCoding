# Space Invaders Game

A graphical Space Invaders game built with Pygame. The starter's collision bug and the four tasks in the assignment README are implemented here.

## Setup

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python main.py
```

## Controls

- Move: `Left` / `Right` or `A` / `D`
- Fire: `Space`
- After Game Over: `1` Easy, `2` Medium, or `3` Hard starts a fresh round; `Q` or `Esc` exits.

Each difficulty changes enemy marching speed and enemy fire probability. Sound effects for shots, destroyed enemies, and game over are synthesized in memory. The game continues silently if audio hardware is unavailable.

## Implemented tasks

1. **Collision detection:** each bullet is tested once against the living enemy list; collisions are resolved with survivor lists, avoiding mutation during iteration and duplicate hits.
2. **Game over:** a visual overlay shows the final score and waits for a replay choice or exit.
3. **Replay:** each difficulty starts a fresh round with reset score, player, enemies, and bullets.
4. **Sound:** firing, enemy destruction, and game over have short generated effects.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Assignment evidence

The untouched starter source is stored in `../Lab-4/recordings/before-source/` for capturing the required before video. Capture real 10-second gameplay videos before and after the changes; the videos are not fabricated or included. `docs/LLM_PROMPT_LOG.md` records the prompts and implementation review. Export this conversation from the chat application to provide its shareable chat-history page/link if your submission portal requires one.
