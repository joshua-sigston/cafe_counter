# Project 1 — Cafe Counter

A terminal cafe. The customer types commands. You look up prices in a dictionary, keep a cart, and never crash on bad typing.

This is the same thinking as Minesweeper’s difficulty menu and `reveal 2 3` parser, without a grid.

---

## What you are making

```text
Welcome to Byte Cafe
Commands: menu, add <item>, remove <item>, cart, checkout, quit

> menu
  muffin  $3
  tea     $2
  soup    $5

> add muffin
Added muffin. Cart total: $3

> add banana
We don't sell banana. Type menu to see items.

> checkout
You ordered: muffin
Total: $3
Thanks!
```

---

## Skills this trains

| Skill | Where it shows up | Later in Minesweeper |
| --- | --- | --- |
| Dictionary | `MENU["muffin"]` is a price | `DIFFICULTIES["beginner"]` is a size |
| `while True` until valid | Bad item name asks again | Bad difficulty asks again |
| `.strip()` and `.lower()` | `Add Muffin` still works | `Reveal 2 3` still works |
| `.split()` | `"add muffin"` → `["add", "muffin"]` | `"flag 2 3"` → `["flag", "2", "3"]` |
| Check `len(parts)` first | `"add"` alone does not crash | `"reveal"` alone does not crash |
| `return` vs `print` | Helpers hand data back | `choose_difficulty()` returns a dict |

---

## Files to create

```text
01-cafe-counter/
├── PROJECT_GUIDE.md    # this file
├── main.py             # starts the program
└── cafe.py             # menu, cart, command parser
```

A one-file version is fine if imports bother you.

Run from this folder:

```bash
python3 main.py
```

---

## Step 1 — Welcome and Git

Create `main.py` that prints a cafe name.

```bash
python3 --version
python3 main.py
git init
git add .
git commit -m "Start cafe counter project"
```

**Checkpoint:** you see the welcome line. You have one commit.

---

## Step 2 — The menu dictionary

**The idea:** a dictionary maps a word to a value. You ask “what does muffin cost?” and get `3`.

**What `MENU` is supposed to do:** answer “is this a real item?” and “what does it cost?”

```python
MENU = {
    "muffin": 3,
    "tea": 2,
    "soup": 5,
}
```

Write `show_menu()` that **prints** every item and price. Loop the dictionary:

```python
for name, price in MENU.items():
    print(name, price)
```

**Checkpoint:** running the file prints three items. Commit.

---

## Step 3 — `choose_item()` (valid names only)

**The idea:** never assume the human typed a real key. Check first.

**What it is supposed to do:**

1. Ask for an item name.
2. Clean it: `.strip().lower()`.
3. If that name is in `MENU`, **return** the name (the string).
4. If not, print a short message and ask again.

```python
def choose_item():
    while True:
        name = input("Item: ").strip().lower()
        if name in MENU:
            return name
        print("We don't sell that. Try again.")
```

`name in MENU` is `True` only when `name` is one of the keys. Only then is `MENU[name]` safe.

Test with `muffin`, `MUFFIN`, ` banana `, and `pizza`.

**Checkpoint:** valid names return a string. Invalid names ask again. No crash. Commit.

Common mistake: `print(name)` but never `return name`. Then the caller gets `None`.

---

## Step 4 — Parse a whole command

**The idea:** one typed line can be several words. Split it, then look at the first word.

**What `parse_command(user_text)` is supposed to do:** turn a string into a tuple the rest of the program can use.

| They type | After `.split()` | You return |
| --- | --- | --- |
| `menu` | `["menu"]` | `("menu",)` |
| `quit` | `["quit"]` | `("quit",)` |
| `cart` | `["cart"]` | `("cart",)` |
| `checkout` | `["checkout"]` | `("checkout",)` |
| `add muffin` | `["add", "muffin"]` | `("add", "muffin")` |
| `remove tea` | `["remove", "tea"]` | `("remove", "tea")` |
| `add` | `["add"]` | `("invalid", "add needs an item")` |
| `banana` | `["banana"]` | `("invalid", "unknown command")` |
| empty Enter | `[]` | `("invalid", "type a command")` |

**How to write it:**

```python
def parse_command(user_text):
    parts = user_text.strip().lower().split()
    # 1. If parts is empty, return invalid
    # 2. command = parts[0]
    # 3. If command is menu, quit, cart, or checkout: return that
    # 4. If command is add or remove:
    #        if len(parts) != 2: return invalid
    #        else return (command, parts[1])
    # 5. Otherwise return invalid
```

**Check `len(parts)` before `parts[1]`.** That is the crash you are training yourself not to hit.

Test `parse_command` by itself with `print`. Do not wire the cafe loop yet.

**Checkpoint:** every row in the table above behaves. Commit.

---

## Step 5 — The cart

**The idea:** the cart is a **list** of item names. Adding appends. Removing takes one copy out.

**What it is supposed to do:**

- `add_to_cart(cart, name)` — if `name` is in `MENU`, append it. Else print why not.
- `remove_from_cart(cart, name)` — if that name is in the list, `.remove(name)` once. Else say it is not in the cart.
- `cart_total(cart)` — **return** (do not only print) the sum of `MENU[item]` for each item in the cart.
- `show_cart(cart)` — print the items and the total.

Start with `cart = []` in the main loop.

**Checkpoint:** add two muffins and one tea. Total is 8. Remove one muffin. Total is 5. Commit.

---

## Step 6 — The cafe loop

**What `run_cafe()` is supposed to do:** greet, then repeat until quit or checkout.

```text
cart = []
while True:
    read a line
    parse it
    if invalid: print the reason; continue
    if menu: show_menu()
    if cart: show_cart(cart)
    if add: add_to_cart(...)
    if remove: remove_from_cart(...)
    if checkout: print the total; break
    if quit: break
```

`main.py` should only start it:

```python
from cafe import run_cafe

if __name__ == "__main__":
    run_cafe()
```

Do not call `run_cafe()` at the bottom of `cafe.py` unless that call is inside `if __name__ == "__main__":`. Otherwise importing the file starts the cafe twice.

**Checkpoint:** you can order, make a typo, fix it, check out, and quit. No traceback. Commit.

---

## Testing checklist

- [ ] `MENU` lookup works for every item
- [ ] Unknown item on `add` does not crash
- [ ] `add` with no item name does not crash
- [ ] `ADD MUFFIN` works (capitals and spaces)
- [ ] Checkout prints the right total
- [ ] `quit` leaves the program
- [ ] Empty Enter prints a friendly message

---

## Thinking pattern to keep

> **Never trust typed text.** Clean it, split it, check the length, check the key, then use it.

When you write Minesweeper’s `parse_command("reveal 2 3")`, this is the same function with coordinates instead of muffins.