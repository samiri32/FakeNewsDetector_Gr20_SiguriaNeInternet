# Fake News Detector

### Universiteti i Prishtinës

### Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike

#### Drejtimi: Inxhinieri Kompjuterike

#### Viti: III

#### Semestri: V

#### Lenda: Siguria në Internet

#### Profesorët: PhD.c Mërgim H. HOTI, Prof. Dr. Blerim REXHA

#### Studentët: Arlind BYTYQI, Enes HASANI, Marigona MORINA, Samir SIMNICA

#### Grupi i projektit: 20

##### Prishtinë, janar 2022

## Pershkrimi i projektit
#### Ky "Fake News Detector" detekton lajmet e rreme ne gjuhen shqipe. Aplikacioni eshte shkruar ne gjuhen programuese Python dhe bazohet ne nje dataset ku jane ndare lajmet e rreme dhe te verteta ne portalet shqiptare gjate viteve te fundit, dataset perbehet prej perafersisht 2000 lajmeve te rreme dhe 2000 te verteta, te ndare nje lajm per fajll. Skripta "WriteTOCSV.py" i lexon lajmet neper keto fajlla dhe i shkruan ne fajllin "CSV_news.csv". Në skriptën "stopwords.py" gjenden fjalët e ndaluara të cilat përdoren nga skripta "FakeNewsDetector.py" për para-procesim të tekstit. Skripta "scrapAndCSVwrite.py" sahere që ekezekutohet merr lajme nga faqja "kallxo.com" dhe i shkruan në fajllin "ScrapAndWriteToCSV.csv". "FakeNewsDetector" është skripta kryesore e cila përmbanë modelin matematikorë për detektimin e lajmeve të rreme, pas ekzekutimit automatikisht testohet saktesia e modelit me disa lajme nga fajlli "CSV_news.csv", por ka edhe funksionin manual_testing(lajme) i cili mund të përdoret për predikim të vërtetsisë të cilit do lajm.

## Description:
#### This "Fake News Detector" detects fake news in Albanian. The application is written in the Python programming language and is based on a dataset where false and true news gathered from Albanian portals in recent years are placed. The dataset consists of approximately 2000 false and 2000 true news, separated as one article per file. The script "WriteTOCSV.py" reads the news in these files and writes them into the file "CSV_news.csv". The script "stopwords.py" contains stop words(these words contain very little information) that are used by the script "FakeNewsDetector.py" for pre-processing the text. The script "scrapAndCSVwrite.py" receives news from the site "kallxo.com" whenever it is executed and writes them to the file "ScrapAndWriteToCSV.csv". "FakeNewsDetector" is the main script that contains the mathematical model for detecting fake news, after execution the accuracy of the model is automatically tested using some news from the file "CSV_news.csv", but it also has the function manual_testing(news) which can be used to predict if the news is fake or not.

## Referencat:
#### https://github.com/rexshijaku/alb-fake-news-corpus
#### https://github.com/explosion/spaCy/blob/master/spacy/lang/sq/stop_words.py?fbclid=IwAR11jfEbSSW6raQ18TaFgB5ifmbhgvKh9zx9Xp4mYayuE78F9svT2WtKEoA
