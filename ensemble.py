import pandas as pd
import os.path

geneTypes = ['nociceptionGenes', 'mechanoreceptionGenes', 'mechanoreception1Genes', 'mechanoreception2Genes', 'proprioceptionGenes']
dataTags = ['hier', 'kmeans', 'leiden', 'wgcna', 'dbscan', 'hdb']

for geneType in geneTypes:
    geneUnion = []
    for tag in dataTags:
        if os.path.isfile('data/' + tag + geneType + '.csv'):
            data = pd.read_csv('data/' + tag + geneType + '.csv')
            genes = data.iloc[:, 1].tolist()
            if (geneUnion == []):
                geneUnion = genes
            else:
                geneUnion = set(geneUnion).intersection(set(genes))

    df = pd.DataFrame(list(geneUnion))
    df.to_csv('data/' + geneType + '.csv', index=False, header=False)