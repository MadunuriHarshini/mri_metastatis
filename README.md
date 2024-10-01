# mri_metastatis
Nested U-Net
The Nested U-Net architecture builds upon the classic U-Net model by incorporating a series of nested skip pathways. This design allows the model to capture features at multiple resolutions, improving the flow of information throughout the network. As a result, it excels at retaining both local and global context, making it particularly suited for complex medical images where the boundaries of lesions may not be well-defined.

Attention U-Net
Attention U-Net integrates an attention mechanism into the U-Net architecture, enabling the model to focus on the most relevant parts of the input images. This is especially beneficial in brain metastasis segmentation, where the tumors can have irregular shapes and vary significantly in appearance. By emphasizing critical regions, the Attention U-Net enhances the segmentation performance and reduces false positives.
