# Math video pipeline

The scheduled GitHub Actions job renders four videos per day in mixed mode. The shared rotation contains 119 MPM2D lessons and ten geometric proofs. The first slot goes to a proof while any remain in the current cycle. Each topic has a stable ID, so new topics become eligible immediately.

## Visual proofs

The ten proof scenes use on-screen geometric motion and short equations on a white background. Their curriculum tags cover HKDSE, IB Mathematics AA/AI, and Ontario MPM2D, MCR3U, MHF4U, and MCV4U as applicable.

```sh
python run_pipeline.py --mode visual_proof --batch 1 --topic-id diff_of_squares --skip-upload --output-dir output
```

Use `--mode lesson` for the original lesson bank, `--mode visual_proof` for the proof bank, or `--mode mixed` for both. Proofs render at 1080×1920 and 30 fps. Each Edge TTS segment is decoded to 48 kHz PCM and measured with ffprobe. Silence of less than one video frame aligns the end of each clip to a frame boundary. Manim renders one timed clip per narration segment. The pipeline verifies every clip's frame count, then checks the muxed audio and video start times and durations before allowing upload.

## Publication history

The workflow stores `published_history.json` on the dedicated `publication-history` branch. It creates the branch on its first upload. Each upload gets two checkpoints. The first records the topic ID and intended publication time under `pending`. The second adds the successfully scheduled topic ID to `published` and clears `pending`. The next selection starts a new cycle once all topic IDs in the selected mode have been scheduled. Entries from outside that mode stay in history.

If an upload stops between checkpoints, check the pending lesson and schedule time in YouTube Studio. If the video exists, add its topic ID to `published`. If the upload failed, leave that list as it is. In both cases, set `pending` to `null` and save the change on the history branch before rerunning. Topics published before tracking began can be seeded by ID in the first cycle.

For local publishing, use `--history PATH` to share a history file across runs. To participate in the **same queue as Actions**, use an up-to-date worktree of the remote history branch, pass the file in that worktree to `--history`, and include `--sync-history`. A conflicting Git push stops the run before a competing upload starts.

To render a local preview, use `python run_pipeline.py --skip-upload --batch 1 --topic-id circle_chord --output-dir output`. Previews do not advance publication history.

## Diagram data

- A `linear_graph` uses a square coordinate range and a tick spacing. Each entry in `lines` is a triple of coefficients for **ax + by = c**, including vertical lines. An optional `radius` draws a circle centred at the origin. Dots are triples of x, y and label. Optional `segments` join pairs of single-letter dot labels.
- A `triangle` lists three vertices counterclockwise. Its three side labels follow edges AB, BC and CA. Angle labels follow A, B and C. An empty label omits the arc and `right` draws a square marker. With the right angle at B, side colours identify adjacent, opposite and hypotenuse relative to angle A.
