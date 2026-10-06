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
| Escrita e marketing | Guias próprios de público, roteiros, voz e calendário; integrações adicionais |
| Mídia | Fluxo integrado de narração, cenas animadas, legendas, montagem e publicação |

## O que pode fazer em cada área

### Sites e sistemas web

Pode orientar a criação de páginas de apresentação, sites institucionais, lojas, blogs e painéis. Os módulos abordam componentes, rotas, formulários, busca e atualização de dados, gerenciamento de estado, interfaces responsivas e integração com serviços. Incluem React, Next.js, Vue, Angular, TanStack, CMS, WordPress e Shopify.

Também pode revisar organização visual, acessibilidade e desempenho de uma interface existente. Para WordPress, há guias de plugins, blocos, temas, REST API, ambiente de desenvolvimento e investigação de desempenho. O módulo de Shopify orienta trabalho no ecossistema da plataforma.

**Entregas possíveis:** arquivos de um site, componentes reutilizáveis, configuração de rotas, propostas de integração, correções e instruções para executar o projeto. Publicar na internet depende de acesso ao provedor e das ferramentas disponíveis.

**Exemplo:** “Crie um site para uma escola com apresentação, cursos, formulário de contato e versão para celular. Confira os links e explique como publicar.”

**Módulos incorporados:** `frontend-design`, `web-artifacts-builder`, `react-best-practices`, `web-design-guidelines`, `react-view-transitions`, `deploy-to-vercel`, `vercel-optimize`, `react-expert`, `nextjs-developer`, `vue-expert`, `angular-architect`, `api-designer`, `shopify-expert`, `tanstack-start`, `tanstack-router`, `tanstack-query`, `tanstack-store`, `nextjs`, `payload-cms`, `figma-to-code`, `design-system`, `wordpress-router`, `wp-project-triage`, `wp-plugin-development`, `wp-block-development`, `wp-block-themes`, `wp-rest-api`, `wp-interactivity-api`, `wp-abilities-api`, `wp-wpcli-and-ops`, `wp-performance`, `wp-phpstan`, `wp-playground`, `blueprint`, `wp-env`, `wpds`.

### Aplicativos

Pode orientar aplicativos para Android e iOS com Expo, React Native ou Flutter, além de desenvolvimento com Kotlin e Swift. Os guias cobrem estrutura do projeto, navegação, telas, componentes nativos, animações, consumo de dados e integração entre código web e nativo. Para desktop, há um módulo de Tauri.

Os módulos de Flutter também abordam layouts responsivos, localização, serialização JSON, testes de widgets e testes de integração. Os módulos Expo/EAS tratam de desenvolvimento, builds, atualizações, observação e distribuição, conforme o serviço e suas permissões.

**Entregas possíveis:** código de telas e fluxos, estrutura de aplicativo, integração com API, testes e instruções de build. A publicação em lojas exige contas, configuração, requisitos da loja e possíveis custos; a skill não fornece esses acessos.

**Exemplo:** “Crie um app de agendamento com lista de horários, cadastro e confirmação. Escolha a tecnologia adequada e explique como testar.”

**Módulos incorporados:** `expo-overview`, `expo-project-structure`, `expo-router`, `expo-native-ui`, `expo-ui`, `expo-design-system`, `expo-animation`, `expo-data-fetching`, `expo-web-to-native`, `expo-dom`, `expo-module`, `expo-brownfield`, `expo-dev-client`, `expo-examples`, `expo-app-clip`, `expo-upgrade`, `eas-app-stores`, `eas-hosting`, `eas-workflows`, `eas-update`, `eas-observe`, `eas-update-insights`, `eas-simulator`, `flutter-apply-architecture-best-practices`, `flutter-build-responsive-layout`, `flutter-fix-layout-issues`, `flutter-setup-declarative-routing`, `flutter-use-http-package`, `flutter-implement-json-serialization`, `flutter-setup-localization`, `flutter-add-widget-preview`, `flutter-add-widget-test`, `flutter-add-integration-test`, `react-native-expert`, `flutter-expert`, `kotlin-specialist`, `swift-expert`, `tauri`.

### Programas e serviços

Pode orientar programas, APIs, ferramentas de terminal, serviços com comunicação em tempo real e integrações. Os módulos incluem Python, JavaScript, TypeScript, Java, C#, C++, PHP, Ruby, Go e Rust e frameworks como FastAPI, Django, NestJS, Spring Boot, Laravel, Rails e .NET.

Há módulos de desenho de APIs, GraphQL, WebSockets, servidores MCP e extensões de navegador. Para projetos de IA, há guias de RAG, pipelines de aprendizado de máquina e ajuste de modelos. Um módulo de sistemas embarcados orienta projetos que interagem com hardware.

**Entregas possíveis:** código de um serviço ou programa, definição de endpoints, validações, organização de dados, testes e documentação de execução. Treinamento de modelos e operação de hardware dependem de dados, infraestrutura e dispositivos adequados.

**Exemplo:** “Crie uma API de estoque em Python com cadastro, entrada e saída de produtos, validação de dados e testes.”

