import pandas as pd

def fillDF(_vertetesia, dataFrame):
    i=1
    while i<=2000:
        try:
            with open ("full_texts/{vertetesia}/{numri}.txt".format(vertetesia=_vertetesia, numri=i), 'r', encoding='utf-8') as file:
                var = file.read()
                fake = 1 if _vertetesia=="fake" else 0
                dictionary = {'lajmi': var, 'vertetesia': fake}
                dataFrame = dataFrame.append(dictionary, ignore_index=True)
                i=i+1
                pass
        except:  
            print(i);
            i=i+1;
            file.close()
    return dataFrame
    

data=[]
dataFrame = pd.DataFrame(data, columns =['lajmi', 'vertetesia'])
dataFrame = fillDF("true", dataFrame)
dataFrame = fillDF("fake", dataFrame)
dataFrame = dataFrame.sample(frac=1)
dataFrame.to_csv('CSV_news.csv', index=False, mode='a')