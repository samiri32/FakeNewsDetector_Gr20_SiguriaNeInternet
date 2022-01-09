# Fake News Detector

### Universiteti i Prishtinës

### Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike

#### Drejtimi: Inxhinieri Kompjuterike

#### Viti: III

#### Semestri: V

#### Lenda: Siguria në Internet

#### Profesorët: PhD.c Mërgim H. HOTI, Prof. Dr. Blerim REXHA

#### Studentët: Enes Hasani, Samir Simnica

#### Grupi i projektit: 7 && 10

##### Prishtinë, janar 2022

## Pershkrimi i projektit
#### Ky "Fake News Detector" detekton lajmet e rreme ne gjuhen shqipe. Aplikacioni eshte shkruar ne gjuhen programuese Python dhe bazohet ne nje dataset ku jane ndare lajmet e rreme dhe te verteta ne portalet shqiptare gjate viteve te fundit, dataset perbehet prej perafersisht 2000 lajmeve te rreme dhe 2000 te verteta, te ndare nje lajm per fajll. Skripta "WriteTOCSV.py" i lexon lajmet neper keto fajlla dhe i shkruan ne fajllin "CSV_news.csv". Në skriptën "stopwords.py" gjenden fjalët e ndaluara të cilat përdoren nga skripta "FakeNewsDetector.py" për para-procesim të tekstit. Skripta "scrapAndCSVwrite.py" sahere që ekezekutohet merr lajme nga faqja "kallxo.com" dhe i shkruan në fajllin "ScrapAndËriteToCSV.csv". "FakeNeësDetector" është skripta kryesore e cila përmabnë modelin matematikorë për detektimin e lajmeve të rreme, pas ekzekutimit automatikisht testohet saktesia e modelit me disa lajme nga fajlli "CSV_news.csv", por ka edhe funksionin manual_testing(lajme) i cili mund të përdoret për predikim të vërtetsisë të cilit do lajm
