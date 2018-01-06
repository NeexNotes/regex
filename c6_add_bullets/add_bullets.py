#! python3

import pyperclip

# grab data from clipboard
text = pyperclip.paste()

# add * bullets to every line
lines = text.split("\n")  # split text on new line characters
for line in range(len(lines)):
    lines[line] = "* " + lines[line]  # add * to each line

# join text back with the same split/join character
text = "\n".join(lines)

# export back to clipboard
pyperclip.copy(text)
