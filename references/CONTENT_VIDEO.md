# Conteúdo e vídeo: fluxo integrado

Este fluxo pertence à única skill `universal-skills`. Os 14 guias próprios são referências carregadas por tarefa, não skills adicionais. Planejamento e escrita podem ser realizados pelo agente com esses guias; geração, edição e publicação precisam de ferramentas adequadas.

| Função | Habilidades relacionadas | Guia incluído |
|---|---|---|
| Escolher nicho, público e temas | `audience-research`, `content-pillars`, `idea-generation-and-ideation`, `social-strategy` | [nicho-publico](modules/content-nicho-publico/GUIDE.md) |
| Planejar séries e produção em lotes | `content-calendar`, `batch-content-plan` | [series-calendario](modules/content-series-calendario/GUIDE.md) |
| Criar roteiros curtos e storyboard | `short-form-video-script`, `reels-script`, `tiktok-script`, `scripting-and-storyboarding`, `hook-writer` | [roteiro-curto](modules/content-roteiro-curto/GUIDE.md) |
| Ajustar escrita e identidade da voz | `writing-style-and-tone`, `voice-builder` | [voz-escrita](modules/content-voz-escrita/GUIDE.md) |
| Preparar e produzir narração por IA | `ai-voiceover` | [narracao](modules/content-narracao/GUIDE.md) |
| Produzir vídeo narrado com várias cenas | `Higgsfield:faceless-video` | [faceless](modules/content-faceless/GUIDE.md) |
| Criar cenas com movimento | `PixVerse:pixverse-create-video`, `kling`, `luma`, `runway`, `veo-3` | [cenas-movimento](modules/content-cenas-movimento/GUIDE.md) |
| Criar ou corrigir legendas | `remotion-legendas`, `captions-and-clipping`, `PixVerse:pixverse-captions` | [legendas](modules/content-legendas/GUIDE.md) |
| Montar e editar o vídeo | `remotion-criar-video`, `remotion-cenas-animacoes`, `remotion-audio-video`, `PixVerse:pixverse-video-editing` | [montagem](modules/content-montagem/GUIDE.md) |
| Visualizar e exportar | `remotion-visualizar-video`, `remotion-exportar-video` | [exportacao](modules/content-exportacao/GUIDE.md) |
| Preparar publicação no YouTube | `youtube-publishing-and-metadata` | [youtube](modules/content-youtube/GUIDE.md) |
| Preparar publicação no TikTok | `tiktok-video-publishing` | [tiktok](modules/content-tiktok/GUIDE.md) |
| Agendar e acompanhar publicações | `scheduling-and-queue` | [agendamento](modules/content-agendamento/GUIDE.md) |
| Conferir formato e qualidade | `platform-specs-and-validation`, `analisar-videos` | [qualidade-video](modules/content-qualidade-video/GUIDE.md) |

## Executar do início ao fim

1. Identificar objetivo, público, idioma, estilo, plataforma, duração, orçamento e ferramentas disponíveis. Reaproveitar decisões já fornecidas.
2. Ler os guias de nicho, calendário, roteiro e voz necessários. Entregar brief, roteiro e storyboard com fatos conferidos.
3. Conferir geração disponível e preparar manifesto. Priorizar plugins conectados, execução remota e opções gratuitas quando esse for o pedido; não presumir créditos gratuitos.
4. Gerar narração e cenas. Guardar IDs de tarefas e resultados, sem duplicar solicitações em andamento. Verificar falhas antes de continuar.
5. Alinhar legendas, montar, pré-visualizar e exportar. Conferir formato e qualidade usando o arquivo real.
6. Preparar metadados. Publicar ou agendar dentro da autorização do usuário, guardando ID e status confirmado.
7. Relatar entregas e bloqueios. Nunca confundir instruções, um agendamento futuro e uma postagem concluída.

## Manifesto recomendado

Registrar por episódio: ID, tema, fontes, roteiro, estilo, personagens, cenas, duração pretendida, áudio, clipes, legendas, arquivo final, plataforma, conta, horário com fuso, IDs externos e status. Não registrar tokens ou senhas.

Status: planejado → roteiro pronto → gerando → montando → revisando → pronto → agendado/publicado; falhas ficam registradas com etapa e causa. Retomar a etapa falha sem regenerar materiais aprovados.

## Dependências e limites

- Higgsfield e PixVerse: integrações opcionais. Conferir ferramentas disponíveis e instruções do plugin instalado; os contratos de execução podem ser específicos ao serviço.
- Kling, Luma, Runway e Veo: provedores opcionais; limites, custo e acesso variam.
- Remotion: requer Node.js, projeto e recursos de renderização; preferir servidor quando o computador do usuário for limitado.
- Metricool ou WoopSocial: publicadores opcionais. Conferir redes, contas e operações realmente oferecidas.
- Não há daemon, executor recorrente ou conta de rede social embutidos. Produção diária exige configuração externa e validação do fluxo completo.
- AITuber e Pexo não foram adicionadas por este fluxo: a atualização corresponde às funções e habilidades selecionadas pelo usuário.

## Exemplos de uso

“Use universal-skills para pesquisar um nicho, criar uma série de sete Shorts e produzir o primeiro vídeo anime com personagens em movimento. Use apenas plugins conectados e opções gratuitas disponíveis.”

“Use universal-skills para revisar meu roteiro, criar storyboard, narração, legendas e vídeo vertical. Agende no canal que eu indicar e informe o status confirmado.”

Os nomes Higgsfield:faceless-video e PixVerse:pixverse-* são aliases legíveis. No catálogo de plugins, podem aparecer com prefixo do identificador da integração, como app-6a3293e129088191abf0875820e839da:faceless-video ou pixverse:pixverse-create-video. Localizar pelo sufixo e conferir a descrição.
