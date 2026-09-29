# Relatório de rascunho

## Arquivos escritos

- `resumes/conta-simples-engenheira-software-senior-pt.tex`
- `resumes/conta-simples-engenheira-software-senior-pt.pdf`
- `resumes/conta-simples-engenheira-software-senior-pt.raw.txt`
- `resumes/conta-simples-engenheira-software-senior-pt.layout.txt`
- `reports/conta-simples-engenheira-software-senior-message.md`
- `reports/conta-simples-engenheira-software-senior-draft.md`
- `state/app-conta-simples-engenheira-software-senior.md`, com uma linha anexada ao log.

## Bullets alterados em relação à base

- DexCare 1: priorizei TypeScript, Express, Koa e integrações orientadas a eventos.
- DexCare 2: movi o bullet de APIs REST para a segunda posição e priorizei contratos de integração e a redução de 25%.
- DexCare 3: movi o bullet do EMR Epic para a terceira posição e mantive a redução de 15%.
- DexCare 4: priorizei PostgreSQL, DynamoDB, Redis e AWS SDK v3.
- DexCare 5: explicitei interfaces React no monitoramento com Datadog RUM.
- DexCare 6: priorizei Claude Code, Codex, regras, lint, complexidade e testes.
- Luizalabs 1: troquei `entregaram` por `sustentaram` na emissão de notas fiscais.
- Luizalabs 4: troquei `suítes` e `gate` por `testes automatizados` no CI/CD.
- Lippaus, Entry-level 2: explicitei a conversão de requisitos de clientes em entregas.
- Os demais bullets ficaram iguais à base.

## Marcadores [UNVERIFIED]

- `POO | SOLID | Design Patterns | Clean Code | React Native | Mocha | Testing Library | AWS Serverless | NoSQL | Agentes de IA [UNVERIFIED]`: um marcador cobre o grupo de palavras-chave. O brief exige confirmação de Lucas para esses termos. AWS, DynamoDB e os ambientes com Claude Code e Codex têm fatos próximos, mas não removem o marcador exigido pelo brief.

## Tokens da vaga não incluídos

- `Kotlin`: não está no DOSSIER e é uma alternativa na vaga.
- `avaliar criticamente os resultados` e `evolução de skills`: o DOSSIER confirma regras e controles de qualidade para agentes, mas não confirma essas formulações.
- `Mentalidade protagonista`: o DOSSIER confirma liderança de escopo, mas não confirma esta descrição subjetiva.
- `Abertura de Conta em Fintech`: não está no DOSSIER. O CV mantém somente o domínio fiscal e de emissão de notas confirmado para Luizalabs.
- `boas práticas de integração`: o DOSSIER confirma contratos OpenAPI/Swagger, mas não usa essa formulação.

## Verificação

- `tectonic`: concluído com código 0.
- PDF: uma página.
- `pdftotext` e `pdftotext -layout`: contato, quatro seções, DexCare, Luizalabs, dois blocos da Lippaus Distribuidora e FAESA extraídos.
- `grep -n UNVERIFIED`: um hit, descrito acima.
- `grep -in 'ruby\|rails'`: zero hits.
