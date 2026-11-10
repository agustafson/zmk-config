# Learning Colemak-DH and Miryoku on your Totem

This plan practises three things together: Colemak-DH letters, Miryoku's thumb layers and the punctuation you actually use in Go and TypeScript. Your everyday work supplies most of the practice; short sessions target the parts that feel uncertain. The timing below is a flexible starting point, not a deadline.

## Before you start

- **With the Totem:** use the macOS **U.S. or ABC** input source. The firmware already produces Colemak-DH; applying another layout on the Mac will remap it a second time.
- **Without the Totem:** leave the MacBook in QWERTY or use a separately installed Colemak-DH macOS input source. Apple's built-in Colemak is standard Colemak, not DH. If you use a DH source on the MacBook, switch back to U.S./ABC for the Totem unless you have independently configured per-device remapping. The [Colemak-DH project](https://colemakmods.github.io/mod-dh/) provides information about layouts and downloads.
- Keep the [base diagram](../draw/miryoku-base.png) and [all-layer diagram](../draw/miryoku-layers.png) visible. Check a website's on-screen keyboard carefully: it may show a conventional physical keyboard or standard Colemak rather than your split Totem and its layers. Trust the characters the site asks for and your diagram over its finger illustration.
- Use a relaxed hand position and take breaks. Try the physical keyboard and layer timings before making a major change. A short daily session is plenty to start; pause if you feel pain, tingling or persistent discomfort.

## A 25–30 minute practice session

