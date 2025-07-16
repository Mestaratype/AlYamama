## FontSpector report

fontspector version: 1.3.0






## Check results




<details><summary>[3] fonts/variable</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) (opentype/family/consistent_family_name)</summary>
    <div>








- 🔥 **FAIL** 2 different family names were found:

* 'AlYamama SC' (found in fonts fonts/variable/AlYamamaSC[wght].ttf)
* 'AlYamama' (found in fonts fonts/variable/AlYamama[wght].ttf) [code: inconsistent-family-name]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent (family/win_ascent_and_descent)</summary>
    <div>








- 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1132, but got 904 instead. [code: ascent]
  
  


- 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 474, but got 277 instead. [code: descent]
  
  


- 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1132, but got 904 instead. [code: ascent]
  
  


- 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 474, but got 277 instead. [code: descent]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** fonts/variable/AlYamama[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee
* U+0305 COMBINING OVERLINE: try adding one of: gothic, coptic, elbasan, math, glagolitic
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, canadian-aboriginal, duployan, old-permic, tai-le, malayalam, math, todhri, syriac, coptic, tifinagh
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+031A COMBINING LEFT ANGLE ABOVE: try adding math
* U+0320 COMBINING MINUS SIGN BELOW: try adding syriac
* U+0324 COMBINING DIAERESIS BELOW: try adding one of: cherokee, duployan, syriac
* U+0325 COMBINING RING BELOW: try adding syriac
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+032C COMBINING CARON BELOW: try adding math
* U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math
* U+0332 COMBINING LOW LINE: try adding math
* U+033A COMBINING INVERTED BRIDGE BELOW: try adding math
* U+0346 COMBINING BRIDGE ABOVE: try adding math
* U+034D COMBINING LEFT RIGHT ARROW BELOW: try adding math
* U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic
* U+061F ARABIC QUESTION MARK: try adding one of: thaana, nko, yezidi, syriac, hanifi-rohingya, garay, adlam, arabic
* U+0621 ARABIC LETTER HAMZA: try adding one of: arabic, syriac
* U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE: try adding arabic
* U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE: try adding arabic
* U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE: try adding arabic
* U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW: try adding arabic
* U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE: try adding arabic
* U+0627 ARABIC LETTER ALEF: try adding one of: arabic, indic-siyaq-numbers
* U+0628 ARABIC LETTER BEH: try adding arabic
* U+0629 ARABIC LETTER TEH MARBUTA: try adding arabic
* U+062A ARABIC LETTER TEH: try adding arabic
* U+062B ARABIC LETTER THEH: try adding arabic
* U+062C ARABIC LETTER JEEM: try adding arabic
* U+062D ARABIC LETTER HAH: try adding arabic
* U+062E ARABIC LETTER KHAH: try adding arabic
* U+062F ARABIC LETTER DAL: try adding arabic
* U+0630 ARABIC LETTER THAL: try adding arabic
* U+0631 ARABIC LETTER REH: try adding arabic
* U+0632 ARABIC LETTER ZAIN: try adding arabic
* U+0633 ARABIC LETTER SEEN: try adding arabic
* U+0634 ARABIC LETTER SHEEN: try adding arabic
* U+0635 ARABIC LETTER SAD: try adding arabic
* U+0636 ARABIC LETTER DAD: try adding arabic
* U+0637 ARABIC LETTER TAH: try adding arabic
* U+0638 ARABIC LETTER ZAH: try adding arabic
* U+0639 ARABIC LETTER AIN: try adding arabic
* U+063A ARABIC LETTER GHAIN: try adding arabic
* U+0640 ARABIC TATWEEL: try adding one of: hanifi-rohingya, manichaean, sogdian, arabic, psalter-pahlavi, old-uyghur, mandaic, adlam, syriac
* U+0641 ARABIC LETTER FEH: try adding arabic
* U+0642 ARABIC LETTER QAF: try adding arabic
* U+0643 ARABIC LETTER KAF: try adding arabic
* U+0644 ARABIC LETTER LAM: try adding arabic
* U+0645 ARABIC LETTER MEEM: try adding arabic
* U+0646 ARABIC LETTER NOON: try adding arabic
* U+0647 ARABIC LETTER HEH: try adding arabic
* U+0648 ARABIC LETTER WAW: try adding arabic
* U+0649 ARABIC LETTER ALEF MAKSURA: try adding arabic
* U+064A ARABIC LETTER YEH: try adding arabic
* U+064B ARABIC FATHATAN: try adding one of: syriac, arabic
* U+064C ARABIC DAMMATAN: try adding one of: syriac, arabic
* U+064D ARABIC KASRATAN: try adding one of: arabic, syriac
* U+064E ARABIC FATHA: try adding one of: syriac, arabic
* U+064F ARABIC DAMMA: try adding one of: arabic, syriac
* U+0650 ARABIC KASRA: try adding one of: syriac, arabic
* U+0651 ARABIC SHADDA: try adding one of: arabic, syriac
* U+0652 ARABIC SUKUN: try adding one of: syriac, arabic
* U+0653 ARABIC MADDAH ABOVE: try adding one of: arabic, syriac
* U+0654 ARABIC HAMZA ABOVE: try adding one of: syriac, arabic
* U+0655 ARABIC HAMZA BELOW: try adding one of: arabic, syriac
* U+0656 ARABIC SUBSCRIPT ALEF: try adding arabic
* U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: syriac, indic-siyaq-numbers, arabic, hanifi-rohingya, thaana, yezidi
* U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: arabic, thaana, syriac, yezidi, indic-siyaq-numbers
* U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: yezidi, indic-siyaq-numbers, syriac, arabic, thaana
* U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: syriac, yezidi, indic-siyaq-numbers, thaana, arabic
* U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: syriac, indic-siyaq-numbers, thaana, arabic, yezidi
* U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: thaana, yezidi, indic-siyaq-numbers, syriac, arabic
* U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: thaana, yezidi, indic-siyaq-numbers, arabic, syriac
* U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: yezidi, indic-siyaq-numbers, arabic, syriac, thaana
* U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: thaana, arabic, yezidi, syriac, indic-siyaq-numbers
* U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: yezidi, thaana, syriac, arabic, indic-siyaq-numbers
* U+066E ARABIC LETTER DOTLESS BEH: try adding arabic
* U+066F ARABIC LETTER DOTLESS QAF: try adding arabic
* U+0670 ARABIC LETTER SUPERSCRIPT ALEF: try adding one of: arabic, syriac
* U+06A1 ARABIC LETTER DOTLESS FEH: try adding arabic
* U+06A4 ARABIC LETTER VEH: try adding arabic
* U+06BA ARABIC LETTER NOON GHUNNA: try adding arabic
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2016 DOUBLE VERTICAL LINE: try adding math
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2070 SUPERSCRIPT ZERO: try adding math
* U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math
* U+2074 SUPERSCRIPT FOUR: try adding math
* U+2075 SUPERSCRIPT FIVE: try adding math
* U+2076 SUPERSCRIPT SIX: try adding math
* U+2077 SUPERSCRIPT SEVEN: try adding math
* U+2078 SUPERSCRIPT EIGHT: try adding math
* U+2079 SUPERSCRIPT NINE: try adding math
* U+207A SUPERSCRIPT PLUS SIGN: try adding math
* U+207B SUPERSCRIPT MINUS: try adding math
* U+207C SUPERSCRIPT EQUALS SIGN: try adding math
* U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math
* U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math
* U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math
* U+2080 SUBSCRIPT ZERO: try adding math
* U+2081 SUBSCRIPT ONE: try adding math
* U+2082 SUBSCRIPT TWO: try adding math
* U+2083 SUBSCRIPT THREE: try adding math
* U+2084 SUBSCRIPT FOUR: try adding math
* U+2085 SUBSCRIPT FIVE: try adding math
* U+2086 SUBSCRIPT SIX: try adding math
* U+2087 SUBSCRIPT SEVEN: try adding math
* U+2088 SUBSCRIPT EIGHT: try adding math
* U+2089 SUBSCRIPT NINE: try adding math
* U+208A SUBSCRIPT PLUS SIGN: try adding math
* U+208B SUBSCRIPT MINUS: try adding math
* U+208C SUBSCRIPT EQUALS SIGN: try adding math
* U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math
* U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math
* U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math
* U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math
* U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math
* U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math
* U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math
* U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math
* U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math
* U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math
* U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math
* U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math
* U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math
* U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math
* U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math
* U+2117 SOUND RECORDING COPYRIGHT: try adding math
* U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols
* U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols
* U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols
* U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols
* U+215F FRACTION NUMERATOR ONE: try adding symbols
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+222B INTEGRAL: try adding math
* U+2248 ALMOST EQUAL TO: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CA LOZENGE: try adding one of: symbols, math
* U+25CC DOTTED CIRCLE: try adding one of: saurashtra, tifinagh, syriac, oriya, tai-viet, tagbanwa, myanmar, gujarati, sharada, tirhuta, thaana, hanifi-rohingya, mongolian, devanagari, kharoshthi, lao, tagalog, manichaean, duployan, javanese, lepcha, masaram-gondi, psalter-pahlavi, brahmi, math, adlam, canadian-aboriginal, elbasan, caucasian-albanian, khojki, tamil, bassa-vah, buhid, balinese, gunjala-gondi, limbu, malayalam, armenian, ahom, hanunoo, kaithi, kannada, kayah-li, marchen, meetei-mayek, chakma, old-permic, pahawh-hmong, phags-pa, dogra, osage, bhaiksuki, miao, khudawadi, soyombo, syloti-nagri, grantha, coptic, wancho, warang-citi, yi, gurmukhi, nko, khmer, tai-le, hebrew, symbols, buginese, cham, thai, takri, mandaic, music, bengali, rejang, tai-tham, mahajani, new-tai-lue, sundanese, siddham, telugu, batak, mende-kikakui, sinhala, newa, tibetan, sogdian, zanabazar-square, modi

Or you can add the above codepoints to one of the subsets supported by the font: greek, latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** fonts/variable/AlYamamaSC[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee
* U+0305 COMBINING OVERLINE: try adding one of: gothic, coptic, elbasan, math, glagolitic
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, canadian-aboriginal, duployan, old-permic, tai-le, malayalam, math, todhri, syriac, coptic, tifinagh
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+031A COMBINING LEFT ANGLE ABOVE: try adding math
* U+0320 COMBINING MINUS SIGN BELOW: try adding syriac
* U+0324 COMBINING DIAERESIS BELOW: try adding one of: cherokee, duployan, syriac
* U+0325 COMBINING RING BELOW: try adding syriac
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+032C COMBINING CARON BELOW: try adding math
* U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math
* U+0332 COMBINING LOW LINE: try adding math
* U+033A COMBINING INVERTED BRIDGE BELOW: try adding math
* U+0346 COMBINING BRIDGE ABOVE: try adding math
* U+034D COMBINING LEFT RIGHT ARROW BELOW: try adding math
* U+0361 COMBINING DOUBLE INVERTED BREVE: try adding coptic
* U+061F ARABIC QUESTION MARK: try adding one of: thaana, nko, yezidi, syriac, hanifi-rohingya, garay, adlam, arabic
* U+0621 ARABIC LETTER HAMZA: try adding one of: arabic, syriac
* U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE: try adding arabic
* U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE: try adding arabic
* U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE: try adding arabic
* U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW: try adding arabic
* U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE: try adding arabic
* U+0627 ARABIC LETTER ALEF: try adding one of: arabic, indic-siyaq-numbers
* U+0628 ARABIC LETTER BEH: try adding arabic
* U+0629 ARABIC LETTER TEH MARBUTA: try adding arabic
* U+062A ARABIC LETTER TEH: try adding arabic
* U+062B ARABIC LETTER THEH: try adding arabic
* U+062C ARABIC LETTER JEEM: try adding arabic
* U+062D ARABIC LETTER HAH: try adding arabic
* U+062E ARABIC LETTER KHAH: try adding arabic
* U+062F ARABIC LETTER DAL: try adding arabic
* U+0630 ARABIC LETTER THAL: try adding arabic
* U+0631 ARABIC LETTER REH: try adding arabic
* U+0632 ARABIC LETTER ZAIN: try adding arabic
* U+0633 ARABIC LETTER SEEN: try adding arabic
* U+0634 ARABIC LETTER SHEEN: try adding arabic
* U+0635 ARABIC LETTER SAD: try adding arabic
* U+0636 ARABIC LETTER DAD: try adding arabic
* U+0637 ARABIC LETTER TAH: try adding arabic
* U+0638 ARABIC LETTER ZAH: try adding arabic
* U+0639 ARABIC LETTER AIN: try adding arabic
* U+063A ARABIC LETTER GHAIN: try adding arabic
* U+0640 ARABIC TATWEEL: try adding one of: hanifi-rohingya, manichaean, sogdian, arabic, psalter-pahlavi, old-uyghur, mandaic, adlam, syriac
* U+0641 ARABIC LETTER FEH: try adding arabic
* U+0642 ARABIC LETTER QAF: try adding arabic
* U+0643 ARABIC LETTER KAF: try adding arabic
* U+0644 ARABIC LETTER LAM: try adding arabic
* U+0645 ARABIC LETTER MEEM: try adding arabic
* U+0646 ARABIC LETTER NOON: try adding arabic
* U+0647 ARABIC LETTER HEH: try adding arabic
* U+0648 ARABIC LETTER WAW: try adding arabic
* U+0649 ARABIC LETTER ALEF MAKSURA: try adding arabic
* U+064A ARABIC LETTER YEH: try adding arabic
* U+064B ARABIC FATHATAN: try adding one of: syriac, arabic
* U+064C ARABIC DAMMATAN: try adding one of: syriac, arabic
* U+064D ARABIC KASRATAN: try adding one of: arabic, syriac
* U+064E ARABIC FATHA: try adding one of: syriac, arabic
* U+064F ARABIC DAMMA: try adding one of: arabic, syriac
* U+0650 ARABIC KASRA: try adding one of: syriac, arabic
* U+0651 ARABIC SHADDA: try adding one of: arabic, syriac
* U+0652 ARABIC SUKUN: try adding one of: syriac, arabic
* U+0653 ARABIC MADDAH ABOVE: try adding one of: arabic, syriac
* U+0654 ARABIC HAMZA ABOVE: try adding one of: syriac, arabic
* U+0655 ARABIC HAMZA BELOW: try adding one of: arabic, syriac
* U+0656 ARABIC SUBSCRIPT ALEF: try adding arabic
* U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: syriac, indic-siyaq-numbers, arabic, hanifi-rohingya, thaana, yezidi
* U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: arabic, thaana, syriac, yezidi, indic-siyaq-numbers
* U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: yezidi, indic-siyaq-numbers, syriac, arabic, thaana
* U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: syriac, yezidi, indic-siyaq-numbers, thaana, arabic
* U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: syriac, indic-siyaq-numbers, thaana, arabic, yezidi
* U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: thaana, yezidi, indic-siyaq-numbers, syriac, arabic
* U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: thaana, yezidi, indic-siyaq-numbers, arabic, syriac
* U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: yezidi, indic-siyaq-numbers, arabic, syriac, thaana
* U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: thaana, arabic, yezidi, syriac, indic-siyaq-numbers
* U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: yezidi, thaana, syriac, arabic, indic-siyaq-numbers
* U+066E ARABIC LETTER DOTLESS BEH: try adding arabic
* U+066F ARABIC LETTER DOTLESS QAF: try adding arabic
* U+0670 ARABIC LETTER SUPERSCRIPT ALEF: try adding one of: arabic, syriac
* U+06A1 ARABIC LETTER DOTLESS FEH: try adding arabic
* U+06A4 ARABIC LETTER VEH: try adding arabic
* U+06BA ARABIC LETTER NOON GHUNNA: try adding arabic
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2016 DOUBLE VERTICAL LINE: try adding math
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2070 SUPERSCRIPT ZERO: try adding math
* U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math
* U+2074 SUPERSCRIPT FOUR: try adding math
* U+2075 SUPERSCRIPT FIVE: try adding math
* U+2076 SUPERSCRIPT SIX: try adding math
* U+2077 SUPERSCRIPT SEVEN: try adding math
* U+2078 SUPERSCRIPT EIGHT: try adding math
* U+2079 SUPERSCRIPT NINE: try adding math
* U+207A SUPERSCRIPT PLUS SIGN: try adding math
* U+207B SUPERSCRIPT MINUS: try adding math
* U+207C SUPERSCRIPT EQUALS SIGN: try adding math
* U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math
* U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math
* U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math
* U+2080 SUBSCRIPT ZERO: try adding math
* U+2081 SUBSCRIPT ONE: try adding math
* U+2082 SUBSCRIPT TWO: try adding math
* U+2083 SUBSCRIPT THREE: try adding math
* U+2084 SUBSCRIPT FOUR: try adding math
* U+2085 SUBSCRIPT FIVE: try adding math
* U+2086 SUBSCRIPT SIX: try adding math
* U+2087 SUBSCRIPT SEVEN: try adding math
* U+2088 SUBSCRIPT EIGHT: try adding math
* U+2089 SUBSCRIPT NINE: try adding math
* U+208A SUBSCRIPT PLUS SIGN: try adding math
* U+208B SUBSCRIPT MINUS: try adding math
* U+208C SUBSCRIPT EQUALS SIGN: try adding math
* U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math
* U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math
* U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math
* U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math
* U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math
* U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math
* U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math
* U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math
* U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math
* U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math
* U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math
* U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math
* U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math
* U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math
* U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math
* U+2117 SOUND RECORDING COPYRIGHT: try adding math
* U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols
* U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols
* U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols
* U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols
* U+215F FRACTION NUMERATOR ONE: try adding symbols
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+222B INTEGRAL: try adding math
* U+2248 ALMOST EQUAL TO: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CA LOZENGE: try adding one of: symbols, math
* U+25CC DOTTED CIRCLE: try adding one of: saurashtra, tifinagh, syriac, oriya, tai-viet, tagbanwa, myanmar, gujarati, sharada, tirhuta, thaana, hanifi-rohingya, mongolian, devanagari, kharoshthi, lao, tagalog, manichaean, duployan, javanese, lepcha, masaram-gondi, psalter-pahlavi, brahmi, math, adlam, canadian-aboriginal, elbasan, caucasian-albanian, khojki, tamil, bassa-vah, buhid, balinese, gunjala-gondi, limbu, malayalam, armenian, ahom, hanunoo, kaithi, kannada, kayah-li, marchen, meetei-mayek, chakma, old-permic, pahawh-hmong, phags-pa, dogra, osage, bhaiksuki, miao, khudawadi, soyombo, syloti-nagri, grantha, coptic, wancho, warang-citi, yi, gurmukhi, nko, khmer, tai-le, hebrew, symbols, buginese, cham, thai, takri, mandaic, music, bengali, rejang, tai-tham, mahajani, new-tai-lue, sundanese, siddham, telugu, batak, mende-kikakui, sinhala, newa, tibetan, sogdian, zanabazar-square, modi

Or you can add the above codepoints to one of the subsets supported by the font: greek, latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[18] fonts/variable/AlYamama[wght].ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. (base_has_width)</summary>
    <div>








- 🔥 **FAIL** The following glyphs had zero advance width:
* fraction (Some(8260)) [code: zero-width-bases]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. (case_mapping)</summary>
    <div>








- 🔥 **FAIL** The following glyphs are missing case-swapping counterparts:

| Glyph present in the font                        | Missing case-swapping counterpart                  |
|--------------------------------------------------|----------------------------------------------------|
| U+028A: LATIN SMALL LETTER UPSILON               | U+01B1: LATIN CAPITAL LETTER UPSILON               |
| U+0280: LATIN LETTER SMALL CAPITAL R             | U+01A6: LATIN LETTER YR                            |
| U+0266: LATIN SMALL LETTER H WITH HOOK           | U+A7AA: LATIN CAPITAL LETTER H WITH HOOK           |
| U+0289: LATIN SMALL LETTER U BAR                 | U+0244: LATIN CAPITAL LETTER U BAR                 |
| U+0259: LATIN SMALL LETTER SCHWA                 | U+018F: LATIN CAPITAL LETTER SCHWA                 |
| U+0292: LATIN SMALL LETTER EZH                   | U+01B7: LATIN CAPITAL LETTER EZH                   |
| U+026A: LATIN LETTER SMALL CAPITAL I             | U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I       |
| U+A78B: LATIN CAPITAL LETTER SALTILLO            | U+A78C: LATIN SMALL LETTER SALTILLO                |
| U+0257: LATIN SMALL LETTER D WITH HOOK           | U+018A: LATIN CAPITAL LETTER D WITH HOOK           |
| U+025B: LATIN SMALL LETTER OPEN E                | U+0190: LATIN CAPITAL LETTER OPEN E                |
| U+028B: LATIN SMALL LETTER V WITH HOOK           | U+01B2: LATIN CAPITAL LETTER V WITH HOOK           |
| U+026C: LATIN SMALL LETTER L WITH BELT           | U+A7AD: LATIN CAPITAL LETTER L WITH BELT           |
| U+0199: LATIN SMALL LETTER K WITH HOOK           | U+0198: LATIN CAPITAL LETTER K WITH HOOK           |
| U+026F: LATIN SMALL LETTER TURNED M              | U+019C: LATIN CAPITAL LETTER TURNED M              |
| U+0254: LATIN SMALL LETTER OPEN O                | U+0186: LATIN CAPITAL LETTER OPEN O                |
| U+0272: LATIN SMALL LETTER N WITH LEFT HOOK      | U+019D: LATIN CAPITAL LETTER N WITH LEFT HOOK      |
| U+028C: LATIN SMALL LETTER TURNED V              | U+0245: LATIN CAPITAL LETTER TURNED V              |
| U+0256: LATIN SMALL LETTER D WITH TAIL           | U+0189: LATIN CAPITAL LETTER AFRICAN D             |
| U+0253: LATIN SMALL LETTER B WITH HOOK           | U+0181: LATIN CAPITAL LETTER B WITH HOOK           |
| U+0188: LATIN SMALL LETTER C WITH HOOK           | U+0187: LATIN CAPITAL LETTER C WITH HOOK           |
| U+0268: LATIN SMALL LETTER I WITH STROKE         | U+0197: LATIN CAPITAL LETTER I WITH STROKE         |
| U+027D: LATIN SMALL LETTER R WITH TAIL           | U+2C64: LATIN CAPITAL LETTER R WITH TAIL           |
| U+AB53: LATIN SMALL LETTER CHI                   | U+A7B3: LATIN CAPITAL LETTER CHI                   |
| U+0288: LATIN SMALL LETTER T WITH RETROFLEX HOOK | U+01AE: LATIN CAPITAL LETTER T WITH RETROFLEX HOOK |
| U+0263: LATIN SMALL LETTER GAMMA                 | U+0194: LATIN CAPITAL LETTER GAMMA                 |
| U+0264: LATIN SMALL LETTER RAMS HORN             | U+A7CB: LATIN CAPITAL LETTER RAMS HORN             |
| U+0260: LATIN SMALL LETTER G WITH HOOK           | U+0193: LATIN CAPITAL LETTER G WITH HOOK           |
| U+0269: LATIN SMALL LETTER IOTA                  | U+0196: LATIN CAPITAL LETTER IOTA                  |
| U+0265: LATIN SMALL LETTER TURNED H              | U+A78D: LATIN CAPITAL LETTER TURNED H              |
| U+01AD: LATIN SMALL LETTER T WITH HOOK           | U+01AC: LATIN CAPITAL LETTER T WITH HOOK           |
| U+01A5: LATIN SMALL LETTER P WITH HOOK           | U+01A4: LATIN CAPITAL LETTER P WITH HOOK           |
| U+0283: LATIN SMALL LETTER ESH                   | U+01A9: LATIN CAPITAL LETTER ESH                   |
| U+0275: LATIN SMALL LETTER BARRED O              | U+019F: LATIN CAPITAL LETTER O WITH MIDDLE TILDE   |
| U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL   | U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL   | [code: missing-case-counterparts]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:
* waslaar [code: no-contour]
  
  


- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     infered from the typical ammounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni1EBC (U+1EBC): found 1, expected one of: {2, 3}
* uni1EF8 (U+1EF8): found 1, expected one of: {2, 3}
* T_T (unencoded): found 2, expected one of: {1}
* uni029B (U+029B): found 2, expected one of: {1}
* uni0255 (U+0255): found 1, expected one of: {2}
* uni0188 (U+0188): found 2, expected one of: {1}
* uni1D6D (U+1D6D): found 3, expected one of: {2}
* uni02A3 (U+02A3): found 2, expected one of: {3}
* uni02A5 (U+02A5): found 3, expected one of: {4}
* uni025D (U+025D): found 3, expected one of: {1}
* uni0258 (U+0258): found 1, expected one of: {2}
* uni0286 (U+0286): found 1, expected one of: {2}
* uni025A (U+025A): found 4, expected one of: {2}
* uni0293 (U+0293): found 1, expected one of: {2}
* uni1D6E (U+1D6E): found 2, expected one of: {1}
* uni02A1 (U+02A1): found 2, expected one of: {1}
* uni02A2 (U+02A2): found 2, expected one of: {1}
* uni029D (U+029D): found 2, expected one of: {3}
* uni0284 (U+0284): found 2, expected one of: {1}
* uni026E (U+026E): found 2, expected one of: {1}
* uni0264 (U+0264): found 1, expected one of: {2}
* uni1D73 (U+1D73): found 3, expected one of: {1}
* uni1D72 (U+1D72): found 2, expected one of: {1}
* uni0282 (U+0282): found 2, expected one of: {1}
* uni1D74 (U+1D74): found 3, expected one of: {1}
* uni1D75 (U+1D75): found 3, expected one of: {1}
* uni021B.1 (U+021B): found 1, expected one of: {3, 2, 4}
* uni0291 (U+0291): found 1, expected one of: {2}
* uni1D76 (U+1D76): found 3, expected one of: {1}
* uni0290 (U+0290): found 2, expected one of: {1}
* Ccedilla.sc (unencoded): found 2, expected one of: {1}
* K.sc (unencoded): found 2, expected one of: {1}
* Q.sc (unencoded): found 3, expected one of: {2}
* uni01C2 (U+01C2): found 3, expected one of: {1}
* uni0621 (U+0621): found 2, expected one of: {1}
* uni0623 (U+0623): found 3, expected one of: {2}
* uni0625 (U+0625): found 3, expected one of: {2}
* uni066E (U+066E): found 3, expected one of: {1}
* uni066E.fina (unencoded): found 3, expected one of: {1}
* uni066E.medi (unencoded): found 2, expected one of: {1}
* uni066E.init (unencoded): found 2, expected one of: {1}
* uni0628 (U+0628): found 4, expected one of: {2}
* uni062A (U+062A): found 5, expected one of: {2, 3}
* uni062B (U+062B): found 6, expected one of: {3, 2, 4}
* uni0631 (U+0631): found 2, expected one of: {1}
* uni0632 (U+0632): found 3, expected one of: {2}
* uni0633 (U+0633): found 6, expected one of: {3, 1}
* uni0634 (U+0634): found 9, expected one of: {4, 3, 6, 0}
* uni0635 (U+0635): found 6, expected one of: {2}
* uni0636 (U+0636): found 7, expected one of: {3}
* uni0637 (U+0637): found 4, expected one of: {2, 3}
* uni0638 (U+0638): found 5, expected one of: {3, 4}
* uni0639 (U+0639): found 2, expected one of: {1}
* uni0641 (U+0641): found 5, expected one of: {3, 2}
* uni06A4 (U+06A4): found 7, expected one of: {4, 5, 0}
* uni06A1 (U+06A1): found 4, expected one of: {1, 2}
* uni06A1.fina (unencoded): found 4, expected one of: {2}
* uni066F.fina (unencoded): found 3, expected one of: {2}
* uni0643 (U+0643): found 4, expected one of: {1, 2}
* uni0644 (U+0644): found 2, expected one of: {1}
* uni0645 (U+0645): found 3, expected one of: {2, 1}
* uni0646 (U+0646): found 3, expected one of: {2}
* uni06BA (U+06BA): found 2, expected one of: {1}
* uni0647 (U+0647): found 1, expected one of: {2}
* uni0624 (U+0624): found 4, expected one of: {2, 3}
* uni0649 (U+0649): found 2, expected one of: {1}
* uni064A (U+064A): found 4, expected one of: {2, 3}
* uni0626 (U+0626): found 4, expected one of: {2}
* uni0662 (U+0662): found 2, expected one of: {1}
* uni0663 (U+0663): found 3, expected one of: {1}
* uni0666 (U+0666): found 2, expected one of: {1}
* asterisk (U+002A): found 6, expected one of: {1, 3, 2, 5}
* uni02E5 (U+02E5): found 2, expected one of: {1}
* uni02E9 (U+02E9): found 2, expected one of: {1}
* uni02E6 (U+02E6): found 2, expected one of: {1}
* uni02E8 (U+02E8): found 2, expected one of: {1}
* uni02E7 (U+02E7): found 2, expected one of: {1}
* uni02DE (U+02DE): found 2, expected one of: {1}
* uni0654 (U+0654): found 2, expected one of: {1}
* uni0655 (U+0655): found 2, expected one of: {1}
* uni0654064C (unencoded): found 4, expected one of: {3}
* uni0654064E (unencoded): found 3, expected one of: {2}
* uni0654064B (unencoded): found 4, expected one of: {3}
* uni06540652 (unencoded): found 4, expected one of: {3}
* uni06550650 (unencoded): found 3, expected one of: {2}
* uni0655064D (unencoded): found 4, expected one of: {3}
* uni0651 (U+0651): found 2, expected one of: {1}
* uni0651064C (unencoded): found 4, expected one of: {2, 3}
* uni0651064D (unencoded): found 4, expected one of: {3}
* uni0651064E (unencoded): found 3, expected one of: {2}
* uni06510650 (unencoded): found 3, expected one of: {2}
* uni06510670 (unencoded): found 3, expected one of: {2}
* uni031A (U+031A): found 2, expected one of: {1}
* uni032A (U+032A): found 3, expected one of: {1}
* uni033A (U+033A): found 3, expected one of: {1}
* uni033B (U+033B): found 6, expected one of: {2}
* uni033C (U+033C): found 2, expected one of: {1}
* uni0346 (U+0346): found 3, expected one of: {1}
* uni0349 (U+0349): found 2, expected one of: {1}
* uni034A (U+034A): found 2, expected one of: {1} [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure small caps glyphs are available (missing_small_caps_glyphs)</summary>
    <div>








- 🔥 **FAIL** The following letters did not take part in smcp substitutions:
* uni0287
* uni0254
* uni025E
* epsilontonos
* uni0250
* uni0264
* uni0255
* uni03C2
* uni0291
* eta
* psi
* uni02AB
* kappa
* uni0251
* uni026F
* uni029C
* uni028F
* epsilon
* uni028C
* omicron
* uni02AF
* uni02A3
* uni026E
* uni00B5
* uni026B
* uni0267
* uni0283
* uni029B
* uni02AC
* uni027E
* etatonos
* uni1D74
* uni0263
* uni0288
* uni026C
* uni0256
* alpha
* uni0272
* uni0275
* uni0282
* iotatonos
* uni1D6F
* xi
* uni0261
* rho
* uni1D6D
* uni0274
* uni0237
* uni027D
* nu
* upsilon
* uni1D6E
* uni1D73
* uni1EF9
* uni0293
* uni0199
* uni02AD
* uni0280
* uni1D75
* uni1D72
* chi
* uni02A9
* uni0260
* uni02A8
* uni029F
* uni0262
* uni026D
* uni01AD
* uni0278
* uni027A
* uni028A
* uni0290
* dotlessi
* uni0297
* iotadieresistonos
* beta
* uni0266
* uni027F
* uni1D6C
* lambda
* uni0252
* uni0259
* uni029A
* uni025C
* uni0277
* uni0289
* omicrontonos
* uni0279
* uni027C
* uni02AE
* uniAB53
* sigma
* uni0286
* uni028E
* uni02A2
* uni025F
* uni027B
* uni02A4
* gamma
* uni1E21
* uni026A
* uni0296
* uni0253
* pi
* uni0281
* omegatonos
* uni0269
* tau
* florin
* uni025A
* uni0285
* delta
* uni0270
* uni0295
* uni1D76
* uni02A6
* upsilondieresistonos
* zeta
* phi
* uni0273
* upsilontonos
* uni0292
* uni028D
* uni02A1
* uni0258
* theta
* uni0284
* uni1D71
* uni0188
* uni03BC
* iotadieresis
* uni0299
* uni02A0
* uni02AA
* uni028B
* uni02A7
* uni0257
* uni029D
* uni025D
* uni029E
* uni03D7
* upsilondieresis
* uni0271
* uni1D70
* uni1EBD
* uni02A5
* uni0276
* iota
* alphatonos
* omega
* uni01A5
* uni025B
* uni0268
* uni0298
* uni0265
* uni021B.1 [code: missing-smcp-lowercase]
  
  


- 🔥 **FAIL** The following letters did not take part in c2sc substitutions:
* Alpha
* uni1E20
* Psi
* uni03A9
* Chi
* uni1EBC
* Nu
* Pi
* Omegatonos
* Upsilontonos
* Epsilon
* Omicrontonos
* Omicron
* Lambda
* Alphatonos
* Theta
* Upsilon
* Etatonos
* Eta
* Gamma
* Rho
* Iota
* uni021A.1
* Tau
* Upsilondieresis
* Phi
* Xi
* Sigma
* Beta
* Mu
* uni03CF
* Iotatonos
* uni0394
* uni1EF8
* uniA78B
* Kappa
* Zeta
* Epsilontonos
* Iotadieresis [code: missing-c2sc-uppercase]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Space and non-breaking space have the same width? (whitespace_widths)</summary>
    <div>








- 🔥 **FAIL** The space glyph named space is 204 font units wide, non-breaking space named (uni00A0) is 252 font units wide, and both should be positive and the same. GlyphsApp has "Sidebearing arithmetic" (https://glyphsapp.com/tutorials/spacing) which allows you to set the non-breaking space width to always equal the space width. [code: different-widths]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- 🔥 **FAIL** Failed language shaping:

| Message                                                          | Languages         |
|------------------------------------------------------------------|-------------------|
| Mandatory orthography codepoints:                                | * nl_Latn (Dutch) |
|   Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́' |                   |
|   Shaper didn't attach acutecomb to j when shaping the text 'íj́' |                   | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                                                                                            | Languages                    |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                                                                                  | * el_Grek (Greek)            |
|   The following auxiliary characters are missing from the font: ἀ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἄ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἂ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἆ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἁ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἅ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἃ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἇ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ᾶ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἐ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἔ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἒ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἑ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἕ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἓ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἠ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἤ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἢ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἦ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἡ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἥ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἣ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἧ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῆ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἰ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἴ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἲ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἶ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἱ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἵ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἳ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἷ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῖ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῗ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὄ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὂ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὃ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὐ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὔ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὒ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὖ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὑ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὕ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὓ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὗ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῦ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῧ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὤ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὢ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὦ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὥ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὣ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὧ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῶ                                                                  |                              |
| Small caps for Latin letters:                                                                                                      | * nl_Latn (Dutch)            |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĳ' and shaping the text 'ĳ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * lt_Latn (Lithuanian)       |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ą' and shaping the text 'ą' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ę' and shaping the text 'ę' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ė' and shaping the text 'ė' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'į' and shaping the text 'į' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ų' and shaping the text 'ų' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĩ' and shaping the text 'ĩ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ũ' and shaping the text 'ũ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǥ                                                                  |                              |
|   The following auxiliary characters are missing from the font: Ʒ                                                                  |                              |
|   The following auxiliary characters are missing from the font: Ǯ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ǥ                                                                  |                              |
| Small caps for Latin letters:                                                                                                      | * sk_Latn (Slovak)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ď' and shaping the text 'ď' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĺ' and shaping the text 'ĺ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ľ' and shaping the text 'ľ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ň' and shaping the text 'ň' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŕ' and shaping the text 'ŕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ť' and shaping the text 'ť' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ő' and shaping the text 'ő' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ű' and shaping the text 'ű' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sv_Latn (Swedish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * cy_Latn (Welsh)            |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẃ' and shaping the text 'ẃ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẁ' and shaping the text 'ẁ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŵ' and shaping the text 'ŵ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẅ' and shaping the text 'ẅ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ỳ' and shaping the text 'ỳ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŷ' and shaping the text 'ŷ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sr_Latn (Serbian (Latin))  |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * fr_Latn (French)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * cs_Latn (Czech)            |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ď' and shaping the text 'ď' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ě' and shaping the text 'ě' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ň' and shaping the text 'ň' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ť' and shaping the text 'ť' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ů' and shaping the text 'ů' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ľ' and shaping the text 'ľ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ł' and shaping the text 'ł' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŕ' and shaping the text 'ŕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * pl_Latn (Polish)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ą' and shaping the text 'ą' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ę' and shaping the text 'ę' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ł' and shaping the text 'ł' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ń' and shaping the text 'ń' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ś' and shaping the text 'ś' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ź' and shaping the text 'ź' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ż' and shaping the text 'ż' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * pt_Latn (Portuguese)       |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * da_Latn (Danish)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǿ' and shaping the text 'ǿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * ca_Latn (Catalan)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŀ' and shaping the text 'ŀ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * fi_Latn (Finnish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ą' and shaping the text 'ą' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ċ' and shaping the text 'ċ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ď' and shaping the text 'ď' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ð' and shaping the text 'ð' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ě' and shaping the text 'ě' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ė' and shaping the text 'ė' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ę' and shaping the text 'ę' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ğ' and shaping the text 'ğ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ģ' and shaping the text 'ģ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ȟ' and shaping the text 'ȟ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ħ' and shaping the text 'ħ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'į' and shaping the text 'į' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǩ' and shaping the text 'ǩ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ķ' and shaping the text 'ķ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĺ' and shaping the text 'ĺ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ľ' and shaping the text 'ľ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ļ' and shaping the text 'ļ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ł' and shaping the text 'ł' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ń' and shaping the text 'ń' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ň' and shaping the text 'ň' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ņ' and shaping the text 'ņ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŋ' and shaping the text 'ŋ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ő' and shaping the text 'ő' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŕ' and shaping the text 'ŕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ś' and shaping the text 'ś' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŝ' and shaping the text 'ŝ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ș' and shaping the text 'ș' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ť' and shaping the text 'ť' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ţ' and shaping the text 'ţ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ț' and shaping the text 'ț' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŧ' and shaping the text 'ŧ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ů' and shaping the text 'ů' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ű' and shaping the text 'ű' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ų' and shaping the text 'ų' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ź' and shaping the text 'ź' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ż' and shaping the text 'ż' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǯ' and shaping the text 'ǯ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'þ' and shaping the text 'þ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * nb_Latn (Norwegian Bokmål) |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ń' and shaping the text 'ń' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŋ' and shaping the text 'ŋ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŧ' and shaping the text 'ŧ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ                                                                  |                              |
| Small caps for Latin letters:                                                                                                      | * lv_Latn (Latvian)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ģ' and shaping the text 'ģ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ķ' and shaping the text 'ķ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ļ' and shaping the text 'ļ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ņ' and shaping the text 'ņ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŗ' and shaping the text 'ŗ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * hu_Latn (Hungarian)        |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ő' and shaping the text 'ő' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ű' and shaping the text 'ű' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * is_Latn (Icelandic)        |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ð' and shaping the text 'ð' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'þ' and shaping the text 'þ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * mt_Latn (Maltese)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ċ' and shaping the text 'ċ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ġ' and shaping the text 'ġ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ħ' and shaping the text 'ħ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ż' and shaping the text 'ż' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sq_Latn (Albanian)         |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: ſ                                                                  | * fr_Latn (French)           |
| Small caps for Latin letters:                                                                                                      | * ro_Latn (Romanian)         |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ș' and shaping the text 'ș' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ț' and shaping the text 'ț' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ţ' and shaping the text 'ţ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * es_Latn (Spanish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * hr_Latn (Croatian)         |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * tr_Latn (Turkish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ğ' and shaping the text 'ğ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * it_Latn (Italian)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * en_Latn (English)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * de_Latn (German)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ğ' and shaping the text 'ğ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * lt_Latn (Lithuanian)       |
|   Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'                                                              |                              |
|   Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'                                                              |                              |
|   Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'                                                              |                              |
|   Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'                                                              |                              |
|   Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'                                                           |                              |
|   Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'                                                           |                              |
|   Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'                                                           |                              |
|   Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'                                                           |                              |
|   Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'                                                           |                              |
|   Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'                                                           |                              |
|   Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'                                                           |                              |
|   Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'                                                           |                              |
|   Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'                                                              |                              |
|   Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'                                                                |                              |
|   Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'                                                              |                              |
|   Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'                                                              |                              |
|   Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'                                                                |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to J when shaping the text 'J̃'                                                                    |                              |
|   Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'                                                                      |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to L when shaping the text 'L̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to M when shaping the text 'M̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to R when shaping the text 'R̃'                                                                    |                              |
|   Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'                                                              |                              |
|   Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'                                                              |                              |
|   Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'                                                              |                              |
|   Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'                                                              |                              |
|   Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'                                                              |                              |
|   Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'                                                              |                              |
|   Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'                                                              |                              |
|   Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'                                                              |                              |
|   Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'                                                           |                              |
|   Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'                                                           |                              |
|   Shaper didn't attach uni0307 to i when shaping the text 'i̇́'                                                                      |                              |
|   Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'                                                              |                              |
|   Shaper didn't attach uni0307 to i when shaping the text 'i̇̀'                                                                      |                              |
|   Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'                                                              |                              |
|   Shaper didn't attach uni0307 to i when shaping the text 'i̇̃'                                                                      |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'                                                              |                              |
|   Shaper didn't attach acutecomb to iogonek when shaping the text 'į́'                                                              |                              |
|   Shaper didn't attach uni0307 to iogonek when shaping the text 'į̇́'                                                                |                              |
|   Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'                                                              |                              |
|   Shaper didn't attach tildecomb to iogonek when shaping the text 'į̃'                                                              |                              |
|   Shaper didn't attach uni0307 to iogonek when shaping the text 'į̇̃'                                                                |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to j when shaping the text 'j̃'                                                                    |                              |
|   Shaper didn't attach uni0307 to j when shaping the text 'j̇̃'                                                                      |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to l when shaping the text 'l̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to m when shaping the text 'm̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to r when shaping the text 'r̃'                                                                    |                              |
|   Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'                                                              |                              |
|   Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'                                                              |                              |
|   Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'                                                              |                              |
|   Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'                                                              |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/name/family_name_compliance)</summary>
    <div>








- 🔥 **FAIL** "AlYamama" is a CamelCased name. To solve this, simply use spaces instead in the font name. [code: camelcase]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check a font's STAT table contains compulsory Axis Values. (googlefonts/STAT/compulsory_axis_values)</summary>
    <div>








- 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

| Name      | Axis | Current Value | Expected Value | Current Flags | Expected Flags | Current Linked Value | Expected Linked Value |
|-----------|------|---------------|----------------|---------------|----------------|----------------------|-----------------------|
| Black     | wght | 900           | 900            | 0             | 0              | N/A                  | N/A                   |
| Bold      | wght | 700           | 700            | 0             | 0              | N/A                  | N/A                   |
| ExtraBold | wght | 800           | 800            | 0             | 0              | N/A                  | N/A                   |
| Light     | wght | 300           | 300            | 0             | 0              | N/A                  | N/A                   |
| Medium    | wght | N/A           | 500            | N/A           | 0              | N/A                  | N/A                   |
| Regular   | wght | 400           | 400            | 2             | 2              | 700                  | 700                   |
| SemiBold  | wght | 600           | 600            | 0             | 0              | N/A                  | N/A                   |

 [code: bad-axis-values]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? (ligature_carets)</summary>
    <div>








- ⚠️ **WARN** This font lacks caret positioning values for these ligature glyphs:
	- * F_F_H
* f_f_j.sc
* F_F_J
* fi.sc
* f_f_t.sc
* fl.sc
* f_f_i.sc
* t_t.sc
* F_K
* f_f_l.sc
* F_F_I
* f_f_h.sc
* f_t.sc
* f_j.sc
* T_T
* f_f.sc
* F_F
* F_I
* F_L
* F_B
* f_h.sc
* F_T
* F_F_L
* f_f_k.sc
* F_H
* F_F_K
* f_b.sc
* F_F_T
* f_k.sc
* F_J
* F_F_B
* f_f_b.sc

 [code: incomplete-caret-pos-data]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>








- ⚠️ **WARN** The most common width is 676 among a set of 13  math glyphs.
The following math glyphs have a different width, though:
width=667: equal
width=509: logicalnot, greaterequal, greater [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>








- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>








- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* uni0162.sc
* Zdotaccent.sc
* u.inferior
* v.inferior
* .null
* twodotsverticalabovear
* twodotsverticalbelowar
* threedotsdownabovear
* threedotsdownbelowar
* threedotsdowncenterar
* threedotsupbelowar
* waslaar
* miniKehehar
* gafsarkashabovear
* gafsarkashcenterar
* doublestrokear
* uni030C.alt.case
* uni0308.sc
* uni0307.sc
* gravecomb.sc
* acutecomb.sc
* uni030B.sc
* uni030C.alt.sc
* uni0302.sc
* uni030C.sc
* uni0306.sc
* uni030A.sc
* tildecomb.sc
* uni0304.sc
* uni0327.sc
* uni0328.sc
* Dotlessi.sc [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:
* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings: * i̋
* i̊
* į̄
* į́
* į̃
* į̀
* į̌
* į̂
* ɨ̧́
* ɨ̧̀
* ɨ̧̌
* ɨ̧̂
* ɨ̈
* ɨ̄
* ɨ̋
* ɨ́
* ɨ̏
* ɨ̃
* ɨ̀
* ɨ̌
* ɨ̂
* j̈
* j̄
* j́
* j̃
* j̀The dot of soft dotted characters _should_ disappear in other cases, for example: * ʲ̪͋
* ʲ̪̈
* ʲ̪̆
* ʲ̪͆
* ʲ̪̄
* ʲ̪̋
* ʲ̪̇
* ʲ̪́
* ʲ̪̏
* ʲ̪̃
* ʲ̪̀
* ʲ̪̌
* ʲ̪̽
* ʲ̪̊
* ʲ̪̅
* ʲ̪͊
* ʲ̪̂
* ʲ̪͌
* ʲ̞͋
* ʲ̞̈
* ʲ̞̆
* ʲ̞͆
* ʲ̞̄
* ʲ̞̋
* ʲ̞̇
* ʲ̞́
* ʲ̞̏
* ʲ̞̃
* ʲ̞̀
* ʲ̞̌
* ʲ̞̽
* ʲ̞̊
* ʲ̞̅
* ʲ̞͊
* ʲ̞̂
* ʲ̞͌
* ʲ͇͋
* ʲ͇̈
* ʲ͇̆
* ʲ͇͆
* ʲ͇̄
* ʲ͇̋
* ʲ͇̇
* ʲ͇́
* ʲ͇̏
* ʲ͇̃
* ʲ͇̀
* ʲ͇̌
* ʲ͇̽
* ʲ͇̊
* ʲ͇̅
* ʲ͇͊
* ʲ͇̂
* ʲ͇͌
* ʲ̧͋
* ʲ̧̈
* ʲ̧̆
* ʲ̧͆
* ʲ̧̄
* ʲ̧̋
* ʲ̧̇
* ʲ̧́
* ʲ̧̏
* ʲ̧̃
* ʲ̧̀
* ʲ̧̌
* ʲ̧̽
* ʲ̧̊
* ʲ̧̅
* ʲ̧͊
* ʲ̧̂
* ʲ̧͌
* ʲ̜͋
* ʲ̜̈
* ʲ̜̆
* ʲ̜͆
* ʲ̜̄
* ʲ̜̋
* ʲ̜̇
* ʲ̜́
* ʲ̜̏
* ʲ̜̃
* ʲ̜̀
* ʲ̜̌
* ʲ̜̽
* ʲ̜̊
* ʲ̜̅
* ʲ̜͊
* ʲ̜̂
* ʲ̜͌
* ʲ̘͋
* ʲ̘̈
* ʲ̘̆
* ʲ̘͆
* ʲ̘̄
* ʲ̘̋
* ʲ̘̇
* ʲ̘́
* ʲ̘̏
* ʲ̘̃
* ʲ̘̀
* ʲ̘̌
* ʲ̘̽
* ʲ̘̊
* ʲ̘̅
* ʲ̘͊
* ʲ̘̂
* ʲ̘͌
* ʲ̺͋
* ʲ̺̈
* ʲ̺̆
* ʲ̺͆
* ʲ̺̄
* ʲ̺̋
* ʲ̺̇
* ʲ̺́
* ʲ̺̏
* ʲ̺̃
* ʲ̺̀
* ʲ̺̌
* ʲ̺̽
* ʲ̺̊
* ʲ̺̅
* ʲ̺͊
* ʲ̺̂
* ʲ̺͌
* ʲ͈͋
* ʲ͈̈
* ʲ͈̆
* ʲ͈͆
* ʲ͈̄
* ʲ͈̋
* ʲ͈̇
* ʲ͈́
* ʲ͈̏
* ʲ͈̃
* ʲ͈̀
* ʲ͈̌
* ʲ͈̽
* ʲ͈̊
* ʲ͈̅
* ʲ͈͊
* ʲ͈̂
* ʲ͈͌
* ʲ̹͋
* ʲ̹̈
* ʲ̹̆
* ʲ̹͆
* ʲ̹̄
* ʲ̹̋
* ʲ̹̇
* ʲ̹́
* ʲ̹̏
* ʲ̹̃
* ʲ̹̀
* ʲ̹̌
* ʲ̹̽
* ʲ̹̊
* ʲ̹̅
* ʲ̹͊
* ʲ̹̂
* ʲ̹͌
* ʲ̙͋
* ʲ̙̈
* ʲ̙̆
* ʲ̙͆
* ʲ̙̄
* ʲ̙̋
* ʲ̙̇
* ʲ̙́
* ʲ̙̏
* ʲ̙̃
* ʲ̙̀
* ʲ̙̌
* ʲ̙̽
* ʲ̙̊
* ʲ̙̅
* ʲ̙͊
* ʲ̙̂
* ʲ̙͌
* ʲ̠͋
* ʲ̠̈
* ʲ̠̆
* ʲ̠͆
* ʲ̠̄
* ʲ̠̋
* ʲ̠̇
* ʲ̠́
* ʲ̠̏
* ʲ̠̃
* ʲ̠̀
* ʲ̠̌
* ʲ̠̽
* ʲ̠̊
* ʲ̠̅
* ʲ̠͊
* ʲ̠̂
* ʲ̠͌
* ʲ̼͋
* ʲ̼̈
* ʲ̼̆
* ʲ̼͆
* ʲ̼̄
* ʲ̼̋
* ʲ̼̇
* ʲ̼́
* ʲ̼̏
* ʲ̼̃
* ʲ̼̀
* ʲ̼̌
* ʲ̼̽
* ʲ̼̊
* ʲ̼̅
* ʲ̼͊
* ʲ̼̂
* ʲ̼͌
* ʲ̻͋
* ʲ̻̈
* ʲ̻̆
* ʲ̻͆
* ʲ̻̄
* ʲ̻̋
* ʲ̻̇
* ʲ̻́
* ʲ̻̏
* ʲ̻̃
* ʲ̻̀
* ʲ̻̌
* ʲ̻̽
* ʲ̻̊
* ʲ̻̅
* ʲ̻͊
* ʲ̻̂
* ʲ̻͌
* ʲ͎͋
* ʲ͎̈
* ʲ͎̆
* ʲ͎͆
* ʲ͎̄
* ʲ͎̋
* ʲ͎̇
* ʲ͎́
* ʲ͎̏
* ʲ͎̃
* ʲ͎̀
* ʲ͎̌
* ʲ͎̽
* ʲ͎̊
* ʲ͎̅
* ʲ͎͊
* ʲ͎̂
* ʲ͎͌
* ʲ̩͋
* ʲ̩̈
* ʲ̩̆
* ʲ̩͆
* ʲ̩̄
* ʲ̩̋
* ʲ̩̇
* ʲ̩́
* ʲ̩̏
* ʲ̩̃
* ʲ̩̀
* ʲ̩̌
* ʲ̩̽
* ʲ̩̊
* ʲ̩̅
* ʲ̩͊
* ʲ̩̂
* ʲ̩͌
* ʲ̰͋
* ʲ̰̈
* ʲ̰̆
* ʲ̰͆
* ʲ̰̄
* ʲ̰̋
* ʲ̰̇
* ʲ̰́
* ʲ̰̏
* ʲ̰̃
* ʲ̰̀
* ʲ̰̌
* ʲ̰̽
* ʲ̰̊
* ʲ̰̅
* ʲ̰͊
* ʲ̰̂
* ʲ̰͌
* ʲ̟͋
* ʲ̟̈
* ʲ̟̆
* ʲ̟͆
* ʲ̟̄
* ʲ̟̋
* ʲ̟̇
* ʲ̟́
* ʲ̟̏
* ʲ̟̃
* ʲ̟̀
* ʲ̟̌
* ʲ̟̽
* ʲ̟̊
* ʲ̟̅
* ʲ̟͊
* ʲ̟̂
* ʲ̟͌
* ʲ̥͋
* ʲ̥̈
* ʲ̥̆
* ʲ̥͆
* ʲ̥̄
* ʲ̥̋
* ʲ̥̇
* ʲ̥́
* ʲ̥̏
* ʲ̥̃
* ʲ̥̀
* ʲ̥̌
* ʲ̥̽
* ʲ̥̊
* ʲ̥̅
* ʲ̥͊
* ʲ̥̂
* ʲ̥͌
* ʲ̬͋
* ʲ̬̈
* ʲ̬̆
* ʲ̬͆
* ʲ̬̄
* ʲ̬̋
* ʲ̬̇
* ʲ̬́
* ʲ̬̏
* ʲ̬̃
* ʲ̬̀
* ʲ̬̌
* ʲ̬̽
* ʲ̬̊
* ʲ̬̅
* ʲ̬͊
* ʲ̬̂
* ʲ̬͌
* ʲ̝͋
* ʲ̝̈
* ʲ̝̆
* ʲ̝͆
* ʲ̝̄
* ʲ̝̋
* ʲ̝̇
* ʲ̝́
* ʲ̝̏
* ʲ̝̃
* ʲ̝̀
* ʲ̝̌
* ʲ̝̽
* ʲ̝̊
* ʲ̝̅
* ʲ̝͊
* ʲ̝̂
* ʲ̝͌
* ʲ̲͋
* ʲ̲̈
* ʲ̲̆
* ʲ̲͆
* ʲ̲̄
* ʲ̲̋
* ʲ̲̇
* ʲ̲́
* ʲ̲̏
* ʲ̲̃
* ʲ̲̀
* ʲ̲̌
* ʲ̲̽
* ʲ̲̊
* ʲ̲̅
* ʲ̲͊
* ʲ̲̂
* ʲ̲͌
* ʲ͉͋
* ʲ͉̈
* ʲ͉̆
* ʲ͉͆
* ʲ͉̄
* ʲ͉̋
* ʲ͉̇
* ʲ͉́
* ʲ͉̏
* ʲ͉̃
* ʲ͉̀
* ʲ͉̌
* ʲ͉̽
* ʲ͉̊
* ʲ͉̅
* ʲ͉͊
* ʲ͉̂
* ʲ͉͌
* ʲ̨͋
* ʲ̨̈
* ʲ̨̆
* ʲ̨͆
* ʲ̨̄
* ʲ̨̋
* ʲ̨̇
* ʲ̨́
* ʲ̨̏
* ʲ̨̃
* ʲ̨̀
* ʲ̨̌
* ʲ̨̽
* ʲ̨̊
* ʲ̨̅
* ʲ̨͊
* ʲ̨̂
* ʲ̨͌
* ʲ̤͋
* ʲ̤̈
* ʲ̤̆
* ʲ̤͆
* ʲ̤̄
* ʲ̤̋
* ʲ̤̇
* ʲ̤́
* ʲ̤̏
* ʲ̤̃
* ʲ̤̀
* ʲ̤̌
* ʲ̤̽
* ʲ̤̊
* ʲ̤̅
* ʲ̤͊
* ʲ̤̂
* ʲ̤͌
* ʲ̴͋
* ʲ̴̈
* ʲ̴̆
* ʲ̴͆
* ʲ̴̄
* ʲ̴̋
* ʲ̴̇
* ʲ̴́
* ʲ̴̏
* ʲ̴̃
* ʲ̴̀
* ʲ̴̌
* ʲ̴̽
* ʲ̴̊
* ʲ̴̅
* ʲ̴͊
* ʲ̴̂
* ʲ̴͌
* ʲ͍͋
* ʲ͍̈
* ʲ͍̆
* ʲ͍͆
* ʲ͍̄
* ʲ͍̋
* ʲ͍̇
* ʲ͍́
* ʲ͍̏
* ʲ͍̃
* ʲ͍̀
* ʲ͍̌
* ʲ͍̽
* ʲ͍̊
* ʲ͍̅
* ʲ͍͊
* ʲ͍̂
* ʲ͍͌
* ʲ̦͋
* ʲ̦̈
* ʲ̦̆
* ʲ̦͆
* ʲ̦̄
* ʲ̦̋
* ʲ̦̇
* ʲ̦́
* ʲ̦̏
* ʲ̦̃
* ʲ̦̀
* ʲ̦̌
* ʲ̦̽
* ʲ̦̊
* ʲ̦̅
* ʲ̦͊
* ʲ̦̂
* ʲ̦͌
* ʲ͋
* ʲ̈
* ʲ̆
* ʲ͆
* ʲ̄
* ʲ̋
* ʲ̇
* ʲ́
* ʲ̏
* ʲ̃
* ʲ̀
* ʲ̌
* ʲ̽
* ʲ̊
* ʲ̅
* ʲ͊
* ʲ̂
* ʲ͌
* ʝ̪͋
* ʝ̪̈
* ʝ̪̆
* ʝ̪͆
* ʝ̪̄
* ʝ̪̋
* ʝ̪̇
* ʝ̪́
* ʝ̪̏
* ʝ̪̃
* ʝ̪̀
* ʝ̪̌
* ʝ̪̽
* ʝ̪̊
* ʝ̪̅
* ʝ̪͊
* ʝ̪̂
* ʝ̪͌
* ʝ̞͋
* ʝ̞̈
* ʝ̞̆
* ʝ̞͆
* ʝ̞̄
* ʝ̞̋
* ʝ̞̇
* ʝ̞́
* ʝ̞̏
* ʝ̞̃
* ʝ̞̀
* ʝ̞̌
* ʝ̞̽
* ʝ̞̊
* ʝ̞̅
* ʝ̞͊
* ʝ̞̂
* ʝ̞͌
* ʝ͇͋
* ʝ͇̈
* ʝ͇̆
* ʝ͇͆
* ʝ͇̄
* ʝ͇̋
* ʝ͇̇
* ʝ͇́
* ʝ͇̏
* ʝ͇̃
* ʝ͇̀
* ʝ͇̌
* ʝ͇̽
* ʝ͇̊
* ʝ͇̅
* ʝ͇͊
* ʝ͇̂
* ʝ͇͌
* ʝ̧͋
* ʝ̧̈
* ʝ̧̆
* ʝ̧͆
* ʝ̧̄
* ʝ̧̋
* ʝ̧̇
* ʝ̧́
* ʝ̧̏
* ʝ̧̃
* ʝ̧̀
* ʝ̧̌
* ʝ̧̽
* ʝ̧̊
* ʝ̧̅
* ʝ̧͊
* ʝ̧̂
* ʝ̧͌
* ʝ̜͋
* ʝ̜̈
* ʝ̜̆
* ʝ̜͆
* ʝ̜̄
* ʝ̜̋
* ʝ̜̇
* ʝ̜́
* ʝ̜̏
* ʝ̜̃
* ʝ̜̀
* ʝ̜̌
* ʝ̜̽
* ʝ̜̊
* ʝ̜̅
* ʝ̜͊
* ʝ̜̂
* ʝ̜͌
* ʝ̘͋
* ʝ̘̈
* ʝ̘̆
* ʝ̘͆
* ʝ̘̄
* ʝ̘̋
* ʝ̘̇
* ʝ̘́
* ʝ̘̏
* ʝ̘̃
* ʝ̘̀
* ʝ̘̌
* ʝ̘̽
* ʝ̘̊
* ʝ̘̅
* ʝ̘͊
* ʝ̘̂
* ʝ̘͌
* ʝ̺͋
* ʝ̺̈
* ʝ̺̆
* ʝ̺͆
* ʝ̺̄
* ʝ̺̋
* ʝ̺̇
* ʝ̺́
* ʝ̺̏
* ʝ̺̃
* ʝ̺̀
* ʝ̺̌
* ʝ̺̽
* ʝ̺̊
* ʝ̺̅
* ʝ̺͊
* ʝ̺̂
* ʝ̺͌
* ʝ͈͋
* ʝ͈̈
* ʝ͈̆
* ʝ͈͆
* ʝ͈̄
* ʝ͈̋
* ʝ͈̇
* ʝ͈́
* ʝ͈̏
* ʝ͈̃
* ʝ͈̀
* ʝ͈̌
* ʝ͈̽
* ʝ͈̊
* ʝ͈̅
* ʝ͈͊
* ʝ͈̂
* ʝ͈͌
* ʝ̹͋
* ʝ̹̈
* ʝ̹̆
* ʝ̹͆
* ʝ̹̄
* ʝ̹̋
* ʝ̹̇
* ʝ̹́
* ʝ̹̏
* ʝ̹̃
* ʝ̹̀
* ʝ̹̌
* ʝ̹̽
* ʝ̹̊
* ʝ̹̅
* ʝ̹͊
* ʝ̹̂
* ʝ̹͌
* ʝ̙͋
* ʝ̙̈
* ʝ̙̆
* ʝ̙͆
* ʝ̙̄
* ʝ̙̋
* ʝ̙̇
* ʝ̙́
* ʝ̙̏
* ʝ̙̃
* ʝ̙̀
* ʝ̙̌
* ʝ̙̽
* ʝ̙̊
* ʝ̙̅
* ʝ̙͊
* ʝ̙̂
* ʝ̙͌
* ʝ̠͋
* ʝ̠̈
* ʝ̠̆
* ʝ̠͆
* ʝ̠̄
* ʝ̠̋
* ʝ̠̇
* ʝ̠́
* ʝ̠̏
* ʝ̠̃
* ʝ̠̀
* ʝ̠̌
* ʝ̠̽
* ʝ̠̊
* ʝ̠̅
* ʝ̠͊
* ʝ̠̂
* ʝ̠͌
* ʝ̼͋
* ʝ̼̈
* ʝ̼̆
* ʝ̼͆
* ʝ̼̄
* ʝ̼̋
* ʝ̼̇
* ʝ̼́
* ʝ̼̏
* ʝ̼̃
* ʝ̼̀
* ʝ̼̌
* ʝ̼̽
* ʝ̼̊
* ʝ̼̅
* ʝ̼͊
* ʝ̼̂
* ʝ̼͌
* ʝ̻͋
* ʝ̻̈
* ʝ̻̆
* ʝ̻͆
* ʝ̻̄
* ʝ̻̋
* ʝ̻̇
* ʝ̻́
* ʝ̻̏
* ʝ̻̃
* ʝ̻̀
* ʝ̻̌
* ʝ̻̽
* ʝ̻̊
* ʝ̻̅
* ʝ̻͊
* ʝ̻̂
* ʝ̻͌
* ʝ͎͋
* ʝ͎̈
* ʝ͎̆
* ʝ͎͆
* ʝ͎̄
* ʝ͎̋
* ʝ͎̇
* ʝ͎́
* ʝ͎̏
* ʝ͎̃
* ʝ͎̀
* ʝ͎̌
* ʝ͎̽
* ʝ͎̊
* ʝ͎̅
* ʝ͎͊
* ʝ͎̂
* ʝ͎͌
* ʝ̩͋
* ʝ̩̈
* ʝ̩̆
* ʝ̩͆
* ʝ̩̄
* ʝ̩̋
* ʝ̩̇
* ʝ̩́
* ʝ̩̏
* ʝ̩̃
* ʝ̩̀
* ʝ̩̌
* ʝ̩̽
* ʝ̩̊
* ʝ̩̅
* ʝ̩͊
* ʝ̩̂
* ʝ̩͌
* ʝ̰͋
* ʝ̰̈
* ʝ̰̆
* ʝ̰͆
* ʝ̰̄
* ʝ̰̋
* ʝ̰̇
* ʝ̰́
* ʝ̰̏
* ʝ̰̃
* ʝ̰̀
* ʝ̰̌
* ʝ̰̽
* ʝ̰̊
* ʝ̰̅
* ʝ̰͊
* ʝ̰̂
* ʝ̰͌
* ʝ̟͋
* ʝ̟̈
* ʝ̟̆
* ʝ̟͆
* ʝ̟̄
* ʝ̟̋
* ʝ̟̇
* ʝ̟́
* ʝ̟̏
* ʝ̟̃
* ʝ̟̀
* ʝ̟̌
* ʝ̟̽
* ʝ̟̊
* ʝ̟̅
* ʝ̟͊
* ʝ̟̂
* ʝ̟͌
* ʝ̥͋
* ʝ̥̈
* ʝ̥̆
* ʝ̥͆
* ʝ̥̄
* ʝ̥̋
* ʝ̥̇
* ʝ̥́
* ʝ̥̏
* ʝ̥̃
* ʝ̥̀
* ʝ̥̌
* ʝ̥̽
* ʝ̥̊
* ʝ̥̅
* ʝ̥͊
* ʝ̥̂
* ʝ̥͌
* ʝ̬͋
* ʝ̬̈
* ʝ̬̆
* ʝ̬͆
* ʝ̬̄
* ʝ̬̋
* ʝ̬̇
* ʝ̬́
* ʝ̬̏
* ʝ̬̃
* ʝ̬̀
* ʝ̬̌
* ʝ̬̽
* ʝ̬̊
* ʝ̬̅
* ʝ̬͊
* ʝ̬̂
* ʝ̬͌
* ʝ̝͋
* ʝ̝̈
* ʝ̝̆
* ʝ̝͆
* ʝ̝̄
* ʝ̝̋
* ʝ̝̇
* ʝ̝́
* ʝ̝̏
* ʝ̝̃
* ʝ̝̀
* ʝ̝̌
* ʝ̝̽
* ʝ̝̊
* ʝ̝̅
* ʝ̝͊
* ʝ̝̂
* ʝ̝͌
* ʝ̲͋
* ʝ̲̈
* ʝ̲̆
* ʝ̲͆
* ʝ̲̄
* ʝ̲̋
* ʝ̲̇
* ʝ̲́
* ʝ̲̏
* ʝ̲̃
* ʝ̲̀
* ʝ̲̌
* ʝ̲̽
* ʝ̲̊
* ʝ̲̅
* ʝ̲͊
* ʝ̲̂
* ʝ̲͌
* ʝ͉͋
* ʝ͉̈
* ʝ͉̆
* ʝ͉͆
* ʝ͉̄
* ʝ͉̋
* ʝ͉̇
* ʝ͉́
* ʝ͉̏
* ʝ͉̃
* ʝ͉̀
* ʝ͉̌
* ʝ͉̽
* ʝ͉̊
* ʝ͉̅
* ʝ͉͊
* ʝ͉̂
* ʝ͉͌
* ʝ̨͋
* ʝ̨̈
* ʝ̨̆
* ʝ̨͆
* ʝ̨̄
* ʝ̨̋
* ʝ̨̇
* ʝ̨́
* ʝ̨̏
* ʝ̨̃
* ʝ̨̀
* ʝ̨̌
* ʝ̨̽
* ʝ̨̊
* ʝ̨̅
* ʝ̨͊
* ʝ̨̂
* ʝ̨͌
* ʝ̤͋
* ʝ̤̈
* ʝ̤̆
* ʝ̤͆
* ʝ̤̄
* ʝ̤̋
* ʝ̤̇
* ʝ̤́
* ʝ̤̏
* ʝ̤̃
* ʝ̤̀
* ʝ̤̌
* ʝ̤̽
* ʝ̤̊
* ʝ̤̅
* ʝ̤͊
* ʝ̤̂
* ʝ̤͌
* ʝ̴͋
* ʝ̴̈
* ʝ̴̆
* ʝ̴͆
* ʝ̴̄
* ʝ̴̋
* ʝ̴̇
* ʝ̴́
* ʝ̴̏
* ʝ̴̃
* ʝ̴̀
* ʝ̴̌
* ʝ̴̽
* ʝ̴̊
* ʝ̴̅
* ʝ̴͊
* ʝ̴̂
* ʝ̴͌
* ʝ͍͋
* ʝ͍̈
* ʝ͍̆
* ʝ͍͆
* ʝ͍̄
* ʝ͍̋
* ʝ͍̇
* ʝ͍́
* ʝ͍̏
* ʝ͍̃
* ʝ͍̀
* ʝ͍̌
* ʝ͍̽
* ʝ͍̊
* ʝ͍̅
* ʝ͍͊
* ʝ͍̂
* ʝ͍͌
* ʝ̦͋
* ʝ̦̈
* ʝ̦̆
* ʝ̦͆
* ʝ̦̄
* ʝ̦̋
* ʝ̦̇
* ʝ̦́
* ʝ̦̏
* ʝ̦̃
* ʝ̦̀
* ʝ̦̌
* ʝ̦̽
* ʝ̦̊
* ʝ̦̅
* ʝ̦͊
* ʝ̦̂
* ʝ̦͌
* ʝ͋
* ʝ̈
* ʝ̆
* ʝ͆
* ʝ̄
* ʝ̋
* ʝ̇
* ʝ́
* ʝ̏
* ʝ̃
* ʝ̀
* ʝ̌
* ʝ̽
* ʝ̊
* ʝ̅
* ʝ͊
* ʝ̂
* ʝ͌
* i̪͋
* i̪͆
* i̪̋
* i̪̇
* ȉ̪
* ǐ̪
* i̪̽
* i̪̊
* i̪̅
* i̪͊
* i̪͌
* i̞͋
* i̞͆
* i̞̋
* i̞̇
* ȉ̞
* ǐ̞
* i̞̽
* i̞̊
* i̞̅
* i̞͊
* i̞͌
* i͇͋
* i͇͆
* i͇̋
* i͇̇
* ȉ͇
* ǐ͇
* i͇̽
* i͇̊
* i͇̅
* i͇͊
* i͇͌
* i̧͋
* i̧͆
* i̧̋
* i̧̇
* ȉ̧
* ǐ̧
* i̧̽
* i̧̊
* i̧̅
* i̧͊
* i̧͌
* i̜͋
* i̜͆
* i̜̋
* i̜̇
* ȉ̜
* ǐ̜
* i̜̽
* i̜̊
* i̜̅
* i̜͊
* i̜͌
* i̘͋
* i̘͆
* i̘̋
* i̘̇
* ȉ̘
* ǐ̘
* i̘̽
* i̘̊
* i̘̅
* i̘͊
* i̘͌
* i̺͋
* i̺͆
* i̺̋
* i̺̇
* ȉ̺
* ǐ̺
* i̺̽
* i̺̊
* i̺̅
* i̺͊
* i̺͌
* i͈͋
* i͈͆
* i͈̋
* i͈̇
* ȉ͈
* ǐ͈
* i͈̽
* i͈̊
* i͈̅
* i͈͊
* i͈͌
* i̹͋
* i̹͆
* i̹̋
* i̹̇
* ȉ̹
* ǐ̹
* i̹̽
* i̹̊
* i̹̅
* i̹͊
* i̹͌
* i̙͋
* i̙͆
* i̙̋
* i̙̇
* ȉ̙
* ǐ̙
* i̙̽
* i̙̊
* i̙̅
* i̙͊
* i̙͌
* i̠͋
* i̠͆
* i̠̋
* i̠̇
* ȉ̠
* ǐ̠
* i̠̽
* i̠̊
* i̠̅
* i̠͊
* i̠͌
* i̼͋
* i̼͆
* i̼̋
* i̼̇
* ȉ̼
* ǐ̼
* i̼̽
* i̼̊
* i̼̅
* i̼͊
* i̼͌
* i̻͋
* i̻͆
* i̻̋
* i̻̇
* ȉ̻
* ǐ̻
* i̻̽
* i̻̊
* i̻̅
* i̻͊
* i̻͌
* i͎͋
* i͎͆
* i͎̋
* i͎̇
* ȉ͎
* ǐ͎
* i͎̽
* i͎̊
* i͎̅
* i͎͊
* i͎͌
* i̩͋
* i̩͆
* i̩̋
* i̩̇
* ȉ̩
* ǐ̩
* i̩̽
* i̩̊
* i̩̅
* i̩͊
* i̩͌
* ḭ͋
* ḭ͆
* ḭ̋
* ḭ̇
* ḭ̏
* ḭ̌
* ḭ̽
* ḭ̊
* ḭ̅
* ḭ͊
* ḭ͌
* i̟͋
* i̟͆
* i̟̋
* i̟̇
* ȉ̟
* ǐ̟
* i̟̽
* i̟̊
* i̟̅
* i̟͊
* i̟͌
* i̥͋
* i̥͆
* i̥̋
* i̥̇
* ȉ̥
* ǐ̥
* i̥̽
* i̥̊
* i̥̅
* i̥͊
* i̥͌
* i̬͋
* i̬͆
* i̬̋
* i̬̇
* ȉ̬
* ǐ̬
* i̬̽
* i̬̊
* i̬̅
* i̬͊
* i̬͌
* i̝͋
* i̝͆
* i̝̋
* i̝̇
* ȉ̝
* ǐ̝
* i̝̽
* i̝̊
* i̝̅
* i̝͊
* i̝͌
* i̲͋
* i̲͆
* i̲̋
* i̲̇
* ȉ̲
* ǐ̲
* i̲̽
* i̲̊
* i̲̅
* i̲͊
* i̲͌
* i͉͋
* i͉͆
* i͉̋
* i͉̇
* ȉ͉
* ǐ͉
* i͉̽
* i͉̊
* i͉̅
* i͉͊
* i͉͌
* i̤͋
* i̤͆
* i̤̋
* i̤̇
* ȉ̤
* ǐ̤
* i̤̽
* i̤̊
* i̤̅
* i̤͊
* i̤͌
* i̴͋
* i̴͆
* i̴̋
* i̴̇
* ȉ̴
* ǐ̴
* i̴̽
* i̴̊
* i̴̅
* i̴͊
* i̴͌
* i͍͋
* i͍͆
* i͍̋
* i͍̇
* ȉ͍
* ǐ͍
* i͍̽
* i͍̊
* i͍̅
* i͍͊
* i͍͌
* i̦͋
* i̦͆
* i̦̋
* i̦̇
* ȉ̦
* ǐ̦
* i̦̽
* i̦̊
* i̦̅
* i̦͊
* i̦͌
* i͋
* i͆
* i̇
* ȉ
* ǐ
* i̽
* i̅
* i͊
* i͌
* į̪͋
* į̪̈
* į̪̆
* į̪͆
* į̪̄
* į̪̋
* į̪̇
* į̪́
* į̪̏
* į̪̃
* į̪̀
* į̪̌
* į̪̽
* į̪̊
* į̪̅
* į̪͊
* į̪̂
* į̪͌
* į̞͋
* į̞̈
* į̞̆
* į̞͆
* į̞̄
* į̞̋
* į̞̇
* į̞́
* į̞̏
* į̞̃
* į̞̀
* į̞̌
* į̞̽
* į̞̊
* į̞̅
* į̞͊
* į̞̂
* į̞͌
* į͇͋
* į͇̈
* į͇̆
* į͇͆
* į͇̄
* į͇̋
* į͇̇
* į͇́
* į͇̏
* į͇̃
* į͇̀
* į͇̌
* į͇̽
* į͇̊
* į͇̅
* į͇͊
* į͇̂
* į͇͌
* į̧͋
* į̧̈
* į̧̆
* į̧͆
* į̧̄
* į̧̋
* į̧̇
* į̧́
* į̧̏
* į̧̃
* į̧̀
* į̧̌
* į̧̽
* į̧̊
* į̧̅
* į̧͊
* į̧̂
* į̧͌
* į̜͋
* į̜̈
* į̜̆
* į̜͆
* į̜̄
* į̜̋
* į̜̇
* į̜́
* į̜̏
* į̜̃
* į̜̀
* į̜̌
* į̜̽
* į̜̊
* į̜̅
* į̜͊
* į̜̂
* į̜͌
* į̘͋
* į̘̈
* į̘̆
* į̘͆
* į̘̄
* į̘̋
* į̘̇
* į̘́
* į̘̏
* į̘̃
* į̘̀
* į̘̌
* į̘̽
* į̘̊
* į̘̅
* į̘͊
* į̘̂
* į̘͌
* į̺͋
* į̺̈
* į̺̆
* į̺͆
* į̺̄
* į̺̋
* į̺̇
* į̺́
* į̺̏
* į̺̃
* į̺̀
* į̺̌
* į̺̽
* į̺̊
* į̺̅
* į̺͊
* į̺̂
* į̺͌
* į͈͋
* į͈̈
* į͈̆
* į͈͆
* į͈̄
* į͈̋
* į͈̇
* į͈́
* į͈̏
* į͈̃
* į͈̀
* į͈̌
* į͈̽
* į͈̊
* į͈̅
* į͈͊
* į͈̂
* į͈͌
* į̹͋
* į̹̈
* į̹̆
* į̹͆
* į̹̄
* į̹̋
* į̹̇
* į̹́
* į̹̏
* į̹̃
* į̹̀
* į̹̌
* į̹̽
* į̹̊
* į̹̅
* į̹͊
* į̹̂
* į̹͌
* į̙͋
* į̙̈
* į̙̆
* į̙͆
* į̙̄
* į̙̋
* į̙̇
* į̙́
* į̙̏
* į̙̃
* į̙̀
* į̙̌
* į̙̽
* į̙̊
* į̙̅
* į̙͊
* į̙̂
* į̙͌
* į̠͋
* į̠̈
* į̠̆
* į̠͆
* į̠̄
* į̠̋
* į̠̇
* į̠́
* į̠̏
* į̠̃
* į̠̀
* į̠̌
* į̠̽
* į̠̊
* į̠̅
* į̠͊
* į̠̂
* į̠͌
* į̼͋
* į̼̈
* į̼̆
* į̼͆
* į̼̄
* į̼̋
* į̼̇
* į̼́
* į̼̏
* į̼̃
* į̼̀
* į̼̌
* į̼̽
* į̼̊
* į̼̅
* į̼͊
* į̼̂
* į̼͌
* į̻͋
* į̻̈
* į̻̆
* į̻͆
* į̻̄
* į̻̋
* į̻̇
* į̻́
* į̻̏
* į̻̃
* į̻̀
* į̻̌
* į̻̽
* į̻̊
* į̻̅
* į̻͊
* į̻̂
* į̻͌
* į͎͋
* į͎̈
* į͎̆
* į͎͆
* į͎̄
* į͎̋
* į͎̇
* į͎́
* į͎̏
* į͎̃
* į͎̀
* į͎̌
* į͎̽
* į͎̊
* į͎̅
* į͎͊
* į͎̂
* į͎͌
* į̩͋
* į̩̈
* į̩̆
* į̩͆
* į̩̄
* į̩̋
* į̩̇
* į̩́
* į̩̏
* į̩̃
* į̩̀
* į̩̌
* į̩̽
* į̩̊
* į̩̅
* į̩͊
* į̩̂
* į̩͌
* į̰͋
* į̰̈
* į̰̆
* į̰͆
* į̰̄
* į̰̋
* į̰̇
* į̰́
* į̰̏
* į̰̃
* į̰̀
* į̰̌
* į̰̽
* į̰̊
* į̰̅
* į̰͊
* į̰̂
* į̰͌
* į̟͋
* į̟̈
* į̟̆
* į̟͆
* į̟̄
* į̟̋
* į̟̇
* į̟́
* į̟̏
* į̟̃
* į̟̀
* į̟̌
* į̟̽
* į̟̊
* į̟̅
* į̟͊
* į̟̂
* į̟͌
* į̥͋
* į̥̈
* į̥̆
* į̥͆
* į̥̄
* į̥̋
* į̥̇
* į̥́
* į̥̏
* į̥̃
* į̥̀
* į̥̌
* į̥̽
* į̥̊
* į̥̅
* į̥͊
* į̥̂
* į̥͌
* į̬͋
* į̬̈
* į̬̆
* į̬͆
* į̬̄
* į̬̋
* į̬̇
* į̬́
* į̬̏
* į̬̃
* į̬̀
* į̬̌
* į̬̽
* į̬̊
* į̬̅
* į̬͊
* į̬̂
* į̬͌
* į̝͋
* į̝̈
* į̝̆
* į̝͆
* į̝̄
* į̝̋
* į̝̇
* į̝́
* į̝̏
* į̝̃
* į̝̀
* į̝̌
* į̝̽
* į̝̊
* į̝̅
* į̝͊
* į̝̂
* į̝͌
* į̲͋
* į̲̈
* į̲̆
* į̲͆
* į̲̄
* į̲̋
* į̲̇
* į̲́
* į̲̏
* į̲̃
* į̲̀
* į̲̌
* į̲̽
* į̲̊
* į̲̅
* į̲͊
* į̲̂
* į̲͌
* į͉͋
* į͉̈
* į͉̆
* į͉͆
* į͉̄
* į͉̋
* į͉̇
* į͉́
* į͉̏
* į͉̃
* į͉̀
* į͉̌
* į͉̽
* į͉̊
* į͉̅
* į͉͊
* į͉̂
* į͉͌
* į̨͋
* į̨̈
* į̨̆
* į̨͆
* į̨̄
* į̨̋
* į̨̇
* į̨́
* į̨̏
* į̨̃
* į̨̀
* į̨̌
* į̨̽
* į̨̊
* į̨̅
* į̨͊
* į̨̂
* į̨͌
* į̤͋
* į̤̈
* į̤̆
* į̤͆
* į̤̄
* į̤̋
* į̤̇
* į̤́
* į̤̏
* į̤̃
* į̤̀
* į̤̌
* į̤̽
* į̤̊
* į̤̅
* į̤͊
* į̤̂
* į̤͌
* į̴͋
* į̴̈
* į̴̆
* į̴͆
* į̴̄
* į̴̋
* į̴̇
* į̴́
* į̴̏
* į̴̃
* į̴̀
* į̴̌
* į̴̽
* į̴̊
* į̴̅
* į̴͊
* į̴̂
* į̴͌
* į͍͋
* į͍̈
* į͍̆
* į͍͆
* į͍̄
* į͍̋
* į͍̇
* į͍́
* į͍̏
* į͍̃
* į͍̀
* į͍̌
* į͍̽
* į͍̊
* į͍̅
* į͍͊
* į͍̂
* į͍͌
* į̦͋
* į̦̈
* į̦̆
* į̦͆
* į̦̄
* į̦̋
* į̦̇
* į̦́
* į̦̏
* į̦̃
* į̦̀
* į̦̌
* į̦̽
* į̦̊
* į̦̅
* į̦͊
* į̦̂
* į̦͌
* į͋
* į̈
* į̆
* į͆
* į̋
* į̇
* į̏
* į̽
* į̊
* į̅
* į͊
* į͌
* ɨ̪͋
* ɨ̪̈
* ɨ̪̆
* ɨ̪͆
* ɨ̪̄
* ɨ̪̋
* ɨ̪̇
* ɨ̪́
* ɨ̪̏
* ɨ̪̃
* ɨ̪̀
* ɨ̪̌
* ɨ̪̽
* ɨ̪̊
* ɨ̪̅
* ɨ̪͊
* ɨ̪̂
* ɨ̪͌
* ɨ̞͋
* ɨ̞̈
* ɨ̞̆
* ɨ̞͆
* ɨ̞̄
* ɨ̞̋
* ɨ̞̇
* ɨ̞́
* ɨ̞̏
* ɨ̞̃
* ɨ̞̀
* ɨ̞̌
* ɨ̞̽
* ɨ̞̊
* ɨ̞̅
* ɨ̞͊
* ɨ̞̂
* ɨ̞͌
* ɨ͇͋
* ɨ͇̈
* ɨ͇̆
* ɨ͇͆
* ɨ͇̄
* ɨ͇̋
* ɨ͇̇
* ɨ͇́
* ɨ͇̏
* ɨ͇̃
* ɨ͇̀
* ɨ͇̌
* ɨ͇̽
* ɨ͇̊
* ɨ͇̅
* ɨ͇͊
* ɨ͇̂
* ɨ͇͌
* ɨ̧͋
* ɨ̧̈
* ɨ̧̆
* ɨ̧͆
* ɨ̧̄
* ɨ̧̋
* ɨ̧̇
* ɨ̧̏
* ɨ̧̃
* ɨ̧̽
* ɨ̧̊
* ɨ̧̅
* ɨ̧͊
* ɨ̧͌
* ɨ̜͋
* ɨ̜̈
* ɨ̜̆
* ɨ̜͆
* ɨ̜̄
* ɨ̜̋
* ɨ̜̇
* ɨ̜́
* ɨ̜̏
* ɨ̜̃
* ɨ̜̀
* ɨ̜̌
* ɨ̜̽
* ɨ̜̊
* ɨ̜̅
* ɨ̜͊
* ɨ̜̂
* ɨ̜͌
* ɨ̘͋
* ɨ̘̈
* ɨ̘̆
* ɨ̘͆
* ɨ̘̄
* ɨ̘̋
* ɨ̘̇
* ɨ̘́
* ɨ̘̏
* ɨ̘̃
* ɨ̘̀
* ɨ̘̌
* ɨ̘̽
* ɨ̘̊
* ɨ̘̅
* ɨ̘͊
* ɨ̘̂
* ɨ̘͌
* ɨ̺͋
* ɨ̺̈
* ɨ̺̆
* ɨ̺͆
* ɨ̺̄
* ɨ̺̋
* ɨ̺̇
* ɨ̺́
* ɨ̺̏
* ɨ̺̃
* ɨ̺̀
* ɨ̺̌
* ɨ̺̽
* ɨ̺̊
* ɨ̺̅
* ɨ̺͊
* ɨ̺̂
* ɨ̺͌
* ɨ͈͋
* ɨ͈̈
* ɨ͈̆
* ɨ͈͆
* ɨ͈̄
* ɨ͈̋
* ɨ͈̇
* ɨ͈́
* ɨ͈̏
* ɨ͈̃
* ɨ͈̀
* ɨ͈̌
* ɨ͈̽
* ɨ͈̊
* ɨ͈̅
* ɨ͈͊
* ɨ͈̂
* ɨ͈͌
* ɨ̹͋
* ɨ̹̈
* ɨ̹̆
* ɨ̹͆
* ɨ̹̄
* ɨ̹̋
* ɨ̹̇
* ɨ̹́
* ɨ̹̏
* ɨ̹̃
* ɨ̹̀
* ɨ̹̌
* ɨ̹̽
* ɨ̹̊
* ɨ̹̅
* ɨ̹͊
* ɨ̹̂
* ɨ̹͌
* ɨ̙͋
* ɨ̙̈
* ɨ̙̆
* ɨ̙͆
* ɨ̙̄
* ɨ̙̋
* ɨ̙̇
* ɨ̙́
* ɨ̙̏
* ɨ̙̃
* ɨ̙̀
* ɨ̙̌
* ɨ̙̽
* ɨ̙̊
* ɨ̙̅
* ɨ̙͊
* ɨ̙̂
* ɨ̙͌
* ɨ̠͋
* ɨ̠̈
* ɨ̠̆
* ɨ̠͆
* ɨ̠̄
* ɨ̠̋
* ɨ̠̇
* ɨ̠́
* ɨ̠̏
* ɨ̠̃
* ɨ̠̀
* ɨ̠̌
* ɨ̠̽
* ɨ̠̊
* ɨ̠̅
* ɨ̠͊
* ɨ̠̂
* ɨ̠͌
* ɨ̼͋
* ɨ̼̈
* ɨ̼̆
* ɨ̼͆
* ɨ̼̄
* ɨ̼̋
* ɨ̼̇
* ɨ̼́
* ɨ̼̏
* ɨ̼̃
* ɨ̼̀
* ɨ̼̌
* ɨ̼̽
* ɨ̼̊
* ɨ̼̅
* ɨ̼͊
* ɨ̼̂
* ɨ̼͌
* ɨ̻͋
* ɨ̻̈
* ɨ̻̆
* ɨ̻͆
* ɨ̻̄
* ɨ̻̋
* ɨ̻̇
* ɨ̻́
* ɨ̻̏
* ɨ̻̃
* ɨ̻̀
* ɨ̻̌
* ɨ̻̽
* ɨ̻̊
* ɨ̻̅
* ɨ̻͊
* ɨ̻̂
* ɨ̻͌
* ɨ͎͋
* ɨ͎̈
* ɨ͎̆
* ɨ͎͆
* ɨ͎̄
* ɨ͎̋
* ɨ͎̇
* ɨ͎́
* ɨ͎̏
* ɨ͎̃
* ɨ͎̀
* ɨ͎̌
* ɨ͎̽
* ɨ͎̊
* ɨ͎̅
* ɨ͎͊
* ɨ͎̂
* ɨ͎͌
* ɨ̩͋
* ɨ̩̈
* ɨ̩̆
* ɨ̩͆
* ɨ̩̄
* ɨ̩̋
* ɨ̩̇
* ɨ̩́
* ɨ̩̏
* ɨ̩̃
* ɨ̩̀
* ɨ̩̌
* ɨ̩̽
* ɨ̩̊
* ɨ̩̅
* ɨ̩͊
* ɨ̩̂
* ɨ̩͌
* ɨ̰͋
* ɨ̰̈
* ɨ̰̆
* ɨ̰͆
* ɨ̰̄
* ɨ̰̋
* ɨ̰̇
* ɨ̰́
* ɨ̰̏
* ɨ̰̃
* ɨ̰̀
* ɨ̰̌
* ɨ̰̽
* ɨ̰̊
* ɨ̰̅
* ɨ̰͊
* ɨ̰̂
* ɨ̰͌
* ɨ̟͋
* ɨ̟̈
* ɨ̟̆
* ɨ̟͆
* ɨ̟̄
* ɨ̟̋
* ɨ̟̇
* ɨ̟́
* ɨ̟̏
* ɨ̟̃
* ɨ̟̀
* ɨ̟̌
* ɨ̟̽
* ɨ̟̊
* ɨ̟̅
* ɨ̟͊
* ɨ̟̂
* ɨ̟͌
* ɨ̥͋
* ɨ̥̈
* ɨ̥̆
* ɨ̥͆
* ɨ̥̄
* ɨ̥̋
* ɨ̥̇
* ɨ̥́
* ɨ̥̏
* ɨ̥̃
* ɨ̥̀
* ɨ̥̌
* ɨ̥̽
* ɨ̥̊
* ɨ̥̅
* ɨ̥͊
* ɨ̥̂
* ɨ̥͌
* ɨ̬͋
* ɨ̬̈
* ɨ̬̆
* ɨ̬͆
* ɨ̬̄
* ɨ̬̋
* ɨ̬̇
* ɨ̬́
* ɨ̬̏
* ɨ̬̃
* ɨ̬̀
* ɨ̬̌
* ɨ̬̽
* ɨ̬̊
* ɨ̬̅
* ɨ̬͊
* ɨ̬̂
* ɨ̬͌
* ɨ̝͋
* ɨ̝̈
* ɨ̝̆
* ɨ̝͆
* ɨ̝̄
* ɨ̝̋
* ɨ̝̇
* ɨ̝́
* ɨ̝̏
* ɨ̝̃
* ɨ̝̀
* ɨ̝̌
* ɨ̝̽
* ɨ̝̊
* ɨ̝̅
* ɨ̝͊
* ɨ̝̂
* ɨ̝͌
* ɨ̲͋
* ɨ̲̈
* ɨ̲̆
* ɨ̲͆
* ɨ̲̄
* ɨ̲̋
* ɨ̲̇
* ɨ̲́
* ɨ̲̏
* ɨ̲̃
* ɨ̲̀
* ɨ̲̌
* ɨ̲̽
* ɨ̲̊
* ɨ̲̅
* ɨ̲͊
* ɨ̲̂
* ɨ̲͌
* ɨ͉͋
* ɨ͉̈
* ɨ͉̆
* ɨ͉͆
* ɨ͉̄
* ɨ͉̋
* ɨ͉̇
* ɨ͉́
* ɨ͉̏
* ɨ͉̃
* ɨ͉̀
* ɨ͉̌
* ɨ͉̽
* ɨ͉̊
* ɨ͉̅
* ɨ͉͊
* ɨ͉̂
* ɨ͉͌
* ɨ̨͋
* ɨ̨̈
* ɨ̨̆
* ɨ̨͆
* ɨ̨̄
* ɨ̨̋
* ɨ̨̇
* ɨ̨́
* ɨ̨̏
* ɨ̨̃
* ɨ̨̀
* ɨ̨̌
* ɨ̨̽
* ɨ̨̊
* ɨ̨̅
* ɨ̨͊
* ɨ̨̂
* ɨ̨͌
* ɨ̤͋
* ɨ̤̈
* ɨ̤̆
* ɨ̤͆
* ɨ̤̄
* ɨ̤̋
* ɨ̤̇
* ɨ̤́
* ɨ̤̏
* ɨ̤̃
* ɨ̤̀
* ɨ̤̌
* ɨ̤̽
* ɨ̤̊
* ɨ̤̅
* ɨ̤͊
* ɨ̤̂
* ɨ̤͌
* ɨ̴͋
* ɨ̴̈
* ɨ̴̆
* ɨ̴͆
* ɨ̴̄
* ɨ̴̋
* ɨ̴̇
* ɨ̴́
* ɨ̴̏
* ɨ̴̃
* ɨ̴̀
* ɨ̴̌
* ɨ̴̽
* ɨ̴̊
* ɨ̴̅
* ɨ̴͊
* ɨ̴̂
* ɨ̴͌
* ɨ͍͋
* ɨ͍̈
* ɨ͍̆
* ɨ͍͆
* ɨ͍̄
* ɨ͍̋
* ɨ͍̇
* ɨ͍́
* ɨ͍̏
* ɨ͍̃
* ɨ͍̀
* ɨ͍̌
* ɨ͍̽
* ɨ͍̊
* ɨ͍̅
* ɨ͍͊
* ɨ͍̂
* ɨ͍͌
* ɨ̦͋
* ɨ̦̈
* ɨ̦̆
* ɨ̦͆
* ɨ̦̄
* ɨ̦̋
* ɨ̦̇
* ɨ̦́
* ɨ̦̏
* ɨ̦̃
* ɨ̦̀
* ɨ̦̌
* ɨ̦̽
* ɨ̦̊
* ɨ̦̅
* ɨ̦͊
* ɨ̦̂
* ɨ̦͌
* ɨ͋
* ɨ̆
* ɨ͆
* ɨ̇
* ɨ̽
* ɨ̊
* ɨ̅
* ɨ͊
* ɨ͌
* ⁱ̪͋
* ⁱ̪̈
* ⁱ̪̆
* ⁱ̪͆
* ⁱ̪̄
* ⁱ̪̋
* ⁱ̪̇
* ⁱ̪́
* ⁱ̪̏
* ⁱ̪̃
* ⁱ̪̀
* ⁱ̪̌
* ⁱ̪̽
* ⁱ̪̊
* ⁱ̪̅
* ⁱ̪͊
* ⁱ̪̂
* ⁱ̪͌
* ⁱ̞͋
* ⁱ̞̈
* ⁱ̞̆
* ⁱ̞͆
* ⁱ̞̄
* ⁱ̞̋
* ⁱ̞̇
* ⁱ̞́
* ⁱ̞̏
* ⁱ̞̃
* ⁱ̞̀
* ⁱ̞̌
* ⁱ̞̽
* ⁱ̞̊
* ⁱ̞̅
* ⁱ̞͊
* ⁱ̞̂
* ⁱ̞͌
* ⁱ͇͋
* ⁱ͇̈
* ⁱ͇̆
* ⁱ͇͆
* ⁱ͇̄
* ⁱ͇̋
* ⁱ͇̇
* ⁱ͇́
* ⁱ͇̏
* ⁱ͇̃
* ⁱ͇̀
* ⁱ͇̌
* ⁱ͇̽
* ⁱ͇̊
* ⁱ͇̅
* ⁱ͇͊
* ⁱ͇̂
* ⁱ͇͌
* ⁱ̧͋
* ⁱ̧̈
* ⁱ̧̆
* ⁱ̧͆
* ⁱ̧̄
* ⁱ̧̋
* ⁱ̧̇
* ⁱ̧́
* ⁱ̧̏
* ⁱ̧̃
* ⁱ̧̀
* ⁱ̧̌
* ⁱ̧̽
* ⁱ̧̊
* ⁱ̧̅
* ⁱ̧͊
* ⁱ̧̂
* ⁱ̧͌
* ⁱ̜͋
* ⁱ̜̈
* ⁱ̜̆
* ⁱ̜͆
* ⁱ̜̄
* ⁱ̜̋
* ⁱ̜̇
* ⁱ̜́
* ⁱ̜̏
* ⁱ̜̃
* ⁱ̜̀
* ⁱ̜̌
* ⁱ̜̽
* ⁱ̜̊
* ⁱ̜̅
* ⁱ̜͊
* ⁱ̜̂
* ⁱ̜͌
* ⁱ̘͋
* ⁱ̘̈
* ⁱ̘̆
* ⁱ̘͆
* ⁱ̘̄
* ⁱ̘̋
* ⁱ̘̇
* ⁱ̘́
* ⁱ̘̏
* ⁱ̘̃
* ⁱ̘̀
* ⁱ̘̌
* ⁱ̘̽
* ⁱ̘̊
* ⁱ̘̅
* ⁱ̘͊
* ⁱ̘̂
* ⁱ̘͌
* ⁱ̺͋
* ⁱ̺̈
* ⁱ̺̆
* ⁱ̺͆
* ⁱ̺̄
* ⁱ̺̋
* ⁱ̺̇
* ⁱ̺́
* ⁱ̺̏
* ⁱ̺̃
* ⁱ̺̀
* ⁱ̺̌
* ⁱ̺̽
* ⁱ̺̊
* ⁱ̺̅
* ⁱ̺͊
* ⁱ̺̂
* ⁱ̺͌
* ⁱ͈͋
* ⁱ͈̈
* ⁱ͈̆
* ⁱ͈͆
* ⁱ͈̄
* ⁱ͈̋
* ⁱ͈̇
* ⁱ͈́
* ⁱ͈̏
* ⁱ͈̃
* ⁱ͈̀
* ⁱ͈̌
* ⁱ͈̽
* ⁱ͈̊
* ⁱ͈̅
* ⁱ͈͊
* ⁱ͈̂
* ⁱ͈͌
* ⁱ̹͋
* ⁱ̹̈
* ⁱ̹̆
* ⁱ̹͆
* ⁱ̹̄
* ⁱ̹̋
* ⁱ̹̇
* ⁱ̹́
* ⁱ̹̏
* ⁱ̹̃
* ⁱ̹̀
* ⁱ̹̌
* ⁱ̹̽
* ⁱ̹̊
* ⁱ̹̅
* ⁱ̹͊
* ⁱ̹̂
* ⁱ̹͌
* ⁱ̙͋
* ⁱ̙̈
* ⁱ̙̆
* ⁱ̙͆
* ⁱ̙̄
* ⁱ̙̋
* ⁱ̙̇
* ⁱ̙́
* ⁱ̙̏
* ⁱ̙̃
* ⁱ̙̀
* ⁱ̙̌
* ⁱ̙̽
* ⁱ̙̊
* ⁱ̙̅
* ⁱ̙͊
* ⁱ̙̂
* ⁱ̙͌
* ⁱ̠͋
* ⁱ̠̈
* ⁱ̠̆
* ⁱ̠͆
* ⁱ̠̄
* ⁱ̠̋
* ⁱ̠̇
* ⁱ̠́
* ⁱ̠̏
* ⁱ̠̃
* ⁱ̠̀
* ⁱ̠̌
* ⁱ̠̽
* ⁱ̠̊
* ⁱ̠̅
* ⁱ̠͊
* ⁱ̠̂
* ⁱ̠͌
* ⁱ̼͋
* ⁱ̼̈
* ⁱ̼̆
* ⁱ̼͆
* ⁱ̼̄
* ⁱ̼̋
* ⁱ̼̇
* ⁱ̼́
* ⁱ̼̏
* ⁱ̼̃
* ⁱ̼̀
* ⁱ̼̌
* ⁱ̼̽
* ⁱ̼̊
* ⁱ̼̅
* ⁱ̼͊
* ⁱ̼̂
* ⁱ̼͌
* ⁱ̻͋
* ⁱ̻̈
* ⁱ̻̆
* ⁱ̻͆
* ⁱ̻̄
* ⁱ̻̋
* ⁱ̻̇
* ⁱ̻́
* ⁱ̻̏
* ⁱ̻̃
* ⁱ̻̀
* ⁱ̻̌
* ⁱ̻̽
* ⁱ̻̊
* ⁱ̻̅
* ⁱ̻͊
* ⁱ̻̂
* ⁱ̻͌
* ⁱ͎͋
* ⁱ͎̈
* ⁱ͎̆
* ⁱ͎͆
* ⁱ͎̄
* ⁱ͎̋
* ⁱ͎̇
* ⁱ͎́
* ⁱ͎̏
* ⁱ͎̃
* ⁱ͎̀
* ⁱ͎̌
* ⁱ͎̽
* ⁱ͎̊
* ⁱ͎̅
* ⁱ͎͊
* ⁱ͎̂
* ⁱ͎͌
* ⁱ̩͋
* ⁱ̩̈
* ⁱ̩̆
* ⁱ̩͆
* ⁱ̩̄
* ⁱ̩̋
* ⁱ̩̇
* ⁱ̩́
* ⁱ̩̏
* ⁱ̩̃
* ⁱ̩̀
* ⁱ̩̌
* ⁱ̩̽
* ⁱ̩̊
* ⁱ̩̅
* ⁱ̩͊
* ⁱ̩̂
* ⁱ̩͌
* ⁱ̰͋
* ⁱ̰̈
* ⁱ̰̆
* ⁱ̰͆
* ⁱ̰̄
* ⁱ̰̋
* ⁱ̰̇
* ⁱ̰́
* ⁱ̰̏
* ⁱ̰̃
* ⁱ̰̀
* ⁱ̰̌
* ⁱ̰̽
* ⁱ̰̊
* ⁱ̰̅
* ⁱ̰͊
* ⁱ̰̂
* ⁱ̰͌
* ⁱ̟͋
* ⁱ̟̈
* ⁱ̟̆
* ⁱ̟͆
* ⁱ̟̄
* ⁱ̟̋
* ⁱ̟̇
* ⁱ̟́
* ⁱ̟̏
* ⁱ̟̃
* ⁱ̟̀
* ⁱ̟̌
* ⁱ̟̽
* ⁱ̟̊
* ⁱ̟̅
* ⁱ̟͊
* ⁱ̟̂
* ⁱ̟͌
* ⁱ̥͋
* ⁱ̥̈
* ⁱ̥̆
* ⁱ̥͆
* ⁱ̥̄
* ⁱ̥̋
* ⁱ̥̇
* ⁱ̥́
* ⁱ̥̏
* ⁱ̥̃
* ⁱ̥̀
* ⁱ̥̌
* ⁱ̥̽
* ⁱ̥̊
* ⁱ̥̅
* ⁱ̥͊
* ⁱ̥̂
* ⁱ̥͌
* ⁱ̬͋
* ⁱ̬̈
* ⁱ̬̆
* ⁱ̬͆
* ⁱ̬̄
* ⁱ̬̋
* ⁱ̬̇
* ⁱ̬́
* ⁱ̬̏
* ⁱ̬̃
* ⁱ̬̀
* ⁱ̬̌
* ⁱ̬̽
* ⁱ̬̊
* ⁱ̬̅
* ⁱ̬͊
* ⁱ̬̂
* ⁱ̬͌
* ⁱ̝͋
* ⁱ̝̈
* ⁱ̝̆
* ⁱ̝͆
* ⁱ̝̄
* ⁱ̝̋
* ⁱ̝̇
* ⁱ̝́
* ⁱ̝̏
* ⁱ̝̃
* ⁱ̝̀
* ⁱ̝̌
* ⁱ̝̽
* ⁱ̝̊
* ⁱ̝̅
* ⁱ̝͊
* ⁱ̝̂
* ⁱ̝͌
* ⁱ̲͋
* ⁱ̲̈
* ⁱ̲̆
* ⁱ̲͆
* ⁱ̲̄
* ⁱ̲̋
* ⁱ̲̇
* ⁱ̲́
* ⁱ̲̏
* ⁱ̲̃
* ⁱ̲̀
* ⁱ̲̌
* ⁱ̲̽
* ⁱ̲̊
* ⁱ̲̅
* ⁱ̲͊
* ⁱ̲̂
* ⁱ̲͌
* ⁱ͉͋
* ⁱ͉̈
* ⁱ͉̆
* ⁱ͉͆
* ⁱ͉̄
* ⁱ͉̋
* ⁱ͉̇
* ⁱ͉́
* ⁱ͉̏
* ⁱ͉̃
* ⁱ͉̀
* ⁱ͉̌
* ⁱ͉̽
* ⁱ͉̊
* ⁱ͉̅
* ⁱ͉͊
* ⁱ͉̂
* ⁱ͉͌
* ⁱ̨͋
* ⁱ̨̈
* ⁱ̨̆
* ⁱ̨͆
* ⁱ̨̄
* ⁱ̨̋
* ⁱ̨̇
* ⁱ̨́
* ⁱ̨̏
* ⁱ̨̃
* ⁱ̨̀
* ⁱ̨̌
* ⁱ̨̽
* ⁱ̨̊
* ⁱ̨̅
* ⁱ̨͊
* ⁱ̨̂
* ⁱ̨͌
* ⁱ̤͋
* ⁱ̤̈
* ⁱ̤̆
* ⁱ̤͆
* ⁱ̤̄
* ⁱ̤̋
* ⁱ̤̇
* ⁱ̤́
* ⁱ̤̏
* ⁱ̤̃
* ⁱ̤̀
* ⁱ̤̌
* ⁱ̤̽
* ⁱ̤̊
* ⁱ̤̅
* ⁱ̤͊
* ⁱ̤̂
* ⁱ̤͌
* ⁱ̴͋
* ⁱ̴̈
* ⁱ̴̆
* ⁱ̴͆
* ⁱ̴̄
* ⁱ̴̋
* ⁱ̴̇
* ⁱ̴́
* ⁱ̴̏
* ⁱ̴̃
* ⁱ̴̀
* ⁱ̴̌
* ⁱ̴̽
* ⁱ̴̊
* ⁱ̴̅
* ⁱ̴͊
* ⁱ̴̂
* ⁱ̴͌
* ⁱ͍͋
* ⁱ͍̈
* ⁱ͍̆
* ⁱ͍͆
* ⁱ͍̄
* ⁱ͍̋
* ⁱ͍̇
* ⁱ͍́
* ⁱ͍̏
* ⁱ͍̃
* ⁱ͍̀
* ⁱ͍̌
* ⁱ͍̽
* ⁱ͍̊
* ⁱ͍̅
* ⁱ͍͊
* ⁱ͍̂
* ⁱ͍͌
* ⁱ̦͋
* ⁱ̦̈
* ⁱ̦̆
* ⁱ̦͆
* ⁱ̦̄
* ⁱ̦̋
* ⁱ̦̇
* ⁱ̦́
* ⁱ̦̏
* ⁱ̦̃
* ⁱ̦̀
* ⁱ̦̌
* ⁱ̦̽
* ⁱ̦̊
* ⁱ̦̅
* ⁱ̦͊
* ⁱ̦̂
* ⁱ̦͌
* ⁱ͋
* ⁱ̈
* ⁱ̆
* ⁱ͆
* ⁱ̄
* ⁱ̋
* ⁱ̇
* ⁱ́
* ⁱ̏
* ⁱ̃
* ⁱ̀
* ⁱ̌
* ⁱ̽
* ⁱ̊
* ⁱ̅
* ⁱ͊
* ⁱ̂
* ⁱ͌
* j̪͋
* j̪̈
* j̪̆
* j̪͆
* j̪̄
* j̪̋
* j̪̇
* j̪́
* j̪̏
* j̪̃
* j̪̀
* ǰ̪
* j̪̽
* j̪̊
* j̪̅
* j̪͊
* j̪͌
* j̞͋
* j̞̈
* j̞̆
* j̞͆
* j̞̄
* j̞̋
* j̞̇
* j̞́
* j̞̏
* j̞̃
* j̞̀
* ǰ̞
* j̞̽
* j̞̊
* j̞̅
* j̞͊
* j̞͌
* j͇͋
* j͇̈
* j͇̆
* j͇͆
* j͇̄
* j͇̋
* j͇̇
* j͇́
* j͇̏
* j͇̃
* j͇̀
* ǰ͇
* j͇̽
* j͇̊
* j͇̅
* j͇͊
* j͇͌
* j̧͋
* j̧̈
* j̧̆
* j̧͆
* j̧̄
* j̧̋
* j̧̇
* j̧́
* j̧̏
* j̧̃
* j̧̀
* ǰ̧
* j̧̽
* j̧̊
* j̧̅
* j̧͊
* j̧͌
* j̜͋
* j̜̈
* j̜̆
* j̜͆
* j̜̄
* j̜̋
* j̜̇
* j̜́
* j̜̏
* j̜̃
* j̜̀
* ǰ̜
* j̜̽
* j̜̊
* j̜̅
* j̜͊
* j̜͌
* j̘͋
* j̘̈
* j̘̆
* j̘͆
* j̘̄
* j̘̋
* j̘̇
* j̘́
* j̘̏
* j̘̃
* j̘̀
* ǰ̘
* j̘̽
* j̘̊
* j̘̅
* j̘͊
* j̘͌
* j̺͋
* j̺̈
* j̺̆
* j̺͆
* j̺̄
* j̺̋
* j̺̇
* j̺́
* j̺̏
* j̺̃
* j̺̀
* ǰ̺
* j̺̽
* j̺̊
* j̺̅
* j̺͊
* j̺͌
* j͈͋
* j͈̈
* j͈̆
* j͈͆
* j͈̄
* j͈̋
* j͈̇
* j͈́
* j͈̏
* j͈̃
* j͈̀
* ǰ͈
* j͈̽
* j͈̊
* j͈̅
* j͈͊
* j͈͌
* j̹͋
* j̹̈
* j̹̆
* j̹͆
* j̹̄
* j̹̋
* j̹̇
* j̹́
* j̹̏
* j̹̃
* j̹̀
* ǰ̹
* j̹̽
* j̹̊
* j̹̅
* j̹͊
* j̹͌
* j̙͋
* j̙̈
* j̙̆
* j̙͆
* j̙̄
* j̙̋
* j̙̇
* j̙́
* j̙̏
* j̙̃
* j̙̀
* ǰ̙
* j̙̽
* j̙̊
* j̙̅
* j̙͊
* j̙͌
* j̠͋
* j̠̈
* j̠̆
* j̠͆
* j̠̄
* j̠̋
* j̠̇
* j̠́
* j̠̏
* j̠̃
* j̠̀
* ǰ̠
* j̠̽
* j̠̊
* j̠̅
* j̠͊
* j̠͌
* j̼͋
* j̼̈
* j̼̆
* j̼͆
* j̼̄
* j̼̋
* j̼̇
* j̼́
* j̼̏
* j̼̃
* j̼̀
* ǰ̼
* j̼̽
* j̼̊
* j̼̅
* j̼͊
* j̼͌
* j̻͋
* j̻̈
* j̻̆
* j̻͆
* j̻̄
* j̻̋
* j̻̇
* j̻́
* j̻̏
* j̻̃
* j̻̀
* ǰ̻
* j̻̽
* j̻̊
* j̻̅
* j̻͊
* j̻͌
* j͎͋
* j͎̈
* j͎̆
* j͎͆
* j͎̄
* j͎̋
* j͎̇
* j͎́
* j͎̏
* j͎̃
* j͎̀
* ǰ͎
* j͎̽
* j͎̊
* j͎̅
* j͎͊
* j͎͌
* j̩͋
* j̩̈
* j̩̆
* j̩͆
* j̩̄
* j̩̋
* j̩̇
* j̩́
* j̩̏
* j̩̃
* j̩̀
* ǰ̩
* j̩̽
* j̩̊
* j̩̅
* j̩͊
* j̩͌
* j̰͋
* j̰̈
* j̰̆
* j̰͆
* j̰̄
* j̰̋
* j̰̇
* j̰́
* j̰̏
* j̰̃
* j̰̀
* ǰ̰
* j̰̽
* j̰̊
* j̰̅
* j̰͊
* j̰͌
* j̟͋
* j̟̈
* j̟̆
* j̟͆
* j̟̄
* j̟̋
* j̟̇
* j̟́
* j̟̏
* j̟̃
* j̟̀
* ǰ̟
* j̟̽
* j̟̊
* j̟̅
* j̟͊
* j̟͌
* j̥͋
* j̥̈
* j̥̆
* j̥͆
* j̥̄
* j̥̋
* j̥̇
* j̥́
* j̥̏
* j̥̃
* j̥̀
* ǰ̥
* j̥̽
* j̥̊
* j̥̅
* j̥͊
* j̥͌
* j̬͋
* j̬̈
* j̬̆
* j̬͆
* j̬̄
* j̬̋
* j̬̇
* j̬́
* j̬̏
* j̬̃
* j̬̀
* ǰ̬
* j̬̽
* j̬̊
* j̬̅
* j̬͊
* j̬͌
* j̝͋
* j̝̈
* j̝̆
* j̝͆
* j̝̄
* j̝̋
* j̝̇
* j̝́
* j̝̏
* j̝̃
* j̝̀
* ǰ̝
* j̝̽
* j̝̊
* j̝̅
* j̝͊
* j̝͌
* j̲͋
* j̲̈
* j̲̆
* j̲͆
* j̲̄
* j̲̋
* j̲̇
* j̲́
* j̲̏
* j̲̃
* j̲̀
* ǰ̲
* j̲̽
* j̲̊
* j̲̅
* j̲͊
* j̲͌
* j͉͋
* j͉̈
* j͉̆
* j͉͆
* j͉̄
* j͉̋
* j͉̇
* j͉́
* j͉̏
* j͉̃
* j͉̀
* ǰ͉
* j͉̽
* j͉̊
* j͉̅
* j͉͊
* j͉͌
* j̨͋
* j̨̈
* j̨̆
* j̨͆
* j̨̄
* j̨̋
* j̨̇
* j̨́
* j̨̏
* j̨̃
* j̨̀
* ǰ̨
* j̨̽
* j̨̊
* j̨̅
* j̨͊
* j̨͌
* j̤͋
* j̤̈
* j̤̆
* j̤͆
* j̤̄
* j̤̋
* j̤̇
* j̤́
* j̤̏
* j̤̃
* j̤̀
* ǰ̤
* j̤̽
* j̤̊
* j̤̅
* j̤͊
* j̤͌
* j̴͋
* j̴̈
* j̴̆
* j̴͆
* j̴̄
* j̴̋
* j̴̇
* j̴́
* j̴̏
* j̴̃
* j̴̀
* ǰ̴
* j̴̽
* j̴̊
* j̴̅
* j̴͊
* j̴͌
* j͍͋
* j͍̈
* j͍̆
* j͍͆
* j͍̄
* j͍̋
* j͍̇
* j͍́
* j͍̏
* j͍̃
* j͍̀
* ǰ͍
* j͍̽
* j͍̊
* j͍̅
* j͍͊
* j͍͌
* j̦͋
* j̦̈
* j̦̆
* j̦͆
* j̦̄
* j̦̋
* j̦̇
* j̦́
* j̦̏
* j̦̃
* j̦̀
* ǰ̦
* j̦̽
* j̦̊
* j̦̅
* j̦͊
* j̦͌
* j͋
* j̆
* j͆
* j̋
* j̇
* j̏
* ǰ
* j̽
* j̊
* j̅
* j͊
* j͌ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlapping path segments:

* uni1D73 (U+1D73): Line(Line { p0: (156.0, 253.0), p1: (156.0, 199.0) }) has the same coordinates as a previous segment.
* uni1D75 (U+1D75): Line(Line { p0: (172.0, 258.0), p1: (172.0, 204.0) }) has the same coordinates as a previous segment.
* uni066E (U+066E): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni066E (U+066E): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni066E.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni066E.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628 (U+0628): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628 (U+0628): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0649.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A (U+062A): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A (U+062A): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B (U+062B): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B (U+062B): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633 (U+0633): Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633 (U+0633): Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.fina: Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633.fina: Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.medi: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.medi: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.init: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.init: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634 (U+0634): Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634 (U+0634): Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.fina: Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634.fina: Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.medi: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.medi: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.init: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.init: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0635 (U+0635): Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0635.fina: Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0636 (U+0636): Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0636.fina: Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0637 (U+0637): Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637 (U+0637): Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0637.fina: Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637.fina: Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0637.medi: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637.medi: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0637.init: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637.init: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638 (U+0638): Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638 (U+0638): Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638.fina: Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638.fina: Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638.medi: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638.medi: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638.init: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638.init: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0641 (U+0641): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0641 (U+0641): Line(Line { p0: (392.0, 0.0), p1: (392.0, 76.0) }) has the same coordinates as a previous segment.
* uni0641.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0641.fina: Line(Line { p0: (418.0, 0.0), p1: (418.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A4 (U+06A4): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A4 (U+06A4): Line(Line { p0: (392.0, 0.0), p1: (392.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A4.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A4.fina: Line(Line { p0: (418.0, 0.0), p1: (418.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A1 (U+06A1): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A1 (U+06A1): Line(Line { p0: (392.0, 0.0), p1: (392.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A1.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A1.fina: Line(Line { p0: (418.0, 0.0), p1: (418.0, 76.0) }) has the same coordinates as a previous segment.
* uni0643 (U+0643): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0643 (U+0643): Line(Line { p0: (506.0, 0.0), p1: (506.0, 76.0) }) has the same coordinates as a previous segment.
* uni0643 (U+0643): Line(Line { p0: (559.0, 606.0), p1: (699.0, 636.0) }) has the same coordinates as a previous segment.
* uni0643.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0644 (U+0644): Line(Line { p0: (427.0, 606.0), p1: (567.0, 636.0) }) has the same coordinates as a previous segment.
* uni0644.init: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0646.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni064A.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0626.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni06280649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0628064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06280626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062A0649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062A064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062A0626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062B0649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062B064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062B0626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330631.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330631.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330631.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330631.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330632.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330632.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330632.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330632.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330649.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330649.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633064A.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0633064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633064A.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0633064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330626.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330626.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340631.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340631.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340631.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340631.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340632.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340632.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340632.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340632.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340649.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340649.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634064A.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0634064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634064A.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0634064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340626.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340626.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350631.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350631.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350632.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350632.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0635064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0635064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0635064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0635064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360631.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360631.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360632.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360632.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0636064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0636064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0636064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0636064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni064406440647: Line(Line { p0: (721.0, 517.0), p1: (861.0, 547.0) }) has the same coordinates as a previous segment.
* uni06460649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0646064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06460626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06260649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0626064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06260626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni033C (U+033C): Line(Line { p0: (211.0, -160.0), p1: (182.0, -160.0) }) has the same coordinates as a previous segment. [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'MSTR' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[18] fonts/variable/AlYamamaSC[wght].ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. (base_has_width)</summary>
    <div>








- 🔥 **FAIL** The following glyphs had zero advance width:
* fraction (Some(8260)) [code: zero-width-bases]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. (case_mapping)</summary>
    <div>








- 🔥 **FAIL** The following glyphs are missing case-swapping counterparts:

| Glyph present in the font                        | Missing case-swapping counterpart                  |
|--------------------------------------------------|----------------------------------------------------|
| U+01AD: LATIN SMALL LETTER T WITH HOOK           | U+01AC: LATIN CAPITAL LETTER T WITH HOOK           |
| U+0254: LATIN SMALL LETTER OPEN O                | U+0186: LATIN CAPITAL LETTER OPEN O                |
| U+0188: LATIN SMALL LETTER C WITH HOOK           | U+0187: LATIN CAPITAL LETTER C WITH HOOK           |
| U+0264: LATIN SMALL LETTER RAMS HORN             | U+A7CB: LATIN CAPITAL LETTER RAMS HORN             |
| U+027D: LATIN SMALL LETTER R WITH TAIL           | U+2C64: LATIN CAPITAL LETTER R WITH TAIL           |
| U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL   | U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL   |
| U+0260: LATIN SMALL LETTER G WITH HOOK           | U+0193: LATIN CAPITAL LETTER G WITH HOOK           |
| U+0275: LATIN SMALL LETTER BARRED O              | U+019F: LATIN CAPITAL LETTER O WITH MIDDLE TILDE   |
| U+026A: LATIN LETTER SMALL CAPITAL I             | U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I       |
| U+025B: LATIN SMALL LETTER OPEN E                | U+0190: LATIN CAPITAL LETTER OPEN E                |
| U+0289: LATIN SMALL LETTER U BAR                 | U+0244: LATIN CAPITAL LETTER U BAR                 |
| U+0256: LATIN SMALL LETTER D WITH TAIL           | U+0189: LATIN CAPITAL LETTER AFRICAN D             |
| U+026F: LATIN SMALL LETTER TURNED M              | U+019C: LATIN CAPITAL LETTER TURNED M              |
| U+028B: LATIN SMALL LETTER V WITH HOOK           | U+01B2: LATIN CAPITAL LETTER V WITH HOOK           |
| U+0283: LATIN SMALL LETTER ESH                   | U+01A9: LATIN CAPITAL LETTER ESH                   |
| U+026C: LATIN SMALL LETTER L WITH BELT           | U+A7AD: LATIN CAPITAL LETTER L WITH BELT           |
| U+01A5: LATIN SMALL LETTER P WITH HOOK           | U+01A4: LATIN CAPITAL LETTER P WITH HOOK           |
| U+0257: LATIN SMALL LETTER D WITH HOOK           | U+018A: LATIN CAPITAL LETTER D WITH HOOK           |
| U+0280: LATIN LETTER SMALL CAPITAL R             | U+01A6: LATIN LETTER YR                            |
| U+0292: LATIN SMALL LETTER EZH                   | U+01B7: LATIN CAPITAL LETTER EZH                   |
| U+AB53: LATIN SMALL LETTER CHI                   | U+A7B3: LATIN CAPITAL LETTER CHI                   |
| U+0269: LATIN SMALL LETTER IOTA                  | U+0196: LATIN CAPITAL LETTER IOTA                  |
| U+0263: LATIN SMALL LETTER GAMMA                 | U+0194: LATIN CAPITAL LETTER GAMMA                 |
| U+A78B: LATIN CAPITAL LETTER SALTILLO            | U+A78C: LATIN SMALL LETTER SALTILLO                |
| U+0199: LATIN SMALL LETTER K WITH HOOK           | U+0198: LATIN CAPITAL LETTER K WITH HOOK           |
| U+0272: LATIN SMALL LETTER N WITH LEFT HOOK      | U+019D: LATIN CAPITAL LETTER N WITH LEFT HOOK      |
| U+028A: LATIN SMALL LETTER UPSILON               | U+01B1: LATIN CAPITAL LETTER UPSILON               |
| U+0288: LATIN SMALL LETTER T WITH RETROFLEX HOOK | U+01AE: LATIN CAPITAL LETTER T WITH RETROFLEX HOOK |
| U+0259: LATIN SMALL LETTER SCHWA                 | U+018F: LATIN CAPITAL LETTER SCHWA                 |
| U+0265: LATIN SMALL LETTER TURNED H              | U+A78D: LATIN CAPITAL LETTER TURNED H              |
| U+028C: LATIN SMALL LETTER TURNED V              | U+0245: LATIN CAPITAL LETTER TURNED V              |
| U+0266: LATIN SMALL LETTER H WITH HOOK           | U+A7AA: LATIN CAPITAL LETTER H WITH HOOK           |
| U+0253: LATIN SMALL LETTER B WITH HOOK           | U+0181: LATIN CAPITAL LETTER B WITH HOOK           |
| U+0268: LATIN SMALL LETTER I WITH STROKE         | U+0197: LATIN CAPITAL LETTER I WITH STROKE         | [code: missing-case-counterparts]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:
* waslaar [code: no-contour]
  
  


- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     infered from the typical ammounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni1EBC (U+1EBC): found 1, expected one of: {2, 3}
* uni1EF8 (U+1EF8): found 1, expected one of: {2, 3}
* T_T (unencoded): found 2, expected one of: {1}
* uni029B (U+029B): found 2, expected one of: {1}
* uni0255 (U+0255): found 1, expected one of: {2}
* uni0188 (U+0188): found 2, expected one of: {1}
* uni1D6D (U+1D6D): found 3, expected one of: {2}
* uni02A3 (U+02A3): found 2, expected one of: {3}
* uni02A5 (U+02A5): found 3, expected one of: {4}
* uni025D (U+025D): found 3, expected one of: {1}
* uni0258 (U+0258): found 1, expected one of: {2}
* uni0286 (U+0286): found 1, expected one of: {2}
* uni025A (U+025A): found 4, expected one of: {2}
* uni0293 (U+0293): found 1, expected one of: {2}
* uni1D6E (U+1D6E): found 2, expected one of: {1}
* uni02A1 (U+02A1): found 2, expected one of: {1}
* uni02A2 (U+02A2): found 2, expected one of: {1}
* uni029D (U+029D): found 2, expected one of: {3}
* uni0284 (U+0284): found 2, expected one of: {1}
* uni026E (U+026E): found 2, expected one of: {1}
* uni0264 (U+0264): found 1, expected one of: {2}
* uni1D73 (U+1D73): found 3, expected one of: {1}
* uni1D72 (U+1D72): found 2, expected one of: {1}
* uni0282 (U+0282): found 2, expected one of: {1}
* uni1D74 (U+1D74): found 3, expected one of: {1}
* uni1D75 (U+1D75): found 3, expected one of: {1}
* uni021B.1 (U+021B): found 1, expected one of: {3, 2, 4}
* uni0291 (U+0291): found 1, expected one of: {2}
* uni1D76 (U+1D76): found 3, expected one of: {1}
* uni0290 (U+0290): found 2, expected one of: {1}
* Ccedilla.sc (unencoded): found 2, expected one of: {1}
* K.sc (unencoded): found 2, expected one of: {1}
* Q.sc (unencoded): found 3, expected one of: {2}
* uni01C2 (U+01C2): found 3, expected one of: {1}
* uni0621 (U+0621): found 2, expected one of: {1}
* uni0623 (U+0623): found 3, expected one of: {2}
* uni0625 (U+0625): found 3, expected one of: {2}
* uni066E (U+066E): found 3, expected one of: {1}
* uni066E.fina (unencoded): found 3, expected one of: {1}
* uni066E.medi (unencoded): found 2, expected one of: {1}
* uni066E.init (unencoded): found 2, expected one of: {1}
* uni0628 (U+0628): found 4, expected one of: {2}
* uni062A (U+062A): found 5, expected one of: {2, 3}
* uni062B (U+062B): found 6, expected one of: {3, 2, 4}
* uni0631 (U+0631): found 2, expected one of: {1}
* uni0632 (U+0632): found 3, expected one of: {2}
* uni0633 (U+0633): found 6, expected one of: {3, 1}
* uni0634 (U+0634): found 9, expected one of: {4, 3, 6, 0}
* uni0635 (U+0635): found 6, expected one of: {2}
* uni0636 (U+0636): found 7, expected one of: {3}
* uni0637 (U+0637): found 4, expected one of: {2, 3}
* uni0638 (U+0638): found 5, expected one of: {3, 4}
* uni0639 (U+0639): found 2, expected one of: {1}
* uni0641 (U+0641): found 5, expected one of: {3, 2}
* uni06A4 (U+06A4): found 7, expected one of: {4, 5, 0}
* uni06A1 (U+06A1): found 4, expected one of: {1, 2}
* uni06A1.fina (unencoded): found 4, expected one of: {2}
* uni066F.fina (unencoded): found 3, expected one of: {2}
* uni0643 (U+0643): found 4, expected one of: {1, 2}
* uni0644 (U+0644): found 2, expected one of: {1}
* uni0645 (U+0645): found 3, expected one of: {2, 1}
* uni0646 (U+0646): found 3, expected one of: {2}
* uni06BA (U+06BA): found 2, expected one of: {1}
* uni0647 (U+0647): found 1, expected one of: {2}
* uni0624 (U+0624): found 4, expected one of: {2, 3}
* uni0649 (U+0649): found 2, expected one of: {1}
* uni064A (U+064A): found 4, expected one of: {2, 3}
* uni0626 (U+0626): found 4, expected one of: {2}
* uni0662 (U+0662): found 2, expected one of: {1}
* uni0663 (U+0663): found 3, expected one of: {1}
* uni0666 (U+0666): found 2, expected one of: {1}
* asterisk (U+002A): found 6, expected one of: {1, 3, 2, 5}
* uni02E5 (U+02E5): found 2, expected one of: {1}
* uni02E9 (U+02E9): found 2, expected one of: {1}
* uni02E6 (U+02E6): found 2, expected one of: {1}
* uni02E8 (U+02E8): found 2, expected one of: {1}
* uni02E7 (U+02E7): found 2, expected one of: {1}
* uni02DE (U+02DE): found 2, expected one of: {1}
* uni0654 (U+0654): found 2, expected one of: {1}
* uni0655 (U+0655): found 2, expected one of: {1}
* uni0654064C (unencoded): found 4, expected one of: {3}
* uni0654064E (unencoded): found 3, expected one of: {2}
* uni0654064B (unencoded): found 4, expected one of: {3}
* uni06540652 (unencoded): found 4, expected one of: {3}
* uni06550650 (unencoded): found 3, expected one of: {2}
* uni0655064D (unencoded): found 4, expected one of: {3}
* uni0651 (U+0651): found 2, expected one of: {1}
* uni0651064C (unencoded): found 4, expected one of: {2, 3}
* uni0651064D (unencoded): found 4, expected one of: {3}
* uni0651064E (unencoded): found 3, expected one of: {2}
* uni06510650 (unencoded): found 3, expected one of: {2}
* uni06510670 (unencoded): found 3, expected one of: {2}
* uni031A (U+031A): found 2, expected one of: {1}
* uni032A (U+032A): found 3, expected one of: {1}
* uni033A (U+033A): found 3, expected one of: {1}
* uni033B (U+033B): found 6, expected one of: {2}
* uni033C (U+033C): found 2, expected one of: {1}
* uni0346 (U+0346): found 3, expected one of: {1}
* uni0349 (U+0349): found 2, expected one of: {1}
* uni034A (U+034A): found 2, expected one of: {1} [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure small caps glyphs are available (missing_small_caps_glyphs)</summary>
    <div>








- 🔥 **FAIL** The following letters did not take part in smcp substitutions:
* uni0252
* uni027F
* uni1EF9
* uni029B
* uni0289
* uni0258
* uni03C2
* uni0286
* uni0237
* alphatonos
* nu
* upsilondieresis
* uni02AE
* uni02A8
* uni0268
* tau
* iotadieresistonos
* psi
* uni02AF
* uni0256
* uni02A9
* uni02AD
* uni0275
* uni0282
* uni021B.1
* uni1D73
* uni0287
* uni01A5
* uni00B5
* uni0254
* omicron
* uni02A3
* uni0257
* uni028C
* uni0296
* xi
* uni02AC
* uni025D
* uni0266
* uni0272
* omegatonos
* uni0199
* sigma
* uni02AB
* uni0269
* uni025F
* uni0285
* uni0298
* uni0295
* uni0277
* uni0276
* uni029D
* uni0291
* gamma
* uni0270
* uni02A2
* uni0274
* uni1D70
* uni0288
* delta
* uni0255
* uni026A
* uni1D72
* phi
* uni03D7
* uni1D71
* beta
* uni0188
* uni028D
* uni0271
* uni0299
* etatonos
* uni1D6E
* uni026D
* uni028F
* uni0292
* uni02A1
* uni029E
* uni0290
* uni1D6D
* uni0293
* iota
* chi
* uni0281
* uni025C
* uni0265
* omicrontonos
* uni0267
* uni02A6
* uni1D6C
* kappa
* uni0261
* pi
* uni029A
* uni02AA
* epsilon
* uni1D76
* iotadieresis
* omega
* upsilon
* uni025B
* uni02A5
* dotlessi
* alpha
* uniAB53
* iotatonos
* uni026C
* uni0253
* uni027B
* uni026E
* uni0251
* theta
* uni0284
* uni0297
* uni028E
* uni1D75
* uni01AD
* uni027C
* uni0250
* uni025A
* uni0278
* lambda
* uni02A7
* uni027D
* zeta
* uni025E
* uni0263
* florin
* uni0264
* uni0283
* uni0260
* uni0279
* uni026F
* upsilondieresistonos
* uni0262
* uni1EBD
* uni02A4
* uni028B
* uni029F
* uni027A
* uni03BC
* uni1D74
* uni0273
* uni029C
* upsilontonos
* uni0259
* eta
* epsilontonos
* uni026B
* rho
* uni1D6F
* uni028A
* uni02A0
* uni1E21
* uni027E
* uni0280 [code: missing-smcp-lowercase]
  
  


- 🔥 **FAIL** The following letters did not take part in c2sc substitutions:
* Etatonos
* Iotadieresis
* uni1EF8
* Chi
* Omicron
* Mu
* Nu
* Zeta
* Iotatonos
* Tau
* Phi
* Epsilontonos
* Upsilon
* Lambda
* Gamma
* Beta
* Omegatonos
* Eta
* uni0394
* Theta
* uni021A.1
* Kappa
* Xi
* Omicrontonos
* Psi
* Upsilontonos
* Sigma
* uni03CF
* uniA78B
* uni1EBC
* Rho
* Alphatonos
* Alpha
* Upsilondieresis
* uni1E20
* Epsilon
* Iota
* Pi
* uni03A9 [code: missing-c2sc-uppercase]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Space and non-breaking space have the same width? (whitespace_widths)</summary>
    <div>








- 🔥 **FAIL** The space glyph named space is 204 font units wide, non-breaking space named (uni00A0) is 252 font units wide, and both should be positive and the same. GlyphsApp has "Sidebearing arithmetic" (https://glyphsapp.com/tutorials/spacing) which allows you to set the non-breaking space width to always equal the space width. [code: different-widths]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- 🔥 **FAIL** Failed language shaping:

| Message                                                          | Languages         |
|------------------------------------------------------------------|-------------------|
| Mandatory orthography codepoints:                                | * nl_Latn (Dutch) |
|   Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́' |                   |
|   Shaper didn't attach acutecomb to j when shaping the text 'íj́' |                   | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                                                                                            | Languages                    |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Small caps for Latin letters:                                                                                                      | * ca_Latn (Catalan)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŀ' and shaping the text 'ŀ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * da_Latn (Danish)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǿ' and shaping the text 'ǿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * fr_Latn (French)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǔ' and shaping the text 'ǔ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sq_Latn (Albanian)         |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * it_Latn (Italian)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * el_Grek (Greek)            |
|   The following auxiliary characters are missing from the font: ἀ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἄ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἂ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἆ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἁ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἅ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἃ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἇ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ᾶ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἐ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἔ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἒ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἑ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἕ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἓ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἠ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἤ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἢ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἦ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἡ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἥ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἣ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἧ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῆ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἰ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἴ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἲ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἶ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἱ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἵ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἳ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ἷ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῖ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῗ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὄ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὂ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὃ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὐ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὔ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὒ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὖ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὑ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὕ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὓ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὗ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῦ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῧ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὤ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὢ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὦ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὥ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὣ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ὧ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ῶ                                                                  |                              |
| Small caps for Latin letters:                                                                                                      | * cy_Latn (Welsh)            |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẃ' and shaping the text 'ẃ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẁ' and shaping the text 'ẁ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŵ' and shaping the text 'ŵ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẅ' and shaping the text 'ẅ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ỳ' and shaping the text 'ỳ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŷ' and shaping the text 'ŷ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * nl_Latn (Dutch)            |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĳ' and shaping the text 'ĳ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * lt_Latn (Lithuanian)       |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ą' and shaping the text 'ą' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ę' and shaping the text 'ę' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ė' and shaping the text 'ė' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'į' and shaping the text 'į' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ų' and shaping the text 'ų' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ẽ' and shaping the text 'ẽ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĩ' and shaping the text 'ĩ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ũ' and shaping the text 'ũ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * de_Latn (German)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ğ' and shaping the text 'ğ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: ſ                                                                  | * fr_Latn (French)           |
| Small caps for Latin letters:                                                                                                      | * fi_Latn (Finnish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ą' and shaping the text 'ą' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ċ' and shaping the text 'ċ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ď' and shaping the text 'ď' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ð' and shaping the text 'ð' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ě' and shaping the text 'ě' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ė' and shaping the text 'ė' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ę' and shaping the text 'ę' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ğ' and shaping the text 'ğ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǧ' and shaping the text 'ǧ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ģ' and shaping the text 'ģ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ȟ' and shaping the text 'ȟ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ħ' and shaping the text 'ħ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'į' and shaping the text 'į' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǩ' and shaping the text 'ǩ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ķ' and shaping the text 'ķ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĺ' and shaping the text 'ĺ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ľ' and shaping the text 'ľ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ļ' and shaping the text 'ļ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ł' and shaping the text 'ł' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ń' and shaping the text 'ń' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ň' and shaping the text 'ň' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ņ' and shaping the text 'ņ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŋ' and shaping the text 'ŋ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ő' and shaping the text 'ő' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŕ' and shaping the text 'ŕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ś' and shaping the text 'ś' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŝ' and shaping the text 'ŝ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ș' and shaping the text 'ș' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ť' and shaping the text 'ť' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ţ' and shaping the text 'ţ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ț' and shaping the text 'ț' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŧ' and shaping the text 'ŧ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ů' and shaping the text 'ů' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ű' and shaping the text 'ű' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ų' and shaping the text 'ų' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ź' and shaping the text 'ź' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ż' and shaping the text 'ż' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ʒ' and shaping the text 'ʒ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǯ' and shaping the text 'ǯ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'þ' and shaping the text 'þ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * mt_Latn (Maltese)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ċ' and shaping the text 'ċ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ġ' and shaping the text 'ġ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ħ' and shaping the text 'ħ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ż' and shaping the text 'ż' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǥ                                                                  |                              |
|   The following auxiliary characters are missing from the font: Ʒ                                                                  |                              |
|   The following auxiliary characters are missing from the font: Ǯ                                                                  |                              |
|   The following auxiliary characters are missing from the font: ǥ                                                                  |                              |
| Small caps for Latin letters:                                                                                                      | * nb_Latn (Norwegian Bokmål) |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ǎ' and shaping the text 'ǎ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ń' and shaping the text 'ń' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŋ' and shaping the text 'ŋ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŧ' and shaping the text 'ŧ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * pl_Latn (Polish)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ą' and shaping the text 'ą' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ę' and shaping the text 'ę' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ł' and shaping the text 'ł' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ń' and shaping the text 'ń' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ś' and shaping the text 'ś' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ź' and shaping the text 'ź' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ż' and shaping the text 'ż' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Auxiliary orthography codepoints:                                                                                                  | * lt_Latn (Lithuanian)       |
|   Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'                                                              |                              |
|   Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'                                                              |                              |
|   Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'                                                              |                              |
|   Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'                                                              |                              |
|   Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'                                                           |                              |
|   Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'                                                           |                              |
|   Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'                                                           |                              |
|   Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'                                                           |                              |
|   Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'                                                           |                              |
|   Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'                                                           |                              |
|   Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'                                                           |                              |
|   Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'                                                           |                              |
|   Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'                                                              |                              |
|   Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'                                                                |                              |
|   Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'                                                              |                              |
|   Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'                                                              |                              |
|   Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'                                                                |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to J when shaping the text 'J̃'                                                                    |                              |
|   Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'                                                                      |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to L when shaping the text 'L̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to M when shaping the text 'M̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to R when shaping the text 'R̃'                                                                    |                              |
|   Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'                                                              |                              |
|   Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'                                                              |                              |
|   Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'                                                              |                              |
|   Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'                                                              |                              |
|   Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'                                                              |                              |
|   Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'                                                              |                              |
|   Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'                                                              |                              |
|   Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'                                                              |                              |
|   Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'                                                           |                              |
|   Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'                                                           |                              |
|   Shaper didn't attach uni0307 to i when shaping the text 'i̇́'                                                                      |                              |
|   Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'                                                              |                              |
|   Shaper didn't attach uni0307 to i when shaping the text 'i̇̀'                                                                      |                              |
|   Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'                                                              |                              |
|   Shaper didn't attach uni0307 to i when shaping the text 'i̇̃'                                                                      |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'                                                              |                              |
|   Shaper didn't attach acutecomb to iogonek when shaping the text 'į́'                                                              |                              |
|   Shaper didn't attach uni0307 to iogonek when shaping the text 'į̇́'                                                                |                              |
|   Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'                                                              |                              |
|   Shaper didn't attach tildecomb to iogonek when shaping the text 'į̃'                                                              |                              |
|   Shaper didn't attach uni0307 to iogonek when shaping the text 'į̇̃'                                                                |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to j when shaping the text 'j̃'                                                                    |                              |
|   Shaper didn't attach uni0307 to j when shaping the text 'j̇̃'                                                                      |                              |
|   Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'                                                              |                              |
|   Shaper didn't attach tildecomb to l when shaping the text 'l̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to m when shaping the text 'm̃'                                                                    |                              |
|   Shaper didn't attach tildecomb to r when shaping the text 'r̃'                                                                    |                              |
|   Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'                                                              |                              |
|   Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'                                                              |                              |
|   Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'                                                              |                              |
|   Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'                                                              |                              |
| Auxiliary orthography codepoints:                                                                                                  | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ                                                                  |                              |
| Small caps for Latin letters:                                                                                                      | * hu_Latn (Hungarian)        |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ő' and shaping the text 'ő' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ű' and shaping the text 'ű' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * is_Latn (Icelandic)        |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ð' and shaping the text 'ð' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'þ' and shaping the text 'þ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * hr_Latn (Croatian)         |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * es_Latn (Spanish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * lv_Latn (Latvian)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ģ' and shaping the text 'ģ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ķ' and shaping the text 'ķ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ļ' and shaping the text 'ļ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ņ' and shaping the text 'ņ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŗ' and shaping the text 'ŗ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * pt_Latn (Portuguese)       |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'õ' and shaping the text 'õ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * en_Latn (English)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * ro_Latn (Romanian)         |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ș' and shaping the text 'ș' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ț' and shaping the text 'ț' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ţ' and shaping the text 'ţ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sv_Latn (Swedish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * cs_Latn (Czech)            |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ď' and shaping the text 'ď' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ě' and shaping the text 'ě' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ň' and shaping the text 'ň' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ť' and shaping the text 'ť' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ů' and shaping the text 'ů' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ľ' and shaping the text 'ľ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ł' and shaping the text 'ł' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŕ' and shaping the text 'ŕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sk_Latn (Slovak)           |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ď' and shaping the text 'ď' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĺ' and shaping the text 'ĺ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ľ' and shaping the text 'ľ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ň' and shaping the text 'ň' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŕ' and shaping the text 'ŕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ť' and shaping the text 'ť' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ý' and shaping the text 'ý' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ő' and shaping the text 'ő' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ř' and shaping the text 'ř' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ű' and shaping the text 'ű' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * tr_Latn (Turkish)          |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ç' and shaping the text 'ç' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ğ' and shaping the text 'ğ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ı' and shaping the text 'ı' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ö' and shaping the text 'ö' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ş' and shaping the text 'ş' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ü' and shaping the text 'ü' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'á' and shaping the text 'á' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'à' and shaping the text 'à' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ă' and shaping the text 'ă' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'â' and shaping the text 'â' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ä' and shaping the text 'ä' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ã' and shaping the text 'ã' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ā' and shaping the text 'ā' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'æ' and shaping the text 'æ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'é' and shaping the text 'é' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'è' and shaping the text 'è' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĕ' and shaping the text 'ĕ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ê' and shaping the text 'ê' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ë' and shaping the text 'ë' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ē' and shaping the text 'ē' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'í' and shaping the text 'í' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ì' and shaping the text 'ì' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ĭ' and shaping the text 'ĭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'î' and shaping the text 'î' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ï' and shaping the text 'ï' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ī' and shaping the text 'ī' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ñ' and shaping the text 'ñ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ó' and shaping the text 'ó' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ò' and shaping the text 'ò' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŏ' and shaping the text 'ŏ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ô' and shaping the text 'ô' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ø' and shaping the text 'ø' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ō' and shaping the text 'ō' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'œ' and shaping the text 'œ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ß' and shaping the text 'ß' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ú' and shaping the text 'ú' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ù' and shaping the text 'ù' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ŭ' and shaping the text 'ŭ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'û' and shaping the text 'û' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ū' and shaping the text 'ū' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ÿ' and shaping the text 'ÿ' with features: smcp, the output is expected to be different, but was the same |                              |
| Small caps for Latin letters:                                                                                                      | * sr_Latn (Serbian (Latin))  |
|   When shaping the text 'a' and shaping the text 'a' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'b' and shaping the text 'b' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'c' and shaping the text 'c' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'č' and shaping the text 'č' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ć' and shaping the text 'ć' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'd' and shaping the text 'd' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'đ' and shaping the text 'đ' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'e' and shaping the text 'e' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'f' and shaping the text 'f' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'g' and shaping the text 'g' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'h' and shaping the text 'h' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'i' and shaping the text 'i' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'j' and shaping the text 'j' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'k' and shaping the text 'k' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'l' and shaping the text 'l' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'm' and shaping the text 'm' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'n' and shaping the text 'n' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'o' and shaping the text 'o' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'p' and shaping the text 'p' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'r' and shaping the text 'r' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 's' and shaping the text 's' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'š' and shaping the text 'š' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 't' and shaping the text 't' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'u' and shaping the text 'u' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'v' and shaping the text 'v' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'z' and shaping the text 'z' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'ž' and shaping the text 'ž' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'å' and shaping the text 'å' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'q' and shaping the text 'q' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'w' and shaping the text 'w' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'x' and shaping the text 'x' with features: smcp, the output is expected to be different, but was the same |                              |
|   When shaping the text 'y' and shaping the text 'y' with features: smcp, the output is expected to be different, but was the same |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/name/family_name_compliance)</summary>
    <div>








- 🔥 **FAIL** "AlYamama" is a CamelCased name. To solve this, simply use spaces instead in the font name. [code: camelcase]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check a font's STAT table contains compulsory Axis Values. (googlefonts/STAT/compulsory_axis_values)</summary>
    <div>








- 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

| Name      | Axis | Current Value | Expected Value | Current Flags | Expected Flags | Current Linked Value | Expected Linked Value |
|-----------|------|---------------|----------------|---------------|----------------|----------------------|-----------------------|
| Black     | wght | 900           | 900            | 0             | 0              | N/A                  | N/A                   |
| Bold      | wght | 700           | 700            | 0             | 0              | N/A                  | N/A                   |
| ExtraBold | wght | 800           | 800            | 0             | 0              | N/A                  | N/A                   |
| Light     | wght | 300           | 300            | 0             | 0              | N/A                  | N/A                   |
| Medium    | wght | N/A           | 500            | N/A           | 0              | N/A                  | N/A                   |
| Regular   | wght | 400           | 400            | 2             | 2              | 700                  | 700                   |
| SemiBold  | wght | 600           | 600            | 0             | 0              | N/A                  | N/A                   |

 [code: bad-axis-values]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? (ligature_carets)</summary>
    <div>








- ⚠️ **WARN** This font lacks caret positioning values for these ligature glyphs:
	- * f_b.sc
* f_f.sc
* fl.sc
* f_f_h.sc
* f_f_k.sc
* F_F_K
* f_f_b.sc
* F_K
* F_T
* F_F_L
* fi.sc
* f_f_l.sc
* f_h.sc
* f_f_t.sc
* F_F
* t_t.sc
* f_f_j.sc
* F_F_J
* F_I
* F_F_H
* F_F_I
* f_t.sc
* F_J
* T_T
* F_L
* f_k.sc
* f_j.sc
* f_f_i.sc
* F_F_T
* F_F_B
* F_H
* F_B

 [code: incomplete-caret-pos-data]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>








- ⚠️ **WARN** The most common width is 676 among a set of 13  math glyphs.
The following math glyphs have a different width, though:
width=667: equal
width=509: greater, logicalnot, greaterequal [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>








- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>








- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* uni0162.sc
* Zdotaccent.sc
* u.inferior
* v.inferior
* .null
* twodotsverticalabovear
* twodotsverticalbelowar
* threedotsdownabovear
* threedotsdownbelowar
* threedotsdowncenterar
* threedotsupbelowar
* waslaar
* miniKehehar
* gafsarkashabovear
* gafsarkashcenterar
* doublestrokear
* uni030C.alt.case
* uni0308.sc
* uni0307.sc
* gravecomb.sc
* acutecomb.sc
* uni030B.sc
* uni030C.alt.sc
* uni0302.sc
* uni030C.sc
* uni0306.sc
* uni030A.sc
* tildecomb.sc
* uni0304.sc
* uni0327.sc
* uni0328.sc
* Dotlessi.sc [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:
* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings: * i̊
* i̋
* ɨ̧̌
* ɨ̧́
* ɨ̧̂
* ɨ̧̀
* ɨ̈
* ɨ̄
* ɨ̌
* ɨ́
* ɨ̂
* ɨ̀
* ɨ̏
* ɨ̋
* ɨ̃
* j̈
* j̄
* j́
* j̀
* j̃
* į̄
* į̌
* į́
* į̂
* į̀
* į̃The dot of soft dotted characters _should_ disappear in other cases, for example: * ǐ͈
* i͈̅
* i͈͋
* i͈̊
* i͈̇
* i͈͊
* ȉ͈
* i͈͆
* i͈̋
* i͈͌
* i͈̽
* ǐ̴
* i̴̅
* i̴͋
* i̴̊
* i̴̇
* i̴͊
* ȉ̴
* i̴͆
* i̴̋
* i̴͌
* i̴̽
* ǐ̥
* i̥̅
* i̥͋
* i̥̊
* i̥̇
* i̥͊
* ȉ̥
* i̥͆
* i̥̋
* i̥͌
* i̥̽
* ǐ̪
* i̪̅
* i̪͋
* i̪̊
* i̪̇
* i̪͊
* ȉ̪
* i̪͆
* i̪̋
* i̪͌
* i̪̽
* ǐ̩
* i̩̅
* i̩͋
* i̩̊
* i̩̇
* i̩͊
* ȉ̩
* i̩͆
* i̩̋
* i̩͌
* i̩̽
* ǐ̼
* i̼̅
* i̼͋
* i̼̊
* i̼̇
* i̼͊
* ȉ̼
* i̼͆
* i̼̋
* i̼͌
* i̼̽
* ǐ̟
* i̟̅
* i̟͋
* i̟̊
* i̟̇
* i̟͊
* ȉ̟
* i̟͆
* i̟̋
* i̟͌
* i̟̽
* ǐ̬
* i̬̅
* i̬͋
* i̬̊
* i̬̇
* i̬͊
* ȉ̬
* i̬͆
* i̬̋
* i̬͌
* i̬̽
* ǐ̻
* i̻̅
* i̻͋
* i̻̊
* i̻̇
* i̻͊
* ȉ̻
* i̻͆
* i̻̋
* i̻͌
* i̻̽
* ǐ̠
* i̠̅
* i̠͋
* i̠̊
* i̠̇
* i̠͊
* ȉ̠
* i̠͆
* i̠̋
* i̠͌
* i̠̽
* ǐ̺
* i̺̅
* i̺͋
* i̺̊
* i̺̇
* i̺͊
* ȉ̺
* i̺͆
* i̺̋
* i̺͌
* i̺̽
* ǐ͍
* i͍̅
* i͍͋
* i͍̊
* i͍̇
* i͍͊
* ȉ͍
* i͍͆
* i͍̋
* i͍͌
* i͍̽
* ǐ̤
* i̤̅
* i̤͋
* i̤̊
* i̤̇
* i̤͊
* ȉ̤
* i̤͆
* i̤̋
* i̤͌
* i̤̽
* ǐ̲
* i̲̅
* i̲͋
* i̲̊
* i̲̇
* i̲͊
* ȉ̲
* i̲͆
* i̲̋
* i̲͌
* i̲̽
* ǐ̹
* i̹̅
* i̹͋
* i̹̊
* i̹̇
* i̹͊
* ȉ̹
* i̹͆
* i̹̋
* i̹͌
* i̹̽
* ǐ̘
* i̘̅
* i̘͋
* i̘̊
* i̘̇
* i̘͊
* ȉ̘
* i̘͆
* i̘̋
* i̘͌
* i̘̽
* ḭ̌
* ḭ̅
* ḭ͋
* ḭ̊
* ḭ̇
* ḭ͊
* ḭ̏
* ḭ͆
* ḭ̋
* ḭ͌
* ḭ̽
* ǐ̙
* i̙̅
* i̙͋
* i̙̊
* i̙̇
* i̙͊
* ȉ̙
* i̙͆
* i̙̋
* i̙͌
* i̙̽
* ǐ͇
* i͇̅
* i͇͋
* i͇̊
* i͇̇
* i͇͊
* ȉ͇
* i͇͆
* i͇̋
* i͇͌
* i͇̽
* ǐ̞
* i̞̅
* i̞͋
* i̞̊
* i̞̇
* i̞͊
* ȉ̞
* i̞͆
* i̞̋
* i̞͌
* i̞̽
* ǐ̝
* i̝̅
* i̝͋
* i̝̊
* i̝̇
* i̝͊
* ȉ̝
* i̝͆
* i̝̋
* i̝͌
* i̝̽
* ǐ̜
* i̜̅
* i̜͋
* i̜̊
* i̜̇
* i̜͊
* ȉ̜
* i̜͆
* i̜̋
* i̜͌
* i̜̽
* ǐ̧
* i̧̅
* i̧͋
* i̧̊
* i̧̇
* i̧͊
* ȉ̧
* i̧͆
* i̧̋
* i̧͌
* i̧̽
* ǐ̦
* i̦̅
* i̦͋
* i̦̊
* i̦̇
* i̦͊
* ȉ̦
* i̦͆
* i̦̋
* i̦͌
* i̦̽
* ǐ͉
* i͉̅
* i͉͋
* i͉̊
* i͉̇
* i͉͊
* ȉ͉
* i͉͆
* i͉̋
* i͉͌
* i͉̽
* ǐ͎
* i͎̅
* i͎͋
* i͎̊
* i͎̇
* i͎͊
* ȉ͎
* i͎͆
* i͎̋
* i͎͌
* i͎̽
* ǐ
* i̅
* i͋
* i̇
* i͊
* ȉ
* i͆
* i͌
* i̽
* ɨ͈̈
* ɨ͈̄
* ɨ͈̌
* ɨ͈̅
* ɨ͈́
* ɨ͈͋
* ɨ͈̊
* ɨ͈̇
* ɨ͈̂
* ɨ͈͊
* ɨ͈̀
* ɨ͈̏
* ɨ͈͆
* ɨ͈̆
* ɨ͈̋
* ɨ͈͌
* ɨ͈̃
* ɨ͈̽
* ɨ̴̈
* ɨ̴̄
* ɨ̴̌
* ɨ̴̅
* ɨ̴́
* ɨ̴͋
* ɨ̴̊
* ɨ̴̇
* ɨ̴̂
* ɨ̴͊
* ɨ̴̀
* ɨ̴̏
* ɨ̴͆
* ɨ̴̆
* ɨ̴̋
* ɨ̴͌
* ɨ̴̃
* ɨ̴̽
* ɨ̥̈
* ɨ̥̄
* ɨ̥̌
* ɨ̥̅
* ɨ̥́
* ɨ̥͋
* ɨ̥̊
* ɨ̥̇
* ɨ̥̂
* ɨ̥͊
* ɨ̥̀
* ɨ̥̏
* ɨ̥͆
* ɨ̥̆
* ɨ̥̋
* ɨ̥͌
* ɨ̥̃
* ɨ̥̽
* ɨ̪̈
* ɨ̪̄
* ɨ̪̌
* ɨ̪̅
* ɨ̪́
* ɨ̪͋
* ɨ̪̊
* ɨ̪̇
* ɨ̪̂
* ɨ̪͊
* ɨ̪̀
* ɨ̪̏
* ɨ̪͆
* ɨ̪̆
* ɨ̪̋
* ɨ̪͌
* ɨ̪̃
* ɨ̪̽
* ɨ̩̈
* ɨ̩̄
* ɨ̩̌
* ɨ̩̅
* ɨ̩́
* ɨ̩͋
* ɨ̩̊
* ɨ̩̇
* ɨ̩̂
* ɨ̩͊
* ɨ̩̀
* ɨ̩̏
* ɨ̩͆
* ɨ̩̆
* ɨ̩̋
* ɨ̩͌
* ɨ̩̃
* ɨ̩̽
* ɨ̼̈
* ɨ̼̄
* ɨ̼̌
* ɨ̼̅
* ɨ̼́
* ɨ̼͋
* ɨ̼̊
* ɨ̼̇
* ɨ̼̂
* ɨ̼͊
* ɨ̼̀
* ɨ̼̏
* ɨ̼͆
* ɨ̼̆
* ɨ̼̋
* ɨ̼͌
* ɨ̼̃
* ɨ̼̽
* ɨ̨̈
* ɨ̨̄
* ɨ̨̌
* ɨ̨̅
* ɨ̨́
* ɨ̨͋
* ɨ̨̊
* ɨ̨̇
* ɨ̨̂
* ɨ̨͊
* ɨ̨̀
* ɨ̨̏
* ɨ̨͆
* ɨ̨̆
* ɨ̨̋
* ɨ̨͌
* ɨ̨̃
* ɨ̨̽
* ɨ̟̈
* ɨ̟̄
* ɨ̟̌
* ɨ̟̅
* ɨ̟́
* ɨ̟͋
* ɨ̟̊
* ɨ̟̇
* ɨ̟̂
* ɨ̟͊
* ɨ̟̀
* ɨ̟̏
* ɨ̟͆
* ɨ̟̆
* ɨ̟̋
* ɨ̟͌
* ɨ̟̃
* ɨ̟̽
* ɨ̬̈
* ɨ̬̄
* ɨ̬̌
* ɨ̬̅
* ɨ̬́
* ɨ̬͋
* ɨ̬̊
* ɨ̬̇
* ɨ̬̂
* ɨ̬͊
* ɨ̬̀
* ɨ̬̏
* ɨ̬͆
* ɨ̬̆
* ɨ̬̋
* ɨ̬͌
* ɨ̬̃
* ɨ̬̽
* ɨ̻̈
* ɨ̻̄
* ɨ̻̌
* ɨ̻̅
* ɨ̻́
* ɨ̻͋
* ɨ̻̊
* ɨ̻̇
* ɨ̻̂
* ɨ̻͊
* ɨ̻̀
* ɨ̻̏
* ɨ̻͆
* ɨ̻̆
* ɨ̻̋
* ɨ̻͌
* ɨ̻̃
* ɨ̻̽
* ɨ̠̈
* ɨ̠̄
* ɨ̠̌
* ɨ̠̅
* ɨ̠́
* ɨ̠͋
* ɨ̠̊
* ɨ̠̇
* ɨ̠̂
* ɨ̠͊
* ɨ̠̀
* ɨ̠̏
* ɨ̠͆
* ɨ̠̆
* ɨ̠̋
* ɨ̠͌
* ɨ̠̃
* ɨ̠̽
* ɨ̺̈
* ɨ̺̄
* ɨ̺̌
* ɨ̺̅
* ɨ̺́
* ɨ̺͋
* ɨ̺̊
* ɨ̺̇
* ɨ̺̂
* ɨ̺͊
* ɨ̺̀
* ɨ̺̏
* ɨ̺͆
* ɨ̺̆
* ɨ̺̋
* ɨ̺͌
* ɨ̺̃
* ɨ̺̽
* ɨ͍̈
* ɨ͍̄
* ɨ͍̌
* ɨ͍̅
* ɨ͍́
* ɨ͍͋
* ɨ͍̊
* ɨ͍̇
* ɨ͍̂
* ɨ͍͊
* ɨ͍̀
* ɨ͍̏
* ɨ͍͆
* ɨ͍̆
* ɨ͍̋
* ɨ͍͌
* ɨ͍̃
* ɨ͍̽
* ɨ̤̈
* ɨ̤̄
* ɨ̤̌
* ɨ̤̅
* ɨ̤́
* ɨ̤͋
* ɨ̤̊
* ɨ̤̇
* ɨ̤̂
* ɨ̤͊
* ɨ̤̀
* ɨ̤̏
* ɨ̤͆
* ɨ̤̆
* ɨ̤̋
* ɨ̤͌
* ɨ̤̃
* ɨ̤̽
* ɨ̲̈
* ɨ̲̄
* ɨ̲̌
* ɨ̲̅
* ɨ̲́
* ɨ̲͋
* ɨ̲̊
* ɨ̲̇
* ɨ̲̂
* ɨ̲͊
* ɨ̲̀
* ɨ̲̏
* ɨ̲͆
* ɨ̲̆
* ɨ̲̋
* ɨ̲͌
* ɨ̲̃
* ɨ̲̽
* ɨ̹̈
* ɨ̹̄
* ɨ̹̌
* ɨ̹̅
* ɨ̹́
* ɨ̹͋
* ɨ̹̊
* ɨ̹̇
* ɨ̹̂
* ɨ̹͊
* ɨ̹̀
* ɨ̹̏
* ɨ̹͆
* ɨ̹̆
* ɨ̹̋
* ɨ̹͌
* ɨ̹̃
* ɨ̹̽
* ɨ̘̈
* ɨ̘̄
* ɨ̘̌
* ɨ̘̅
* ɨ̘́
* ɨ̘͋
* ɨ̘̊
* ɨ̘̇
* ɨ̘̂
* ɨ̘͊
* ɨ̘̀
* ɨ̘̏
* ɨ̘͆
* ɨ̘̆
* ɨ̘̋
* ɨ̘͌
* ɨ̘̃
* ɨ̘̽
* ɨ̰̈
* ɨ̰̄
* ɨ̰̌
* ɨ̰̅
* ɨ̰́
* ɨ̰͋
* ɨ̰̊
* ɨ̰̇
* ɨ̰̂
* ɨ̰͊
* ɨ̰̀
* ɨ̰̏
* ɨ̰͆
* ɨ̰̆
* ɨ̰̋
* ɨ̰͌
* ɨ̰̃
* ɨ̰̽
* ɨ̙̈
* ɨ̙̄
* ɨ̙̌
* ɨ̙̅
* ɨ̙́
* ɨ̙͋
* ɨ̙̊
* ɨ̙̇
* ɨ̙̂
* ɨ̙͊
* ɨ̙̀
* ɨ̙̏
* ɨ̙͆
* ɨ̙̆
* ɨ̙̋
* ɨ̙͌
* ɨ̙̃
* ɨ̙̽
* ɨ͇̈
* ɨ͇̄
* ɨ͇̌
* ɨ͇̅
* ɨ͇́
* ɨ͇͋
* ɨ͇̊
* ɨ͇̇
* ɨ͇̂
* ɨ͇͊
* ɨ͇̀
* ɨ͇̏
* ɨ͇͆
* ɨ͇̆
* ɨ͇̋
* ɨ͇͌
* ɨ͇̃
* ɨ͇̽
* ɨ̞̈
* ɨ̞̄
* ɨ̞̌
* ɨ̞̅
* ɨ̞́
* ɨ̞͋
* ɨ̞̊
* ɨ̞̇
* ɨ̞̂
* ɨ̞͊
* ɨ̞̀
* ɨ̞̏
* ɨ̞͆
* ɨ̞̆
* ɨ̞̋
* ɨ̞͌
* ɨ̞̃
* ɨ̞̽
* ɨ̝̈
* ɨ̝̄
* ɨ̝̌
* ɨ̝̅
* ɨ̝́
* ɨ̝͋
* ɨ̝̊
* ɨ̝̇
* ɨ̝̂
* ɨ̝͊
* ɨ̝̀
* ɨ̝̏
* ɨ̝͆
* ɨ̝̆
* ɨ̝̋
* ɨ̝͌
* ɨ̝̃
* ɨ̝̽
* ɨ̜̈
* ɨ̜̄
* ɨ̜̌
* ɨ̜̅
* ɨ̜́
* ɨ̜͋
* ɨ̜̊
* ɨ̜̇
* ɨ̜̂
* ɨ̜͊
* ɨ̜̀
* ɨ̜̏
* ɨ̜͆
* ɨ̜̆
* ɨ̜̋
* ɨ̜͌
* ɨ̜̃
* ɨ̜̽
* ɨ̧̈
* ɨ̧̄
* ɨ̧̅
* ɨ̧͋
* ɨ̧̊
* ɨ̧̇
* ɨ̧͊
* ɨ̧̏
* ɨ̧͆
* ɨ̧̆
* ɨ̧̋
* ɨ̧͌
* ɨ̧̃
* ɨ̧̽
* ɨ̦̈
* ɨ̦̄
* ɨ̦̌
* ɨ̦̅
* ɨ̦́
* ɨ̦͋
* ɨ̦̊
* ɨ̦̇
* ɨ̦̂
* ɨ̦͊
* ɨ̦̀
* ɨ̦̏
* ɨ̦͆
* ɨ̦̆
* ɨ̦̋
* ɨ̦͌
* ɨ̦̃
* ɨ̦̽
* ɨ͉̈
* ɨ͉̄
* ɨ͉̌
* ɨ͉̅
* ɨ͉́
* ɨ͉͋
* ɨ͉̊
* ɨ͉̇
* ɨ͉̂
* ɨ͉͊
* ɨ͉̀
* ɨ͉̏
* ɨ͉͆
* ɨ͉̆
* ɨ͉̋
* ɨ͉͌
* ɨ͉̃
* ɨ͉̽
* ɨ͎̈
* ɨ͎̄
* ɨ͎̌
* ɨ͎̅
* ɨ͎́
* ɨ͎͋
* ɨ͎̊
* ɨ͎̇
* ɨ͎̂
* ɨ͎͊
* ɨ͎̀
* ɨ͎̏
* ɨ͎͆
* ɨ͎̆
* ɨ͎̋
* ɨ͎͌
* ɨ͎̃
* ɨ͎̽
* ɨ̅
* ɨ͋
* ɨ̊
* ɨ̇
* ɨ͊
* ɨ͆
* ɨ̆
* ɨ͌
* ɨ̽
* ʝ͈̈
* ʝ͈̄
* ʝ͈̌
* ʝ͈̅
* ʝ͈́
* ʝ͈͋
* ʝ͈̊
* ʝ͈̇
* ʝ͈̂
* ʝ͈͊
* ʝ͈̀
* ʝ͈̏
* ʝ͈͆
* ʝ͈̆
* ʝ͈̋
* ʝ͈͌
* ʝ͈̃
* ʝ͈̽
* ʝ̴̈
* ʝ̴̄
* ʝ̴̌
* ʝ̴̅
* ʝ̴́
* ʝ̴͋
* ʝ̴̊
* ʝ̴̇
* ʝ̴̂
* ʝ̴͊
* ʝ̴̀
* ʝ̴̏
* ʝ̴͆
* ʝ̴̆
* ʝ̴̋
* ʝ̴͌
* ʝ̴̃
* ʝ̴̽
* ʝ̥̈
* ʝ̥̄
* ʝ̥̌
* ʝ̥̅
* ʝ̥́
* ʝ̥͋
* ʝ̥̊
* ʝ̥̇
* ʝ̥̂
* ʝ̥͊
* ʝ̥̀
* ʝ̥̏
* ʝ̥͆
* ʝ̥̆
* ʝ̥̋
* ʝ̥͌
* ʝ̥̃
* ʝ̥̽
* ʝ̪̈
* ʝ̪̄
* ʝ̪̌
* ʝ̪̅
* ʝ̪́
* ʝ̪͋
* ʝ̪̊
* ʝ̪̇
* ʝ̪̂
* ʝ̪͊
* ʝ̪̀
* ʝ̪̏
* ʝ̪͆
* ʝ̪̆
* ʝ̪̋
* ʝ̪͌
* ʝ̪̃
* ʝ̪̽
* ʝ̩̈
* ʝ̩̄
* ʝ̩̌
* ʝ̩̅
* ʝ̩́
* ʝ̩͋
* ʝ̩̊
* ʝ̩̇
* ʝ̩̂
* ʝ̩͊
* ʝ̩̀
* ʝ̩̏
* ʝ̩͆
* ʝ̩̆
* ʝ̩̋
* ʝ̩͌
* ʝ̩̃
* ʝ̩̽
* ʝ̼̈
* ʝ̼̄
* ʝ̼̌
* ʝ̼̅
* ʝ̼́
* ʝ̼͋
* ʝ̼̊
* ʝ̼̇
* ʝ̼̂
* ʝ̼͊
* ʝ̼̀
* ʝ̼̏
* ʝ̼͆
* ʝ̼̆
* ʝ̼̋
* ʝ̼͌
* ʝ̼̃
* ʝ̼̽
* ʝ̨̈
* ʝ̨̄
* ʝ̨̌
* ʝ̨̅
* ʝ̨́
* ʝ̨͋
* ʝ̨̊
* ʝ̨̇
* ʝ̨̂
* ʝ̨͊
* ʝ̨̀
* ʝ̨̏
* ʝ̨͆
* ʝ̨̆
* ʝ̨̋
* ʝ̨͌
* ʝ̨̃
* ʝ̨̽
* ʝ̟̈
* ʝ̟̄
* ʝ̟̌
* ʝ̟̅
* ʝ̟́
* ʝ̟͋
* ʝ̟̊
* ʝ̟̇
* ʝ̟̂
* ʝ̟͊
* ʝ̟̀
* ʝ̟̏
* ʝ̟͆
* ʝ̟̆
* ʝ̟̋
* ʝ̟͌
* ʝ̟̃
* ʝ̟̽
* ʝ̬̈
* ʝ̬̄
* ʝ̬̌
* ʝ̬̅
* ʝ̬́
* ʝ̬͋
* ʝ̬̊
* ʝ̬̇
* ʝ̬̂
* ʝ̬͊
* ʝ̬̀
* ʝ̬̏
* ʝ̬͆
* ʝ̬̆
* ʝ̬̋
* ʝ̬͌
* ʝ̬̃
* ʝ̬̽
* ʝ̻̈
* ʝ̻̄
* ʝ̻̌
* ʝ̻̅
* ʝ̻́
* ʝ̻͋
* ʝ̻̊
* ʝ̻̇
* ʝ̻̂
* ʝ̻͊
* ʝ̻̀
* ʝ̻̏
* ʝ̻͆
* ʝ̻̆
* ʝ̻̋
* ʝ̻͌
* ʝ̻̃
* ʝ̻̽
* ʝ̠̈
* ʝ̠̄
* ʝ̠̌
* ʝ̠̅
* ʝ̠́
* ʝ̠͋
* ʝ̠̊
* ʝ̠̇
* ʝ̠̂
* ʝ̠͊
* ʝ̠̀
* ʝ̠̏
* ʝ̠͆
* ʝ̠̆
* ʝ̠̋
* ʝ̠͌
* ʝ̠̃
* ʝ̠̽
* ʝ̺̈
* ʝ̺̄
* ʝ̺̌
* ʝ̺̅
* ʝ̺́
* ʝ̺͋
* ʝ̺̊
* ʝ̺̇
* ʝ̺̂
* ʝ̺͊
* ʝ̺̀
* ʝ̺̏
* ʝ̺͆
* ʝ̺̆
* ʝ̺̋
* ʝ̺͌
* ʝ̺̃
* ʝ̺̽
* ʝ͍̈
* ʝ͍̄
* ʝ͍̌
* ʝ͍̅
* ʝ͍́
* ʝ͍͋
* ʝ͍̊
* ʝ͍̇
* ʝ͍̂
* ʝ͍͊
* ʝ͍̀
* ʝ͍̏
* ʝ͍͆
* ʝ͍̆
* ʝ͍̋
* ʝ͍͌
* ʝ͍̃
* ʝ͍̽
* ʝ̤̈
* ʝ̤̄
* ʝ̤̌
* ʝ̤̅
* ʝ̤́
* ʝ̤͋
* ʝ̤̊
* ʝ̤̇
* ʝ̤̂
* ʝ̤͊
* ʝ̤̀
* ʝ̤̏
* ʝ̤͆
* ʝ̤̆
* ʝ̤̋
* ʝ̤͌
* ʝ̤̃
* ʝ̤̽
* ʝ̲̈
* ʝ̲̄
* ʝ̲̌
* ʝ̲̅
* ʝ̲́
* ʝ̲͋
* ʝ̲̊
* ʝ̲̇
* ʝ̲̂
* ʝ̲͊
* ʝ̲̀
* ʝ̲̏
* ʝ̲͆
* ʝ̲̆
* ʝ̲̋
* ʝ̲͌
* ʝ̲̃
* ʝ̲̽
* ʝ̹̈
* ʝ̹̄
* ʝ̹̌
* ʝ̹̅
* ʝ̹́
* ʝ̹͋
* ʝ̹̊
* ʝ̹̇
* ʝ̹̂
* ʝ̹͊
* ʝ̹̀
* ʝ̹̏
* ʝ̹͆
* ʝ̹̆
* ʝ̹̋
* ʝ̹͌
* ʝ̹̃
* ʝ̹̽
* ʝ̘̈
* ʝ̘̄
* ʝ̘̌
* ʝ̘̅
* ʝ̘́
* ʝ̘͋
* ʝ̘̊
* ʝ̘̇
* ʝ̘̂
* ʝ̘͊
* ʝ̘̀
* ʝ̘̏
* ʝ̘͆
* ʝ̘̆
* ʝ̘̋
* ʝ̘͌
* ʝ̘̃
* ʝ̘̽
* ʝ̰̈
* ʝ̰̄
* ʝ̰̌
* ʝ̰̅
* ʝ̰́
* ʝ̰͋
* ʝ̰̊
* ʝ̰̇
* ʝ̰̂
* ʝ̰͊
* ʝ̰̀
* ʝ̰̏
* ʝ̰͆
* ʝ̰̆
* ʝ̰̋
* ʝ̰͌
* ʝ̰̃
* ʝ̰̽
* ʝ̙̈
* ʝ̙̄
* ʝ̙̌
* ʝ̙̅
* ʝ̙́
* ʝ̙͋
* ʝ̙̊
* ʝ̙̇
* ʝ̙̂
* ʝ̙͊
* ʝ̙̀
* ʝ̙̏
* ʝ̙͆
* ʝ̙̆
* ʝ̙̋
* ʝ̙͌
* ʝ̙̃
* ʝ̙̽
* ʝ͇̈
* ʝ͇̄
* ʝ͇̌
* ʝ͇̅
* ʝ͇́
* ʝ͇͋
* ʝ͇̊
* ʝ͇̇
* ʝ͇̂
* ʝ͇͊
* ʝ͇̀
* ʝ͇̏
* ʝ͇͆
* ʝ͇̆
* ʝ͇̋
* ʝ͇͌
* ʝ͇̃
* ʝ͇̽
* ʝ̞̈
* ʝ̞̄
* ʝ̞̌
* ʝ̞̅
* ʝ̞́
* ʝ̞͋
* ʝ̞̊
* ʝ̞̇
* ʝ̞̂
* ʝ̞͊
* ʝ̞̀
* ʝ̞̏
* ʝ̞͆
* ʝ̞̆
* ʝ̞̋
* ʝ̞͌
* ʝ̞̃
* ʝ̞̽
* ʝ̝̈
* ʝ̝̄
* ʝ̝̌
* ʝ̝̅
* ʝ̝́
* ʝ̝͋
* ʝ̝̊
* ʝ̝̇
* ʝ̝̂
* ʝ̝͊
* ʝ̝̀
* ʝ̝̏
* ʝ̝͆
* ʝ̝̆
* ʝ̝̋
* ʝ̝͌
* ʝ̝̃
* ʝ̝̽
* ʝ̜̈
* ʝ̜̄
* ʝ̜̌
* ʝ̜̅
* ʝ̜́
* ʝ̜͋
* ʝ̜̊
* ʝ̜̇
* ʝ̜̂
* ʝ̜͊
* ʝ̜̀
* ʝ̜̏
* ʝ̜͆
* ʝ̜̆
* ʝ̜̋
* ʝ̜͌
* ʝ̜̃
* ʝ̜̽
* ʝ̧̈
* ʝ̧̄
* ʝ̧̌
* ʝ̧̅
* ʝ̧́
* ʝ̧͋
* ʝ̧̊
* ʝ̧̇
* ʝ̧̂
* ʝ̧͊
* ʝ̧̀
* ʝ̧̏
* ʝ̧͆
* ʝ̧̆
* ʝ̧̋
* ʝ̧͌
* ʝ̧̃
* ʝ̧̽
* ʝ̦̈
* ʝ̦̄
* ʝ̦̌
* ʝ̦̅
* ʝ̦́
* ʝ̦͋
* ʝ̦̊
* ʝ̦̇
* ʝ̦̂
* ʝ̦͊
* ʝ̦̀
* ʝ̦̏
* ʝ̦͆
* ʝ̦̆
* ʝ̦̋
* ʝ̦͌
* ʝ̦̃
* ʝ̦̽
* ʝ͉̈
* ʝ͉̄
* ʝ͉̌
* ʝ͉̅
* ʝ͉́
* ʝ͉͋
* ʝ͉̊
* ʝ͉̇
* ʝ͉̂
* ʝ͉͊
* ʝ͉̀
* ʝ͉̏
* ʝ͉͆
* ʝ͉̆
* ʝ͉̋
* ʝ͉͌
* ʝ͉̃
* ʝ͉̽
* ʝ͎̈
* ʝ͎̄
* ʝ͎̌
* ʝ͎̅
* ʝ͎́
* ʝ͎͋
* ʝ͎̊
* ʝ͎̇
* ʝ͎̂
* ʝ͎͊
* ʝ͎̀
* ʝ͎̏
* ʝ͎͆
* ʝ͎̆
* ʝ͎̋
* ʝ͎͌
* ʝ͎̃
* ʝ͎̽
* ʝ̈
* ʝ̄
* ʝ̌
* ʝ̅
* ʝ́
* ʝ͋
* ʝ̊
* ʝ̇
* ʝ̂
* ʝ͊
* ʝ̀
* ʝ̏
* ʝ͆
* ʝ̆
* ʝ̋
* ʝ͌
* ʝ̃
* ʝ̽
* j͈̈
* j͈̄
* ǰ͈
* j͈̅
* j͈́
* j͈͋
* j͈̊
* j͈̇
* j͈͊
* j͈̀
* j͈̏
* j͈͆
* j͈̆
* j͈̋
* j͈͌
* j͈̃
* j͈̽
* j̴̈
* j̴̄
* ǰ̴
* j̴̅
* j̴́
* j̴͋
* j̴̊
* j̴̇
* j̴͊
* j̴̀
* j̴̏
* j̴͆
* j̴̆
* j̴̋
* j̴͌
* j̴̃
* j̴̽
* j̥̈
* j̥̄
* ǰ̥
* j̥̅
* j̥́
* j̥͋
* j̥̊
* j̥̇
* j̥͊
* j̥̀
* j̥̏
* j̥͆
* j̥̆
* j̥̋
* j̥͌
* j̥̃
* j̥̽
* j̪̈
* j̪̄
* ǰ̪
* j̪̅
* j̪́
* j̪͋
* j̪̊
* j̪̇
* j̪͊
* j̪̀
* j̪̏
* j̪͆
* j̪̆
* j̪̋
* j̪͌
* j̪̃
* j̪̽
* j̩̈
* j̩̄
* ǰ̩
* j̩̅
* j̩́
* j̩͋
* j̩̊
* j̩̇
* j̩͊
* j̩̀
* j̩̏
* j̩͆
* j̩̆
* j̩̋
* j̩͌
* j̩̃
* j̩̽
* j̼̈
* j̼̄
* ǰ̼
* j̼̅
* j̼́
* j̼͋
* j̼̊
* j̼̇
* j̼͊
* j̼̀
* j̼̏
* j̼͆
* j̼̆
* j̼̋
* j̼͌
* j̼̃
* j̼̽
* j̨̈
* j̨̄
* ǰ̨
* j̨̅
* j̨́
* j̨͋
* j̨̊
* j̨̇
* j̨͊
* j̨̀
* j̨̏
* j̨͆
* j̨̆
* j̨̋
* j̨͌
* j̨̃
* j̨̽
* j̟̈
* j̟̄
* ǰ̟
* j̟̅
* j̟́
* j̟͋
* j̟̊
* j̟̇
* j̟͊
* j̟̀
* j̟̏
* j̟͆
* j̟̆
* j̟̋
* j̟͌
* j̟̃
* j̟̽
* j̬̈
* j̬̄
* ǰ̬
* j̬̅
* j̬́
* j̬͋
* j̬̊
* j̬̇
* j̬͊
* j̬̀
* j̬̏
* j̬͆
* j̬̆
* j̬̋
* j̬͌
* j̬̃
* j̬̽
* j̻̈
* j̻̄
* ǰ̻
* j̻̅
* j̻́
* j̻͋
* j̻̊
* j̻̇
* j̻͊
* j̻̀
* j̻̏
* j̻͆
* j̻̆
* j̻̋
* j̻͌
* j̻̃
* j̻̽
* j̠̈
* j̠̄
* ǰ̠
* j̠̅
* j̠́
* j̠͋
* j̠̊
* j̠̇
* j̠͊
* j̠̀
* j̠̏
* j̠͆
* j̠̆
* j̠̋
* j̠͌
* j̠̃
* j̠̽
* j̺̈
* j̺̄
* ǰ̺
* j̺̅
* j̺́
* j̺͋
* j̺̊
* j̺̇
* j̺͊
* j̺̀
* j̺̏
* j̺͆
* j̺̆
* j̺̋
* j̺͌
* j̺̃
* j̺̽
* j͍̈
* j͍̄
* ǰ͍
* j͍̅
* j͍́
* j͍͋
* j͍̊
* j͍̇
* j͍͊
* j͍̀
* j͍̏
* j͍͆
* j͍̆
* j͍̋
* j͍͌
* j͍̃
* j͍̽
* j̤̈
* j̤̄
* ǰ̤
* j̤̅
* j̤́
* j̤͋
* j̤̊
* j̤̇
* j̤͊
* j̤̀
* j̤̏
* j̤͆
* j̤̆
* j̤̋
* j̤͌
* j̤̃
* j̤̽
* j̲̈
* j̲̄
* ǰ̲
* j̲̅
* j̲́
* j̲͋
* j̲̊
* j̲̇
* j̲͊
* j̲̀
* j̲̏
* j̲͆
* j̲̆
* j̲̋
* j̲͌
* j̲̃
* j̲̽
* j̹̈
* j̹̄
* ǰ̹
* j̹̅
* j̹́
* j̹͋
* j̹̊
* j̹̇
* j̹͊
* j̹̀
* j̹̏
* j̹͆
* j̹̆
* j̹̋
* j̹͌
* j̹̃
* j̹̽
* j̘̈
* j̘̄
* ǰ̘
* j̘̅
* j̘́
* j̘͋
* j̘̊
* j̘̇
* j̘͊
* j̘̀
* j̘̏
* j̘͆
* j̘̆
* j̘̋
* j̘͌
* j̘̃
* j̘̽
* j̰̈
* j̰̄
* ǰ̰
* j̰̅
* j̰́
* j̰͋
* j̰̊
* j̰̇
* j̰͊
* j̰̀
* j̰̏
* j̰͆
* j̰̆
* j̰̋
* j̰͌
* j̰̃
* j̰̽
* j̙̈
* j̙̄
* ǰ̙
* j̙̅
* j̙́
* j̙͋
* j̙̊
* j̙̇
* j̙͊
* j̙̀
* j̙̏
* j̙͆
* j̙̆
* j̙̋
* j̙͌
* j̙̃
* j̙̽
* j͇̈
* j͇̄
* ǰ͇
* j͇̅
* j͇́
* j͇͋
* j͇̊
* j͇̇
* j͇͊
* j͇̀
* j͇̏
* j͇͆
* j͇̆
* j͇̋
* j͇͌
* j͇̃
* j͇̽
* j̞̈
* j̞̄
* ǰ̞
* j̞̅
* j̞́
* j̞͋
* j̞̊
* j̞̇
* j̞͊
* j̞̀
* j̞̏
* j̞͆
* j̞̆
* j̞̋
* j̞͌
* j̞̃
* j̞̽
* j̝̈
* j̝̄
* ǰ̝
* j̝̅
* j̝́
* j̝͋
* j̝̊
* j̝̇
* j̝͊
* j̝̀
* j̝̏
* j̝͆
* j̝̆
* j̝̋
* j̝͌
* j̝̃
* j̝̽
* j̜̈
* j̜̄
* ǰ̜
* j̜̅
* j̜́
* j̜͋
* j̜̊
* j̜̇
* j̜͊
* j̜̀
* j̜̏
* j̜͆
* j̜̆
* j̜̋
* j̜͌
* j̜̃
* j̜̽
* j̧̈
* j̧̄
* ǰ̧
* j̧̅
* j̧́
* j̧͋
* j̧̊
* j̧̇
* j̧͊
* j̧̀
* j̧̏
* j̧͆
* j̧̆
* j̧̋
* j̧͌
* j̧̃
* j̧̽
* j̦̈
* j̦̄
* ǰ̦
* j̦̅
* j̦́
* j̦͋
* j̦̊
* j̦̇
* j̦͊
* j̦̀
* j̦̏
* j̦͆
* j̦̆
* j̦̋
* j̦͌
* j̦̃
* j̦̽
* j͉̈
* j͉̄
* ǰ͉
* j͉̅
* j͉́
* j͉͋
* j͉̊
* j͉̇
* j͉͊
* j͉̀
* j͉̏
* j͉͆
* j͉̆
* j͉̋
* j͉͌
* j͉̃
* j͉̽
* j͎̈
* j͎̄
* ǰ͎
* j͎̅
* j͎́
* j͎͋
* j͎̊
* j͎̇
* j͎͊
* j͎̀
* j͎̏
* j͎͆
* j͎̆
* j͎̋
* j͎͌
* j͎̃
* j͎̽
* ǰ
* j̅
* j͋
* j̊
* j̇
* j͊
* j̏
* j͆
* j̆
* j̋
* j͌
* j̽
* ʲ͈̈
* ʲ͈̄
* ʲ͈̌
* ʲ͈̅
* ʲ͈́
* ʲ͈͋
* ʲ͈̊
* ʲ͈̇
* ʲ͈̂
* ʲ͈͊
* ʲ͈̀
* ʲ͈̏
* ʲ͈͆
* ʲ͈̆
* ʲ͈̋
* ʲ͈͌
* ʲ͈̃
* ʲ͈̽
* ʲ̴̈
* ʲ̴̄
* ʲ̴̌
* ʲ̴̅
* ʲ̴́
* ʲ̴͋
* ʲ̴̊
* ʲ̴̇
* ʲ̴̂
* ʲ̴͊
* ʲ̴̀
* ʲ̴̏
* ʲ̴͆
* ʲ̴̆
* ʲ̴̋
* ʲ̴͌
* ʲ̴̃
* ʲ̴̽
* ʲ̥̈
* ʲ̥̄
* ʲ̥̌
* ʲ̥̅
* ʲ̥́
* ʲ̥͋
* ʲ̥̊
* ʲ̥̇
* ʲ̥̂
* ʲ̥͊
* ʲ̥̀
* ʲ̥̏
* ʲ̥͆
* ʲ̥̆
* ʲ̥̋
* ʲ̥͌
* ʲ̥̃
* ʲ̥̽
* ʲ̪̈
* ʲ̪̄
* ʲ̪̌
* ʲ̪̅
* ʲ̪́
* ʲ̪͋
* ʲ̪̊
* ʲ̪̇
* ʲ̪̂
* ʲ̪͊
* ʲ̪̀
* ʲ̪̏
* ʲ̪͆
* ʲ̪̆
* ʲ̪̋
* ʲ̪͌
* ʲ̪̃
* ʲ̪̽
* ʲ̩̈
* ʲ̩̄
* ʲ̩̌
* ʲ̩̅
* ʲ̩́
* ʲ̩͋
* ʲ̩̊
* ʲ̩̇
* ʲ̩̂
* ʲ̩͊
* ʲ̩̀
* ʲ̩̏
* ʲ̩͆
* ʲ̩̆
* ʲ̩̋
* ʲ̩͌
* ʲ̩̃
* ʲ̩̽
* ʲ̼̈
* ʲ̼̄
* ʲ̼̌
* ʲ̼̅
* ʲ̼́
* ʲ̼͋
* ʲ̼̊
* ʲ̼̇
* ʲ̼̂
* ʲ̼͊
* ʲ̼̀
* ʲ̼̏
* ʲ̼͆
* ʲ̼̆
* ʲ̼̋
* ʲ̼͌
* ʲ̼̃
* ʲ̼̽
* ʲ̨̈
* ʲ̨̄
* ʲ̨̌
* ʲ̨̅
* ʲ̨́
* ʲ̨͋
* ʲ̨̊
* ʲ̨̇
* ʲ̨̂
* ʲ̨͊
* ʲ̨̀
* ʲ̨̏
* ʲ̨͆
* ʲ̨̆
* ʲ̨̋
* ʲ̨͌
* ʲ̨̃
* ʲ̨̽
* ʲ̟̈
* ʲ̟̄
* ʲ̟̌
* ʲ̟̅
* ʲ̟́
* ʲ̟͋
* ʲ̟̊
* ʲ̟̇
* ʲ̟̂
* ʲ̟͊
* ʲ̟̀
* ʲ̟̏
* ʲ̟͆
* ʲ̟̆
* ʲ̟̋
* ʲ̟͌
* ʲ̟̃
* ʲ̟̽
* ʲ̬̈
* ʲ̬̄
* ʲ̬̌
* ʲ̬̅
* ʲ̬́
* ʲ̬͋
* ʲ̬̊
* ʲ̬̇
* ʲ̬̂
* ʲ̬͊
* ʲ̬̀
* ʲ̬̏
* ʲ̬͆
* ʲ̬̆
* ʲ̬̋
* ʲ̬͌
* ʲ̬̃
* ʲ̬̽
* ʲ̻̈
* ʲ̻̄
* ʲ̻̌
* ʲ̻̅
* ʲ̻́
* ʲ̻͋
* ʲ̻̊
* ʲ̻̇
* ʲ̻̂
* ʲ̻͊
* ʲ̻̀
* ʲ̻̏
* ʲ̻͆
* ʲ̻̆
* ʲ̻̋
* ʲ̻͌
* ʲ̻̃
* ʲ̻̽
* ʲ̠̈
* ʲ̠̄
* ʲ̠̌
* ʲ̠̅
* ʲ̠́
* ʲ̠͋
* ʲ̠̊
* ʲ̠̇
* ʲ̠̂
* ʲ̠͊
* ʲ̠̀
* ʲ̠̏
* ʲ̠͆
* ʲ̠̆
* ʲ̠̋
* ʲ̠͌
* ʲ̠̃
* ʲ̠̽
* ʲ̺̈
* ʲ̺̄
* ʲ̺̌
* ʲ̺̅
* ʲ̺́
* ʲ̺͋
* ʲ̺̊
* ʲ̺̇
* ʲ̺̂
* ʲ̺͊
* ʲ̺̀
* ʲ̺̏
* ʲ̺͆
* ʲ̺̆
* ʲ̺̋
* ʲ̺͌
* ʲ̺̃
* ʲ̺̽
* ʲ͍̈
* ʲ͍̄
* ʲ͍̌
* ʲ͍̅
* ʲ͍́
* ʲ͍͋
* ʲ͍̊
* ʲ͍̇
* ʲ͍̂
* ʲ͍͊
* ʲ͍̀
* ʲ͍̏
* ʲ͍͆
* ʲ͍̆
* ʲ͍̋
* ʲ͍͌
* ʲ͍̃
* ʲ͍̽
* ʲ̤̈
* ʲ̤̄
* ʲ̤̌
* ʲ̤̅
* ʲ̤́
* ʲ̤͋
* ʲ̤̊
* ʲ̤̇
* ʲ̤̂
* ʲ̤͊
* ʲ̤̀
* ʲ̤̏
* ʲ̤͆
* ʲ̤̆
* ʲ̤̋
* ʲ̤͌
* ʲ̤̃
* ʲ̤̽
* ʲ̲̈
* ʲ̲̄
* ʲ̲̌
* ʲ̲̅
* ʲ̲́
* ʲ̲͋
* ʲ̲̊
* ʲ̲̇
* ʲ̲̂
* ʲ̲͊
* ʲ̲̀
* ʲ̲̏
* ʲ̲͆
* ʲ̲̆
* ʲ̲̋
* ʲ̲͌
* ʲ̲̃
* ʲ̲̽
* ʲ̹̈
* ʲ̹̄
* ʲ̹̌
* ʲ̹̅
* ʲ̹́
* ʲ̹͋
* ʲ̹̊
* ʲ̹̇
* ʲ̹̂
* ʲ̹͊
* ʲ̹̀
* ʲ̹̏
* ʲ̹͆
* ʲ̹̆
* ʲ̹̋
* ʲ̹͌
* ʲ̹̃
* ʲ̹̽
* ʲ̘̈
* ʲ̘̄
* ʲ̘̌
* ʲ̘̅
* ʲ̘́
* ʲ̘͋
* ʲ̘̊
* ʲ̘̇
* ʲ̘̂
* ʲ̘͊
* ʲ̘̀
* ʲ̘̏
* ʲ̘͆
* ʲ̘̆
* ʲ̘̋
* ʲ̘͌
* ʲ̘̃
* ʲ̘̽
* ʲ̰̈
* ʲ̰̄
* ʲ̰̌
* ʲ̰̅
* ʲ̰́
* ʲ̰͋
* ʲ̰̊
* ʲ̰̇
* ʲ̰̂
* ʲ̰͊
* ʲ̰̀
* ʲ̰̏
* ʲ̰͆
* ʲ̰̆
* ʲ̰̋
* ʲ̰͌
* ʲ̰̃
* ʲ̰̽
* ʲ̙̈
* ʲ̙̄
* ʲ̙̌
* ʲ̙̅
* ʲ̙́
* ʲ̙͋
* ʲ̙̊
* ʲ̙̇
* ʲ̙̂
* ʲ̙͊
* ʲ̙̀
* ʲ̙̏
* ʲ̙͆
* ʲ̙̆
* ʲ̙̋
* ʲ̙͌
* ʲ̙̃
* ʲ̙̽
* ʲ͇̈
* ʲ͇̄
* ʲ͇̌
* ʲ͇̅
* ʲ͇́
* ʲ͇͋
* ʲ͇̊
* ʲ͇̇
* ʲ͇̂
* ʲ͇͊
* ʲ͇̀
* ʲ͇̏
* ʲ͇͆
* ʲ͇̆
* ʲ͇̋
* ʲ͇͌
* ʲ͇̃
* ʲ͇̽
* ʲ̞̈
* ʲ̞̄
* ʲ̞̌
* ʲ̞̅
* ʲ̞́
* ʲ̞͋
* ʲ̞̊
* ʲ̞̇
* ʲ̞̂
* ʲ̞͊
* ʲ̞̀
* ʲ̞̏
* ʲ̞͆
* ʲ̞̆
* ʲ̞̋
* ʲ̞͌
* ʲ̞̃
* ʲ̞̽
* ʲ̝̈
* ʲ̝̄
* ʲ̝̌
* ʲ̝̅
* ʲ̝́
* ʲ̝͋
* ʲ̝̊
* ʲ̝̇
* ʲ̝̂
* ʲ̝͊
* ʲ̝̀
* ʲ̝̏
* ʲ̝͆
* ʲ̝̆
* ʲ̝̋
* ʲ̝͌
* ʲ̝̃
* ʲ̝̽
* ʲ̜̈
* ʲ̜̄
* ʲ̜̌
* ʲ̜̅
* ʲ̜́
* ʲ̜͋
* ʲ̜̊
* ʲ̜̇
* ʲ̜̂
* ʲ̜͊
* ʲ̜̀
* ʲ̜̏
* ʲ̜͆
* ʲ̜̆
* ʲ̜̋
* ʲ̜͌
* ʲ̜̃
* ʲ̜̽
* ʲ̧̈
* ʲ̧̄
* ʲ̧̌
* ʲ̧̅
* ʲ̧́
* ʲ̧͋
* ʲ̧̊
* ʲ̧̇
* ʲ̧̂
* ʲ̧͊
* ʲ̧̀
* ʲ̧̏
* ʲ̧͆
* ʲ̧̆
* ʲ̧̋
* ʲ̧͌
* ʲ̧̃
* ʲ̧̽
* ʲ̦̈
* ʲ̦̄
* ʲ̦̌
* ʲ̦̅
* ʲ̦́
* ʲ̦͋
* ʲ̦̊
* ʲ̦̇
* ʲ̦̂
* ʲ̦͊
* ʲ̦̀
* ʲ̦̏
* ʲ̦͆
* ʲ̦̆
* ʲ̦̋
* ʲ̦͌
* ʲ̦̃
* ʲ̦̽
* ʲ͉̈
* ʲ͉̄
* ʲ͉̌
* ʲ͉̅
* ʲ͉́
* ʲ͉͋
* ʲ͉̊
* ʲ͉̇
* ʲ͉̂
* ʲ͉͊
* ʲ͉̀
* ʲ͉̏
* ʲ͉͆
* ʲ͉̆
* ʲ͉̋
* ʲ͉͌
* ʲ͉̃
* ʲ͉̽
* ʲ͎̈
* ʲ͎̄
* ʲ͎̌
* ʲ͎̅
* ʲ͎́
* ʲ͎͋
* ʲ͎̊
* ʲ͎̇
* ʲ͎̂
* ʲ͎͊
* ʲ͎̀
* ʲ͎̏
* ʲ͎͆
* ʲ͎̆
* ʲ͎̋
* ʲ͎͌
* ʲ͎̃
* ʲ͎̽
* ʲ̈
* ʲ̄
* ʲ̌
* ʲ̅
* ʲ́
* ʲ͋
* ʲ̊
* ʲ̇
* ʲ̂
* ʲ͊
* ʲ̀
* ʲ̏
* ʲ͆
* ʲ̆
* ʲ̋
* ʲ͌
* ʲ̃
* ʲ̽
* ⁱ͈̈
* ⁱ͈̄
* ⁱ͈̌
* ⁱ͈̅
* ⁱ͈́
* ⁱ͈͋
* ⁱ͈̊
* ⁱ͈̇
* ⁱ͈̂
* ⁱ͈͊
* ⁱ͈̀
* ⁱ͈̏
* ⁱ͈͆
* ⁱ͈̆
* ⁱ͈̋
* ⁱ͈͌
* ⁱ͈̃
* ⁱ͈̽
* ⁱ̴̈
* ⁱ̴̄
* ⁱ̴̌
* ⁱ̴̅
* ⁱ̴́
* ⁱ̴͋
* ⁱ̴̊
* ⁱ̴̇
* ⁱ̴̂
* ⁱ̴͊
* ⁱ̴̀
* ⁱ̴̏
* ⁱ̴͆
* ⁱ̴̆
* ⁱ̴̋
* ⁱ̴͌
* ⁱ̴̃
* ⁱ̴̽
* ⁱ̥̈
* ⁱ̥̄
* ⁱ̥̌
* ⁱ̥̅
* ⁱ̥́
* ⁱ̥͋
* ⁱ̥̊
* ⁱ̥̇
* ⁱ̥̂
* ⁱ̥͊
* ⁱ̥̀
* ⁱ̥̏
* ⁱ̥͆
* ⁱ̥̆
* ⁱ̥̋
* ⁱ̥͌
* ⁱ̥̃
* ⁱ̥̽
* ⁱ̪̈
* ⁱ̪̄
* ⁱ̪̌
* ⁱ̪̅
* ⁱ̪́
* ⁱ̪͋
* ⁱ̪̊
* ⁱ̪̇
* ⁱ̪̂
* ⁱ̪͊
* ⁱ̪̀
* ⁱ̪̏
* ⁱ̪͆
* ⁱ̪̆
* ⁱ̪̋
* ⁱ̪͌
* ⁱ̪̃
* ⁱ̪̽
* ⁱ̩̈
* ⁱ̩̄
* ⁱ̩̌
* ⁱ̩̅
* ⁱ̩́
* ⁱ̩͋
* ⁱ̩̊
* ⁱ̩̇
* ⁱ̩̂
* ⁱ̩͊
* ⁱ̩̀
* ⁱ̩̏
* ⁱ̩͆
* ⁱ̩̆
* ⁱ̩̋
* ⁱ̩͌
* ⁱ̩̃
* ⁱ̩̽
* ⁱ̼̈
* ⁱ̼̄
* ⁱ̼̌
* ⁱ̼̅
* ⁱ̼́
* ⁱ̼͋
* ⁱ̼̊
* ⁱ̼̇
* ⁱ̼̂
* ⁱ̼͊
* ⁱ̼̀
* ⁱ̼̏
* ⁱ̼͆
* ⁱ̼̆
* ⁱ̼̋
* ⁱ̼͌
* ⁱ̼̃
* ⁱ̼̽
* ⁱ̨̈
* ⁱ̨̄
* ⁱ̨̌
* ⁱ̨̅
* ⁱ̨́
* ⁱ̨͋
* ⁱ̨̊
* ⁱ̨̇
* ⁱ̨̂
* ⁱ̨͊
* ⁱ̨̀
* ⁱ̨̏
* ⁱ̨͆
* ⁱ̨̆
* ⁱ̨̋
* ⁱ̨͌
* ⁱ̨̃
* ⁱ̨̽
* ⁱ̟̈
* ⁱ̟̄
* ⁱ̟̌
* ⁱ̟̅
* ⁱ̟́
* ⁱ̟͋
* ⁱ̟̊
* ⁱ̟̇
* ⁱ̟̂
* ⁱ̟͊
* ⁱ̟̀
* ⁱ̟̏
* ⁱ̟͆
* ⁱ̟̆
* ⁱ̟̋
* ⁱ̟͌
* ⁱ̟̃
* ⁱ̟̽
* ⁱ̬̈
* ⁱ̬̄
* ⁱ̬̌
* ⁱ̬̅
* ⁱ̬́
* ⁱ̬͋
* ⁱ̬̊
* ⁱ̬̇
* ⁱ̬̂
* ⁱ̬͊
* ⁱ̬̀
* ⁱ̬̏
* ⁱ̬͆
* ⁱ̬̆
* ⁱ̬̋
* ⁱ̬͌
* ⁱ̬̃
* ⁱ̬̽
* ⁱ̻̈
* ⁱ̻̄
* ⁱ̻̌
* ⁱ̻̅
* ⁱ̻́
* ⁱ̻͋
* ⁱ̻̊
* ⁱ̻̇
* ⁱ̻̂
* ⁱ̻͊
* ⁱ̻̀
* ⁱ̻̏
* ⁱ̻͆
* ⁱ̻̆
* ⁱ̻̋
* ⁱ̻͌
* ⁱ̻̃
* ⁱ̻̽
* ⁱ̠̈
* ⁱ̠̄
* ⁱ̠̌
* ⁱ̠̅
* ⁱ̠́
* ⁱ̠͋
* ⁱ̠̊
* ⁱ̠̇
* ⁱ̠̂
* ⁱ̠͊
* ⁱ̠̀
* ⁱ̠̏
* ⁱ̠͆
* ⁱ̠̆
* ⁱ̠̋
* ⁱ̠͌
* ⁱ̠̃
* ⁱ̠̽
* ⁱ̺̈
* ⁱ̺̄
* ⁱ̺̌
* ⁱ̺̅
* ⁱ̺́
* ⁱ̺͋
* ⁱ̺̊
* ⁱ̺̇
* ⁱ̺̂
* ⁱ̺͊
* ⁱ̺̀
* ⁱ̺̏
* ⁱ̺͆
* ⁱ̺̆
* ⁱ̺̋
* ⁱ̺͌
* ⁱ̺̃
* ⁱ̺̽
* ⁱ͍̈
* ⁱ͍̄
* ⁱ͍̌
* ⁱ͍̅
* ⁱ͍́
* ⁱ͍͋
* ⁱ͍̊
* ⁱ͍̇
* ⁱ͍̂
* ⁱ͍͊
* ⁱ͍̀
* ⁱ͍̏
* ⁱ͍͆
* ⁱ͍̆
* ⁱ͍̋
* ⁱ͍͌
* ⁱ͍̃
* ⁱ͍̽
* ⁱ̤̈
* ⁱ̤̄
* ⁱ̤̌
* ⁱ̤̅
* ⁱ̤́
* ⁱ̤͋
* ⁱ̤̊
* ⁱ̤̇
* ⁱ̤̂
* ⁱ̤͊
* ⁱ̤̀
* ⁱ̤̏
* ⁱ̤͆
* ⁱ̤̆
* ⁱ̤̋
* ⁱ̤͌
* ⁱ̤̃
* ⁱ̤̽
* ⁱ̲̈
* ⁱ̲̄
* ⁱ̲̌
* ⁱ̲̅
* ⁱ̲́
* ⁱ̲͋
* ⁱ̲̊
* ⁱ̲̇
* ⁱ̲̂
* ⁱ̲͊
* ⁱ̲̀
* ⁱ̲̏
* ⁱ̲͆
* ⁱ̲̆
* ⁱ̲̋
* ⁱ̲͌
* ⁱ̲̃
* ⁱ̲̽
* ⁱ̹̈
* ⁱ̹̄
* ⁱ̹̌
* ⁱ̹̅
* ⁱ̹́
* ⁱ̹͋
* ⁱ̹̊
* ⁱ̹̇
* ⁱ̹̂
* ⁱ̹͊
* ⁱ̹̀
* ⁱ̹̏
* ⁱ̹͆
* ⁱ̹̆
* ⁱ̹̋
* ⁱ̹͌
* ⁱ̹̃
* ⁱ̹̽
* ⁱ̘̈
* ⁱ̘̄
* ⁱ̘̌
* ⁱ̘̅
* ⁱ̘́
* ⁱ̘͋
* ⁱ̘̊
* ⁱ̘̇
* ⁱ̘̂
* ⁱ̘͊
* ⁱ̘̀
* ⁱ̘̏
* ⁱ̘͆
* ⁱ̘̆
* ⁱ̘̋
* ⁱ̘͌
* ⁱ̘̃
* ⁱ̘̽
* ⁱ̰̈
* ⁱ̰̄
* ⁱ̰̌
* ⁱ̰̅
* ⁱ̰́
* ⁱ̰͋
* ⁱ̰̊
* ⁱ̰̇
* ⁱ̰̂
* ⁱ̰͊
* ⁱ̰̀
* ⁱ̰̏
* ⁱ̰͆
* ⁱ̰̆
* ⁱ̰̋
* ⁱ̰͌
* ⁱ̰̃
* ⁱ̰̽
* ⁱ̙̈
* ⁱ̙̄
* ⁱ̙̌
* ⁱ̙̅
* ⁱ̙́
* ⁱ̙͋
* ⁱ̙̊
* ⁱ̙̇
* ⁱ̙̂
* ⁱ̙͊
* ⁱ̙̀
* ⁱ̙̏
* ⁱ̙͆
* ⁱ̙̆
* ⁱ̙̋
* ⁱ̙͌
* ⁱ̙̃
* ⁱ̙̽
* ⁱ͇̈
* ⁱ͇̄
* ⁱ͇̌
* ⁱ͇̅
* ⁱ͇́
* ⁱ͇͋
* ⁱ͇̊
* ⁱ͇̇
* ⁱ͇̂
* ⁱ͇͊
* ⁱ͇̀
* ⁱ͇̏
* ⁱ͇͆
* ⁱ͇̆
* ⁱ͇̋
* ⁱ͇͌
* ⁱ͇̃
* ⁱ͇̽
* ⁱ̞̈
* ⁱ̞̄
* ⁱ̞̌
* ⁱ̞̅
* ⁱ̞́
* ⁱ̞͋
* ⁱ̞̊
* ⁱ̞̇
* ⁱ̞̂
* ⁱ̞͊
* ⁱ̞̀
* ⁱ̞̏
* ⁱ̞͆
* ⁱ̞̆
* ⁱ̞̋
* ⁱ̞͌
* ⁱ̞̃
* ⁱ̞̽
* ⁱ̝̈
* ⁱ̝̄
* ⁱ̝̌
* ⁱ̝̅
* ⁱ̝́
* ⁱ̝͋
* ⁱ̝̊
* ⁱ̝̇
* ⁱ̝̂
* ⁱ̝͊
* ⁱ̝̀
* ⁱ̝̏
* ⁱ̝͆
* ⁱ̝̆
* ⁱ̝̋
* ⁱ̝͌
* ⁱ̝̃
* ⁱ̝̽
* ⁱ̜̈
* ⁱ̜̄
* ⁱ̜̌
* ⁱ̜̅
* ⁱ̜́
* ⁱ̜͋
* ⁱ̜̊
* ⁱ̜̇
* ⁱ̜̂
* ⁱ̜͊
* ⁱ̜̀
* ⁱ̜̏
* ⁱ̜͆
* ⁱ̜̆
* ⁱ̜̋
* ⁱ̜͌
* ⁱ̜̃
* ⁱ̜̽
* ⁱ̧̈
* ⁱ̧̄
* ⁱ̧̌
* ⁱ̧̅
* ⁱ̧́
* ⁱ̧͋
* ⁱ̧̊
* ⁱ̧̇
* ⁱ̧̂
* ⁱ̧͊
* ⁱ̧̀
* ⁱ̧̏
* ⁱ̧͆
* ⁱ̧̆
* ⁱ̧̋
* ⁱ̧͌
* ⁱ̧̃
* ⁱ̧̽
* ⁱ̦̈
* ⁱ̦̄
* ⁱ̦̌
* ⁱ̦̅
* ⁱ̦́
* ⁱ̦͋
* ⁱ̦̊
* ⁱ̦̇
* ⁱ̦̂
* ⁱ̦͊
* ⁱ̦̀
* ⁱ̦̏
* ⁱ̦͆
* ⁱ̦̆
* ⁱ̦̋
* ⁱ̦͌
* ⁱ̦̃
* ⁱ̦̽
* ⁱ͉̈
* ⁱ͉̄
* ⁱ͉̌
* ⁱ͉̅
* ⁱ͉́
* ⁱ͉͋
* ⁱ͉̊
* ⁱ͉̇
* ⁱ͉̂
* ⁱ͉͊
* ⁱ͉̀
* ⁱ͉̏
* ⁱ͉͆
* ⁱ͉̆
* ⁱ͉̋
* ⁱ͉͌
* ⁱ͉̃
* ⁱ͉̽
* ⁱ͎̈
* ⁱ͎̄
* ⁱ͎̌
* ⁱ͎̅
* ⁱ͎́
* ⁱ͎͋
* ⁱ͎̊
* ⁱ͎̇
* ⁱ͎̂
* ⁱ͎͊
* ⁱ͎̀
* ⁱ͎̏
* ⁱ͎͆
* ⁱ͎̆
* ⁱ͎̋
* ⁱ͎͌
* ⁱ͎̃
* ⁱ͎̽
* ⁱ̈
* ⁱ̄
* ⁱ̌
* ⁱ̅
* ⁱ́
* ⁱ͋
* ⁱ̊
* ⁱ̇
* ⁱ̂
* ⁱ͊
* ⁱ̀
* ⁱ̏
* ⁱ͆
* ⁱ̆
* ⁱ̋
* ⁱ͌
* ⁱ̃
* ⁱ̽
* į͈̈
* į͈̄
* į͈̌
* į͈̅
* į͈́
* į͈͋
* į͈̊
* į͈̇
* į͈̂
* į͈͊
* į͈̀
* į͈̏
* į͈͆
* į͈̆
* į͈̋
* į͈͌
* į͈̃
* į͈̽
* į̴̈
* į̴̄
* į̴̌
* į̴̅
* į̴́
* į̴͋
* į̴̊
* į̴̇
* į̴̂
* į̴͊
* į̴̀
* į̴̏
* į̴͆
* į̴̆
* į̴̋
* į̴͌
* į̴̃
* į̴̽
* į̥̈
* į̥̄
* į̥̌
* į̥̅
* į̥́
* į̥͋
* į̥̊
* į̥̇
* į̥̂
* į̥͊
* į̥̀
* į̥̏
* į̥͆
* į̥̆
* į̥̋
* į̥͌
* į̥̃
* į̥̽
* į̪̈
* į̪̄
* į̪̌
* į̪̅
* į̪́
* į̪͋
* į̪̊
* į̪̇
* į̪̂
* į̪͊
* į̪̀
* į̪̏
* į̪͆
* į̪̆
* į̪̋
* į̪͌
* į̪̃
* į̪̽
* į̩̈
* į̩̄
* į̩̌
* į̩̅
* į̩́
* į̩͋
* į̩̊
* į̩̇
* į̩̂
* į̩͊
* į̩̀
* į̩̏
* į̩͆
* į̩̆
* į̩̋
* į̩͌
* į̩̃
* į̩̽
* į̼̈
* į̼̄
* į̼̌
* į̼̅
* į̼́
* į̼͋
* į̼̊
* į̼̇
* į̼̂
* į̼͊
* į̼̀
* į̼̏
* į̼͆
* į̼̆
* į̼̋
* į̼͌
* į̼̃
* į̼̽
* į̨̈
* į̨̄
* į̨̌
* į̨̅
* į̨́
* į̨͋
* į̨̊
* į̨̇
* į̨̂
* į̨͊
* į̨̀
* į̨̏
* į̨͆
* į̨̆
* į̨̋
* į̨͌
* į̨̃
* į̨̽
* į̟̈
* į̟̄
* į̟̌
* į̟̅
* į̟́
* į̟͋
* į̟̊
* į̟̇
* į̟̂
* į̟͊
* į̟̀
* į̟̏
* į̟͆
* į̟̆
* į̟̋
* į̟͌
* į̟̃
* į̟̽
* į̬̈
* į̬̄
* į̬̌
* į̬̅
* į̬́
* į̬͋
* į̬̊
* į̬̇
* į̬̂
* į̬͊
* į̬̀
* į̬̏
* į̬͆
* į̬̆
* į̬̋
* į̬͌
* į̬̃
* į̬̽
* į̻̈
* į̻̄
* į̻̌
* į̻̅
* į̻́
* į̻͋
* į̻̊
* į̻̇
* į̻̂
* į̻͊
* į̻̀
* į̻̏
* į̻͆
* į̻̆
* į̻̋
* į̻͌
* į̻̃
* į̻̽
* į̠̈
* į̠̄
* į̠̌
* į̠̅
* į̠́
* į̠͋
* į̠̊
* į̠̇
* į̠̂
* į̠͊
* į̠̀
* į̠̏
* į̠͆
* į̠̆
* į̠̋
* į̠͌
* į̠̃
* į̠̽
* į̺̈
* į̺̄
* į̺̌
* į̺̅
* į̺́
* į̺͋
* į̺̊
* į̺̇
* į̺̂
* į̺͊
* į̺̀
* į̺̏
* į̺͆
* į̺̆
* į̺̋
* į̺͌
* į̺̃
* į̺̽
* į͍̈
* į͍̄
* į͍̌
* į͍̅
* į͍́
* į͍͋
* į͍̊
* į͍̇
* į͍̂
* į͍͊
* į͍̀
* į͍̏
* į͍͆
* į͍̆
* į͍̋
* į͍͌
* į͍̃
* į͍̽
* į̤̈
* į̤̄
* į̤̌
* į̤̅
* į̤́
* į̤͋
* į̤̊
* į̤̇
* į̤̂
* į̤͊
* į̤̀
* į̤̏
* į̤͆
* į̤̆
* į̤̋
* į̤͌
* į̤̃
* į̤̽
* į̲̈
* į̲̄
* į̲̌
* į̲̅
* į̲́
* į̲͋
* į̲̊
* į̲̇
* į̲̂
* į̲͊
* į̲̀
* į̲̏
* į̲͆
* į̲̆
* į̲̋
* į̲͌
* į̲̃
* į̲̽
* į̹̈
* į̹̄
* į̹̌
* į̹̅
* į̹́
* į̹͋
* į̹̊
* į̹̇
* į̹̂
* į̹͊
* į̹̀
* į̹̏
* į̹͆
* į̹̆
* į̹̋
* į̹͌
* į̹̃
* į̹̽
* į̘̈
* į̘̄
* į̘̌
* į̘̅
* į̘́
* į̘͋
* į̘̊
* į̘̇
* į̘̂
* į̘͊
* į̘̀
* į̘̏
* į̘͆
* į̘̆
* į̘̋
* į̘͌
* į̘̃
* į̘̽
* į̰̈
* į̰̄
* į̰̌
* į̰̅
* į̰́
* į̰͋
* į̰̊
* į̰̇
* į̰̂
* į̰͊
* į̰̀
* į̰̏
* į̰͆
* į̰̆
* į̰̋
* į̰͌
* į̰̃
* į̰̽
* į̙̈
* į̙̄
* į̙̌
* į̙̅
* į̙́
* į̙͋
* į̙̊
* į̙̇
* į̙̂
* į̙͊
* į̙̀
* į̙̏
* į̙͆
* į̙̆
* į̙̋
* į̙͌
* į̙̃
* į̙̽
* į͇̈
* į͇̄
* į͇̌
* į͇̅
* į͇́
* į͇͋
* į͇̊
* į͇̇
* į͇̂
* į͇͊
* į͇̀
* į͇̏
* į͇͆
* į͇̆
* į͇̋
* į͇͌
* į͇̃
* į͇̽
* į̞̈
* į̞̄
* į̞̌
* į̞̅
* į̞́
* į̞͋
* į̞̊
* į̞̇
* į̞̂
* į̞͊
* į̞̀
* į̞̏
* į̞͆
* į̞̆
* į̞̋
* į̞͌
* į̞̃
* į̞̽
* į̝̈
* į̝̄
* į̝̌
* į̝̅
* į̝́
* į̝͋
* į̝̊
* į̝̇
* į̝̂
* į̝͊
* į̝̀
* į̝̏
* į̝͆
* į̝̆
* į̝̋
* į̝͌
* į̝̃
* į̝̽
* į̜̈
* į̜̄
* į̜̌
* į̜̅
* į̜́
* į̜͋
* į̜̊
* į̜̇
* į̜̂
* į̜͊
* į̜̀
* į̜̏
* į̜͆
* į̜̆
* į̜̋
* į̜͌
* į̜̃
* į̜̽
* į̧̈
* į̧̄
* į̧̌
* į̧̅
* į̧́
* į̧͋
* į̧̊
* į̧̇
* į̧̂
* į̧͊
* į̧̀
* į̧̏
* į̧͆
* į̧̆
* į̧̋
* į̧͌
* į̧̃
* į̧̽
* į̦̈
* į̦̄
* į̦̌
* į̦̅
* į̦́
* į̦͋
* į̦̊
* į̦̇
* į̦̂
* į̦͊
* į̦̀
* į̦̏
* į̦͆
* į̦̆
* į̦̋
* į̦͌
* į̦̃
* į̦̽
* į͉̈
* į͉̄
* į͉̌
* į͉̅
* į͉́
* į͉͋
* į͉̊
* į͉̇
* į͉̂
* į͉͊
* į͉̀
* į͉̏
* į͉͆
* į͉̆
* į͉̋
* į͉͌
* į͉̃
* į͉̽
* į͎̈
* į͎̄
* į͎̌
* į͎̅
* į͎́
* į͎͋
* į͎̊
* į͎̇
* į͎̂
* į͎͊
* į͎̀
* į͎̏
* į͎͆
* į͎̆
* į͎̋
* į͎͌
* į͎̃
* į͎̽
* į̈
* į̅
* į͋
* į̊
* į̇
* į͊
* į̏
* į͆
* į̆
* į̋
* į͌
* į̽ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlapping path segments:

* uni1D73 (U+1D73): Line(Line { p0: (156.0, 253.0), p1: (156.0, 199.0) }) has the same coordinates as a previous segment.
* uni1D75 (U+1D75): Line(Line { p0: (172.0, 258.0), p1: (172.0, 204.0) }) has the same coordinates as a previous segment.
* uni066E (U+066E): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni066E (U+066E): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni066E.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni066E.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628 (U+0628): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628 (U+0628): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0628.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0649.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A (U+062A): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A (U+062A): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062A.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B (U+062B): Line(Line { p0: (626.0, 76.0), p1: (626.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B (U+062B): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni062B.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633 (U+0633): Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633 (U+0633): Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.fina: Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633.fina: Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.medi: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.medi: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.init: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633.init: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634 (U+0634): Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634 (U+0634): Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.fina: Line(Line { p0: (991.0, 0.0), p1: (991.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634.fina: Line(Line { p0: (750.0, 76.0), p1: (750.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.medi: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.medi: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.init: Line(Line { p0: (552.0, 76.0), p1: (552.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634.init: Line(Line { p0: (307.0, 76.0), p1: (307.0, 0.0) }) has the same coordinates as a previous segment.
* uni0635 (U+0635): Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0635.fina: Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0636 (U+0636): Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0636.fina: Line(Line { p0: (1160.0, 0.0), p1: (1217.0, 153.0) }) has the same coordinates as a previous segment.
* uni0637 (U+0637): Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637 (U+0637): Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0637.fina: Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637.fina: Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0637.medi: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637.medi: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0637.init: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0637.init: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638 (U+0638): Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638 (U+0638): Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638.fina: Line(Line { p0: (159.0, 606.0), p1: (299.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638.fina: Line(Line { p0: (207.0, 0.0), p1: (207.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638.medi: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638.medi: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0638.init: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0638.init: Line(Line { p0: (102.0, 0.0), p1: (102.0, 76.0) }) has the same coordinates as a previous segment.
* uni0641 (U+0641): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0641 (U+0641): Line(Line { p0: (392.0, 0.0), p1: (392.0, 76.0) }) has the same coordinates as a previous segment.
* uni0641.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0641.fina: Line(Line { p0: (418.0, 0.0), p1: (418.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A4 (U+06A4): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A4 (U+06A4): Line(Line { p0: (392.0, 0.0), p1: (392.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A4.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A4.fina: Line(Line { p0: (418.0, 0.0), p1: (418.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A1 (U+06A1): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A1 (U+06A1): Line(Line { p0: (392.0, 0.0), p1: (392.0, 76.0) }) has the same coordinates as a previous segment.
* uni06A1.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni06A1.fina: Line(Line { p0: (418.0, 0.0), p1: (418.0, 76.0) }) has the same coordinates as a previous segment.
* uni0643 (U+0643): Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0643 (U+0643): Line(Line { p0: (506.0, 0.0), p1: (506.0, 76.0) }) has the same coordinates as a previous segment.
* uni0643 (U+0643): Line(Line { p0: (559.0, 606.0), p1: (699.0, 636.0) }) has the same coordinates as a previous segment.
* uni0643.fina: Line(Line { p0: (304.0, 76.0), p1: (304.0, 0.0) }) has the same coordinates as a previous segment.
* uni0644 (U+0644): Line(Line { p0: (427.0, 606.0), p1: (567.0, 636.0) }) has the same coordinates as a previous segment.
* uni0644.init: Line(Line { p0: (53.0, 606.0), p1: (193.0, 636.0) }) has the same coordinates as a previous segment.
* uni0646.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni064A.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni0626.init: Line(Line { p0: (88.0, 76.0), p1: (88.0, 0.0) }) has the same coordinates as a previous segment.
* uni06280649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0628064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06280626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062A0649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062A064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062A0626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062B0649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062B064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni062B0626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330631.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330631.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330631.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330631.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330632.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330632.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330632.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330632.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330649.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330649.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633064A.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0633064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0633064A.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0633064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0633064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330626.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06330626.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06330626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06330626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340631.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340631.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340631.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340631.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340632.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340632.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340632.fina.liga: Line(Line { p0: (663.0, 76.0), p1: (663.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340632.fina.liga: Line(Line { p0: (908.0, 0.0), p1: (908.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340649.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340649.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634064A.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0634064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0634064A.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni0634064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0634064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340626.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06340626.fina.liga: Line(Line { p0: (1069.0, 0.0), p1: (1069.0, 76.0) }) has the same coordinates as a previous segment.
* uni06340626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06340626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350631.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350631.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350632.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350632.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06350649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0635064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0635064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0635064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0635064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06350626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06350626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360631.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360631.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360632.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360632.fina.liga: Line(Line { p0: (663.0, 0.0), p1: (663.0, 76.0) }) has the same coordinates as a previous segment.
* uni06360649.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360649.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360649.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0636064A.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0636064A.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni0636064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0636064A.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360626.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360626.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni06360626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06360626.fina.liga: Line(Line { p0: (824.0, 76.0), p1: (824.0, 0.0) }) has the same coordinates as a previous segment.
* uni064406440647: Line(Line { p0: (721.0, 517.0), p1: (861.0, 547.0) }) has the same coordinates as a previous segment.
* uni06460649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0646064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06460626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06260649.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni0626064A.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni06260626.fina.liga: Line(Line { p0: (663.0, 195.0), p1: (715.0, 237.0) }) has the same coordinates as a previous segment.
* uni033C (U+033C): Line(Line { p0: (211.0, -160.0), p1: (182.0, -160.0) }) has the same coordinates as a previous segment. [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'MSTR' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 23 | 26 | 12 | 205 | 64 | 
| 7% | 8% | 4% | 64% | 20% | 



