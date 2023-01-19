def regress_out_cells (data_df, cellcounts, is_age):
    X = data_df.values
    cpg_names = data_df.columns
    cells_cols = ['CD8T', 'CD4T', 'NK', 'Bcell', 'Gran']
    if is_age:
        cells_cols.append('Age')
    cellcounts_sub = cellcounts[cells_cols]
    data = cellcounts_sub.values
    
    X_r = np.array(X)
    for i in tqdm(range(len(cpg_names)), ncols = 100):
        beta = X[:, i]
        model = LinearRegression()
        model.fit(data, beta)
        beta_pred = model.predict(data)
        X_r[:, i] = beta - beta_pred + np.mean(beta)
    return X_r