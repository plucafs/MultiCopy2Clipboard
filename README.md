# MultiCopy2Clipboard
Copy a note field's text during reviews

<a href="#install">Install</a>
<span>&nbsp;&nbsp;-&nbsp;&nbsp;</span>
<a href="#usage">Usage</a>
<span>&nbsp;&nbsp;-&nbsp;&nbsp;</span>
<a href="#configs">Configs</a>
<span>&nbsp;&nbsp;-&nbsp;&nbsp;</span>
<a href="#credits">Credits</a>

### Install
[⮤ Back to top](#multicopy2clipboard)
1. Open Anki
2. Open the addons window (Tools > Add-ons)
3. Click on Get addons...
4. Paste the addon id: 2060281054 ([addon page](https://ankiweb.net/shared/info/2060281054))
5. Click on Ok

### Usage
[⮤ Back to top](#multicopy2clipboard)
1. Open the Addons window (Tools > Add-ons)
2. Select the MultiCopy2Clipboard addon
3. Click on Config
4. Place the note field value you want to copy based on the review state (during question or answer)
5. Place (eventually) the fallback values up to 9

### Configs
[⮤ Back to top](#multicopy2clipboard)
| Config                      | Example                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| questionField / answerField | "questionField0": "Front",<br>"answerField0": "" | Inside the **questionField0**, place the name of the note field you want to copy when the question is displayed.<br><br>Inside the **answerField0**, place the name of the note field you want to copy when the answer is displayed.<br><br>Each subsequent questionField and answerField (1, 2, 3, ...) are used as **fallbacks**. They'll be used until a value can be found.<br><br>You can populate only the questionField(s) or answerField(s). |
| stripHtml                   | `100％の<b>ジュース</b>。 ⟶ 100％のジュース。`                 | Determines if the html from the text of the note field will be removed or not.                                                                                                                                                                                                                                                                                                                                                                       |
| stripFurigana               | `僕[ぼく]が正[まさ]しく導[みちび]かないと ⟶ 僕が正しく導かないと`           | Determines if the furigana from the text of the note field will be removed or not.                                                                                                                                                                                                                                                                                                                                                                   |


#### Credits
[⮤ Back to top](#multicopy2clipboard)

Based on [1525025114](https://web.archive.org/web/20221024213458/https://ankiweb.net/shared/info/1525025114)

See the \_\_init\_\_.py file for a complete overview of the edits
