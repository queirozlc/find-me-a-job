# Base CV draft report, fix round 7

Date: 2026-09-01. Author: Resume Architect (Quill). Not graded. Hand to the ATS Analyzer.

## Deliverables

- `~/career/resumes/base-en.tex` -> `base-en.pdf`, `base-en.raw.txt`, `base-en.layout.txt`
- `~/career/resumes/base-pt.tex` -> `base-pt.pdf`, `base-pt.raw.txt`, `base-pt.layout.txt`
- Final renders: `~/career/reports/visual/base-en-1.png`, `base-pt-1.png`

## Round 7 content

### Changed or new bullets, English

- D2: Keep bookable slots synced with hospital records and reduce wrong bookings by 15% by integrating Epic EMR time-slot flows.
- D3: Isolate tenant data, enforce API contracts, and reduce authentication friction by 25% using Auth0 JWT and OpenAPI validation on multi-tenant REST APIs.
- D5: Reduce release risk by 7% by shipping behind LaunchDarkly/OpenFeature flags and monitoring React with Datadog RUM.
- D7: Reduce new-client pilot friction by 33% by helping implement the Shared Platform Initiative (SPI), replacing per-customer environments with shared service instances and isolated configuration, secrets, and data stores.
- L2: Improved invoice throughput by 20% and fault tolerance by moving SEFAZ communication to asynchronous BullMQ queues.
- L3: Gave operations visibility into fiscal workflows and cut support tickets by 18% by building back-office dashboards on tax microservices.
- P2: Handled high-volume orders, notifications, and integrations with 26% more processing capacity through asynchronous BullMQ jobs.

### Changed or new bullets, Portuguese

- D2: Mantém horários sincronizados e reduz reservas incorretas em 15% integrando fluxos de horários do EMR Epic.
- D3: Isola dados, garante contratos de API e reduz o atrito de autenticação em 25% com Auth0 JWT e OpenAPI em REST APIs multi-tenant.
- D5: Reduz o risco de releases em 7% com flags LaunchDarkly/OpenFeature e monitoração React no Datadog RUM.
- D7: Reduz em 33% o atrito ao pilotar novos clientes ajudando a implementar a Shared Platform Initiative (SPI), substituindo ambientes por cliente por instâncias compartilhadas com configurações, segredos e dados isolados.
- L2: Melhorou em 20% a vazão de notas e a tolerância a falhas levando a comunicação SEFAZ para filas BullMQ assíncronas.
- L3: Deu visibilidade aos fluxos fiscais e reduziu chamados de suporte em 18% criando dashboards de backoffice sobre os microsserviços.
- P2: Tratou pedidos, notificações e integrações com 26% mais capacidade usando jobs assíncronos BullMQ.

All other bullets and both full Summaries remain unchanged. Each file contains
the seven exact supplied percentages once: 7%, 15%, 18%, 20%, 25%, 26%, 33%.

## Skills

Added `RabbitMQ` and `AMQP` to the Backend group in both languages. No service
name was added.

## Page-fit fallback

The new content overflowed at `6pt`. Per Lucas's instruction, inter-role and
pre-Education spacing is now `5pt`. The first wording pass still overflowed,
so only the seven changed/new bullets were tightened; no bullet was dropped
and the Summary was not shortened.

## Build and artifact checks

- Final `tectonic base-en.tex`: success.
- Final `tectonic base-pt.tex`: success.
- Raw and layout `pdftotext` extractions regenerated for both PDFs.
- `pdftoppm -png -r 60` renders regenerated for both PDFs.

| Check | EN | PT |
|---|---:|---:|
| Pages | 1 | 1 |
| Inter-role spacing | 5pt | 5pt |
| Exact percentage values present | 7 of 7 | 7 of 7 |
| `RabbitMQ` appearances | 1 | 1 |
| `AMQP` appearances | 1 | 1 |
| `SPI` whole-word appearances | 1 | 1 |
| Maximum load-bearing term count | 3 | 3 |
| `[UNVERIFIED]` in source/raw | 0 | 0 |

## Visual inspection

Both final PNGs show the complete Education block and all 16 bullets. No
clipping, overlap, broken glyph, or second page is visible.

## Handoff status

The last `maestri list` showed only `Recruiter ` connected and no ATS Analyzer,
so no rubric request could be routed from this seat.
