---
name: governanca-documental-institucional
description: "Cria, revisa, corrige, materializa e valida documentos institucionais conforme a Governança Documental da organização, incluindo DOCX, estrutura OOXML, sumário, títulos, controle de revisão e gates. Use para documentos formais institucionais e suas revisões; não institucionalize anotações pessoais, rascunhos descartáveis ou análises técnicas não documentais."
metadata:
  version: "1.0.0"
  scope: "mesma-organizacao"
---

# Governança Documental Institucional

## Finalidade e fronteira

Esta Skill ativa a Governança Documental da organização em **qualquer conversa ou projeto que disponha dela**, sem depender de instruções de um projeto específico, de um tópico, de uma pessoa, de um modelo ou de uma ferramenta específica. A Skill é um mecanismo de execução, **não é uma quinta fonte normativa**.

**Acionar** para criação, edição, revisão, regeneração, materialização ou validação de **resultados documentais institucionais**. A natureza institucional decorre de finalidade, público e contexto, não da extensão do arquivo. **Não impor** capa, controle de revisão, referências ou outros requisitos institucionais a arquivos pessoais, temporários e descartáveis sem caráter institucional. Perguntas técnicas comuns não acionam por si só esse fluxo.

## Fontes obrigatórias e autoridade

Consulte as versões empacotadas abaixo, conforme suas responsabilidades, **antes de executar a parte documental afetada**:

1. **Qualidade e Construção de Conteúdo Documental Institucional** — construção e gate semântico: `references/normativas/Diretriz_Qualidade_Construcao_Conteudo_Documental_Institucional_v1.2.docx`.
2. **Padronização Documental Institucional** — DOCX, apresentação, estilos, títulos, sumário, OOXML e gate formal: `references/normativas/Diretriz_Padronizacao_Documental_Institucional_v3.4.docx`.
3. **Contrato Operacional de Execução Documental por IA** — classificação de fontes, autonomia, evidências, correções, gates e liberação: `references/normativas/Contrato_Operacional_Execucao_Documental_por_IA_v0.7.docx`.
4. **Modelo Formal do Workflow de Execução Documental por IA** — Solicitação, Resultados, UEs, estados, dependências, bloqueios e transições: `references/normativas/Modelo_Formal_Workflow_Execucao_Documental_IA_v0.4.docx`.

Esses **DOCX originais são canônicos**. Para leitura por agentes, `references/consulta/*.md` contém transcrições de texto **derivadas**, sem autoridade independente, geradas de forma determinística. Se um detalhe depender de tabela, diagrama, estilo, formatação ou conflito entre representações, consulte o DOCX e não conclua pela transcrição isolada. Use `python scripts/sync_sources.py --check` quando o runtime permitir verificar correspondência. Em caso de divergência material entre arquivos do pacote, **não escolha silenciosamente uma variante**.

Outras normas, templates, decisões e fontes específicas vigentes podem prevalecer em seu escopo. Não presuma conteúdos específicos que não tenham sido disponibilizados. Se uma fonte materialmente necessária não estiver acessível, bloqueie somente a parte dependente; resultados independentes podem prosseguir.

## Workflow de execução

1. **Classificar** a natureza de cada Resultado separadamente: institucional, auxiliar não institucional ou outro; determinar finalidade, público, escopo, contexto, premissas e fontes específicas pertinentes. Não confundir formato DOCX com natureza institucional.
2. **Qualificar a evidência e as decisões**: distinguir fatos informados, fontes verificadas, hipóteses, inferências, decisões vigentes e recomendações. Não inventar dados, autoridade, papéis, aprovação ou regra institucional.
3. **Verificar premissas de revisão**: confirmar defeitos objetivamente verificáveis no artefato original antes de intervir. Se a condição não existir, concluir sem alteração legítima. Se o artefato necessário não estiver disponível em forma adequada à tarefa, explicitar impedimento, sem reconstruí-lo de memória.
4. **Produzir e integrar conteúdo** conforme a Diretriz de Qualidade, preservando coesão, proporção, proveniência e hierarquia. Integrar as UEs antes do gate global de conteúdo; respeitar os estados e bloqueios do Modelo Formal. **Não** liberar um Resultado parcial sob rótulo de final.
5. **Aplicar gate semântico** ao Resultado consolidado. Em correções exclusivamente formais, reutilizar conteúdo previamente válido apenas sob as condições de bypass do Modelo Formal; se surgir problema semântico, retornar ao gate adequado.
6. **Materializar** DOCX institucional segundo a Padronização e os templates aplicáveis. Usar estilos de títulos efetivos e hierárquicos; priorizar sumário atualizável; bookmarks necessários são permitidos se não prejudicarem navegação e integridade OOXML.
7. **Executar gate formal**: verificar tanto representação visual em todas as páginas quanto estrutura interna do DOCX, incluindo `w:pPr` antes dos elementos de conteúdo, títulos/níveis, âncoras/hyperlinks, campos de sumário, tabelas e paginação. Se houver ferramenta de inspeção disponível, usar `scripts/audit_docx.py` como **auxílio técnico**, jamais como substituto do gate integral das normas. A verificação com Word para Web ou ambiente equivalente deve ocorrer quando esse for um ambiente relevante e houver acesso; se impossível, declarar limitação, sem alegar compatibilidade testada.
8. **Revisões restritas**: comparar antes/depois quanto a conteúdo, decisões, estilo, partes estruturais e elementos não abrangidos; aplicar mínima correção suficiente. Defeito introduzido exige novo gate.
9. **Liberar somente Resultados válidos** conforme o Modelo Formal. Declarar separadamente ações pretendidas, executadas e efetivamente verificadas. Documentar pendências, limitações e versões das fontes efetivamente utilizadas; não declarar conformidade integral sem evidência.

## Capacidades e limites de execução

- Use as ferramentas efetivamente disponíveis para leitura, edição, renderização e inspeção. **Não invente** ferramentas, evidências ou execução no Word para Web.
- Se não conseguir ler um DOCX requerido, materializar ou renderizar/inspecionar um artefato obrigatório, não libere a parte afetada como conforme. Entregas independentes podem avançar de acordo com o Modelo Formal.
- O código de auditoria do pacote realiza verificações **parciais** de OOXML, não valida conteúdo semântico, identidade visual inteira, interoperabilidade real nem substitui a inspeção das páginas.
- Para preparar ou revisar esta distribuição, execute `python scripts/verify_package.py`, a partir da raiz da Skill, quando Python estiver disponível. A versão e os hashes da combinação homologada encontram-se em `../../manifest.json` no repositório; releases podem ser empacotadas com `manifest.json` junto à Skill.

## Casos-limite

- **DOCX auxiliar para reunião pessoal:** produzir arquivo simples; não aplicar automaticamente capa/sumário/controle institucional.
- **Dois DOCX, um institucional e outro pessoal:** classificar e validar cada Resultado por sua própria natureza.
- **Template obrigatório ausente ou decisão humana material indisponível:** manter bloqueio localizado; não substituir por preferência própria.
- **Bookmarks `secXX`/sumário:** preservar apenas âncoras necessárias e validamente estruturadas; não deixar identificadores técnicos substituírem os títulos no leitor.
- **Pedido de revisão sem defeito comprovado:** responder que nenhuma alteração era necessária, preservando o artefato.
