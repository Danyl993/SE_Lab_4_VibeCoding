# Lab 4 LLM Prompt Log

This log records the task prompts used during the implementation and the code-review decisions. It is a concise work log, not a verbatim export of the Codex conversation. Use the conversation share/export controls in Codex to provide the complete conversation required by the assignment.

## Repository review

**Prompt:** Read the official Lab 4 handout and the assigned repository README. Identify each deliverable and all implementation requirements. Keep all work local; do not create or push a GitHub repository.

**Review notes:** The handout requests four feature tasks based on the assigned README, two genuine 10-second gameplay videos, updated code, a chat-history document/PDF, and separate commits per task. The user's no-push instruction overrides the handout's push step. The clone's origin remote remains the assigned SETAPESU26 repository.

## Task 1 - Collision detection

**Prompt:** Fix the player-bullet collision loop so rapid or simultaneous hits cannot be skipped when bullets/enemies are removed. Ensure one bullet damages at most one living enemy and each enemy awards score only once.

**Review notes:** Replaced mutation of `player_bullets` while iterating with a survivor list. The living enemy candidate list is updated immediately after each hit. Added a regression test with two bullets hitting two enemies in one update.

## Task 2 - Game-over screen

**Prompt:** When an enemy bullet hits the player or the enemy grid reaches the player's line, stop gameplay and render a game-over screen that displays the final score and waits for input.

**Review notes:** The engine now enters a stable game-over state, displays the final score, and does not continue updating the round. The game-over effect is triggered only once per round.

## Task 3 - Replay and difficulty

**Prompt:** On the game-over screen, let the player restart with Easy, Medium, or Hard enemy speed/fire probability, or exit. Restart a clean round and reset score, player, enemies, and bullets.

**Review notes:** Number keys 1, 2, and 3 start a new round. Q and Esc exit. Difficulty parameters are centralized in `GameEngine.DIFFICULTIES`.

## Task 4 - Sound feedback

**Prompt:** Add distinct firing, enemy-destruction, and game-over sounds without requiring external audio asset files. Keep the game usable if the host has no audio device.

**Review notes:** Short tones are synthesized in memory and playback failures are handled gracefully. Tests use SDL's dummy video and audio drivers.

## Verification prompt

**Prompt:** Run the project's tests and validate collision scoring, both game-over triggers, the replay difficulty/reset flow, sound handling, and game-over rendering. Do not fabricate gameplay recordings.

**Review notes:** See `../IMPLEMENTATION_REPORT.md` for the actual test command/results and recording steps. Record both videos in real gameplay using the instructions there.
