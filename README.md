# YouTube Audio Ceļu Pārveide Tekstā

> [!TIP]
> Kods ir paredzēts Visual Studio Code!

> [!NOTE] 
>Nepieciešams ielādēt šādas bibliotēkas un lietotnes:
> 
>selenium
> 
>tkinter
>
> Googe Chrome
>
> Ielādēt var ar: `pip install -r requirements.txt`

## Projekta Autori 🔨

- Maksims Koļcovs, 15. grupa | 231RDB363
- Daniels Pauls Savickis, 12. grupa | 231RDB067


## Projekta Pamatmērķis un Uzdevumi 🎯

Mūsu projekta mērķis ir izstrādāt programmatūru jeb skriptu, kas pildīs sekojošus uzdevumus:

1. **Audio ceļu iegūšana no YouTube:** Izstrādāsim kodu, kas izmanto Selenium bibliotēku, lai iegūtu audio ceļus no YouTube platformas.
2. **Ceļu saglabāšana `.csv` dokumentā:** Izgūtos ceļus skriptam automātiski ir jāsaglabā `.csv` dokumentā.
3. **Lietotāju pārliecināšana:** Mūsu galvenais uzdevums ir pārliecināt lietotājus par šī skripta praktiskumu.

## Uzdevumu Padziļinātais Skaidrojums ⚙

`Audio ceļu iegūšana no YouTube`: paveikt šo uzdevumu var izmantojot `Selenium` bibliotēkas plāšās iespējas. Galvenais uzdevums, lai to panāktu ir izvēlēties pareizo ceļu līdz `Transcript` audio ceļiem. Nepieciešams uzrakstīt skriptu, kas pildīs cilvēka darbības: uzpiest uz *Google Chroome* pārlūku > nonākt *YouTube* platformā > uzspiest uz video > apstiprināt  *cookies* > uzspiest uz `more` jeb `vairāk` > uzpiest `Transcript`. Automizējot šīs darbības mēs varam panākt, ka lietotājs izgūst šos ceļus savām vajadzībām.

`Ceļu saglabāšana .csv`: Lai izgūta informācija jeb `Transcript` būtu vieglāk pārskatāms mēs piedāvajam to saglabāt atsevišķā `.csv` datnē. Musuprāt, tādā veidā viss teksts būs daudz pārskatamāks, jo `terminālā` vai `YouTube` ir daudz neērtāk pārskatīt un kopēt to, ja ir tāda nepieciešamība. Šo uzdevumu arī var paveikt izmantojot `Selenium` plašo funkcionalitāti, iegūto `Transcript` `Selenium` ievieto `.csv` datnē.

`Lietotāju pārliecināšana`: Jebkuras programmatūras pamatmērķis ir pielietojums. Mēs gribam pārliecināt lieotājus, ka mūsu kods var atvieglot to dzīvi. Tāpēc tiks demonstrēti reālie pielietojuma piemēri.


## Izmantoto Python Bibliotēku Saraksts un Izmantošanas Skaidrojums 🐍


Mūsu Python skriptā mēs izmantojām vairākas bibliotēkas:

- `Selenium`: Ļoti elastīga un viegli saprotama, un bagāta bibliotēka. Šajā kodā tā tika izmanota, lai automizētu vairākas darbības YouTube tīmekā vietnē. `Selenium WebDriver` tiek izmantots, lai inicializētu Chrome pārlūku. Tas tiek izdarīts ar `webdriver.Chrome()` funkciju. `WebDriver` tiek izmantots, lai atrastu konkrētus elemntus lapā un uz tiem uzpiestu. Tas tiek panākts, izmantojot `driver.find_element(By.XPATH, xpath)` un `element.click()` funkcijas. `WebDriverWait` un `expected_condition` funcijas arī izmanto `WebDrver` līdz konkrētas darbības izpīldās. Izgūst tekstu arī palīdzeja `WebDriver` rīks izmantojot `element.text` īpašību, tas palīdz izgūst tekstu no konkrēta elementa. Darbības ar elementiem, piemēram, pārvietot kursoru uz elementu tiek realizēts izmantojot `WebDriver` un `ActionChains` klasi. Apstrādāt kļūdas mums arī palīdzēja `Selenium`, kas var rasties strādājot un veicot darbības ar elementiem. `try/expect` bloki palīdzēja atrast un atrisināt dažādas kļūdas.

- `Time`: Bibliotēka nodrošina funckijas, lai varētu strādāt ar laiku dažādos uzdevumos. Šajā skriptā `sleep` funckija tiek izmantota, lai aizskavētu skripta izpildi.

- `csv`: Šī bibliotēka nodrošina iespēju strādāt ar CSV failiem Python programmēšanas valodā. Šajā skriptā mēs to izmantojām, lai saglabātu iegūto transkriptu CSV failā.

- `tkinter`: Python grafiskā (GUI - A graphical user interface) bibliotēka. Šajā kodā mēs to izmantojām, lai izveidotu GUI logu.

## Programmatūras Izmantošanas Metodes 🔍

Šo programmatūru var lietot, piemēram, šādi:

1. **Valodas apguvei, piemēram, lietotājs var izlasīt teikumus un to strūkturu, komentēt un pat pierakstīt izrunas.**
2. **Dažādu darbu rakstīšanai, piemēram, ZPD (zinātniski pētnieciskais darbs), Baklaura darbs, referāti, ērti norādīt atsauci, jo ir norādīts precīzs laiks no video.**
3. **Bibliotēkas `Selenium` un programmēšanas valodas `Python` pilnveidošanai, jo šajā skriptā ir veiktas vairākas dažādas darbības.**
4. **Dziesmu `lyrics` izveidei.**
>[!WARNING]
> Svarīgi pieminēt, ka ne visiem video `YouTube` ir pieejami `Transcripti!`

## Programmatūras Konfigurēšana 💼

Lai kods nostrādātu ir nepieciešams veikt papildinājumus kodā, lai būtu ērtāk atrast varat lietot ctrl+f un uzrakstīt `#here`. Tur tiks aprakstīts, ko nepieciešams izmainīt / pievienot !

## Izmantotie Avoti 💡

1. https://www.geeksforgeeks.org/find_element_by_xpath-driver-method-selenium-python/ - "How to use driver.find_element(By.XPATH) method in Selenium?" > Python 3 > element = driver.find_element(By.XPATH, "//form[input/@name ='search']") [Last Updated : 16 Mar, 2023 by 
NaveenArora]
2. https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html - "The ActionChains implementation." > [Last updated: MARCH 23, 2023]
3. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax - Basic writing and formatting syntax > [snapshot: 20:36:25 JANUARY 17, 2024]
4. https://stackoverflow.com/questions/12698843/how-do-i-pass-options-to-the-selenium-chrome-driver-using-python - Usage to create a Chrome driver instance - [Answered May 30, 2023 at 11:19 by kit4py and edited May 30, 2023 at 11:59 by user21985260]
5. https://www.youtube.com/watch?v=t0PBBPuPgaw&list=PL2poe6dHjzLy6qW74W9KhxzFyDKbz6qXz&index=9 - 5. lekcija. Selenium izmantošana pārlūkprogrammas vadībai Python valodā - By Aleksejs Jurenoks, video uploaded [19 Nov 2023].