1. **5 min — find letters.** Use [keybr](https://www.keybr.com/) or a slow alphabet/word exercise. Glance at the diagram when needed. Aim for relaxed, consistent fingers and low errors rather than speed.
2. **7 min — useful bigrams.** In [Ngram Type](https://ranelpadon.github.io/ngram-type/), try Bigrams, Top 50, Combination 3 and Repetition 3. Include pairs such as `th he in er an re on at en nd`. Gradually increase Combination to 5–10, then lower Repetition toward 1. Keep speed thresholds low enough that you aren't trapped. Its [instructions](https://github.com/ranelpadon/ngram-type#features) describe the lesson controls and Custom data source.
3. **4 min — trigrams and awkward pairs.** Choose common trigrams or enter a few of your own difficult pairs in Ngram Type's Custom data source. Focus on clean transitions, especially common patterns involving the DH positions. [TypingFirst's bigram lesson](https://www.typingfirst.com/ngram-typing-practice/bigram-part-1.htm) is a simple alternative.
4. **5 min — ordinary text.** In [Monkeytype](https://monkeytype.com/), choose an English word test and practise at a comfortable pace. Once the letters feel less surprising, turn on its **punctuation** option; try **numbers** separately before combining them. Its [project documentation](https://github.com/monkeytypegame/monkeytype#features) lists both modes.
5. **5–9 min — symbols and real code.** Work through one of the symbol drills below, then a short Go or TypeScript example in a scratch editor or code trainer. Start this on day one, even if you spend just a minute or two. Finish by practising a few real navigation or shortcut actions.

Two shorter sessions can be easier to sustain. An accuracy target around 95–98% is a practical personal guide, not a scientifically established requirement; go slower when errors become frequent. Don't force a WPM target or perfect runs. WPM in prose, code, symbols and normal work measures different things.

## Which sites help with symbols?

- **Monkeytype:** punctuation and numbers modes make a useful bridge from plain prose to mixed text. They do not guarantee a useful distribution of code syntax, so complement them with code-specific practice. Its custom text mode is another option for your own short examples; the site's behaviour and available controls can change.
- **Ngram Type:** the Custom data source lets you supply short tokens for practising a difficult pattern such as `:=`, `=>`, `!=`, `[]` or `${`. Try a small set first; its lesson generator is word-oriented, so use a code trainer or editor for multiline snippets and exact spacing. [Ngram Type features](https://github.com/ranelpadon/ngram-type#features).
- **Code trainers:** [Typre](https://www.typre.dev/) lists Go, TypeScript, JavaScript, Python and Rust plus a special-character drill. [typing.io](https://typing.io/) uses open-source code and has JavaScript lessons; its [pricing page](https://typing.io/pricing) lists free lessons and paid custom code uploads. Try them and keep whichever feels comfortable; don't assume their keyboard diagrams understand layers.
- **Scratch editor:** best for practising the full workflow, including Tab, Enter, auto-paired brackets, selection, navigation and shortcuts. A typing test sees the resulting characters, but generally cannot tell whether you used the intended layer or chord. If auto-pairing interferes with a drill, temporarily turn it off in the scratch file or practise with it deliberately enabled.

Only paste code into third-party websites if you're allowed to share it. The examples below are safe practice text; keep private work code in your own editor.

## Symbol and layer drills

Use the layer diagram rather than memorising everything at once. Hold the **right inner Enter thumb for Sym** and the **right Backspace thumb for Num**. Practise deliberately pressing the target key while holding the layer, releasing the layer, and returning to letters. First type each group slowly, then mix it into words or code:

1. **Pairs:** `()` `{}` `[]` `<>`. Try `(name)`, `{value}`, `[index]` and `<Type>`; include the closing character every time.
2. **Operators and separators:** `=` `+` `-` `_` `:` `;` `/` and `\`. Then `:=`, `!=`, `==`, `=>`, `->`, `&&`, `||` and `//`.
3. **Numbers:** on Num, practise `123 456 789 0`, then realistic values such as `8080`, `2026-11-11` and `v1.2.3`. For sustained entry, practise the Miryoku layer lock and its exit action from the layout guide. It stays locked until explicitly changed; this is not automatic Num Word.
4. **Backticks:** on Base, try the **F+P** chord and practise `` ` `` inside a template or Markdown fragment. The keymap also has backtick on Nav and Fun. Practise `Cmd+backtick` separately for macOS window cycling.
5. **Fence:** W+F+P emits the Raycast trigger `;;fence`; with the provided Raycast snippet configured, it should expand into a fenced block. It doesn't send Enter. First test in a scratch document, then an unsent draft in each browser, desktop and terminal agent you actually use. Expansion and insertion are controlled by Raycast and the host app; do not assume every input field handles multiline text the same way.

Use the unmodified character as the goal, not an assumption about physical keys: for example, a character on Sym might already include a Shift modifier in its firmware binding. Practise code with the actual hold and release actions used by your layout.

## Practice snippets

Type these manually in a scratch editor, or choose comparable public examples in a code trainer:

```go
func readConfig(path string) (Config, error) {
    if err != nil { return Config{}, err }
    return cfg, nil
}
```

```ts
const message = `hello ${user.name}`;
const items = list.filter((item) => item.active);
const by_id: Record<string, number> = { count: 42 };
```

Then try changing `42`, selecting a word, copying and pasting it, and moving by arrow and page. Include brackets, braces, quotes, underscore, colon and backtick over the course of a week. Separately practise holding the Mouse layer, moving the pointer, scrolling and clicking, then use Homerow for an actual target.

## Progress over the first few weeks

- **Days 1–3:** locate letters, Space, Backspace, Escape, Sym and Num; try a little real typing and a few symbols each day. Look at the diagram freely.
- **Days 4–7:** mix bigrams into words, and practise pairs of symbols in realistic short fragments. Try common Mac shortcuts and navigation. Adjust timings if modifiers or combos repeatedly misfire.
- **Weeks 2–3:** let real work be the largest share. Spend drill time on the particular letter transitions, layer changes or symbols you find slow. Compare a consistent 30–60-second Monkeytype prose test a few times a week and keep any code practice score separate.
- **Later:** keep a short warm-up if useful. Judge progress by relaxed accuracy, coding flow, reliable shortcuts and comfort during normal work rather than a single best WPM score.

## Homerow and extras

The left far-pinky key is **Hyper** (Cmd+Ctrl+Option+Shift); the right far-pinky key is **Meh** (Ctrl+Option+Shift). These are held modifiers, not standalone Homerow actions: assign a suitable Hyper- or Meh-plus-key shortcut in Homerow and check for conflicts. Use those actions in ordinary work, and compare them with the Mouse layer and your trackpad. Avoid changing several key positions at once unless something is uncomfortable or unreliable.

When checking progress, note frequent mistakes, layer/shortcut misfires, fatigue and the tasks that are getting easier. A trainer score alone does not establish an improvement in programming speed or comfort.
