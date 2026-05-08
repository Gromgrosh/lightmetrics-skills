#!/usr/bin/env bash
# figma-audit installer — symlinks this folder into ~/.claude/skills/figma-audit

set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$HOME/.claude/skills/figma-audit"

# 1. Verify SKILL.md is in this folder
if [ ! -f "$SOURCE_DIR/SKILL.md" ]; then
    echo "ERROR: SKILL.md not found in $SOURCE_DIR" >&2
    echo "Run this script from the figma-audit-share folder." >&2
    exit 1
fi

# 2. Ensure ~/.claude/skills exists
mkdir -p "$HOME/.claude/skills"

# 3. Handle existing install
if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
    if [ -L "$TARGET" ]; then
        EXISTING="$(readlink "$TARGET")"
        if [ "$EXISTING" = "$SOURCE_DIR" ]; then
            echo "✓ Symlink already points to $SOURCE_DIR — nothing to do."
            exit 0
        fi
        echo "Existing symlink: $TARGET -> $EXISTING"
    else
        echo "Existing item at $TARGET (not a symlink)"
    fi
    read -r -p "Replace it with a symlink to $SOURCE_DIR? [y/N] " confirm
    case "$confirm" in
        y|Y|yes|YES) rm -rf "$TARGET" ;;
        *) echo "Aborted." ; exit 1 ;;
    esac
fi

# 4. Create the symlink
ln -s "$SOURCE_DIR" "$TARGET"
echo "✓ Symlinked $TARGET -> $SOURCE_DIR"

# 5. Verify
if [ ! -f "$TARGET/SKILL.md" ]; then
    echo "ERROR: Symlink created but $TARGET/SKILL.md is not readable." >&2
    exit 1
fi

echo "✓ Install complete."
echo ""
echo "Next: restart Claude Code (or reload skills) to pick up figma-audit."
echo "Then invoke: \"Audit this Figma file: <figma-url>\""
