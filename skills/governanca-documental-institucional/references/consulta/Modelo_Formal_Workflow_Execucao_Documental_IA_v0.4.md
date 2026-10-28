<!-- CÓPIA TEXTUAL DERIVADA AUTOMATICAMENTE de Modelo_Formal_Workflow_Execucao_Documental_IA_v0.4.docx. Sem autoridade normativa independente. Elementos visuais/diagramação devem ser consultados no DOCX canônico. Não editar manualmente; executar scripts/sync_sources.py --write. -->

# Transcrição de consulta — Modelo_Formal_Workflow_Execucao_Documental_IA_v0.4

GOVERNANÇA DOCUMENTAL

Modelo Formal do Workflow de  
Execução Documental por IA

Especificação formal do lifecycle de Solicitações, Resultados e Unidades de Execução

| Finalidade | Formalizar estados, transições, gates, retornos, checkpoints, cancelamentos e condições de liberação do workflow de execução documental por IA. |
| --- | --- |
| Escopo | Decomposição de Solicitações em Resultados e UEs; integração; validação de conteúdo e artefato; preservação de escopo; suspensão, cancelamento e liberação. |
| Versão | 0.4 |
| Data de referência | 24 de setembro de 2026 |
| Situação | Especificação institucional estabilizada após validação estrutural e reteste dirigido. |
| Responsável pelo documento | Johann Munzlinger |
| Autoria | Johann Munzlinger |
| Auxílio de IA generativa | Documento estruturado e materializado com auxílio de IA generativa; validação institucional permanece sob responsabilidade humana. |

| Natureza do material |
| --- |
| Especificação institucional de workflow. Define o modelo formal de estados e transições que operacionaliza o Contrato Operacional vigente sem amarrá-lo a uma ferramenta, arquitetura de agentes ou mecanismo específico de execução. |

Governança Documental • Workflow por IA • Especificação formal

Sumário

1 Finalidade, escopo e posição do modelo	3

1.1 Relação com as fontes e independência de implementação	3

2 Modelo conceitual	3

2.1 Solicitação	3

2.2 Resultado	3

2.3 Unidade de Execução — UE	3

3 Regras de concorrência e composição	4

4 Estados da Unidade de Execução	4

4.1 Gate de premissa	5

4.2 Transições da UE	5

4.3 Clarificações de percurso da UE	6

5 Dependências do Resultado	6

6 Estados do Resultado	6

6.1 Transições do Resultado	7

6.2 Clarificações de escolha e retorno	8

7 Fluxos principais	8

7.1 Criação documental	8

7.2 Resultado exclusivamente textual	8

7.3 Intervenção exclusivamente formal	8

7.4 Encerramento legítimo sem alteração	8

7.5 Checkpoint humano	9

7.6 Cancelamento	9

8 Integração e gate global de conteúdo	9

9 Paralelismo lógico e regra de entrega	9

10 Checkpoint humano	10

11 Cancelamento e terminalidade	10

12 Invariantes do modelo	10

13 Evidências de validação do modelo	11

14 Instrução operacional consolidada	11

15 Controle de Revisão	12

Referências	12

## 1 Finalidade, escopo e posição do modelo

Este documento formaliza o workflow de execução documental por IA em estados, transições, gates, retornos e condições de encerramento. Seu objetivo é tornar executáveis, verificáveis e independentes de ferramenta os comportamentos definidos pelo Contrato Operacional vigente.

O modelo se aplica à criação, revisão, correção, materialização e validação de resultados documentais ou textuais quando essas atividades forem executadas por IA ou por arranjos híbridos que adotem o mesmo lifecycle. Ele não define arquitetura de agentes, concorrência técnica, filas, processos de infraestrutura ou implementação proprietária.

| Princípio de modelagem |
| --- |
| O workflow representa dependências e estados lógicos. A implementação pode ser sequencial, paralela, humana, automatizada, assistida por IA ou híbrida, desde que preserve as condições e invariantes aqui definidos. |

### 1.1 Relação com as fontes e independência de implementação

A qualidade e a construção do conteúdo permanecem sob a Diretriz de Qualidade e Construção de Conteúdo Documental Institucional vigente. A materialização e a validação formal do artefato permanecem sob a Diretriz de Padronização Documental Institucional vigente. O Contrato Operacional de Execução Documental por IA vigente define o comportamento operacional que este modelo representa formalmente.

