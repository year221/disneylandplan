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

## Activity colors and Lightning Lane Multi Pass

- The plan timeline and map color each stop by type: ride, walk-through, show, play area, meet & greet, food, rest/other. Each stop also carries a text label, so color is not the only cue.
- ⚡ marks attractions on Disneyland Park's Lightning Lane Multi Pass list (13 attractions). Rise of the Resistance is marked "Single Pass only". The list was taken from Disneyland's Lightning Lane page on Nov 26, 2026. It changes, so confirm in the Disneyland app. To update it, edit the `LANE` table in `index.html`.
- "Multi Pass" filter on the Rides tab shows only eligible attractions.
- "Add a food, rest or custom stop" on the plan tab adds your own stops. They are saved in your plan code and link as an optional field, so older codes and links still load.

## Live waits vs estimates

- Every wait is labeled. **LIVE** is a posted wait fetched from the web in the last 30 minutes. **ESTIMATE** is the typical wait written into this page. It is a rough guess, not historical data and not a forecast for your date. **YOUR EDIT** is a number you typed, and it wins over the other two. **CLOSED NOW** means the source reports the ride closed, so the estimate is used.
- Sources, tried in order: Queue-Times, then ThemeParks.wiki. Both are unofficial, so values can differ from the Disneyland app.
- "↻ Refresh waits" fetches again. "Auto-refresh every 5 min" refreshes while the tab is open, and the page also refreshes when you return to the tab. "Use live waits" turns the feature off.
- Live waits are for right now, so they only help on the day you visit. They are not saved in plan codes or links. Only waits you typed are saved.

## Show times

- Show times come from the ThemeParks.wiki live feed and cover today only (park time, Pacific). They are labeled **TODAY'S SCHEDULE**. Shows with no times posted say so.
- Show cards list today's showings. In the plan, a show stop has a showtime menu. "Next showing" picks the first showing at least 10 minutes after you would arrive, and the timeline holds until the show starts. If the showing you picked starts before you would arrive, the stop says so.
- "Add a show, parade or music set from today's schedule" adds entertainment that is not already in the list, such as fireworks or parades. The land on the map is a guess for these.
- A chosen showtime is saved in your plan code and link as an optional field, so older codes still load. A code only keeps the clock time, so on another day check that the show runs then.

## Durations

Each stop shows an approximate ride or show length (⏱) on the plan and on the ride cards. The plan also breaks each stop into walk, wait or hold, and length, and totals them at the bottom. Lengths are rough figures written into this page, not official numbers.
