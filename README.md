# **Monitore resultados e estatísticas de futebol em tempo real no Telegram com Python**

![Imagem de capa](https://github.com/jeffersonrafael/FutebolAPI-Bot/blob/main/assets/capa.png)




<div align="center">
    <a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python 3.11"></a>
    <a href="https://core.telegram.org/bots"><img src="https://img.shields.io/badge/Telegram%20Bot-%2300A5E.svg?style=flat&logo=telegram&logoColor=blue" alt="Telegram Bot"></a> 
    <a href="https://restfulapi.net/"><img src="https://img.shields.io/badge/REST%20API-%2300A5E.svg?style=flat&logo=api&logoColor=white" alt="REST API"></a> 
</div>



# Resumo

Este projeto faz integração com 3 APIs. Duas APIs externas, uma para o sistema de pagamento e a outra para o recebimento dos dados de futebol. 

Este produto irá oferecer aos usuários monitoramento **gratuito** sobre seus times e campeonatos preferidos. E oferecerá acesso à nossa **inteligência artificial que realiza previsões** dos eventos esportivos, a partir de uma mensalidade bastante acessível.



### Quais informações temos acesso via API?
- Detalhes sobre a partida, como status, horário, ao vivo e etc...  
- Dados sobre o campeonato, como posição do time na tabela, rodada, temporada e etc...  
- As informações de partidas ao vivo são enviadas com um **delay** para contas com acesso gratuito à API.
  - Quanto tempo tem o delay?


## Tecnologias

**Linguagem de programação**
> Python == 3.8.8

**Bibliotecas**
> Requests  
> Python-Telegram-Bot

## Arquitetura do projeto

```mermaid
graph TD
    subgraph APIsExternas
        api1[API FOOTBALL-DATA]
        api2[API MERCADO PAGO]
    end
    subgraph Processamento
        id1[(Database)]
        id2[Modelo de AI]
    end
    subgraph Bot
        bot[Bot Telegram]
    end

    api1 --> id1
    api2 --> id1
    id1 --> APIsExternas

    id1 --> Bot
    bot --> id1

    id2 --> id1
    id1 --> id2
    id2 --> Bot

```

## Interação do bot com o usuário

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centralizar GIF
    </title>
    <style>
            .gif-container {
                text-align: center;
            }
            .gif-container img {
                width: 200px; /* Defina a largura desejada */
                height: 435px; /* Defina a altura desejada */
            }
    </style>
</head>
<body>
    <div class="gif-container">
        <img src="./assets/video_2024-12-14_13-45-32.gif" alt="Esse gif apresenta uma demonstração do conceito do Bot Telegram construído até agora.">
    </div>
</body>
</html>


# Licensa

Attribution-NonCommercial 4.0 International