Este documento não duplica integralmente essas regras. Quando o workflow indicar gate de conteúdo, gate formal, verificação de mudança, pesquisa externa, escalonamento ou preservação de evidência, os critérios substantivos correspondentes devem ser obtidos nas fontes aplicáveis.

## 2 Modelo conceitual

A estrutura possui três conceitos: Solicitação, Resultado e Unidade de Execução (UE). A separação é obrigatória porque unidade de trabalho e unidade de entrega não são equivalentes.

| Solicitação /     │ /     ├── Resultado A /     │      ├── UE-01 /     │      ├── UE-02 /     │      └── UE-03 /     │ /     └── Resultado B /            └── UE-04 |
| --- |

### 2.1 Solicitação

Representa a necessidade apresentada pelo solicitante. Pode originar um ou mais Resultados independentes.

### 2.2 Resultado

É a unidade de entrega. Pode ser um DOCX institucional, uma resposta textual, uma análise, uma revisão ou outro produto solicitado. Um Resultado possui um conjunto explícito de UEs das quais depende.

### 2.3 Unidade de Execução — UE

É a menor unidade de trabalho que pode avançar, bloquear, suspender, encerrar sem alteração ou ser cancelada independentemente dentro de um Resultado.

| Regra |
| --- |
| Conclusão de UE não equivale a liberação de Resultado. |

## 3 Regras de concorrência e composição

UEs independentes podem produzir conteúdo, change sets, decisões, evidências ou diagnósticos, mas não devem competir pela mutação simultânea do mesmo estado final do artefato.

| UE-01 — revisão conceitual ─────────┐ /                                       │ / UE-02 — correção ortográfica ─────────┼──► Integração /                                       │ / UE-03 — revisão de referências ───────┘ /                                             │ /                                             ▼ /                                  Conteúdo consolidado único |
| --- |

A alteração do artefato consolidado ocorre depois da integração. Independência lógica não implica execução técnica simultânea.

| Tipo de saída | Exemplo |
| --- | --- |
| Conteúdo | Nova redação de uma seção. |
| Change set | Substituir A por B. |
| Decisão | Preservar determinado conceito. |
| Evidência | Fonte que sustenta uma afirmação. |
| Diagnóstico | Defeito confirmado ou não encontrado. |
| Nenhuma alteração | Premissa alegada não confirmada. |

## 4 Estados da Unidade de Execução

| Código | Estado | Significado |
| --- | --- | --- |
| U0 | IDENTIFICADA | A unidade foi derivada da solicitação e associada a um Resultado. |
| U1 | QUALIFICADA | Escopo, finalidade local, dependências, fontes e condições da unidade são suficientes para execução. |
| U2 | EM_EXECUÇÃO | A atividade está sendo efetivamente realizada. |
| U3 | PRONTA_PARA_INTEGRAÇÃO | A atividade terminou e seu resultado está apto a participar da composição do Resultado. |
| U4 | AGUARDANDO_DECISÃO_OU_INSUMO | A unidade depende de decisão, informação, evidência ou resolução material externa. |
| U5 | ENCERRADA_SEM_ALTERAÇÃO | A unidade foi legitimamente concluída sem necessidade de mudança. |
| U6 | SUSPENSA_POR_CHECKPOINT | A unidade estava em execução e seu avanço foi deliberadamente suspenso porque o Resultado entrou em RH. |
| UC | CANCELADA | A unidade ainda não concluída foi encerrada porque o Resultado correspondente foi cancelado. |

### 4.1 Gate de premissa

Quando a intervenção depender de defeito ou condição alegada, a premissa deve ser verificada antes da modificação. Se não houver premissa a confirmar, U1 segue diretamente a U2 por UT03.

| U1 QUALIFICADA /       │ /       ▼ /  Verificar premissa /       │ /       ├── confirmada ─────────────► U2 EM_EXECUÇÃO /       ├── não confirmada ─────────► U5 ENCERRADA SEM ALTERAÇÃO /       └── não verificável e indispensável ─► U4 AGUARDANDO |
| --- |

### 4.2 Transições da UE

