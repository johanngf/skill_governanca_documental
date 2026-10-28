# Homologação funcional da Skill — cenários de regressão

**Ambiente obrigatório:** conversa nova e comum, sem fontes de projeto específicas, sem Diretrizes de Atuação de um projeto personalizado. A Skill deve estar instalada e suas fontes disponíveis por seu próprio pacote. Execute duas vezes, uma com `@governanca-documental-institucional` e outra solicitando o caso sem mencioná-la, para testar acionamento explícito e implícito.

## H01 — Resultado institucional

> Crie um DOCX institucional intitulado “Avaliação Preliminar de Atendimento”, registrando que uma equipe compartilhada atende solicitações internas, há relatos de aumento de demanda e dúvidas de priorização, mas não existem métricas consolidadas fornecidas nem mudança de processo aprovada. Distinga fatos informados, hipóteses e limites; avalie proporcionalmente uma etapa adicional de aprovação. O documento não deve criar responsabilidades nem instituir mudanças. Entregue o arquivo final validado.

**Aceitação:** quatro fontes consumidas conforme escopo; DOCX institucional; gate de conteúdo; títulos estruturados; sumário condizente, navegável e atualizável quando aplicável; conformidade formal documentada e limitações explicitadas. Não inventar números, decisões ou autoria.

## H02 — Material auxiliar

> Crie um DOCX pessoal e descartável, de uma página, com checklist de cinco perguntas para reunião sobre priorização. Não é documento institucional.

**Aceitação:** arquivo simples, sem institucionalização automática. Skill pode deixar de ser acionada; se acionada, deve preservar proporcionalidade.

## H03 — Solicitação mista

> Crie dois arquivos DOCX separados: (1) uma nota institucional preliminar sobre priorização interna, sem mudanças aprovadas; (2) uma lista pessoal descartável de perguntas para a equipe. Não misture os tratamentos.

**Aceitação:** Resultados independentes, com governança específica e entrega sem confusão de estilos/controles.

## H04 — Insumo indispensável ausente

> Crie uma nota institucional e, independentemente, uma matriz institucional que **deve utilizar exatamente** um template obrigatório não anexado nem disponível. Não reconstrua o template.

**Aceitação:** nota independente liberável após os gates; matriz bloqueada por falta de fonte específica; sem inferência inventada.

## H05 — Falha de OOXML controlada

Use um DOCX institucional com bookmark inserido **antes** de `w:pPr` em um título. Solicite revisão integral **sem indicar onde está o defeito**.

**Aceitação:** defeito detectado e corrigido estruturalmente; texto e estilos anteriores preservados; nenhum `w:pPr` fora da ordem; renderização e navegação efetiva verificadas onde houver acesso. Validar com `scripts/audit_docx.py` como evidência técnica complementar.

## H06 — Word para Web

Abrir o arquivo H01 no Word para Web, verificar títulos e subníveis legíveis, hyperlinks do sumário e formatação; salvar/baixar e comparar DOCX. Registrar separadamente **abertura/navegação observada** e **regravação comprovada**. Não aceitar apenas renderização local como prova de interoperabilidade.

## Regra de encerramento

A aprovação depende de evidências documentais e de inspeção, não apenas de uma declaração do executor. Falhas em H01/H05/H06 são bloqueantes para homologação da Skill. Registrar versão da Skill, fontes, modelo/host, data e resultados de cada teste. Uma execução pontual aprovada não assegura confiabilidade estatística.

## H07 — Acionamento sem `@`

Executar em conversa comum fora de projeto específico, com a Skill instalada, **sem selecioná-la explicitamente**. Pedir uma nota institucional em DOCX sobre riscos potenciais na triagem de solicitações internas sem métricas, mudanças aprovadas ou responsáveis nomeados.

**Aceitação do artefato:** separar relatos e hipóteses, materializar com a governança institucional e validar conteúdo, formato e OOXML. **Aceitação do acionamento:** exigir evidência de acesso real às referências e, quando disponível, evento/registro de seleção da Skill. Referir-se a quatro fontes em um DOCX comprova no máximo comportamento consistente com a Skill, não o mecanismo causal da invocação.

O resultado do H07 realizado em 28/10/2026 consta em `HOMOLOGACAO.md`.
