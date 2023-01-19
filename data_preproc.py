import pickle
import pandas as pd

def open_file(file_directory):
    with open(file_directory, 'rb') as f:
        file = pd.DataFrame(pickle.load(f))
    file = file.reset_index(drop = True)
    return file

def regional_division(pheno, betas, directory_folder, region_name):
    pheno_region = pheno.loc[(pheno['Region'] == region_name)]
    betas_region = betas.loc[pheno.index[pheno['Region'] == region_name]]
    return pheno_region, betas_region
    
def data_preproc(directory_folder, pheno_folder, betas_folder):
    pheno = open_file(pheno_folder)
    betas = open_file(betas_folder)

    for i in range(len(pheno)):
        if str(pheno['index_origin'][i])[0:2] == 'TR' or pheno['Status'][i] == 'ESRD':
            pheno = pheno.drop(index = i)
            betas = betas.drop(index = i)
    pheno = pheno.reset_index(drop = True)
    betas = betas.reset_index(drop = True)

    pheno_central, betas_central = regional_division(pheno, betas, directory_folder, 'Central')
    pheno_yakutia, betas_yakutia = regional_division(pheno, betas, directory_folder, 'Yakutia')
    return pheno_central, betas_central, pheno_yakutia, betas_yakutia