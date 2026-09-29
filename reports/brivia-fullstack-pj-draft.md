# Relatório do rascunho Brivia

## Arquivos escritos

- `resumes/brivia-fullstack-pj-pt.tex`
- `resumes/brivia-fullstack-pj-pt.pdf`
- `resumes/brivia-fullstack-pj-pt.raw.txt`
- `resumes/brivia-fullstack-pj-pt.layout.txt`
- `reports/brivia-fullstack-pj-message.md`
- `reports/brivia-fullstack-pj-draft.md`
- `state/app-brivia-fullstack-pj.md`, somente uma linha de log adicionada

## Bullets alterados em relação à base

- DexCare D1: Posicionei os serviços como backend em TypeScript, Express e Koa. Mantive reservas orientadas a eventos.
- DexCare D4: Reforcei PostgreSQL e o resultado de conectar dados de reservas aos serviços AWS.
- DexCare D5: Mantive o resultado de 7%, as flags e o Datadog RUM. Usei `frontend` para respeitar o limite de aparições de React.
- DexCare D6: Usei a expressão da vaga `ferramentas de IA` e mantive Claude Code, Codex e os controles de qualidade confirmados.
- Luizalabs L1: Acrescentei a expressão confirmada `processamento distribuído` aos microsserviços em Node.js, Java e Go.
- Luizalabs L2: Coloquei o resultado de 20% antes do método com filas BullMQ.
- Luizalabs L3: Coloquei o resultado de 18% antes do método com dashboards de backoffice.
- Luizalabs L4: Reforcei as esteiras de CI/CD com Docker, Kubernetes, GCP, ArgoCD, Vitest e Jest.
- Lippaus P2: Coloquei o resultado de 26% antes do processamento assíncrono com BullMQ.
- Lippaus P3: Liguei o escopo e a comunicação com stakeholders à entrega confirmada de funcionalidades JavaScript.
- Lippaus E1: Troquei o verbo inicial `Desenvolvi` por `Construí`.
- Lippaus E2: Nomeei React Native e mantive a entrega de ponta a ponta, os requisitos de negócio e as restrições técnicas.

## Marcadores [UNVERIFIED]

Nenhum.

## Verificação

- `tectonic` gerou o PDF. O compilador emitiu avisos de solicitação das fontes Roboto e nenhum erro de build.
- `pdfinfo` informou uma página.
- As extrações raw e layout contêm o bloco de contato e os quatro cabeçalhos obrigatórios.
- A base contém quatro blocos de Experiência e um bloco de Formação. Os cinco blocos `resumeSubheading` foram extraídos com empresa ou escola, cargo, data e local.
- A inspeção visual não encontrou corte, sobreposição, glifo quebrado ou texto ilegível.
- `grep -n UNVERIFIED` não retornou resultados.
- A varredura obrigatória de termos proibidos não retornou resultados.
- React, TypeScript, JavaScript, Node.js, Go, PostgreSQL, APIs, IA, BullMQ e microsserviços aparecem no máximo três vezes como termos completos no CV.

## Tokens da vaga que não foram usados

- `experiência sólida` e `domínio`: O DOSSIER.md não atribui esses níveis de profundidade.
- `aplicações web escaláveis`: O DOSSIER.md confirma aplicações web, mas não confirma escala.
- `evolução de APIs`: O DOSSIER.md confirma construção de APIs, mas não usa esta afirmação.
- `BFF` e `arquitetura BFF`: O Maestro brief identifica BFF como lacuna.
- `boas práticas de engenharia`: O DOSSIER.md confirma regras, lint e testes, mas não usa esta afirmação ampla.
- `code review`: Não consta no DOSSIER.md.
- `times multidisciplinares`, `Produto`, `UX`, `Dados` e `QA`: O DOSSIER.md confirma comunicação com stakeholders, mas não identifica estes times.
- `modelos de IA/ML`: O DOSSIER.md confirma ferramentas de IA, mas não confirma integração com modelos.
- `soluções orientadas a dados`, `indicadores`, `scores`, `recomendações` e `modelos preditivos`: Não constam no DOSSIER.md.
- `certificações em Cloud/DevOps`: O Maestro brief informa que não há certificações no DOSSIER.md.
- `automação`: O DOSSIER.md confirma fluxos agênticos e ferramentas de IA, mas não usa este termo mais amplo.
- `equipamento próprio`: Não consta no DOSSIER.md e ficou como pergunta para Lucas na triagem.