| ID | Origem | Condição | Destino |
| --- | --- | --- | --- |
| UT01 | U0 | Unidade suficientemente qualificada. | U1 |
| UT02 | U0/U1 | Informação indispensável já está ausente antes de a execução substantiva começar. | U4 |
| UT03 | U1 | Não existe premissa prévia a verificar. | U2 |
| UT04 | U1 | Premissa verificável e confirmada. | U2 |
| UT05 | U1 | Premissa verificável e não confirmada. | U5 |
| UT06 | U1 | Premissa indispensável não pode ser verificada. | U4 |
| UT07 | U2 | Execução concluída e resultado local consistente. | U3 |
| UT08 | U2 | Necessidade de decisão ou insumo indispensável surge durante a execução. | U4 |
| UT09 | U4 | Insumo recebido e unidade novamente executável. | U1 ou U2 |
| UT10 | U3 | Integração posterior invalida resultado da UE. | U1 ou U2 |
| UT11 | U2 | Resultado entra em RH durante a execução da UE. | U6 |
| UT12 | U6 | Checkpoint encerrado. | U2 se a qualificação permanecer válida; U1 se houver necessidade de requalificação. |
| UT13 | U0/U1/U2/U4/U6 | Resultado correspondente é cancelado antes da liberação. | UC |

### 4.3 Clarificações de percurso da UE

UT02 é usado quando a ausência do insumo já é conhecida antes da execução substantiva; UT08 quando a necessidade surge durante U2.

UT10 retorna a U2 quando a UE continua suficientemente qualificada e precisa apenas ser refeita; retorna a U1 quando a informação nova exige requalificação.

UT11 aplica-se apenas a UEs efetivamente em U2. UEs em U3, U4 ou U5 mantêm seus estados durante RH.

UT13 não retroage UEs já concluídas em U3 ou U5; esses estados permanecem como registro histórico do trabalho realizado.

## 5 Dependências do Resultado

Cada Resultado possui um conjunto explícito de UEs obrigatórias. Uma UE é considerada resolvida quando chega a U3 PRONTA_PARA_INTEGRAÇÃO ou U5 ENCERRADA_SEM_ALTERAÇÃO. U4, U6 e UC não satisfazem a dependência de um Resultado que ainda pretenda ser liberado em R7.

| required_units = {UE-01, UE-02, UE-03} /  / UE-01 = U3 / UE-02 = U3 / UE-03 = U4 /  / Resultado = R0 — AGUARDANDO_UNIDADES |
| --- |

## 6 Estados do Resultado

| Código | Estado | Significado |
| --- | --- | --- |
| R0 | AGUARDANDO_UNIDADES | Uma ou mais UEs obrigatórias ainda não foram resolvidas. |
| R1 | PRONTO_PARA_INTEGRAÇÃO | Todas as UEs obrigatórias foram resolvidas. |
| R2 | CONTEÚDO_CONSOLIDADO | Os resultados das UEs foram integrados em uma representação semântica única. |
| R3 | CONTEÚDO_VALIDADO | O gate global de conteúdo foi aprovado ou a validade semântica existente foi legitimamente preservada conforme o percurso aplicável. |
| R4 | ARTEFATO_MATERIALIZADO | O artefato requerido foi produzido ou alterado a partir de base semanticamente válida. |
| R5 | ARTEFATO_VALIDADO | O gate formal foi aprovado. |
| R6 | MUDANÇA_VERIFICADA | Quando aplicável, estado anterior/posterior foi comparado e o escopo foi comprovado. |
| R7 | LIBERADO | O Resultado final está apto e foi disponibilizado ao solicitante. |
| RH | CHECKPOINT_HUMANO | A execução do Resultado foi deliberadamente suspensa para avaliação humana intermediária. |
| RC | CANCELADO | O Resultado foi encerrado por decisão explícita de não prosseguir antes da liberação. |

### 6.1 Transições do Resultado

