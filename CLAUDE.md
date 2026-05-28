# Pironman 5 - Documentation

## Repository Overview

This is the **English source** for the Pironman 5 documentation.

- **This repo**: branch `docs` (English source)
- **Remote**: `github.com:sunfounder/pironman5`
- **Translation branches**: `docs-fr` (French), `docs-cn` (Chinese), `docs-de` (German), `docs-es` (Spanish), `docs-it` (Italian), `docs-ja` (Japanese)

Local working copies for French translation: `../pironman5` (branch `docs-fr`).

## Translation Sync Workflow

When English `docs` is updated, changes must be synced to `docs-fr` (and other translation branches). **Do NOT wholesale copy files** — this overwrites translations with English.

### Step 1: Fetch and compare
```bash
cd ../pironman5
git fetch origin docs
git diff --name-status docs-fr origin/docs
# A = new files, D = deleted files, M = modified files
```

### Step 2: Sync non-RST files (images, assets, configs)
These don't need translation, just copy:
```bash
# Add new non-RST files
git diff --name-only --diff-filter=A docs-fr origin/docs | grep -v "\.rst$" | tr '\n' '\0' | xargs -0 -r git checkout origin/docs --

# Remove files deleted in English
git diff --name-only --diff-filter=D docs-fr origin/docs | tr '\n' '\0' | xargs -0 -r git rm --

# Update modified non-RST files
git diff --name-only --diff-filter=M docs-fr origin/docs | grep -v "\.rst$" | tr '\n' '\0' | xargs -0 -r git checkout origin/docs --
```

### Step 3: Replace old hello message blocks
English docs replaced `.. note::` hello blocks with `.. include:: /index.rst`. Apply the same to French files that still have inline `Bonjour...` hello notes. Use Perl for multiline replacement:
```perl
perl -i -0777 -pe 's/^\.\. note::\s*\n\s*\n\s{4}Bonjour.*?link_sf_facebook.*?\n\s*\n/.. include:: \/index.rst\n   :start-after: start_hello_message\n   :end-before: end_hello_message\n\n\n/s' "$file"
```
Skip key files that need full translation (handle manually in Step 4).

### Step 4: Translate RST files with content changes
For RST files where English content actually changed (beyond the hello block):
1. Read English version: `git show origin/docs:<path>`
2. Read current French version
3. Translate English text to French, preserving ALL RST directives, anchors, images, code blocks
4. Write back

**Files that frequently change** (check these first):
- `docs/source/index.rst`
- `docs/source/pironman5/faq.rst`
- `docs/source/pironman5_max/faq.rst`
- `docs/source/pironman5/set_up/set_up_rpi_os.rst`
- `docs/source/pironman5_max/set_up/set_up_rpi_os.rst`
- `docs/source/pironman5/set_up/set_up_umbrel.rst`
- `docs/source/pironman5_max/set_up/set_up_umbrel.rst`
- `docs/source/pironman5/control/control_with dashboard.rst`
- `docs/source/pironman5/control/control_with_commands.rst`
- `docs/source/pironman5_max/control/control_pironman5.rst`
- `docs/source/pironman5_max/control/control_with dashboard.rst`
- `docs/source/pironman5_max/control/control_with_commands.rst`

### Step 5: Verify
```bash
git status
git diff --name-status docs-fr origin/docs
```
Files showing as "M" are mostly expected — French text naturally differs from English text. Verify structural consistency: same anchors, same section count, same image references.

## Key Design

### Hello message centralization
`docs/source/index.rst` contains the centralized hello message between `.. start_hello_message` and `.. end_hello_message` markers. All other RST files include it via:
```rst
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message
```
When updating the hello message, **only modify `index.rst`** — all other files inherit it automatically. Translation branches must keep these markers in place with translated text.

### Include-based FAQ structure
`pironman5/faq.rst` contains `.. start_faq_xxx` / `.. end_faq_xxx` markers around each section. `pironman5_max/faq.rst` uses `.. include:: ../pironman5/faq.rst` to pull in shared sections. Translation branches inherit this structure — translating the base FAQ automatically propagates to variants.

### Anchor naming conventions
- `pironman5` (base): anchors use `_5` suffix, e.g., `.. _view_control_dashboard_5:`
- `pironman5_max`: anchors use `max_` prefix or no suffix, e.g., `.. _max_view_control_commands:`
- `pironman5_mini`: anchors use `_mini` suffix
- `pironman5_promax`: anchors use `_promax` suffix

### Product variant structure
```
docs/source/
├── index.rst
├── conf.py
├── pironman5/          # Base Pironman 5
├── pironman5_max/      # Pironman 5 MAX
├── pironman5_mini/     # Pironman 5 Mini
└── pironman5_promax/   # Pironman 5 Pro MAX
```

### Files identical across all 4 variants
When updating these in English, changes apply to all variants:
- `home_server/nextcloud.rst`, `home_server/plex.rst`
- `install/install_batocera.rst`, `install/install_raspberry_os.rst`, `install/install_umbrel.rst`
- `hardware/oled_screen.rst`, `hardware/power_switch_convertor.rst`, `hardware/tower_cooler.rst`

## Common Pitfalls

1. **Do NOT `git checkout origin/docs -- *.rst`** — this overwrites French translations with English.
2. **Do NOT `git merge -X theirs`** — same problem, all French content replaced by English.
3. **Do NOT `git merge -X ours`** — keeps old French but blocks English structural updates.
4. **"Modified" RST files in diff are expected** — French text differs from English text. Don't assume all diffs need fixing.
5. **File names with spaces** (e.g., `run_power_off copy.png`) — use null-delimited xargs: `tr '\n' '\0' | xargs -0`
6. **Windows environment**: No `make`, use `sphinx-build -b html source build/html`. Python may be blocked by Windows App Execution Aliases — use full path or Perl.

## Build

```bash
cd docs
pip install -r requirements.txt
sphinx-build -b html source build/html
```
