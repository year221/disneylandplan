# Disneyland Park Planner

A single-page app for planning a day at Disneyland Park (Anaheim). No build step and no server.

- Endless-scroll list of rides with age group, height minimum, land and notes
- Click-to-play ride videos (YouTube) on each card
- 1–5 star preference score per ride, with "Top picks" and "Best score first" views
- Day planner: pick rides, set your arrival time, get an arrive-at time for each ride and a simplified route map
- Save your plan in the browser, or copy a plan code to move it between devices

## Host it on GitHub Pages

1. Put `index.html` at the root of a repo.
2. Repo **Settings → Pages → Build and deployment**: Source = "Deploy from a branch", Branch = `main`, folder = `/ (root)`.
3. Open `https://<your-username>.github.io/<repo-name>/` after about a minute.

## Notes

- Wait times are rough defaults. Edit them in the plan.
- The map is a sketch, not to scale.
- Videos are third-party YouTube uploads and some uploaders disable embedding. Every card also has an "Open on YouTube" link.
- Heights and ride availability change. Check the official Disneyland app.