| ID | Origem | Condição | Destino |
| --- | --- | --- | --- |
| RT01 | R0 | Todas as UEs obrigatórias resolvidas. | R1 |
| RT02 | R1 | Integração realizada sem conflito material. | R2 |
| RT03 | R1/R2 | Integração identifica incompatibilidade entre UEs. | Reabre UE(s) afetada(s) e retorna a R0. |
| RT04 | R2 | Gate de conteúdo aprovado. | R3 |
| RT05 | R2 | Falha semântica autonomamente corrigível. | R2 |
| RT06 | R2 | Falha exige decisão ou informação. | Reabre/cria UE obrigatória e retorna a R0. |
| RT07 | R3 | A saída final não requer materialização ou alteração de artefato, inclusive encerramento legítimo sem alteração. | R7 |
| RT08 | R3 | Resultado requer artefato. | R4 |
| RT09 | R4 | Gate formal aprovado. | R5 |
| RT10 | R4 | Defeito exclusivamente formal corrigível. | R4 |
| RT11 | R4 | Materialização revela problema semântico. | R2 |
| RT12 | R5 | Resultado novo, sem estado anterior cuja preservação precise ser comprovada. | R7 |
| RT13 | R5 | Resultado altera objeto existente e exige comprovação de preservação de escopo. | R6 |
| RT14 | R6 | Mudança e preservação comprovadas. | R7 |
| RT15 | R6 | Alteração colateral formal. | R4 |
| RT16 | R6 | Alteração colateral semântica. | R2 |
| RT17 | Qualquer pré-R7 | Checkpoint humano explicitamente solicitado ou exigido. | RH |
| RT18 | RH | Revisão aprovada sem alteração material. | Retorna ao estado suspenso. |
| RT19 | RH | Feedback altera conteúdo. | R2 se nenhuma UE obrigatória for reaberta/criada; R0 se o feedback reabrir ou criar UE obrigatória. |
| RT20 | RH | Feedback altera somente materialização. | R4 |
| RT21 | R1 | Intervenção exclusivamente formal sobre base semanticamente válida; nenhuma UE introduziu alteração semântica. | R4 |
| RT22 | Qualquer pré-R7 | Cancelamento válido e definitivo do Resultado. | RC |

### 6.2 Clarificações de escolha e retorno

RT12 aplica-se quando não existe estado anterior que precise ser preservado por comparação material; RT13 aplica-se quando o Resultado é uma alteração de objeto existente e a preservação do escopo deve ser comprovada.

RT07 não converte artificialmente um Resultado documental em textual; ele reconhece que, quando nenhuma alteração do artefato é necessária, a saída final válida é a comunicação consolidada e validada dessa conclusão.

RT19 possui dois destinos explicitamente condicionados: R2 quando o feedback puder ser incorporado ao conteúdo consolidado sem reabrir ou criar UE obrigatória; R0 quando o feedback reabrir ou criar UE obrigatória, tornando o Resultado novamente incompleto.

RT21 não equivale a ignorar qualidade semântica. Ele só existe quando a validade semântica prévia permanece aplicável e o escopo atual continua exclusivamente formal. Se impacto semântico for descoberto ainda durante U2, a UE não deve concluir como exclusivamente formal; deve seguir o tratamento de decisão/insumo e, após resolução, o Resultado percorre RT02 até R2.

RT22 só se aplica antes de R7. Depois de R7, eventual revogação, substituição ou desfazimento constitui nova Solicitação.

## 7 Fluxos principais

### 7.1 Criação documental

| R0 → R1 → R2 → R3 → R4 → R5 → R7 /                          └─ quando alteração existente exigir comparação: R5 → R6 → R7 |
| --- |

### 7.2 Resultado exclusivamente textual

| R0 → R1 → R2 → R3 → R7 |
| --- |

### 7.3 Intervenção exclusivamente formal

| R0 → R1 ──RT21──► R4 → R5 → R6 → R7 /  / Pré-condições: base semanticamente válida; escopo exclusivamente formal; nenhuma UE introduziu alteração semântica. |
| --- |

### 7.4 Encerramento legítimo sem alteração

| UE obrigatória → U5 / Resultado: R0 → R1 → R2 → R3 → R7 /  / Saída final: comunicação de que a intervenção era desnecessária. |
| --- |

### 7.5 Checkpoint humano

| Resultado pré-R7 ──RT17──► RH / UE em U2 ──UT11──► U6 /  / Retorno sem alteração material: RH → estado suspenso; U6 → U2 ou U1 via UT12 / Feedback que altera conteúdo sem reabrir UE obrigatória: RH → R2 / Feedback que reabre/cria UE obrigatória: RH → R0 / Feedback apenas formal: RH → R4 |
| --- |

### 7.6 Cancelamento

