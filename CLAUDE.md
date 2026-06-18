# Pironman 5 - Documentation

## Important Rules

1. **Do NOT switch branches** — the user will manually switch to the target branch before asking you to work.
2. **Do NOT build** — the user will run `sphinx-build` themselves to check for errors.
3. **Do NOT push or upload** — never run `git push` or `gh pr` unless explicitly asked.
4. **Do NOT wholesale copy files** — this overwrites translations with English.

## Repository Overview

- **This repo**: branch `docs` (English source)
- **Remote**: `github.com:sunfounder/pironman5`
- **Translation branches**: `docs-fr` (French), `docs-cn` (Chinese), `docs-de` (German), `docs-es` (Spanish), `docs-it` (Italian), `docs-ja` (Japanese)

Local working copies:
- `../pironman5` — used for whichever translation branch is currently checked out
- `../pironman5 - Copy` — this repo, `docs` branch (English source)

## Translation Sync Workflow

When English `docs` is updated, changes must be synced to the active translation branch. The user will have already switched `../pironman5` to the correct branch.

### Step 1: Understand what changed
Check recent commits on `docs` to see what actually changed:
```bash
git log origin/docs --oneline --since="<recent-date>"
```
Then for each commit, list changed files:
```bash
git diff <commit>^..<commit> --name-only
```
This is more reliable than `git diff --name-status <translation-branch> origin/docs` because the latter shows ALL differences including pre-existing translation text.

### Step 2: Sync non-RST files (images, assets, configs)
These don't need translation, just copy from `origin/docs`. Replace `<branch>` with the current translation branch name:
```bash
cd ../pironman5
# Add new non-RST files
git diff --name-only --diff-filter=A origin/<branch> origin/docs | grep -v "\.rst$" | tr '\n' '\0' | xargs -0 -r git checkout origin/docs --

# Remove files deleted in English
git diff --name-only --diff-filter=D origin/<branch> origin/docs | grep -v "\.rst$" | tr '\n' '\0' | xargs -0 -r git rm --

# Update modified non-RST files
git diff --name-only --diff-filter=M origin/<branch> origin/docs | grep -v "\.rst$" | tr '\n' '\0' | xargs -0 -r git checkout origin/docs --
```

### Step 3: Ensure index.rst has hello message markers
If the translation's `index.rst` doesn't have `.. start_hello_message` / `.. end_hello_message` markers, add empty ones at the very top:
```rst
.. start_hello_message

..

.. end_hello_message
```
The `..` (Sphinx empty comment) ensures `.. include::` directives in other files pull in non-empty content, preventing "Unexpected section title" errors.

### Step 4: Replace old hello message blocks
English docs use `.. include:: /index.rst` for the hello message. Replace old `.. note::` hello blocks in translation files:
```perl
perl -i -0777 -pe 's/^\.\. note::\s*\n\s*\n\s{4}.*?link_sf_facebook.*?\n\s*\n/.. include:: \/index.rst\n   :start-after: start_hello_message\n   :end-before: end_hello_message\n\n\n/s' "$file"
```
Skip `index.rst` and `conf.py`. Use `while IFS= read -r f` to handle filenames with spaces.

### Step 5: Apply mechanical term replacements
The `bf6d86f` commit renamed several terms. Apply the same changes in translation files using Perl:

**English → Target language term mapping:**

| English old | English new | Spanish | Chinese | Japanese | German | French |
|---|---|---|---|---|---|---|
| PWM Fan | CPU Fan | Ventilador PWM → Ventilador de la CPU | PWM 风扇 → CPU 风扇 | PWMファン → CPUファン | PWM-Lüfter → CPU-Lüfter | Ventilateur PWM → Ventilateur du CPU |
| RGB Fans | GPIO Fans | Ventiladores RGB → Ventiladores GPIO | RGB 风扇 → GPIO 风扇 | RGBファン → GPIOファン | RGB-Lüfter → GPIO-Lüfter | Ventilateurs RGB → Ventilateurs GPIO |

Also update the spec table in `index.rst`:
- `RGB Fans Number` / `Número de Ventiladores RGB` / `RGB 风扇数量` / `RGBファン数` / `Anzahl RGB-Lüfter` → GPIO equivalent

### Step 6: Apply small fixes (URLs, log paths, refs)

**Log paths** — replace old log paths in `hardware/io_board.rst` (both variants):
- `/opt/pironman5/log` → `/var/log/pironman5/pironman5.log`
- `/var/log/pironman5/pm_auto.oled.log` → `/var/log/pironman5/pironman5.log`

