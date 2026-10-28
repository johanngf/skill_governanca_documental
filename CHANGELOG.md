# Changelog

## 1.0.0 — 2026-10-28

- Promovida a distribuição estável após a bateria funcional H00–H07, com limites de evidência registrados em `tests/HOMOLOGACAO.md`.
- H07: DOCX institucional em conversa independente, fontes e execução documental condizentes com a Skill e indicação visual apresentada pelo usuário; não há log direto do evento de acionamento automático.
- Reexecutados oito testes automatizados: integridade de fontes, portabilidade do diretório, auditoria OOXML, coerência de status de release e de versão entre frontmatter e manifesto.
- `build_release.py` passa a ler a versão do manifesto, evitando divergência entre o nome do ZIP e a distribuição.
- Nenhuma alteração nas quatro fontes normativas, nos espelhos Markdown derivados ou no workflow operacional `SKILL.md` (exceto metadado de versão).
- Distribuição restrita à organização; a publicação e instalação no GitHub/ChatGPT continuam sendo ações separadas.

## 1.0.0-rc.2 — 2026-10-27

- Incorporadas evidências dos testes H00–H06; permanência de pendência para acionamento automático (não testado).
- Corrigida a validação de identidade da Skill quando o host renomeia a pasta de instalação: identidade conferida entre `SKILL.md` e `manifest.json`; nome físico divergente gera aviso no modo runtime.
- Acrescentado `--strict-dir-name` obrigatório no empacotamento e CI, preservando conformidade com a especificação Agent Skills no diretório distribuído.
- Incluídos testes de regressão para diretório renomeado, verificação estrita e divergência real de identidade.
- Não houve alteração das quatro fontes normativas, das transcrições ou das regras operacionais da Skill.
- **Pendente antes da versão estável:** homologação da rc.2 instalada e acionamento automático em conversa independente.


## 1.0.0-rc.1 — 2026-10-26

- Primeira distribuição candidata independente de projeto.
- Incluídas quatro fontes vigentes, sem modificá-las: Qualidade 1.2, Padronização 3.4, Contrato 0.7 e Modelo Formal 0.4.
- Definido ponto de entrada `SKILL.md` com classificação proporcional, gates, bloqueios localizados e regras de execução.
- Acrescentados manifesto, transcrições de leitura derivadas e validação de integridade.
- Acrescentada auditoria OOXML auxiliar para regressão do problema de títulos/bookmarks.
- **Pendente:** homologação da Skill instalada em ambiente limpo e teste de interoperabilidade na aplicação consumidora.
