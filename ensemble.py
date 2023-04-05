import pandas as pd

geneTypes = ['nociceptionGenes', 'mechanoreception1Genes', 'mechanoreception2Genes', 'proprioceptionGenes']
dataTags = ['hier', 'kmeans']

for geneType in geneTypes:
    geneUnion = []
    for tag in dataTags:
        data = pd.read_csv('data/' + tag + geneType + '.csv')
        genes = data.iloc[:, 1].tolist()
        if (geneUnion == []):
            geneUnion = genes
        else:
            geneUnion = list(set(geneUnion) & set(genes))

    df = pd.DataFrame(geneUnion)
    df.to_csv('data/' + geneType + '.csv', index=False, header=False)
