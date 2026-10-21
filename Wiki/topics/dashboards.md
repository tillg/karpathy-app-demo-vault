---
type: topic
tags: [dashboard]
updated: 2026-10-21
sources: []
related: [index, mountains, tour-log, coffee]
---

# Dashboards

Live tables over the wiki's properties, written as [Obsidian Bases](https://obsidian.md/help/bases/syntax) blocks.
They update themselves when a page changes, so this page needs no upkeep. Edit a block to change what it shows.

## Tours, highest first

Every tour page (`kind: tour`), with its activity, region, summit height and the date it was last done
([[tour-log]]).

```base
filters:
  and:
    - file.inFolder("Wiki")
    - 'kind == "tour"'
views:
  - type: table
    name: Tours
    order: [file.basename, activity, region, summit_m, difficulty, done]
    sort:
      - property: summit_m
        direction: DESC
properties:
  file.basename:
    displayName: Tour
  summit_m:
    displayName: Summit (m)
  done:
    displayName: Last done
```

## Coffee sources

The source summaries tagged `coffee`, newest first.

```base
filters:
  and:
    - file.inFolder("Wiki/sources")
    - file.hasTag("coffee")
    - 'type == "source"'
views:
  - type: table
    name: Coffee sources
    order: [file.basename, updated, related]
    sort:
      - property: updated
        direction: DESC
    limit: 20
properties:
  file.basename:
    displayName: Source
```
