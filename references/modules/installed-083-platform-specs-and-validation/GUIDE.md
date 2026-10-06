# platform-specs-and-validation

## Finalidade

Platform specs and publish validation — per-platform requirements and the validate-before-publish step for multi-platform fan-out. Use when fanning a post out to multiple platforms, when a post is getting rejected, when mapping per-platform postType/required fields, or to run the validate-before-publish step. Encodes the per-platform postType enums, required-field matrices, and media rules from the OpenAPI spec, and runs POST /posts/validate so a post lands correctly on every target. Uses the CHECK framework. The keystone the per-platform format skills point to. WoopSocial validates + publishes atomically and has no update endpoint; the agent maps fields and fixes spec violations, but human-judgment calls (disclosure truthfulness, privacy intent) stay with the person; metrics never fabricated. Distinct from the per-platform format skills (one platform's content) and scheduling-and-queue (timing).

## Dependência

Este é um registro de integração. As instruções originais, ferramentas e contas não são incorporadas. Confira se a habilidade ou plugin `platform-specs-and-validation` está instalado no ambiente atual e leia suas instruções pela interface disponível. Se não estiver, indique essa dependência sem inventar um comando de instalação ou resultado.

## Execução

Identifique o resultado e os arquivos fornecidos; confira as ferramentas realmente disponíveis. Execute as etapas autorizadas usando o plugin original. Na ausência dele, entregue somente as partes que puder concluir com as ferramentas atuais e explique o que ficou pendente. Verifique o resultado antes de informar sucesso.