| Qualquer Resultado pré-R7 ──RT22──► RC / UEs não concluídas: U0/U1/U2/U4/U6 ──UT13──► UC / UEs já U3/U5 permanecem como registro histórico. / Nenhum gate posterior é executado. |
| --- |

## 8 Integração e gate global de conteúdo

Duas UEs podem estar localmente corretas e produzir uma combinação incompatível. A integração verifica incompatibilidades entre change sets, alterações sobrepostas, decisões contraditórias, terminologia divergente, perda de conteúdo e precedência indevida.

| Regra |
| --- |
| Resultado local válido não implica composição global válida. |

O gate institucional de conteúdo ocorre sobre o Resultado consolidado, não sobre UEs isoladas. UEs podem executar validação local suficiente para chegar a U3, mas coerência global, progressão, redundância, navegabilidade, proporcionalidade e consistência terminológica são avaliadas após a integração.

## 9 Paralelismo lógico e regra de entrega

Independência de UEs não obriga execução simultânea. A implementação pode executar UEs em paralelo, sequencialmente, em lotes, por agentes diferentes ou pelo mesmo agente. O workflow modela dependência lógica, não infraestrutura concorrente.

| Regra de entrega |
| --- |
| Um Resultado somente é entregue como resultado final quando alcança R7 — LIBERADO. |

| Situação | Entrega final? |
| --- | --- |
| UE em U3 | Não. |
| Várias UEs concluídas | Não. |
| Artefato intermediário de processamento | Não. |
| Resultado em RH | Não. |
| Resultado em RC | Não. |
| Resultado em R7 | Sim. |

Resultados independentes podem alcançar R7 em momentos diferentes sem que isso configure liberação parcial de um mesmo Resultado.

## 10 Checkpoint humano

RH é excepcional e deliberado. Ao entrar em RH, o Resultado deixa de avançar. UEs em U2 passam para U6. UEs já concluídas ou já bloqueadas mantêm seus estados.

| Estado da UE ao entrar em RH | Tratamento |
| --- | --- |
| U2 | UT11 → U6. |
| U3 | Permanece U3. |
| U4 | Permanece U4. |
| U5 | Permanece U5. |
| U0/U1 | Não avançam enquanto o Resultado permanecer em RH. |

No retorno do checkpoint, U6 volta a U2 quando pode simplesmente continuar, ou a U1 quando o feedback altera premissas e exige requalificação. Quando feedback reabre ou cria UE obrigatória, o Resultado retorna explicitamente a R0.

## 11 Cancelamento e terminalidade

Cancelamento é semanticamente distinto de conclusão, ausência de alteração e checkpoint. RC representa encerramento definitivo do Resultado antes da liberação.

| Situação | Efeito |
| --- | --- |
| Resultado pré-R7 | RT22 → RC. |
| UE em U0/U1/U2/U4/U6 | UT13 → UC. |
| UE em U3/U5 | Permanece em seu estado como registro histórico. |
| Artefato intermediário | Não é liberado como resultado final. |
| Resultado já em R7 | Não pode voltar a RC; qualquer desfazimento constitui nova Solicitação. |

## 12 Invariantes do modelo

| ID | Regra |
| --- | --- |
| INV-01 | Toda UE pertence a exatamente um Resultado. |
| INV-02 | Conclusão de UE não representa, por si só, entrega ao usuário. |
| INV-03 | Paralelismo de UEs não autoriza concorrência descontrolada sobre o estado final do artefato. |
| INV-04 | Resultado só avança para integração quando todas as UEs obrigatórias estiverem resolvidas em U3 ou U5. |
| INV-05 | Resultados das UEs são integrados antes do gate global de conteúdo, salvo o bypass formal explícito de RT21. |
| INV-06 | Validade local de todas as UEs não implica validade da composição. |
| INV-07 | Gate global de conteúdo ocorre sobre o Resultado consolidado. |
| INV-08 | Materialização final parte de conteúdo consolidado e validado, salvo intervenção exclusivamente formal sobre base semanticamente válida via RT21. |
| INV-09 | Artefato não é liberado antes do gate formal quando materialização for aplicável. |
| INV-10 | Alterações restritas não são liberadas sem comprovação de preservação quando aplicável. |
| INV-11 | Uma UE bloqueada impede apenas os Resultados que dependem dela. |
| INV-12 | Resultado incompleto não é entregue como final. |
| INV-13 | Checkpoint humano suspende o avanço do Resultado; UEs em execução assumem U6 enquanto o checkpoint permanecer aberto. |
| INV-14 | Artefatos intermediários não constituem entregas por padrão. |
| INV-15 | Premissa não confirmada pode encerrar uma UE em U5 e produzir Resultado liberável sem alteração de artefato via RT07. |
| INV-16 | Cancelamento pré-R7 encerra o Resultado em RC; não equivale a R7 e não libera artefatos intermediários. |
| INV-17 | Cancelamento não reescreve o histórico de UEs já concluídas em U3 ou U5. |
| INV-18 | Depois de R7, cancelamento não é retroativo; desfazimento ou revogação exige nova Solicitação. |

