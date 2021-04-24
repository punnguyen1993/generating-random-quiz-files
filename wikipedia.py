#! python3
#bulletpoint.py - add star to wikipedia

import pyperclip

m = pyperclip.paste()

# execute code with m
m_sp = m.split("\n")
for i in range(len(m_sp)):
    m_sp[i] = "* " + m_sp[i]
new_m = "\n".join(m_sp)

pyperclip.copy(new_m)
