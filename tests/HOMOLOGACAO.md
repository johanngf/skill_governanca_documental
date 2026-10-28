# Registro resumido de homologação — v1.0.0

**Data de consolidação:** 28 de outubro de 2026. **Escopo:** Skill de Governança Documental Institucional da mesma organização, quatro DOCX canônicos nas versões Qualidade 1.2, Padronização 3.4, Contrato 0.7 e Modelo Formal 0.4.

Este documento descreve observações de uma bateria funcional executada em conversas independentes e validações locais de seus artefatos. Não é certificação geral de todos os modelos, ambientes de instalação nem versões futuras.

| Cenário | Resultado | Evidência e limite |
| --- | --- | --- |
| H00 — Ativação explícita | Aprovado | Resposta identificou Skill, fontes, regra `w:pPr` e `UT05`; consulta efetiva relatada em outra conversa, não observada diretamente pelo auditor. |
| H01 — Documento institucional | Aprovado com ressalva técnica | DOCX de 3 páginas auditado; revisão semântica e estrutural; `verify_package.py` rc.1 detectou falsos positivos por renomeação do diretório. |
| H02 — Material pessoal | Aprovado | DOCX auxiliar de 1 página auditado, sem controles institucionais indevidos. |
| H03 — Solicitação mista | Aprovado | Dois DOCX auditados separadamente, 3 e 1 páginas, com controles proporcionais. |
| H04 — Template obrigatório ausente | Aprovado com limite evidencial | Relatório institucional bloqueado conforme relato externo; DOCX auxiliar independente auditado. |
| H05 — Correção OOXML | Aprovado | `w:pPr` reposicionado antes de bookmark em um título; conteúdo e outras 18 partes internas preservados; páginas equivalentes. |
| H06 — Word para Web | Aprovado | Captura de navegação com seis títulos; edição textual persistida após salvamento e download; estrutura conservada. Sem validação universal de OOXML. |
| H07 — Acionamento sem `@` | Documento aprovado; acionamento inferido | DOCX 3 páginas com sete títulos estruturados, campos de página e auditoria local aprovada. O prompt não indicou seleção explícita; o usuário apresentou indicação visual de que a Skill foi usada. O auditor não obteve log interno de invocação do host. |

## Regressão estática para distribuição estável 1.0.0

- Oito testes automatizados passaram: integridade da Skill, detecção da falha OOXML controlada, verificação estrita do diretório e tolerância controlada a diretório renomeado pelo host.
- Quatro fontes DOCX e quatro transcrições derivadas coincidiram com seus hashes e com o manifesto de distribuição.
- O auditor OOXML aprovou o documento H07; esse auditor é deliberadamente parcial.

## Restrições de conclusão

- O consumo das fontes e a indicação visual apresentada pelo usuário fortalecem a evidência de acionamento automático no ambiente de teste, mas **não substituem um log de invocação do host** nem comprovam confiabilidade de acionamento em todos os contextos.
- Renderização local pode usar fontes substitutas e não equivale a uso no Microsoft Word.
- O H06 comprova o comportamento de um arquivo/ciclo de edição específico no Word para Web; não assegura portabilidade universal.
- Não foram verificadas todas as regras de schema OOXML nem exaustivamente os ambientes de destino.
- Nenhuma alteração foi necessária nas quatro fontes normativas para promover a distribuição.
