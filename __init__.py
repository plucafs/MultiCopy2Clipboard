# -*- coding: utf-8 -*-
#  Copyright (C) 2012 Christopher Brochtrup
#
#  This file is part of Copy2Clipboard
#
#  Copy2Clipboard is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Copy2Clipboard is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Copy2Clipboard. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
# Description:
#
# Copy2Clipboard will automatically copy a single card field to the clipboard
# when either the card's question side is shown or when the card's answer side
# is shown (or both, if desired).
#
# There are up to 10 (from 0 to 9) fallback values in case a field can't be found.
# The fields are checked in order, and the first value found is returned.
#
# Default behavior:
#
#   * When the card's question is shown:
#       Nothing will be copied to the clipboard.
#
#   * When the card's answer is shown:
#       The card's "Front" field will be copied to the clipboard (if one exists).
#
# To change the default behavior simply edit the questionField0 or answerField0
# variables via Anki - Tools - Add-ons - copy2clipboard - Config.
#
###############################################################################
# Version: 1.1
# Tested with Anki 2.0.3
# Contact: cb4960@gmail.com
###############################################################################
# Version: 1.2
# Tested with Anki 2.1.5
# Contact: kelciour@gmail.com
###############################################################################
# Version: 1.3, 1.4
# Tested with Anki 24.06.3
# Contact: plucafz@proton.me
###############################################################################

#### Includes ####

import re 
from io import StringIO
from html.parser import HTMLParser
from aqt import mw
from aqt.reviewer import Reviewer
from anki.hooks import wrap
try:
    from PyQt6.QtWidgets import QApplication
except ImportError:
    try:    
        from PyQt5.QtWidgets import QApplication
    except ImportError:
        from PyQt4.QtGui import QApplication

#### Functions ####

# Reference: https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()


def do_strip_html(text):
    s = MLStripper()
    s.feed(text)
    return s.get_data()


def do_strip_furigana(text):
    """
    Removes the text inside the opening ([) and closing (]) square brackets.

    Removes the brackets.

    Useful for stripping furigana from japanese sentences formatted like this:

    僕[ぼく]が正[まさ]しく導[みちび]かないと ⟶ 僕が正しく導かないと
    """
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in text:
        if i == '[':
            skip1c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret


def copy_text_to_clipboard(text, strip_html, strip_furigana):
    clipboard = QApplication.clipboard()
    if strip_html:
        text = do_strip_html(text)
    if strip_furigana:
        text = do_strip_furigana(text)
    clipboard.setText(text)


def copy_field(field_to_copy, strip_html, strip_furigana, card):
    is_copied = False
    for field in card.model()['flds']:
        fieldName = field['name']
        if(fieldName == field_to_copy):
            value = card.note()[fieldName]
            copy_text_to_clipboard(value, strip_html, strip_furigana)
            is_copied = True
    return is_copied


def _on_show_question(self):
    config = mw.addonManager.getConfig(__name__)
    for i in range(0, 9):
        field = config['questionField' + str(i)]
        strip_html = config['stripHtml']
        strip_furigana = config['stripFurigana']
        is_copied = copy_field(field, strip_html, strip_furigana, self.card)
        if not is_copied:
            continue
        return


def _on_show_answer(self):
    config = mw.addonManager.getConfig(__name__)
    for i in range(0, 9):
        field = config['answerField' + str(i)]
        strip_html = config['stripHtml']
        strip_furigana = config['stripFurigana']
        is_copied = copy_field(field, strip_html, strip_furigana, self.card)
        if not is_copied:
            continue
        return


#### Main ####

Reviewer._showQuestion = wrap(Reviewer._showQuestion, _on_show_question)
Reviewer._showAnswer = wrap(Reviewer._showAnswer, _on_show_answer)