**35_screen URL** — in `optional_modules/35_screen.rst` (both variants):
- `http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi` → `https://docs.sunfounder.com/projects/35-ips-screen/en/latest/get_started/get_started.html`

**Duplicate link_openai_platform** — if `openclaw.rst` has a local `.. |link_openai_platform| raw:: html` definition, remove it. `conf.py` already defines it in `rst_epilog`.

**Anchor/Ref fixes** (must match English exactly):
- `pironman5` (base): `_set_up_pironman5` → `_set_up_pironman5_5`, `_view_control_commands` → `_view_control_commands_5`, `_view_control_dashboard` → `_view_control_dashboard_5`, `:ref:`standard_download_pironman5_module` → `:ref:`install_pironman5_module_5`
- `pironman5_max`: `_set_up_umbrel` → `_set_up_umbrel_max`, `.. include:: /pironman5_max/important_notice.rst` → remove it, `:ref:`max_download_pironman5_module` → `:ref:`install_pironman5_module_max`, `:ref:`max_view_control_dashboard` → `:ref:`view_control_dashboard`
- Remove commented Batocera line (`.. * For the **Batocera.linux**...`) in `control_pironman5.rst`

### Step 7: Translate RST files with content changes
For each RST file that actually changed in the commits, use background agents for efficiency. Give each agent a clear list of files and these rules:

**Translation rules:**
- Preserve ALL RST directives, anchors, images, code blocks exactly
- Keep technical terms as-is: GPIO, RGB, OLED, CPU, GPU, RAM, NVMe, SSD, I2C, PWM, PCIe
- Keep English anchors matching English exactly
- Adjust `===`/`---`/`^^^` underline to match translated title length (each CJK char ≈ 2 ASCII for underline width)
- No local `|link_xxx|` definitions — all links live in `conf.py`'s `rst_epilog`
- `conf.py`: keep translated link text (e.g., `aquí` not `here` in Spanish)

**For Chinese (docs-cn):** Use full-width punctuation: `，` `。` `、` `：` `（）`
**For Japanese (docs-ja):** Use full-width punctuation: `、` `。` `「」`
**For other languages:** Use standard punctuation for that language

**Files that always need checking** (from `bf6d86f` and `f3125f3` commits):

*pironman5 (base):*
- `set_up/set_up_rpi_os.rst` — curl installer, PiPower 5, model selection, component checklist, CPU fan curve
- `set_up/set_up_umbrel.rst` — Umbrel Community App Store (11 steps with screenshots)
- `set_up/set_up_pironman5.rst` — anchor fix only
- `control/control_with_dashboard.rst` — new Dashboard structure (Temperature/Storage/Memory/Network/Processor + Interface/OLED/RGB/GPIO Fans/System)
- `control/control_with_commands.rst` — JSON config with "system" wrapper, expanded help text
- `compitable_nvme_ssd.rst` — table format with 4 categories (Verified/Stable/Compatible/Not Recommended)
- `faq.rst` — add `.. start_faq_xxx`/`.. end_faq_xxx` markers around all sections
- `home_server/openclaw.rst` — ref fix

*pironman5_max:*
- `set_up/set_up_rpi_os.rst` — same as base but MAX-specific anchors
- `set_up/set_up_umbrel.rst` — same App Store method
- `control/control_with_dashboard.rst` — same as base + Fan LED (ON/OFF/FOLLOW)
- `control/control_with_commands.rst` — MAX-specific: `gpio_fan_led`, `-fl`/`-fp` options
- `faq.rst` — use `.. include:: ../pironman5/faq.rst` for shared sections
- `home_server/openclaw.rst` — ref fix

### Step 8: Fix title underlines
After translation, use this Perl script to auto-fix all title underlines that are too short:
```perl
perl -i -0777 -pe '
sub fix { my($t,$u)=@_; my $c=substr($u,0,1); my $n=length($t)+2; $c x $n }
s{^(.+)\n([\-]{3,}|[\^]{3,}|[\=]{3,})\n}{
  my $t=$1; my $u=$2;
  if(length($u)<length($t)){"$t\n".fix($t,$u)."\n"}
  else{"$t\n$u\n"}
}gem;
' <files>
```
This preserves the underline character (`---`, `===`, or `^^^`) and extends it to match the title width.

### Step 9: Verify
```bash
git status
```
After all changes, the user will compile and report errors. Fix any remaining WARNINGs or ERRORs.

### Step 10: Post-sync image verification (if image warnings appear)
If `sphinx-build` reports "image file not readable" warnings, the images likely exist in the git history of both branches but are missing from the working tree. This happens when images were added in English commits that predate the translation branch's fork point — `git diff` won't show them as different.

