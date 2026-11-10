# Combo reference

Chords are physical positions named by the Colemak-DH base layer. Keys are pressed together. On home-row combos, the tap is shown first and the combined modifier hold after `/`. A dash means the tap has no action.

| Left-hand chord | Action | Right-hand chord | Action |
|---|---|---|---|
| W+F | Esc | L+U | `#` |
| F+P | Backtick | U+Y | `*` |
| W+P | `@` | L+Y | `+` |
| W+F+P | Raycast fence | Y+' | `&` |
| Q+W | `$` | N+E | `(` / Shift+Cmd |
| R+S | Tab / Shift+Opt | E+I | `)` / Shift+Opt |
| S+T | — / Shift+Cmd | N+I | `-` / Cmd+Opt |
| R+T | `=` / Opt+Cmd | N+E+I | `_` / Shift+Opt+Cmd |
| R+S+T | — / Shift+Opt+Cmd | I+O | `^` / Opt+Ctrl |
| A+R | `%` / Ctrl+Opt | H+comma | `[` |
| X+C | Copy | comma+period | `]` |
| C+D | Paste | H+period | `/` |
| X+D | Cut | H+comma+period | `|` |
| X+C+D | `\` | period+? | `~` |
| Z+X | Undo | | |

On Nav, N+E / E+I send `<` / `>` and H+comma / comma+period send `{` / `}`. On Base/Num, Shift changes the parentheses to angle brackets and the square brackets to braces. F+P is limited to Base/Nav to avoid intercepting 8 and 9 on the number layer; the fence is Base only.

Most chords use 18 ms with a 150 ms prior-idle gate. F+P and W+F+P use 50 ms with no idle gate. These are starting values and need real-world testing. Overlapping pairs and triples may delay recognition or produce a different result when not all fingers arrive together. Avoid relying on W+F+P until the Raycast snippet has been tested in a safe field.
