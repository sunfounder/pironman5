# Pironman 5 - Documentation (French Translation)

## Primary Reference

The authoritative CLAUDE.md is in the **English source repo**: `../pironman5 - Copy/CLAUDE.md`

All sync workflows, design notes, and common pitfalls are documented there. This file contains only French-specific supplements.

## French Branch Info

- **Branch**: `docs-fr`
- **Remote**: `origin/docs-fr` on `github.com:sunfounder/pironman5`
- **English source**: `origin/docs`

## Quick Sync

When English `docs` is updated:
```bash
git fetch origin docs
# Follow the 5-step workflow in ../pironman5 - Copy/CLAUDE.md
```

## French-Specific Notes

- The `index.rst` hello message between `start_hello_message` / `end_hello_message` markers must be kept in **French** — all other files include it
- `pironman5/faq.rst` contains translated FAQ sections with `start_faq_xxx` / `end_faq_xxx` include markers — keep these in French
- `pironman5_promax/` folder contains mostly English content (newer product, not yet fully translated to French)
- `pironman5_mini/` folder was not modified in recent docs updates — its French content should be preserved
