# YouTube Audio Ceļu Pārveide Tekstā

> [!TIP]
> Kods ir paredzēts Visual Studio Code!

> [!NOTE] 
>Nepieciešams ielādēt šādas bibliotēkas un lietotnes:
> 
>pip install selenium
> 
>pip install csv
> 
>pip install tkinter
>
> Googe Chrome

## Projekta Autori 🔨

- Maksims Koļcovs, 15. grupa | 231RDB363
- Daniels Pauls Savickis, 12. grupa | 231RDB067



## Projekta Pamatmērķis un Uzdevumi 🎯

Mūsu projekta mērķis ir izstrādāt programmatūru jeb skriptu, kas pildīs sekojošus uzdevumus:

1. **Audio ceļu iegūšana no YouTube:** Izstrādāsim kodu, kas izmanto Selenium bibliotēku, lai iegūtu audio ceļus no YouTube platformas.
2. **Ceļu saglabāšana `.csv` dokumentā:** Izgūtos ceļus skriptam automātiski ir jāsaglabā `.csv` dokumentā.
3. **Lietotāju pārliecināšana:** Mūsu galvenais uzdevums ir pārliecināt lietotājus par šī skripta praktiskumu.

## Uzdevumu padziļinātais skaidrojums

`Audio ceļu iegūšana no YouTube`: paveikt šo uzdevumu var izmantojot `Selenium` bibliotēkas plāšās iespējas. Galvenais uzdevums, lai to panāktu ir izvēlēties pareizo ceļu līdz `Transcript` audio ceļiem. Nepieciešams uzrakstīt skriptu, kas pildīs cilvēka darbības: uzpiest uz *Google Chroome* pārlūku > nonākt *YouTube* platformā > uzspiest uz video > apstiprināt  *cookies* > uzspiest uz `more` jeb `vairāk` > uzpiest `Transcript`. Automizējot šīs darbības mēs varam panākt, ka lietotājs izgūst šos ceļus savām vajadzībām.

`Ceļu saglabāšana .csv`: Lai izgūta informācija jeb `Transcript` būtu vieglāk pārskatāms mēs piedāvajam to saglabāt atsevišķā `.csv` datnē. Lai tu realizētu mēs izmantojām


## Izmantoto Python bibliotēku saraksts un izmantošanas skaidrojums 🐍


Mūsu Python skriptā mēs izmantojām vairākas bibliotēkas:

- `Selenium`: Ļoti elastīga un viegli saprotama, un bagāta bibliotēka. Šajā kodā tā tika izmanota, lai automizētu vairākas darbības YouTube tīmekā vietnē. `Selenium WebDriver` tiek izmantots, lai inicializētu Chrome pārlūku. Tas tiek izdarīts ar `webdriver.Chrome()` funkciju. `WebDriver` tiek izmantots, lai atrastu konkrētus elemntus lapā un uz tiem uzpiestu. Tas tiek panākts, izmantojot `driver.find_element(By.XPATH, xpath)` un `element.click()` funkcijas. `WebDriverWait` un `expected_condition` funcijas arī izmanto `WebDrver` līdz konkrētas darbības izpīldās. Izgūst tekstu arī palīdzeja `WebDriver` rīks izmantojot `element.text` īpašību, tas palīdz izgūst tekstu no konkrēta elementa. Darbības ar elementiem, piemēram, pārvietot kursoru uz elementu tiek realizēts izmantojot `WebDriver` un `ActionChains` klasi. Apstrādāt kļūdas mums arī palīdzēja `Selenium`, kas var rasties strādājot un veicot darbības ar elementiem. `try/expect` bloki palīdzēja atrast un atrisināt dažādas kļūdas.

- `Time`: Bibliotēka nodrošina funckijas, lai varētu strādāt ar laiku dažādos uzdevumos. Šajā skriptā `sleep` funckija tiek izmantota, lai aizskavētu skripta izpildi.

- `csv`: Šī bibliotēka nodrošina iespēju strādāt ar CSV failiem Python programmēšanas valodā. Šajā skriptā mēs to izmantojām, lai saglabātu iegūto transkriptu CSV failā.

- `tkinter`: Python grafiskā (GUI - A graphical user interface) bibliotēka. Šajā kodā mēs to izmantojām, lai izveidotu GUI logu.
