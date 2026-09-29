# Hunt 2026-09-04-e triage

Source: `state/source-hunt-2026-09-04-e/events.jsonl`

## Result

- 33 unique records.
- 21 deterministic rejects from the source script.
- 12 records reached semantic review.
- 11 semantic-review records were dropped.
- 1 posting passed triage and mandatory-requirement preflight.

## Deterministic rejects

The script rejected 21 unique records. Recorded reasons include eight reposted records, five over-100 competition records, four hybrid or on-site records, two BairesDev records, one outside-primary-stack title, five without Remote or LatAm evidence, and six without an observable allowed-stack token. Some records have more than one reason.

## Semantic-review drops

| Record | Result | Reason |
|---|---|---|
| AHU Technologies, Full Stack Developer / React Developer, Areeba Khalid | DROP | Mandatory Next.js and Node.js 18 evidence is absent from the dossier. |
| AHU Technologies, Full Stack Developer / React Developer, Eman Fatima | DROP | Duplicate AHU posting. Mandatory Next.js and Node.js 18 evidence is absent from the dossier. |
| Praxis LATAM, Senior Full Stack and Frontend Developers | DROP | Mandatory location is Peru or Colombia. |
| IQVIA, Senior Software Engineer - Full Stack (React/Node.js) | DROP | The official posting states Hybrid in Sao Paulo. |
| PTR Global multi-role post | DROP | The post requires candidates local to Phoenix, Las Vegas, or Salt Lake City. |
| Senior JavaScript Engineer, Elizabeth Olivares | DROP | Mandatory Next.js/SSR, Web Components, design-system, WCAG, Storybook, React Testing Library, Cypress, and Core Web Vitals evidence is absent from the dossier. |
| Beyond Solucoes, two Tech Lead roles | DROP | One role is hybrid and requires financial-investments experience. The remote role is .NET-primary and requires two years as a Tech Lead. |
| P7 Group, Desenvolvedor(a) Full Stack | DROP | Mandatory NestJS, LLM, and RAG evidence is absent from the dossier. |
| NexIA Lab, Desenvolvedor full stack | DROP | Mandatory production LLM/RAG, n8n, LangChain, VPS, Linux, SSH, and named integration evidence is absent from the dossier. |
| Turbi, Desenvolvedor Fullstack Senior (Golang + Web) | DROP | Mandatory Git, Linux/Unix, secure-development, OAuth 2.0, and CSS evidence is absent from the dossier. |
| Jobgether, Senior Full-Stack Engineer - Trading API | DROP | Exact posting 4461922727 already reached a terminal abandoned state in hunt 2026-09-04. |

## Approved

1. Kake, Senior Fullstack Engineer (React + Golang). Segment `agency`. Language `en`. Remote LATAM, paid in USD. The required stack is Go, React, AWS, Docker, Kubernetes, backend services, relational or NoSQL databases, testing, observability, scalability, and equivalent messaging or API tooling.

