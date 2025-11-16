# Swedish Layout Visualization

Detta är en guide för att visa svenska tecken (å, ä, ö) i webbgränssnittet för keymap-visualisering.

## Problem

Webbgränssnittet visar amerikanska tecken istället för svenska tecken eftersom det inte vet om den svenska layouten.

## Lösningar

### 1. Keymap Drawer (Rekommenderat)

Om du använder [keymap-drawer](https://github.com/caksoylar/keymap-drawer), kan du använda den medföljande YAML-filen:

```bash
keymap-drawer config/hillside46.keymap -c visualization/hillside46_swe.yaml
```

### 2. Manuell mappning

För att visa svenska tecken korrekt, behöver du mappa följande tangenter:

| Fysisk tangent | Amerikansk | Svensk |
|----------------|------------|--------|
| `&kp LBRACKET` | `[` | `Å` |
| `&kp SEMI` | `;` | `Ö` |
| `&kp SQT` | `'` | `Ä` |
| `&kp MINUS` | `-` | `+` |
| `&kp EQUAL` | `=` | `´` |
| `&kp NUHS` | `'` | `'` (samma) |
| `&kp NUBS` | `\` | `<` |

### 3. För ZMK Keymap Editor

Om du använder [ZMK Keymap Editor](https://www.leskoff.com/zmk-keymap-editor), kan du:
1. Öppna din keymap-fil
2. Manuellt ändra kommentarerna i keymap-filen för att visa svenska tecken
3. Eller använda en lokal keymap-drawer installation med svensk layout

### 4. För Nick Coutsos Keymap Editor

[Nick Coutsos Keymap Editor](https://nickcoutsos.github.io/keymap-editor/) läser direkt från keymap-filen och visar tangentkoder som de är definierade i `bindings`. 

**Begränsning:** Verktyget visar fysiska tangentkoder (`&kp LBRACKET`, `&kp SEMI`, `&kp SQT`) som amerikanska tecken (`[`, `;`, `'`) istället för svenska tecken (`Å`, `Ö`, `Ä`).

**Lösningar:**

1. **Använd visualiseringsfilen** (Rekommenderat):
   - Öppna `visualization/hillside46_keymap_editor_swe.keymap` i [Nick Coutsos Keymap Editor](https://nickcoutsos.github.io/keymap-editor/)
   - Denna fil använder svenska makron (`SE_ARNG`, `SE_ODIA`, `SE_ADIA`) som kommer att visas i verktyget
   - **OBS:** Denna fil är endast för visualisering - använd inte för att bygga firmware!

2. **Manuell mappning i huvudet:**
   - När du ser `[` i verktyget, tänk på det som `Å`
   - När du ser `;` i verktyget, tänk på det som `Ö`
   - När du ser `'` i verktyget, tänk på det som `Ä`

3. **Använd keymap-drawer istället:**
   - Installera keymap-drawer lokalt och använd `visualization/hillside46_swe.yaml`
   - Detta ger bättre kontroll över hur tangenterna visas

## Användning

### Med keymap-drawer

1. Installera keymap-drawer:
   ```bash
   pip install keymap-drawer
   ```

2. Generera visualisering med svensk layout:
   ```bash
   keymap-drawer config/hillside46.keymap -c visualization/hillside46_swe.yaml -o visualization/hillside46_swe.svg
   ```

### Alternativ: Modifiera keymap-kommentarer

Du kan också uppdatera kommentarerna i `config/hillside46.keymap` för att visa svenska tecken i ASCII-art layouten:

```dts
/* QWERTY (Swedish)
 * -------------------------------------------------------------------------------------------------------------------------------------
 * | §     |   Q   |   W   |   E   |   R   |   T   |-----------------------------------|   Y   |   U   |   I   |   O   |   P   |   Å   |
 * | TAB   |   A   |   S   |   D   |   F   |   G   |-----------------------------------|   H   |   J   |   K   |   L   |   Ö   |   Ä   |
 * ...
 */
```

## Noteringar

- Den faktiska keymap-filen använder fysiska tangentkoder (`&kp LBRACKET`, etc.)
- Webbgränssnittet behöver veta att dessa ska visas som svenska tecken
- Vissa verktyg stöder inte svensk layout direkt - använd keymap-drawer med konfigurationsfilen istället

