# Governança Documental Institucional — Agent Skill

Skill institucional na versão **estável 1.0.0**, com distribuição pública deste pacote expressamente autorizada, reutilizável em diferentes projetos e conversas da mesma organização, sem dependência das Diretrizes de Atuação de um projeto específico.

> **Status:** `1.0.0` — primeira distribuição estável após H00–H07 e regressão estática dos pacotes. O H07 fornece evidência de acionamento sem `@` no ambiente testado (resultado compatível com a Skill e indicação visual apresentada pelo usuário), sem rastreamento interno do host. A instalação, seleção automática e capacidades técnicas podem variar conforme o ambiente; a aprovação não significa interoperabilidade universal.

## Conteúdo

- `skills/governanca-documental-institucional/SKILL.md`: ponto de entrada da Skill, com gatilhos e workflow.
- `skills/governanca-documental-institucional/references/normativas/`: quatro DOCX canônicos **sem alteração de conteúdo**.
- `skills/governanca-documental-institucional/references/consulta/`: transcrições textuais de apoio geradas automaticamente, sem autoridade normativa independente.
- `skills/governanca-documental-institucional/scripts/`: geração/checagem das transcrições, integridade da distribuição e auditoria OOXML auxiliar.
- `manifest.json`: combinação exata de fontes, hashes SHA-256 e estado do release.
- `tests/`: cenários para homologação funcional e ambiente de consumo.

## Instalação e consumo

**Ambiente efetivamente testado:** ChatGPT Plus, utilizando Work, no ambiente registrado na homologação H00–H07. A disponibilidade da instalação não foi comprovada para todos os usuários Plus, contas, regiões, interfaces ou ambientes. Contas individuais não implicam disponibilidade universal de Skills. Não há homologação de interoperabilidade com outras plataformas de IA.

1. Obtenha o asset instalável `governanca-documental-institucional-v1.0.0.zip` na release oficial `v1.0.0` do [repositório canônico](https://github.com/johanngf/skill_governanca_documental/releases). Não use o arquivo automático **Source code (zip)** como pacote de instalação.
2. No ambiente ChatGPT Plus com Work habilitado para Skills, o fluxo documentado é **Plugins > Habilidades > Criar > Carregar do computador**; selecione o ZIP instalável. A interface e a disponibilidade do mecanismo podem variar. Caso o recurso não esteja disponível na conta, a instalação não pode ser presumida como suportada.
3. Confira a disponibilidade da Skill em uma conversa comum, fora de projeto personalizado. O acionamento explícito por `@` é verificável pelo usuário; a invocação automática pode não disponibilizar logs diretamente observáveis.

Publicar uma release no GitHub não instala nem atualiza a Skill nas contas dos usuários. As capacidades técnicas do host para leitura, edição, renderização e inspeção de DOCX continuam condicionando a execução.

**Outros hosts:** o diretório segue a convenção `skills/governanca-documental-institucional/SKILL.md`, mas isso, isoladamente, não comprova instalação ou funcionamento em outros agentes. A descoberta do diretório depende do host e requer homologação específica.

## Repositório canônico e distribuição pública autorizada

O repositório canônico é [johanngf/skill_governanca_documental](https://github.com/johanngf/skill_governanca_documental). A publicação pública do pacote atual **1.0.0**, incluindo as quatro fontes normativas DOCX e suas transcrições derivadas, foi expressamente autorizada. Essa decisão substitui a orientação anterior de manter esta distribuição privada e **não se estende automaticamente a conteúdos ou versões futuras**.

GitHub é a fonte canônica de **versionamento e distribuição da Skill**; os pacotes instaláveis oficiais são os assets de **GitHub Releases**. A autoridade normativa permanece nos DOCX empacotados. As transcrições Markdown não possuem autoridade normativa independente. O campo `distribution_scope: internal-single-organization` do manifesto preservado descreve o escopo de aplicação institucional, sem conceder licença irrestrita nem impedir a publicação autorizada desta versão.

O pacote instalável da versão 1.0.0 é `governanca-documental-institucional-v1.0.0.zip`. O status `release_status: stable` registra a qualificação do pacote, **não comprova que a release foi publicada**. A disponibilidade deve ser conferida na página de releases; a preparação local e a publicação no GitHub são etapas distintas.

Releases publicadas devem ser tratadas como imutáveis. Habilite **Settings > Releases > Enable release immutability** antes da publicação definitiva; prepare a release como rascunho, anexe e revise o ZIP validado e só então publique. Não substitua assets ou mova a tag de uma release publicada. Correções posteriores devem gerar nova versão semântica, com homologação proporcional. Para integração com o portal, utilize o asset versionado, sem endereço `latest`.

As versões de cada norma são independentes da versão da Skill. Alterar qualquer DOCX exige revisar a transcrição derivada, atualizar o manifesto e homologar novamente os cenários afetados. Não acrescente versões históricas à pasta `references/normativas/` de uma mesma distribuição.

## Evidências de homologação

O relatório resumido dos casos H00–H07 está em `tests/HOMOLOGACAO.md`. Os resultados foram observados em uma instalação específica; devem ser repetidos quando houver mudanças relevantes nas normas, scripts, Skill ou ambiente consumidor.

## Empacotamento determinístico

A partir da raiz do repositório, após qualquer alteração de conteúdo ou fontes:

```bash
python scripts/build_release.py
```

Serão criados dois arquivos em `dist/`: o ZIP completo do repositório (cópia auxiliar, sem necessidade de anexá-lo à release) e o ZIP contendo somente o diretório da Skill (asset oficial destinado à instalação). O script só empacota depois de confirmar integridade das fontes e executar os testes estáticos. Os ZIPs ainda não provam aceitação pela interface do ChatGPT.

## Validação local

Na raiz do diretório da Skill:

```bash
python scripts/sync_sources.py --check
python scripts/verify_package.py
# Para verificar a conformidade do diretório de DISTRIBUIÇÃO com a especificação:
python scripts/verify_package.py --strict-dir-name
python scripts/audit_docx.py caminho/do/documento.docx
```

No repositório completo, o script de empacotamento usa a validação estrita do nome de diretório e executa testes de portabilidade, integridade e smoke test do auditor. Ao instalar a Skill, caso o host renomeie a pasta, o verificador emitirá aviso em vez de reprovar fontes íntegras; a Skill distribuída continua obedecendo à convenção oficial de nomes. **Essas validações estáticas não substituem os testes de geração e Word para Web.**

## Dependências e direitos de uso

Os scripts empacotados utilizam somente a biblioteca padrão do Python 3.10+. A execução de documentos institucionais completos depende de capacidades disponíveis no ambiente consumidor para leitura, edição, renderização e inspeção DOCX.

As fontes são documentos institucionais cuja **publicação pública neste pacote 1.0.0 foi expressamente autorizada**. O acesso público ao pacote **não equivale a licença irrestrita de uso, modificação ou redistribuição**, nem autoriza automaticamente divulgar novos materiais ou versões futuras. Autoria, titularidade e demais direitos permanecem sob a organização. Os DOCX continuam sendo as fontes normativas canônicas; as transcrições derivadas servem somente para consulta.
