# Governança Documental Institucional — Agent Skill

Distribuição **estável** de uma Skill institucional reutilizável em diferentes projetos e conversas da mesma organização, sem dependência das Diretrizes de Atuação de um projeto específico.

> **Status:** `1.0.0` — primeira distribuição estável após H00–H07 e regressão estática dos pacotes. O H07 fornece evidência de acionamento sem `@` no ambiente testado (resultado compatível com a Skill e indicação visual apresentada pelo usuário), sem rastreamento interno do host. A instalação, seleção automática e capacidades técnicas podem variar conforme o ambiente; a aprovação não significa interoperabilidade universal.

## Conteúdo

- `skills/governanca-documental-institucional/SKILL.md`: ponto de entrada da Skill, com gatilhos e workflow.
- `skills/governanca-documental-institucional/references/normativas/`: quatro DOCX canônicos **sem alteração de conteúdo**.
- `skills/governanca-documental-institucional/references/consulta/`: transcrições textuais de apoio geradas automaticamente, sem autoridade normativa independente.
- `skills/governanca-documental-institucional/scripts/`: geração/checagem das transcrições, integridade da distribuição e auditoria OOXML auxiliar.
- `manifest.json`: combinação exata de fontes, hashes SHA-256 e estado do release.
- `tests/`: cenários para homologação funcional e ambiente de consumo.

## Instalação e consumo

**ChatGPT (workspace habilitado para Skills):** em Plugins > Habilidades, use Criar > Carregar do computador e selecione o pacote da Skill gerado para distribuição. O mecanismo concreto de upload depende da interface disponível. O ZIP independente da Skill é gerado em `dist/` pelo comando abaixo. Instale o ZIP no ChatGPT e confira a disponibilidade da Skill em uma conversa comum, fora de um projeto personalizado; o acionamento explícito por `@` é verificável pelo usuário, enquanto a invocação automática pode não disponibilizar logs diretamente observáveis. Não presumir que publicar no GitHub instala ou atualiza uma Skill no workspace.

**Agentes que implementam Agent Skills:** utilize o diretório `skills/governanca-documental-institucional/`, respeitando a convenção `SKILL.md`; a descoberta do diretório depende do host. Não afirme suporte para um host sem efetuar teste nele.

## Repositório GitHub institucional

O repositório deve permanecer **privado na organização**, salvo decisão institucional expressa de publicação. Recomenda-se branch protection, revisão por pull request e releases marcadas (por exemplo `v1.0.0` após homologação). GitHub é a fonte canônica de **código e distribuição da Skill**, não substitui a autoridade normativa dos DOCX empacotados.

As versões de cada norma são independentes da versão da Skill. Alterar qualquer DOCX exige revisar a transcrição derivada, atualizar o manifesto e homologar novamente os cenários afetados. Não acrescente versões históricas à pasta `references/normativas/` de uma mesma distribuição.

## Evidências de homologação

O relatório resumido dos casos H00–H07 está em `tests/HOMOLOGACAO.md`. Os resultados foram observados em uma instalação específica; devem ser repetidos quando houver mudanças relevantes nas normas, scripts, Skill ou ambiente consumidor.

## Empacotamento determinístico

A partir da raiz do repositório, após qualquer alteração de conteúdo ou fontes:

```bash
python scripts/build_release.py
```

Serão criados dois arquivos em `dist/`: o ZIP completo do repositório (destinado ao GitHub) e o ZIP contendo somente o diretório da Skill (destinado à instalação). O script só empacota depois de confirmar integridade das fontes e executar os testes estáticos. Os ZIPs ainda não provam aceitação pela interface do ChatGPT.

## Validação local

Na raiz do diretório da Skill:

```bash
python scripts/sync_sources.py --check
python scripts/verify_package.py
# Para verificar a conformidade do diretório de DISTRIBUIÇÃO com a especificação:
python scripts/verify_package.py --strict-dir-name
python scripts/audit_docx.py caminho/do/documento.docx
```

No repositório completo, a CI usa a validação estrita do nome de diretório e executa testes de portabilidade, integridade e smoke test do auditor. Ao instalar a Skill, caso o host renomeie a pasta, o verificador emitirá aviso em vez de reprovar fontes íntegras; a Skill distribuída continua obedecendo à convenção oficial de nomes. **Essas validações estáticas não substituem os testes de geração e Word para Web.**

## Dependências e direitos de uso

Os scripts empacotados utilizam somente a biblioteca padrão do Python 3.10+. A execução de documentos institucionais completos depende de capacidades disponíveis no ambiente consumidor para leitura, edição, renderização e inspeção DOCX.

As fontes são documentos institucionais internos; este pacote **não concede licença pública** ou permissão de redistribuição externa. Autoria, titularidade e política de acesso permanecem sob a organização.
