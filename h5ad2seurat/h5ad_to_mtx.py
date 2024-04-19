import sys
import scanpy as sc
import scipy.io
import scipy.sparse as sp
import gzip
import os

def main(h5ad_path, temp_path):
    adata = sc.read_h5ad(h5ad_path)
    if "gene_symbols" in adata.var.columns:
        adata.var_names = data.var["gene_symbols"]
    
    # check sparse, if not, make it sparse
    if not sp.issparse(adata.X):
        adata.X = sp.csr_matrix(adata.X)
    
    temp_mtx = os.path.join(temp_path, "matrix.mtx.gz")
    temp_barcodes = os.path.join(temp_path, "barcodes.tsv.gz")
    temp_features = os.path.join(temp_path, "features.tsv.gz")
    temp_meta = os.path.join(temp_path, "metadata.csv")

    print("Saving expression matrix to mtx...")
    with gzip.open(temp_mtx, 'wb') as f:
        scipy.io.mmwrite(f, adata.X.T)

    print("Saving barcodes.tsv and features.tsv...")
    adata.obs_names.to_series().to_csv(temp_barcodes, index=False, header=False)
    adata.var_names.to_series().to_csv(temp_features, index=False, header=False)

    adata.obs.to_csv(temp_meta, header=True, index=True)
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])