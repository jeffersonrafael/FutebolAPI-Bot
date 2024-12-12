![Imagem de capa](https://github.com/jeffersonrafael/FutebolAPI-Bot/blob/dev/assets/capa.png)


<div align="center">
    <a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python 3.11"></a>
    <a href="https://core.telegram.org/bots"><img src="https://img.shields.io/badge/Telegram%20Bot-%2300A5E.svg?style=flat&logo=telegram&logoColor=blue" alt="Telegram Bot"></a> 
    <a href="https://restfulapi.net/"><img src="https://img.shields.io/badge/REST%20API-%2300A5E.svg?style=flat&logo=api&logoColor=white" alt="REST API"></a> 
</div>


# Resumo

Uma aplicação que integra uma _API_ de dados de futebol com um _Telegram bot_.


## Descrição

Este projeto utiliza Python 3.8.8, um bot do Telegram e uma REST API para demonstrar funcionalidades incríveis.

### Quais informações temos acesso via API?
- Detalhes sobre a partida, como status, horário, ao vivo e etc...  
- Dados sobre o campeonato, como posição do time na tabela, rodada, temporada e etc...  
- As informações de partidas ao vivo são enviadas com um **delay** para contas com acesso gratuito à API.
  - Quanto tempo tem o delay?


## Instalação




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

## Interação com o usuário



```mermaid
flowchart TD;  
    subgraph 1º escolha do usuário
        
        id1(Premier League)

    end

    subgraph 2º escolha do usuário 

        id1(Premier League) --> id2(Top goleadores)
        id1(Premier League) --> id3(Classificação)
        id1(Premier League) --> id4(head2head)
        id1(Premier League) --> id5(Partidas)
    end

    subgraph 3º escolha do usuário
        
        id5(Partidas) --> id6(Partida em particula)
        id4(head2head) --> id7(Jogador)
        id3(Classificação) --> id7(Jogador)
        id2(Top goleadores) --> id7(Jogador)
        id6(Partida em particula) --> id7(Jogador)
    end


    
```

# Issues 
Deve-se encontrar uma maneira de reduzir o numero de if's



# Configurações

[Link da API com as estatísticas de futebol com dados numa forma machine-readable.](https://www.football-data.org/)

[Documentação com informações detalhadas sobre a API](https://www.football-data.org/documentation/quickstart)

