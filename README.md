## Classificação de Doenças em Folhas de Batata

Este projeto consiste na construção de um modelo de Rede Neural Convolucional (CNN) criado com o TensorFlow para categorizar doenças nas folhas de batata. O modelo que pode distinguir entre folhas de batata saudáveis e doentes foi treinado e testado usando o conjunto de dados [Plant Village](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) do Kaggle. O pré-processamento, que também garante conjuntos de treinamento e teste adequados, permite que a CNN seja otimizada para classificação de imagens usando as funções de perda e otimizadores adequados.

O FastAPI fornece um backend de previsão em tempo real que usa o modelo TensorFlow treinado. Enquanto o Uvicorn administra o aplicativo FastAPI, os Endpoints controlam o upload de imagens e os resultados da categorização. O Docker containeriza os serviços, criando o TensorFlow Serving e o backend FastAPI em contêineres diferentes. O Docker Compose facilita a comunicação contínua e gerencia a rede.

A aplicação front-end baseada em ReactJS fornece uma interface fácil de usar para a classificação de doenças que permite que os usuários coloquem fotos e analisem os resultados. Esta interface funciona com o backend FastAPI para realizar previsões e é containerizada e implantada com os serviços de backend.

<center>

![Demonstração Web](assets/potato-disease-home-page.gif "Demonstração Web")

</center>

### Tecnologias Utilizadas

- **Python:** desenvolvimento backend e construção do modelo de aprendizado de máquina.
- **TensorFlow:** construir e treinar o modelo CNN.
- **TensorFlow Serving:** servir o modelo treinado.
- **FastAPI:** criar a API backend.
- **Uvicorn:** servidor ASGI para a aplicação FastAPI.
- **Docker:** containerizar os serviços.
- **ReactJS:** construir a aplicação frontend.
