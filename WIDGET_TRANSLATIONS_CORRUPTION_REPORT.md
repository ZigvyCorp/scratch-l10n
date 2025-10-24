# Widget Translations Corruption Report
## GUI Locale Files Analysis

**Analysis Date:** 2025-10-24
**Analyzed Files:**
- `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/en.json`
- `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/ja.json`
- `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/de.json`
- `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/pt.json`

**Reference Files:**
- `/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/ja.json`
- `/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/de.json`
- `/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/pt.json`

---

## Executive Summary

**Total widget entries per language:** 117

### Problematic Entries Count

| Language | Total Entries | Problematic | Percentage | Status |
|----------|---------------|-------------|------------|---------|
| Japanese | 117 | 60 | 51% | Mostly parameter order issues |
| German | 117 | 101 | 86% | **SEVERE CORRUPTION** |
| Portuguese | 117 | 101 | 86% | **SEVERE CORRUPTION** |

**Total widget entries needing fixes:** 262

---

## Japanese (ja.json) - 60 Issues

### Issue Types:
- **Parameter order differences:** Most issues are minor parameter ordering differences
- **English text:** 8 entries contain untranslated English
- **Translation variants:** Different word choices than reference l10n

### Critical Issues:

1. **Untranslated English:**
   ```json
   "widget.disableWidget": "[DISABLE] widget [NAME]"
   "widget.disable": "Disbale"  // Typo in English!
   "widget.enable": "Enable"
   "widget.chat.robot": "ROBOT"
   "widget.chat.user": "USER"
   "widget.image.keep": "keep"
   "widget.image.stretch": "stretch"
   "widget.camera.flipped": "flipped"
   ```

2. **Examples of Parameter Order Issues:**
   - GUI: `"動画 [NAME] を [ACTION]"`
   - L10N: `"動画 [ACTION] を [NAME]"`

### Recommendation for Japanese:
Most issues are minor. Consider copying from l10n for consistency, but current GUI translations are functional.

---

## German (de.json) - 101 Issues (CRITICAL)

### Corruption Patterns Detected:

**Severely Corrupted Words:**
- `pfügeing` (should be: `Abstand` or `padding`)
- `Positiein` (should be: `Position` or `bei`)
- `Rest veine` (should be: `Modus`)
- `butaufns` (should be: `Schaltflächen`)
- `saufppe` / `saufppeped` (should be: `stop` / `gestoppt`)
- `regehe` (should be: `entferne`)
- `hinterstegrunde` (should be: `Hintergrund`)
- `boderder` (should be: `Rahmen`)
- `neindermal` (should be: `normal`)
- `ceinfirm` (should be: `bestätige`)
- `Neine` (should be: `None`)
- `Eingabetastes` (gibberish)
- `hoderizeintal` (should be: `horizontal`)
- `ceintainer` (should be: `Container`)
- `aufolbox` (should be: `Werkzeugkasten`)
- `icein` (should be: `Symbol`)
- `rotan Positieine` (should be: `rotiere`)
- `chan Positiein` (should be: `Chat`)
- `upDan Positieinum` (should be: `aktualisiere`)

### Examples of Severely Corrupted Entries:

1. **widget.addTextbox:**
   - **GUI (CORRUPTED):** `"füge textbox an Positiein X [X] Y [Y] width [WIDTH] height [HEIGHT] pfügeing [PADDING] line [MULTIPLELINE] scroll [SCROLL] Rest veine [MODE] as [NAME]"`
   - **L10N (CORRECT):** `"füge Textfeld hinzu bei X [X] Y [Y] Breite [WIDTH] Höhe [HEIGHT] Abstand [PADDING] Zeile [MULTIPLELINE] Scrollen [SCROLL] Modus [MODE] als [NAME]"`

2. **widget.menuItem.stop:**
   - **GUI (CORRUPTED):** `"saufppe"`
   - **L10N (CORRECT):** `"stop"`

3. **widget.setWidgetStyle:**
   - **GUI (CORRUPTED):** `"setze widget hinterstegrunde Farbe [BGCOLOR] boderder Farbe [BORDERCOLOR] boderder width [BORDERWIDTH] boderder radius [BORDERRADIUS] für [NAME]"`
   - **L10N (CORRECT):** `"setze Widget-Hintergrundfarbe [BGCOLOR] Rahmenfarbe [BORDERCOLOR] Rahmenbreite [BORDERWIDTH] Rahmenradius [BORDERRADIUS] für [NAME]"`

