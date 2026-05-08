#!/usr/bin/env bash
# sync-from-canonical.sh — refresh this share folder from the canonical skill
#
# Usage:
#   ./sync-from-canonical.sh             # interactive: shows diff, asks before applying
#   ./sync-from-canonical.sh --apply     # non-interactive: apply without prompting
#   ./sync-from-canonical.sh --dry-run   # show what would change, don't write
#
# Maintainer-only script. Recipients of the share folder should not run this —
# they don't have the canonical folder.

set -euo pipefail

SHARE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CANONICAL_DIR="$(cd "$SHARE_DIR/../figma-audit-skill" 2>/dev/null && pwd || true)"

# 1. Verify canonical folder exists alongside this share folder
if [ -z "$CANONICAL_DIR" ] || [ ! -f "$CANONICAL_DIR/SKILL.md" ]; then
    echo "ERROR: Canonical figma-audit-skill folder not found." >&2
    echo "Expected: $SHARE_DIR/../figma-audit-skill/SKILL.md" >&2
    echo "" >&2
    echo "This script is intended to be run from inside the figma-audit-share folder," >&2
    echo "in a checkout that has both figma-audit-skill/ and figma-audit-share/ as siblings." >&2
    exit 1
fi

# 2. Parse flags
MODE="interactive"
for arg in "$@"; do
    case "$arg" in
        --apply)   MODE="apply" ;;
        --dry-run) MODE="dry-run" ;;
        -h|--help)
            head -12 "$0" | tail -11
            exit 0
            ;;
        *) echo "Unknown flag: $arg" >&2 ; exit 2 ;;
    esac
done

echo "Canonical: $CANONICAL_DIR"
echo "Share:     $SHARE_DIR"
echo ""

# 3. Show what would change
echo "=== Diff (canonical → share) ==="
DIFF_OUTPUT=$(diff -rq "$CANONICAL_DIR/SKILL.md" "$SHARE_DIR/SKILL.md" 2>/dev/null || true)
if [ -n "$DIFF_OUTPUT" ]; then
    echo "$DIFF_OUTPUT"
fi
diff -rq "$CANONICAL_DIR/references" "$SHARE_DIR/references" 2>/dev/null | grep -v -E "^Only in $SHARE_DIR" || true
echo ""

# 4. Detailed diff per file
CHANGED=0
for src in "$CANONICAL_DIR/SKILL.md" "$CANONICAL_DIR/references"/*.md; do
    rel="${src#$CANONICAL_DIR/}"
    dst="$SHARE_DIR/$rel"
    if [ ! -f "$dst" ]; then
        echo "NEW: $rel (in canonical, not in share)"
        CHANGED=1
    elif ! cmp -s "$src" "$dst"; then
        echo "CHANGED: $rel"
        CHANGED=1
    fi
done

if [ "$CHANGED" -eq 0 ]; then
    echo "✓ Share folder is already in sync with canonical. Nothing to do."
    exit 0
fi
echo ""

# 5. Apply
case "$MODE" in
    dry-run)
        echo "(--dry-run: no files written.)"
        exit 0
        ;;
    interactive)
        read -r -p "Apply changes to share folder? [y/N] " confirm
        case "$confirm" in
            y|Y|yes|YES) ;;
            *) echo "Aborted." ; exit 1 ;;
        esac
        ;;
    apply) ;;
esac

# Copy SKILL.md and all reference files. Preserve mtimes.
cp -p "$CANONICAL_DIR/SKILL.md" "$SHARE_DIR/SKILL.md"
cp -p "$CANONICAL_DIR/references"/*.md "$SHARE_DIR/references/"

echo "✓ Synced canonical → share."
echo ""
echo "Next steps for publishing the update:"
echo "  - Review: git diff Projects/Lightmetrics/figma-audit-share/"
echo "  - Commit: git add Projects/Lightmetrics/figma-audit-share/ && git commit"
echo "  - If the share folder is its own repo: cd into it, commit, push, tag a release."
