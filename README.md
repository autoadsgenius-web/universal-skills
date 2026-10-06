# Universal Skills

**Uma skill para coordenar desenvolvimento, conteúdo e mídia no Codex e no Claude Code.** Você informa o resultado desejado; ela consulta o catálogo, escolhe os módulos e orienta o agente a executar e conferir o trabalho. Os guias são carregados conforme a tarefa.

## Para que serve

| Área | Exemplos |
|---|---|
| Sites | Páginas, lojas, painéis, componentes e interfaces responsivas |
| Aplicativos | Expo, React Native, Flutter, Kotlin e Swift |
| Programas e serviços | Python, TypeScript, Java, C#, Go, Rust, APIs e bancos |
| Jogos e extensões | Unity, jogos, extensões de navegador e aplicativos desktop |
| Qualidade | Arquitetura, planejamento, investigação de erros, revisão e testes |
| Escrita e marketing | Encaminhamento para roteiros, revisão, posts, pesquisa e calendário |
| Mídia | Encaminhamento para habilidades de imagens, áudio, vídeo e animação |

## O que vem no pacote

- **115 módulos incorporados de desenvolvimento**, com guias e recursos disponíveis nas fontes originais.
- **329 registros de integração** das habilidades e plugins identificados no ambiente de origem.
- Uma entrada `SKILL.md`, catálogo pesquisável e instalador Python.

São **444 registros**, com sobreposições; não são 444 habilidades únicas. Um registro `bundled` contém o guia. Um registro `adapter` é uma dependência: **não contém as instruções originais nem instala o plugin**. As habilidades de escrita, marketing e mídia estão representadas por adaptadores nesta edição pública. Consulte o [catálogo completo](references/CATALOG.md).

## Requisitos

Tenha Codex ou Claude Code instalado e com acesso a um modelo, e Python **3.10 ou superior** para executar os scripts. Git é opcional. O pacote não fornece assinatura, créditos, credenciais, hospedagem ou ferramentas de geração; cada serviço tem seus próprios planos e limites.

## Baixar

Na página deste repositório no GitHub, clique em **Code → Download ZIP** e extraia o arquivo. Abra um terminal na pasta extraída que contém este README.

Alternativamente, use Git:

```sh
git clone https://github.com/autoadsgenius-web/universal-skills.git universal-skills
cd universal-skills
```

## Instalar no Windows

Na pasta baixada, clique com o botão direito e escolha **Abrir no Terminal**. No PowerShell:

```powershell
py -3 --version
py -3 scripts/install.py --target both
```

Para instalar somente no Codex, troque `both` por `codex`; somente no Claude Code, use `claude`. Se `py` não existir, confira a instalação do Python; se `python --version` mostrar 3.10 ou superior, use `python` no lugar de `py -3`.

## Instalar no macOS ou Linux

No terminal, entre na pasta baixada:

```sh
python3 --version
python3 scripts/install.py --target both
```

Use `--target codex` ou `--target claude` para instalar em apenas uma plataforma.

## Onde fica instalada

| Plataforma | Para seu usuário | Para um projeto |
|---|---|---|
| Codex | `~/.agents/skills/universal-skills/` | `SEU_PROJETO/.agents/skills/universal-skills/` |
| Claude Code | `~/.claude/skills/universal-skills/` | `SEU_PROJETO/.claude/skills/universal-skills/` |

`~` é sua pasta de usuário. No Windows, costuma corresponder a `C:\Users\SEU_USUARIO`. O instalador usa a pasta reconhecida pelo Python.

Para instalar apenas em um projeto, informe a pasta pai das skills. Exemplo no Windows:

```powershell
py -3 scripts/install.py --target codex --dest "C:\Projetos\MeuApp\.agents\skills"
py -3 scripts/install.py --target claude --dest "C:\Projetos\MeuApp\.claude\skills"
```

Exemplo no macOS ou Linux:

```sh
python3 scripts/install.py --target codex --dest /caminho/MeuApp/.agents/skills
python3 scripts/install.py --target claude --dest /caminho/MeuApp/.claude/skills
```

No WSL, execute a instalação dentro do WSL se o agente também rodar nele. Instalar no Windows não instala automaticamente no usuário Linux do WSL.

## Usar no Codex

Abra uma nova sessão no projeto desejado e escreva:

