# MPM2D video pipeline

The scheduled GitHub Actions job renders four lessons per day. With 119 topics, one complete rotation takes 29 days and three slots on day 30. Each topic has a stable ID, so adding lessons mid-cycle makes them eligible immediately.

## Publication history

The workflow stores `published_history.json` on the dedicated `publication-history` branch. It creates the branch on its first upload. Each upload gets two checkpoints. The first records the topic ID and intended publication time under `pending`. The second adds the successfully scheduled topic ID to `published` and clears `pending`. The next selection starts a new cycle once all current topic IDs have been scheduled.

If an upload stops between checkpoints, check the pending lesson and schedule time in YouTube Studio. If the video exists, add its topic ID to `published`. If the upload failed, leave that list as it is. In both cases, set `pending` to `null` and save the change on the history branch before rerunning. Topics published before tracking began can be seeded by ID in the first cycle.

For local publishing, use `--history PATH` to share a history file across runs. To participate in the **same queue as Actions**, use an up-to-date worktree of the remote history branch, pass the file in that worktree to `--history`, and include `--sync-history`. A conflicting Git push stops the run before a competing upload starts.

To render a local preview, use `python run_pipeline.py --skip-upload --batch 1 --topic-id circle_chord --output-dir output`. Previews do not advance publication history.

## Diagram data

- A `linear_graph` uses a square coordinate range and a tick spacing. Each entry in `lines` is a triple of coefficients for **ax + by = c**, including vertical lines. An optional `radius` draws a circle centred at the origin. Dots are triples of x, y and label. Optional `segments` join pairs of single-letter dot labels.
- A `triangle` lists three vertices counterclockwise. Its three side labels follow edges AB, BC and CA. Angle labels follow A, B and C. An empty label omits the arc and `right` draws a square marker. With the right angle at B, side colours identify adjacent, opposite and hypotenuse relative to angle A.