Quick fix — copy all missing images from the English source workspace:
```powershell
# From the translation workspace (e.g., pironman5-rtd-20260319-sync/pironman5)
# Copy images from English source (e.g., pironman5-rtd-20260319/pironman5)
$en = "../pironman5-rtd-20260319/pironman5/docs/source"
$de = "."

# Dashboard images (base)
Copy-Item "$en/pironman5/control/img/dashboard_*.png" "$de/docs/source/pironman5/control/img/" -Force
Copy-Item "$en/pironman5/control/img/dashboard_*.jpg" "$de/docs/source/pironman5/control/img/" -Force
# Dashboard images (MAX)
Copy-Item "$en/pironman5_max/control/img/dashboard_*.png" "$de/docs/source/pironman5_max/control/img/" -Force
Copy-Item "$en/pironman5_max/control/img/dashboard_*.jpg" "$de/docs/source/pironman5_max/control/img/" -Force
# Umbrel images
Copy-Item "$en/pironman5/set_up/img/umbrel_*" "$de/docs/source/pironman5/set_up/img/" -Force
Copy-Item "$en/pironman5_max/set_up/img/umbrel_*" "$de/docs/source/pironman5_max/set_up/img/" -Force
```
Or copy only the specific missing files listed in the warnings.

**Common build errors after sync:**

| Error | Cause | Fix |
|---|---|---|
| `Problem with "start-after" option of "include" directive: Text not found.` | `index.rst` missing `start_hello_message` marker | Add markers (Step 3) |
| `Unexpected section title.` | `.. include::` pulls empty content (promax files) | Add `..` between index.rst markers, or remove include from promax files that start with anchor→title |
| `Duplicate substitution definition name: "link_openai_platform"` | Local `\|link_openai_platform\|` in `openclaw.rst` | Remove local definition, keep conf.py global one |
| `undefined label: 'xxx'` | Anchor name mismatch between translation and English | Sync anchor to match English exactly |
| `Title underline too short.` | Translated title is longer than its underline | Run Step 8 auto-fix |
| `Failed to create a cross reference. A title or caption not found: 'xxx'` | Anchor exists but the section title following it is missing its underline (`---`/`===`/`^^^`). Translation agent may have omitted the underline when translating the title. | Add the missing underline after the translated section title. Example: `.. _install_sdrpp_5:` followed by `SDR++ (SDRpp)` with NO underline → add `^^^^^^^^^^^^^` |
| `image file not readable: path/to/image.png` | Image referenced in RST was added in a new English commit and committed to `origin/docs-de` via git checkout, but the working tree doesn't actually have the file. The `git diff origin/docs-de origin/docs` approach in Step 2 only catches files that DIFFER between branches — if the image already exists identically in both branches' git history, it won't appear in the diff. | Copy missing images manually from the English source workspace using `Copy-Item`. Run a post-sync check: `git status --short` should show the image files if they were properly checked out. |

## Key Design

### Hello message centralization
`docs/source/index.rst` contains the centralized hello message between `.. start_hello_message` and `.. end_hello_message` markers. All other RST files include it via:
```rst
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message
```
When updating the hello message, **only modify `index.rst`** — all other files inherit it automatically. Translation branches must keep these markers in place with translated text. For languages that don't use a hello message (e.g., Chinese), add empty markers with `..` between them.

### Include-based FAQ structure
`pironman5/faq.rst` contains `.. start_faq_xxx` / `.. end_faq_xxx` markers around each section. `pironman5_max/faq.rst` uses `.. include:: ../pironman5/faq.rst` to pull in shared sections. Translation branches inherit this structure — translating the base FAQ automatically propagates to variants.

### Anchor naming conventions
- `pironman5` (base): anchors use `_5` suffix, e.g., `.. _view_control_dashboard_5:`
- `pironman5_max`: anchors use `max_` prefix or no suffix, e.g., `.. _max_view_control_commands:`, `.. _view_control_dashboard:`
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
- `home_server/nextcloud.rst`, `home_server/plex.rst`
- `install/install_batocera.rst`, `install/install_raspberry_os.rst`, `install/install_umbrel.rst`
- `hardware/oled_screen.rst`, `hardware/power_switch_convertor.rst`, `hardware/tower_cooler.rst`

## Common Pitfalls