**Módulos incorporados:** `mcp-builder`, `composition-patterns`, `python-pro`, `django-expert`, `fastapi-expert`, `javascript-pro`, `typescript-pro`, `nestjs-expert`, `csharp-developer`, `dotnet-core-expert`, `java-architect`, `spring-boot-engineer`, `php-pro`, `laravel-specialist`, `rails-expert`, `golang-pro`, `rust-engineer`, `cpp-pro`, `cli-developer`, `graphql-architect`, `websocket-engineer`, `rag-architect`, `ml-pipeline`, `fine-tuning-expert`, `embedded-systems`, `web-extension`.

### Jogos

Pode orientar desenvolvimento de jogos, organização de cenas, sistemas de interação e uso de motores. Os módulos incluem game-developer, game-engine, unity e figma-to-unity. A combinação depende do motor, da linguagem e do projeto existentes.

Pode ajudar a definir o ciclo do jogo, estados, controles, interface, lógica de pontuação e organização dos recursos. O módulo de integração com Figma orienta a passagem de elementos de interface para o projeto compatível.

**Entregas possíveis:** protótipo, scripts de mecânicas, interfaces e passos de teste. Criar arte, áudio e animações depende de recursos fornecidos ou de ferramentas conectadas. A presença desses guias não instala um motor de jogos.

**Exemplo:** “Crie um protótipo de jogo educativo com perguntas, pontuação e tela de resultado; explique como abrir e testar no motor escolhido.”

**Módulos incorporados:** `game-developer`, `unity`, `figma-to-unity`, `game-engine`.

### Qualidade e manutenção

Pode organizar o planejamento, investigar erros, revisar arquitetura e orientar verificações antes de considerar uma tarefa concluída. Os módulos abordam definição do problema, planos de implementação, execução por etapas, testes, depuração e revisão de código.

Há guias de arquitetura, organização de monorepos, revisão de aplicações completas e testes de interfaces web. Esses módulos podem ser combinados com os de sites, apps, programas e jogos conforme a tarefa.

**Entregas possíveis:** diagnóstico com evidências, plano de correção, alterações no código, testes e relatório do que foi verificado. A skill deve distinguir teste executado, análise do código e comportamento ainda não confirmado.

**Exemplo:** “Investigue por que o login falha após atualizar a página, corrija a causa e execute as verificações relevantes.”