```text
Use $universal-skills para criar uma página responsiva para uma escola.
Use React, implemente o projeto e explique como executar e conferir o resultado.
```

```text
Use $universal-skills para investigar o erro de login deste projeto.
Leia o código, corrija a causa e execute as verificações disponíveis.
```

Copiar os arquivos na sua máquina não instala a skill em sessões remotas do ChatGPT. Ambientes remotos ou administrados podem exigir instalação própria.

## Usar no Claude Code

Abra uma nova sessão e digite:

```text
/universal-skills Crie um app de lista de tarefas com Expo.
Inclua criação, edição e conclusão de tarefas e explique como testar.
```

Também pode pedir: `Use universal-skills para revisar esta API Python.`

Esta instalação é para Claude Code. Ela não habilita automaticamente a skill no site claude.ai, no Cowork ou em rotinas na nuvem; essas interfaces têm formas próprias de habilitar habilidades.

## Exemplos de conteúdo e mídia

```text
Use universal-skills para revisar meu roteiro, preservando os fatos e minha maneira de falar.
Confira se há uma habilidade de humanização instalada. Se não houver, informe a dependência.
```

```text
Use universal-skills para planejar um vídeo de anime de 60 segundos.
Confira as ferramentas disponíveis, prepare as cenas e gere apenas o que puder executar.
```

Instalar esta skill não dá acesso automático a Canva, Runway, PixVerse, Supabase, Vercel ou outros serviços. O agente confere o plugin, a conta e as permissões necessárias.

## Conferir e consultar

O instalador imprime o caminho de cada instalação. Confira se existe `SKILL.md` nessa pasta, abra uma nova sessão e invoque a skill pelo nome.

Na pasta baixada, consulte o catálogo:

```sh
python3 scripts/catalog.py react
python3 scripts/catalog.py flutter
python3 scripts/catalog.py humanizer
```

No Windows, use `py -3` no lugar de `python3`. A busca consulta nomes e descrições, que podem estar em inglês. Várias palavras mostram correspondências com pelo menos uma delas.

## Atualizar ou remover

O instalador recusa sobrescrever uma instalação existente. Para atualizar: feche o agente, faça backup da pasta instalada, remova apenas a pasta `universal-skills` antiga e execute o instalador da nova versão. Se usa Git, obtenha a nova versão com `git pull` no clone primeiro. Atualizar o clone não atualiza a cópia instalada.

Para desinstalar, remova apenas a pasta `universal-skills` no destino usado e abra uma nova sessão. Preserve as outras skills.

## Problemas comuns

| Problema | O que conferir |
|---|---|
| Python não encontrado | Instalação do Python e comando usado |
| Script não encontrado | Terminal aberto na pasta que contém este README |
| Instalação já existe | Backup e passos de atualização |
| Skill não aparece | Destino, arquivo `SKILL.md` e nova sessão |
| Serviço indisponível | Plugin, conta e permissões |
| Código precisa de pacotes | Dependências do projeto; o instalador da skill não as instala |
| Guia menciona outro módulo | Catálogo e fonte original; referências podem usar a organização original |

## Limites e validação

O instalador e o catálogo foram verificados em Linux com destinos temporários para Codex e Claude. Isso não equivale a testar cada framework, provedor ou interface de agente. Os comandos de Windows usam os mesmos scripts Python, mas não foram executados em Windows nesta preparação.

Uma skill orienta o agente; não garante correção nem substitui revisão. Scripts de terceiros devem ser inspecionados antes de executar. O agente deve respeitar as permissões do ambiente e conferir o resultado antes de informar sucesso.

## Créditos, licenças e fontes

Veja [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Os módulos de terceiros mantêm suas próprias licenças. A licença da camada de coordenação não relicencia os módulos. Os adaptadores não redistribuem instruções sem permissão confirmada.

- [Documentação oficial de skills no Codex](https://learn.chatgpt.com/docs/build-skills)
- [Diretórios de personalização do Codex](https://learn.chatgpt.com/docs/customization/overview)
- [Documentação oficial de skills no Claude Code](https://code.claude.com/docs/en/skills)

## Contribuir

Abra uma issue com objetivo, plataforma, erro e passos para reproduzir. Não envie senhas, tokens ou dados pessoais. Para novos módulos, informe a fonte e a licença e preserve os créditos. Para alterações nos scripts, inclua uma verificação do comportamento esperado.