4. **widget.confirmTextWithButtons:**
   - **GUI (CORRUPTED):** `"ceinfirm [NAME] durch butaufns [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]"`
   - **L10N (CORRECT):** `"bestätige [NAME] mit Schaltflächen [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]"`

5. **widget.whenVideoStopped:**
   - **GUI (CORRUPTED):** `"Wenn video [NAME] saufppeped"`
   - **L10N (CORRECT):** `"wenn Video [NAME] gestoppt wird"`

6. **widget.updateLastChatMessage:**
   - **GUI (CORRUPTED):** `"upDan Positieinum last chan Positiein message auf [NEWMSG] für chan Positiein [NAME]"`
   - **L10N (CORRECT):** `"aktualisiere letzte Chat-Nachricht auf [NEWMSG] für Chat [NAME]"`

7. **widget.drawChartUsingList:**
   - **GUI (COMPLETELY ENGLISH):** `"draw [CHARTTYPE] chart using list [LIST] x [X] y [Y] width [WIDTH] height [HEIGHT] as [NAME]"`
   - **L10N (CORRECT):** `"zeichne [CHARTTYPE]-Diagramm mit Liste [LIST] x [X] y [Y] Breite [WIDTH] Höhe [HEIGHT] als [NAME]"`

---

## Portuguese (pt.json) - 101 Issues (CRITICAL)

### Corruption Patterns Detected:

**Severely Corrupted Words:**
- `adiciligadoe` (should be: `adicione`)
- `padiciligadoeing` (should be: `preenchimento`)
- `queo` (should be: `quando`)
- `fou` (should be: `for` / `clicado`)
- `butparan` / `butparans` (should be: `botão` / `botões`)
- `pareped` (should be: `parado`)
- `cligadofirm` (should be: `confirmar`)
- `trásgarredligadode` (should be: `fundo`)
- `bouder` (should be: `borda`)
- `fligadot` (should be: `fonte`)
- `nãomed` (should be: `chamado`)
- `na posiçãoual` (should be: `atual`)
- `rna posiçãoio` (should be: `proporção`)
- `sengle` (should be: `single`)
- `ligadoly` (should be: `leitura`)
- `nãoumal` (should be: `normal`)
- `escligadoda` (should be: `esconda`)
- `Nligadoe` (should be: `None`)
- `houizligadotal` (should be: `horizontal`)
- `cligadotainer` (should be: `contêiner`)
- `cna posiçãoegouy` (should be: `categoria`)
- `parna posiçãoal` (should be: `total`)
- `chna posição` (should be: `chat`)
- `icligado` (should be: `ícone`)
- `updna posiçãoa` (should be: `atualize`)
- `paraolbox` (should be: `caixa de ferramentas`)
- `useng` (should be: `using`)

### Examples of Severely Corrupted Entries:

1. **widget.addTextbox:**
   - **GUI (CORRUPTED):** `"adiciligadoe textbox na posição X [X] Y [Y] width [WIDTH] height [HEIGHT] padiciligadoeing [PADDING] line [MULTIPLELINE] scroll [SCROLL] resto dee [MODE] as [NAME]"`
   - **L10N (CORRECT):** `"adicione caixa de texto em X [X] Y [Y] largura [WIDTH] altura [HEIGHT] preenchimento [PADDING] linha [MULTIPLELINE] rolagem [SCROLL] modo [MODE] como [NAME]"`

2. **widget.whenWidgetClicked:**
   - **GUI (CORRUPTED):** `"queo widget [NAME] fou clicado"`
   - **L10N (CORRECT):** `"quando widget [NAME] clicado"`

3. **widget.setTextStyle:**
   - **GUI (CORRUPTED):** `"mude text style [FONT] fligadot tamanho [FONTSIZE] text cou [TEXTCOLOR] boldness [BOLDNESS] text alignment [ALIGMENT] pou widget [NAME]"`
   - **L10N (CORRECT):** `"defina estilo do texto [FONT] tamanho da fonte [FONTSIZE] cor do texto [TEXTCOLOR] negrito [BOLDNESS] alinhamento do texto [ALIGMENT] para widget [NAME]"`