**Módulos incorporados:** `webapp-testing`, `architecture-designer`, `fullstack-guardian`, `monorepo`, `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `requesting-code-review`.

### Escrita e marketing

Esta edição inclui guias próprios para pesquisa de nicho e público, calendário e lotes, roteiro curto e storyboard, voz da escrita, metadados e agendamento. As demais funções desta área permanecem em um **catálogo de integrações**. Ela identifica habilidades de humanização, voz, tom, roteiros, legendas, carrosséis, posts, narrativas, pesquisa de público e planejamento de conteúdo. Os novos guias funcionam dentro da Universal Skills. Para usar instruções originais de outras habilidades do catálogo, elas precisam estar disponíveis.

O catálogo também inclui pesquisa de concorrentes, calendário, campanhas, objetivos, análise de métricas, reaproveitamento de conteúdo e estratégias para Instagram, Facebook, YouTube, TikTok, LinkedIn, Pinterest e outras redes.

**Entregas possíveis com as dependências presentes:** revisão de texto, roteiro, proposta de posts, calendário, planejamento de campanha e análise de dados fornecidos. Pesquisa atual exige fontes; métricas exigem dados reais. Publicação e agendamento dependem de conectores e contas. Não promete viralização nem crescimento garantido.

**Exemplo:** “Revise meu roteiro mantendo os fatos e minha maneira de falar. Confira a habilidade de humanização instalada e mostre a versão final.”

**Consulte os registros desta área** na [distribuição por área](references/CAPABILITIES.md).

### Mídia e animação

Esta edição inclui guias próprios para narração, produção com várias cenas, movimento, legendas, montagem, pré-visualização, exportação e conferência audiovisual. A execução da geração e publicação funciona por **ferramentas externas**. O catálogo identifica habilidades de imagens, edição, narração, música, legendas, cortes, análise de vídeos, animação e composição de cenas. Inclui registros de Remotion, anime e ferramentas de vídeo e design.

Com as dependências presentes, pode coordenar briefing, personagens, referências, cenas, prompts, geração, montagem, legendas e exportação. Anime exige geração e continuidade de personagens; vídeos não são produzidos apenas pela presença de um guia. Os registros de Canva, Runway, Kling, Luma, PixVerse e outros serviços não fornecem acesso a eles.

**Entregas possíveis:** roteiro visual e prompts com as ferramentas básicas; imagens, áudios, cenas animadas ou vídeo final quando houver ferramentas e recursos de execução disponíveis. Duração, resolução, áudio, créditos e exportação dependem do provedor.

**Exemplo:** “Planeje um vídeo de anime de 60 segundos. Confira as ferramentas disponíveis, prepare as cenas e informe quais etapas consegue gerar e montar.”

**Consulte os registros desta área** na [distribuição por área](references/CAPABILITIES.md).

Os registros de apoio, como documentos, planilhas, biblioteca e gestão de plugins, aparecem separadamente no catálogo. Eles também exigem suas ferramentas originais.

Para ver **cada registro distribuído por área**, consulte [CAPABILITIES.md](references/CAPABILITIES.md).

## O que vem no pacote

- **115 módulos incorporados de desenvolvimento**, com guias e recursos disponíveis nas fontes originais.
- **14 guias próprios de conteúdo e vídeo**, com procedimentos incluídos.
- **329 registros de integração** das habilidades e plugins identificados no ambiente de origem.
- Uma entrada `SKILL.md`, catálogo pesquisável e instalador Python.

São **458 registros**, com sobreposições; não são 458 habilidades únicas. Um registro `bundled` contém o guia. Um registro `adapter` é uma dependência: **não contém as instruções originais nem instala o plugin**. Há 14 guias próprios de conteúdo e vídeo; as demais habilidades de escrita, marketing e mídia continuam representadas por adaptadores. Consulte o [catálogo completo](references/CATALOG.md).

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

## Produção de conteúdo e vídeo integrada

Uma única skill coordena as 14 funções abaixo com guias próprios incluídos. Elas não precisam ser instaladas como novas skills. As habilidades relacionadas indicam a função coberta, não uma cópia de instruções privadas.

| Função | Habilidades relacionadas | Guia incluído |
|---|---|---|
| Escolher nicho, público e temas | `audience-research`, `content-pillars`, `idea-generation-and-ideation`, `social-strategy` | [nicho-publico](references/modules/content-nicho-publico/GUIDE.md) |
| Planejar séries e produção em lotes | `content-calendar`, `batch-content-plan` | [series-calendario](references/modules/content-series-calendario/GUIDE.md) |
| Criar roteiros curtos e storyboard | `short-form-video-script`, `reels-script`, `tiktok-script`, `scripting-and-storyboarding`, `hook-writer` | [roteiro-curto](references/modules/content-roteiro-curto/GUIDE.md) |
| Ajustar escrita e identidade da voz | `writing-style-and-tone`, `voice-builder` | [voz-escrita](references/modules/content-voz-escrita/GUIDE.md) |
| Preparar e produzir narração por IA | `ai-voiceover` | [narracao](references/modules/content-narracao/GUIDE.md) |
| Produzir vídeo narrado com várias cenas | `Higgsfield:faceless-video` | [faceless](references/modules/content-faceless/GUIDE.md) |
| Criar cenas com movimento | `PixVerse:pixverse-create-video`, `kling`, `luma`, `runway`, `veo-3` | [cenas-movimento](references/modules/content-cenas-movimento/GUIDE.md) |
| Criar ou corrigir legendas | `remotion-legendas`, `captions-and-clipping`, `PixVerse:pixverse-captions` | [legendas](references/modules/content-legendas/GUIDE.md) |
| Montar e editar o vídeo | `remotion-criar-video`, `remotion-cenas-animacoes`, `remotion-audio-video`, `PixVerse:pixverse-video-editing` | [montagem](references/modules/content-montagem/GUIDE.md) |
| Visualizar e exportar | `remotion-visualizar-video`, `remotion-exportar-video` | [exportacao](references/modules/content-exportacao/GUIDE.md) |
| Preparar publicação no YouTube | `youtube-publishing-and-metadata` | [youtube](references/modules/content-youtube/GUIDE.md) |
| Preparar publicação no TikTok | `tiktok-video-publishing` | [tiktok](references/modules/content-tiktok/GUIDE.md) |
| Agendar e acompanhar publicações | `scheduling-and-queue` | [agendamento](references/modules/content-agendamento/GUIDE.md) |
| Conferir formato e qualidade | `platform-specs-and-validation`, `analisar-videos` | [qualidade-video](references/modules/content-qualidade-video/GUIDE.md) |

O fluxo vai de pesquisa e roteiro até vídeo final e publicação, conforme ferramentas e autorizações disponíveis. Consulte [o procedimento completo](references/CONTENT_VIDEO.md).

**O que funciona sem plugins especializados:** planejamento, revisão da escrita, roteiros, storyboard, direção de narração, manifesto de cenas e metadados. Pesquisa atual exige acesso a fontes.

**O que exige ferramentas:** sintetizar voz, gerar cenas animadas, renderizar arquivos e publicar. Prioriza plugins já conectados. Higgsfield/PixVerse podem executar produção; Remotion depende de ambiente de renderização. Metricool ou WoopSocial podem agendar quando houver suporte à rede e conta escolhidas.

**Movimento real:** um pedido de personagem animado exige cenas com ação visível. Efeitos de zoom sobre imagens não são apresentados como essa entrega.

**Automação diária:** este pacote não instala um serviço que funcione continuamente. É necessário um executor externo para criar vídeos novos diariamente, acompanhar falhas e publicar. Agendar vídeos prontos é uma função diferente.

**Custos:** o pacote não fornece créditos, assinaturas nem contas. Usar uma skill gratuita não torna gratuito o serviço utilizado.

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
