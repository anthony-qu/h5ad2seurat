args <- commandArgs(trailingOnly = TRUE)
temp_dir = args[1]
out_file = args[2]


library(Seurat)
matrix_file = paste0(temp_dir,"/matrix.mtx.gz")
barcodes_file = paste0(temp_dir,"/barcodes.tsv.gz")
features_file =paste0(temp_dir,"/features.tsv.gz")
print("Reading into seurat object...")
exp_mat <- ReadMtx(mtx = matrix_file, cells = barcodes_file, features = features_file, feature.column=1)
seurat_object = CreateSeuratObject(exp_mat)

meta = read.csv(paste0(temp_dir, "/metadata.csv"), row.names=1)
seurat_object@meta.data = meta

# Save as RDS
saveRDS(seurat_object, file = out_file)