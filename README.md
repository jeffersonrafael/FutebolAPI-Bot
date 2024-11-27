![Imagem de capa](../FutebolAPI-Bot/assets/capa.png)


<div align="center">
    <a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python 3.11"></a>
    <a href="https://core.telegram.org/bots"><img src="https://img.shields.io/badge/Telegram%20Bot-%2300A5E.svg?style=flat&logo=telegram&logoColor=blue" alt="Telegram Bot"></a> 
    <a href="https://restfulapi.net/"><img src="https://img.shields.io/badge/REST%20API-%2300A5E.svg?style=flat&logo=api&logoColor=white" alt="REST API"></a> 
</div>

## Descrição

Este projeto utiliza Python 3.11, um bot do Telegram e uma REST API para demonstrar funcionalidades incríveis.

## Instalação



# Resumo

Uma aplicação que integra uma _API_ de dados de futebol com um _Telegram bot_.


## Workflow

```mermaid
flowchart TD;  
    subgraph Sistema
        id1[API] -- Arquivo .json --- id2{Telegram BOT};
    end
    
    id2{Telegram BOT} -- OUTPUT --- id3[User];
    id3[User] -- FEEDBACK --- id2{Telegram BOT}
    
    style id1 fill:#477739
    style id2 fill:#477739
```


# Configurações

[Link da API com as estatísticas de futebol com dados numa forma machine-readable.](https://www.football-data.org/)

