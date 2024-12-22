---
Связи:
Теги: #ML
---
Principal Component Analysis
Метод [[Dimensionality reduction]]

- [[#Visualization in PCA|Visualization in PCA]]
- [[#How it works|How it works]]



## Visualization in PCA
- Оч удобно юзать PCA для визуализации, чтоб отрисовать вектор в 2-3 мерном пространстве, котором мы можем парсить (в отличие от n-мерного, n>3, куда нас обычно вектора приводят)
![[Pasted image 20230831231721.png]]![[Pasted image 20230831231749.png]]![[Pasted image 20230831231921.png]]

## How it works
- How it works with intuition pic 1
- Algo abstract:
	- We need to found Eigenvectors - uncorerelated features for our data 
		- They are usefull because the Eigenvectors of the co-variance matrix from your data.
	- And Eigenvalue - the amount of info retained by each feature
- Algo in practice:
	- Mean Normalize Data
	- Get Covariance Matrix
	- PerformSVD and get 3 matrices
		- First, you will perform the dust products between the matrix containing your word embeddings and the first and columns of the U matrix. Where N equals the number of dimensions that you want to have at the end.  For visualization, it's common practice to have two dimensions, 
		- then you'll get the percentage of variants retained in the new vector space. 
		- As an important side note, your Eigenvectors and Eigenvalues should be organized according to the Eigenvalues in descending order. 
		- This condition will ensure that you retain as much information as possible from your original embedding. 
		- However, most libraries order those matrices for you.

![[Pasted image 20230831232025.png]]
![[Pasted image 20230831232238.png]]
![[Pasted image 20230831232503.png]]
![[Pasted image 20230831232713.png]]
![[Pasted image 20230831232841.png]]