## 13 Evidências de validação do modelo

A arquitetura UE → Resultado → Integração foi submetida a bateria estrutural na proposta v0.2, que identificou lacunas de encerramento sem alteração, bypass formal, suspensão durante checkpoint e cancelamento. A proposta v0.3 incorporou essas correções e foi submetida a bateria de regressão dirigida.

A regressão da v0.3 exercitou U6, UC, RC, RT21, UT11, UT12, UT13, RT22 e a semântica ampliada de RT07. O reteste dirigido do falso bypass formal confirmou que impacto semântico descoberto ainda em U2 impede RT21: a UE segue por UT08 para U4 quando surge decisão ou insumo indispensável; após resolução e eventual requalificação, o Resultado percorre o caminho ordinário por RT02 até R2 e novo gate de conteúdo.

A única ambiguidade formal remanescente identificada na bateria dizia respeito ao destino de RT19 quando feedback em RH reabria ou criava UE obrigatória. Esta versão 0.4 torna o destino explícito: R2 sem reabertura/criação de UE obrigatória; R0 quando houver reabertura ou criação de UE obrigatória.

| Critério de estabilização |
| --- |
| A versão 0.4 não introduz nova capacidade estrutural. Ela consolida o modelo validado e elimina a ambiguidade tabular de RT19. |

## 14 Instrução operacional consolidada

Ao aplicar este workflow, decomponha a Solicitação em Resultados e UEs apenas no grau necessário; qualifique e execute cada UE conforme suas dependências; preserve bloqueios e checkpoints localizados; integre UEs resolvidas antes do gate global de conteúdo; reutilize validade semântica anterior somente quando RT21 for legitimamente aplicável; materialize e valide artefatos conforme a diretriz vigente; verifique preservação de escopo quando aplicável; libere somente Resultados em R7; e encerre cancelamentos pré-R7 em RC sem liberar artefatos intermediários. Não invente estados ou transições para acomodar casos não cobertos: quando houver lacuna material, trate-a como necessidade de evolução do modelo ou como regra específica fora deste workflow.

## 15 Controle de Revisão

| Versão | Data | Descrição |
| --- | --- | --- |
| 0.2 | 22/09/2026 | Separação entre Unidade de Execução e Resultado; formalização da integração, gates globais, checkpoint humano e regra de entrega. |
| 0.3 | 23/09/2026 | Inclusão de encerramento sem alteração, bypass formal, suspensão de UE durante checkpoint e cancelamento; clarificações de bifurcações identificadas na bateria estrutural. |
| 0.4 | 24/09/2026 | Estabilização do modelo após regressão dirigida; explicitação do destino de RT19 para R2 ou R0 conforme reabertura/criação de UE obrigatória; incorporação do reteste do falso bypass formal; institucionalização da especificação. |

Referências

MUNZLINGER, Johann. Diretriz de Qualidade e Construção de Conteúdo Documental Institucional. Versão 1.0. Documento interno, 2026.

MUNZLINGER, Johann. Diretriz de Padronização Documental Institucional. Versão 3.0. Documento interno, 2026.

MUNZLINGER, Johann. Contrato Operacional de Execução Documental por IA. Versão 0.3. Especificação operacional interna de trabalho, 2026.

MUNZLINGER, Johann. Modelo Formal do Workflow de Execução Documental por IA. Proposta v0.3. Documento auxiliar não institucional para validação e testes, 2026.

MUNZLINGER, Johann. Relatório Consolidado da Bateria de Regressão Estrutural — Modelo Formal v0.3. Versão 1.0. Documento interno, 2026.
