# Resumo

Uma aplicação que integra uma _API_ de dados de futebol com um _Telegram bot_.


## Workflow

```mermaid
flowchart LR;  
    id1[API] --> id2{Telegram BOT};
    id2{Telegram BOT} --> id3[User];
    id3[User] --> id2{Telegram BOT}
    
    style id1 fill:#477739
    style id2 fill:#02A0E3
```


# Configurações

[Link da API com as estatísticas de futebol com dados numa forma machine-readable.](https://www.football-data.org/)