4. **widget.setWidgetStyle:**
   - **GUI (CORRUPTED):** `"mude widget trásgarredligadode cou [BGCOLOR] bouder cou [BORDERCOLOR] bouder width [BORDERWIDTH] bouder radius [BORDERRADIUS] pou [NAME]"`
   - **L10N (CORRECT):** `"defina widget cor de fundo [BGCOLOR] cor da borda [BORDERCOLOR] largura da borda [BORDERWIDTH] raio da borda [BORDERRADIUS] para [NAME]"`

5. **widget.currentVideoTime:**
   - **GUI (CORRUPTED):** `"na posiçãoual video time pou [NAME]"`
   - **L10N (CORRECT):** `"tempo atual do vídeo para [NAME]"`

6. **widget.confirmTextWithButtons:**
   - **GUI (CORRUPTED):** `"cligadofirm [NAME] por butparans [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]"`
   - **L10N (CORRECT):** `"confirmar [NAME] com botões [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]"`

7. **widget.whenVideoStopped:**
   - **GUI (CORRUPTED):** `"queo video [NAME] pareped"`
   - **L10N (CORRECT):** `"quando vídeo [NAME] parado"`

8. **widget.drawChartUsingCategory:**
   - **GUI (CORRUPTED):** `"draw pie chart useng cna posiçãoegouy [CATEGORY] e value [VALUE] from table [TABLE] x [X] y [Y] width [WIDTH] height [HEIGHT] as [NAME]"`
   - **L10N (CORRECT):** `"desenhar gráfico de pizza usando categoria [CATEGORY] e valor [VALUE] da tabela [TABLE] x [X] y [Y] largura [WIDTH] altura [HEIGHT] como [NAME]"`

9. **widget.updateLastChatMessage:**
   - **GUI (CORRUPTED):** `"updna posiçãoa last chna posição message para [NEWMSG] pou chna posição [NAME]"`
   - **L10N (CORRECT):** `"update last chat message to [NEWMSG] for chat [NAME]"`

10. **widget.progressBar:**
    - **GUI (CORRUPTED):** `"adiciligadoe progress bar as [VALUE] out de parna posiçãoal [TOTAL] na posição x [X] y [Y] width [WIDTH] height [HEIGHT] cou [COLOR] trásgarredligadode [BGCOLOR] bouder width [BORDER_WIDTH] cou [BORDER_COLOR] as [NAME]"`
    - **L10N (CORRECT):** `"adicione progress bar as [VALUE] out de total [TOTAL] em X [X] y [Y] largura [WIDTH] altura [HEIGHT] cor [COLOR] background [BGCOLOR] largura da borda [BORDER_WIDTH] cor [BORDER_COLOR] como [NAME]"`

---

## Root Cause Analysis

The corruption pattern suggests a **character encoding or find-replace operation gone wrong**:

### German Corruption Pattern:
- Words containing "o" replaced with corrupted variants
- "position" → "Positiein"
- "button" → "butaufn"
- "stop" → "saufppe"
- "container" → "ceintainer"
- Pattern suggests automated corruption, not manual translation errors

### Portuguese Corruption Pattern:
- Words with "n" or "r" replaced with "ligado" variants
- "adicione" → "adiciligadoe"
- "background" → "trásgarredligadode"
- "quando" → "queo"
- "named" → "nãomed"
- Clear signs of automated text corruption

---

## Recommendations

### CRITICAL - Immediate Action Required:

1. **Replace ALL widget entries in German and Portuguese GUI files**
   - Source: `/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/de.json`
   - Source: `/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/pt.json`
   - Target: `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/de.json`
   - Target: `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/pt.json`

2. **Review and update Japanese widget entries**
   - Less critical, but should be synchronized for consistency
   - Source: `/home/binyu/dev/scratch-workspace/scratch-l10n/editor/extensions/ja.json`
   - Target: `/home/binyu/dev/scratch-workspace/scratch-gui/src/lib/locales/ja.json`

3. **Investigate corruption source**
   - Determine how these corruptions occurred
   - Check if other translation keys are affected
   - Prevent future corruption incidents

4. **Testing Priority:**
   - German widget extension: **CRITICAL** (86% corrupted)
   - Portuguese widget extension: **CRITICAL** (86% corrupted)
   - Japanese widget extension: **MEDIUM** (51% minor issues)

---

## Files for Reference

**Detailed analysis report:** `/home/binyu/dev/scratch-workspace/scratch-l10n/widget_translations_analysis_report.txt`

**Analysis script:** `/home/binyu/dev/scratch-workspace/scratch-l10n/analyze_widget_translations.py`
