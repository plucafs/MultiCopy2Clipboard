### MultiCopy2Clipboard

#### questionField and answerField0

Inside the **questionField0**, place the name of the note field you want to copy when the question is displayed.

Inside the **answerField0**, place the name of the note field you want to copy when the answer is displayed.

Each subsequent questionField and answerField (1, 2, 3, ...) are used as **fallbacks**.
They'll be used until a value can be found.

You can populate only the questionField(s) or answerField(s)

---

#### stripHtml

**stripHtml** determines if the html from the text of the note field will be removed or not.

e.g. `100％の<b>ジュース</b>。 ⟶ 100％のジュース。` 

(the **b** tag is removed)