1. **Do NOT `git checkout origin/docs -- *.rst`** — this overwrites translations with English.
2. **Do NOT `git merge -X theirs`** — same problem.
3. **Do NOT `git merge -X ours`** — keeps old translation but blocks English structural updates.
4. **"Modified" RST files in diff are expected** — translated text differs from English. Focus on what COMMITS changed.
5. **File names with spaces** — use null-delimited xargs or `while IFS= read -r f`. Some branches use `control_with dashboard.rst` (space) while English uses `control_with_dashboard.rst` (underscore).
6. **Stash + branch switch = data loss** — avoid this pattern. Ask user to switch branches.
7. **Verify after batch edits** — spot-check files after Perl replacements.
8. **Promax files** — Chinese/Japanese promax files may start with `.. _anchor:` directly (no include). This is OK — don't force-add `.. include::` to these files.
9. **UTF-8 in titles** — Perl's `length()` counts bytes. For German `ü`/`ö`/`ä`, add +2 margin in underline auto-fix.
10. **Missing title underlines after translation** — Translation agents may produce section titles without their required RST underline (especially titles that immediately follow `.. _anchor:` directives). After translation, run Step 8 AND visually spot-check files with new anchors. Sphinx silently skips un-underlined titles and reports "title or caption not found" for any `:ref:` pointing to them.
11. **Images missing from working tree** — After Step 2 (sync non-RST files), images added in new English commits may still be absent from the translation working tree. This happens because images committed to both branches identically won't appear in `git diff`. After sync, verify with: `git status` — all new images should appear as staged changes (from `git checkout origin/docs --`). If the working tree is clean after Step 2 but images are missing, manually copy from the English source workspace.
12. **Step 8 must run AFTER all manual edits** — The title underline auto-fix must be the last step before verification. Any manual underline additions (e.g., fixing "title or caption not found" warnings) should be followed by another run of Step 8 to catch length mismatches.
13. **Cross-reference suffixes** — When translating, agents may use the wrong anchor suffix (e.g., `_max` in a base file, or `_5` in a MAX file). Step 6 catches known patterns, but new patterns may appear in fresh content. Always verify `:ref:` targets match the variant's anchor naming convention.

## Build

```bash
cd docs
pip install -r requirements.txt
sphinx-build -b html source build/html
```
Use `sphinx-build -E` for a clean build (clears cache).

## FAQ Editing Rules

### Where to write

| Content type | Where to put it | Pattern |
|---|---|---|
| Shared across ≥2 products | `pironman5/faq.rst` (base) with `start_xxx` / `end_xxx` markers | Other products `.. include::` it |
| Pro MAX only | `pironman5_promax/faq.rst` directly | No markers, no include |
| Mini only | `pironman5_mini/faq.rst` directly | No markers, no include |

**Decision flow**: Does this FAQ apply to more than one product? → Yes: base + markers + include. No: write directly.

### Which products have which features

| Feature | Base | MAX | Pro MAX | Mini |
|---|---|---|---|---|
| NVMe SSD | ✅ | ✅ dual | ✅ dual | ❌ |
| OLED screen | ✅ | ✅ | ✅ | ❌ |
| 4.3-inch DSI screen | ❌ | ❌ | ✅ | ❌ |
| Voice assistant | ❌ | ❌ | ✅ | ❌ |
| GPIO/RGB fans | ✅ | ✅ | ❌ (PWM only) | ✅ |
| 5-pin custom fans | ❌ | ❌ | ✅ | ❌ |

### Quick Troubleshooting: when to add

Add a Quick Troubleshooting entry when the issue is:
- A common hardware problem (power, screen, fan, NVMe, boot)
- Something a user would encounter during first setup

Skip Quick Troubleshooting for:
- Niche software/compatibility questions (piper-tts, Home Assistant OS)
- Advanced customization (custom OLED, HDMI screen arrangement)

### Anchor naming

- Base: `_xxx_5` suffix — `.. _faq_nvme_link_down_5:`
- MAX: `_xxx_max` suffix — `.. _faq_nvme_link_down_max:`
- Pro MAX: `_xxx_promax` suffix — `.. _faq_nvme_link_down_promax:`
- Mini: `_xxx_mini` suffix

### Common Sphinx errors when editing FAQ

| Error | Likely cause |
|---|---|
| `undefined label` | Missing anchor in target file (e.g., `safe_shutdown_promax` not defined in `set_up_rpi_os.rst`) |
| `duplicate label` | Anchor name reused across files without unique suffix |
| Include pulls nothing | `start-after` / `end-before` markers don't exist or are misspelled |

### Install command unification

All 4 products now use the same curl-based installer:
```shell
curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash
```
With a `.. tip::` for Ubuntu users to `sudo apt install curl -y` first. Model selection (1-4) happens interactively. Do NOT revert to `git clone -b <branch>`.
