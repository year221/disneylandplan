# Disneyland Park Planner

A single-page app for planning a day at Disneyland Park (Anaheim). No build step and no server.

- Endless-scroll list of rides with age group, height minimum, land and notes
- Click-to-play ride videos (YouTube) on each card
- 1–5 star preference score per ride, with "Top picks" and "Best score first" views
- Day planner: pick rides, set your arrival time, get an arrive-at time for each ride and a simplified route map
- Save your plan in the browser, copy a plan code, or copy a full link that opens the same plan on another device
- 62 listings: rides plus shows, walk-throughs, play areas and meet-and-greets, with a "Rides only" filter

## Host it on GitHub Pages

1. Put `index.html` at the root of a repo.
2. Repo **Settings → Pages → Build and deployment**: Source = "Deploy from a branch", Branch = `main`, folder = `/ (root)`.
3. Open `https://<your-username>.github.io/<repo-name>/` after about a minute.

## Notes

- Wait times are rough defaults. Edit them in the plan.
- The map is a sketch, not to scale.
- Videos are third-party YouTube uploads and some uploaders disable embedding. Every card also has an "Open on YouTube" link.
- Heights and ride availability change. Check the official Disneyland app.

## Compatibility

Plan codes (`DL1.` and `DL2.`) and links (`#plan=...`) made by earlier versions keep working. Renamed attractions are mapped to their new names, and plans saved in the browser by earlier versions are still read.
