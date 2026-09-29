# Brief — FullStack Connect talent profile

Portal: `Talent Fullstack` → https://talent.fullstack.com/profile
Operator: Tallow. Author of this brief: Recruiter (Maestro).

## Status of the form right now

The form is **dirty and unsaved**. A `Save` (type=submit) and a `Revert` button
exist but only render while the form is dirty. **Never click Save.** Lucas saves.
Reloading the page discards everything. Do not reload.

### Done already

**Skills tab — 30 rows, complete.** Elixir and Jenkins were removed.
Added: TypeScript, JavaScript, React, Express, Docker, Go, Kubernetes, Java,
Redis, DynamoDB, Google Cloud, React Native, APIs (REST, SOAP), HTML5, Git,
CI/CD, Jest, DataDog. Kept: AWS, Agentic Node, Agentic React,
Agentic React + Node, Agentic Ruby on Rails, CSS, Node, PostgreSQL, RabbitMQ,
Ruby on Rails, SQL, YAML.

**Employment dates — done.**
- `employmentHistory.1.start` = 01/01/2024, `.end` = 01/01/2026 (LuizaLabs)
- `employmentHistory.2.start` = 01/01/2023, `.end` = 01/01/2024 (Lippaus)
- `employmentHistory.0.start` = 03/06/2026, current employer, left as found.

## What is left to do

### 1. Employer 0 — FullStack (current)

Keep the employer `FullStack`. Keep the title `Mid-Level Software Engineer`.
Lucas decided both. Leave the start date alone.

Set the description rich-text editor (TipTap, the 1st `.tiptap.ProseMirror`
on the page) to exactly this. Blank line between every paragraph:

```
Mid-Level Software Engineer

DexCare is a healthcare technology platform that powers patient navigation and scheduling for 57M+ patients across 50 states, serving major health systems including Providence, Kaiser Permanente, and Piedmont.

Designed secure multi-tenant authentication and tenant-aware request processing, strengthening the platform's security posture and supporting its multi-tenant expansion.

Authored a Product Design Review for the Customer Information and Configuration experience, identifying hidden null values and limited in-place editing as causes of duplicate support requests.

Proposed validated in-place editing and role-based authorization, helping eliminate 34% of redundant support tickets and reducing operational bottlenecks.

Contributed across scheduling applications and platform services, including TypeScript/Node.js services built with Express and Koa, React interfaces, PostgreSQL, Sequelize, Drizzle ORM, DynamoDB and DynamoDB Streams, Redis, AWS SDK v3 services, LaunchDarkly, OpenFeature, OpenAPI/Swagger, Datadog RUM, Auth0, Epic EMR integration, and event-driven booking.

Collaborate with product, design, operations, and engineering teams to turn healthcare workflows into secure, reliable software.

Technologies: TypeScript, JavaScript, Node.js, Express, Koa, React, PostgreSQL, Sequelize, Drizzle ORM, DynamoDB, DynamoDB Streams, Redis, AWS SDK v3, LaunchDarkly, OpenFeature, OpenAPI/Swagger, Datadog RUM, Auth0, multi-tenant JWT, Epic EMR integration, event-driven booking, CI/CD.
```

### 2. Employer 1 — LuizaLabs

Replace the whole description with:

```
Mid-Level Software Engineer

Worked on a software engineering engagement for Magazine Luiza, one of Brazil's largest e-commerce companies.

Designed and maintained distributed tax microservices in Node.js and Java, processing thousands of government-compliant invoices daily and supporting the client's e-commerce operation at scale.

Built internal fiscal dashboards and back-office tools that gave finance and operations teams real-time visibility into workflows and reduced manual intervention.

Established cloud-native deployment practices with Docker and Kubernetes on GCP, enabling repeatable releases and reliable rollback across the fiscal platform.

Improved code review quality by introducing structured review practices and clearer pull-request documentation, reducing average review cycles from 3-4 rounds to 1-2.

Technologies: Node.js, Java, TypeScript, JavaScript, React, REST APIs, Docker, Kubernetes, GCP.
```

The old text claimed **Phoenix** and **RabbitMQ** at this employer. Lucas
confirmed both are wrong. They must not appear.

### 3. Employer 2 — Lippaus Distribuidora (Mid-level)

Replace the whole description with:

```
Mid-level Software Engineer

Fast-growing startup powering Heineken's beverage distribution network across Brazil.

Led the design and implementation of a multi-tenant architecture that enabled nationwide distributor expansion, supporting active clients without performance degradation.

Built the asynchronous order processing system handling high-volume operations, orders, notifications, and third-party integrations, making the platform resilient to traffic spikes.

Delivered customer-facing features and internal tools end-to-end, working directly with stakeholders to translate business requirements into production software.

Contributed to scaling the platform from a regional operation to a nationwide network while maintaining reliability and performance across all active distributors.

Technologies: TypeScript, JavaScript, Node.js, React, PostgreSQL, Docker, REST APIs.
```

### 4. New Employer 3 — Lippaus Distribuidora (Entry-level)

Click `Add Employer`. Fill:
- Employer: `Lippaus Distribuidora`
- Present Employer: `No`
- Start `03/01/2021`, End `01/01/2023`
- Description: `Entry-level Fullstack Software Engineer` and nothing else.
  LinkedIn carries no bullets for this role. Do not invent any.

LinkedIn shows Lippaus as two roles with a promotion. That is why this entry
exists.

## Working recipes, already proven on this page

Read state with `evaluate`. Field names are stable, CSS selectors work as
portal selectors, for example `input[name='skills.3.yearsOfExperience']`.

**Dump the form:**
```
maestri portal evaluate "Talent Fullstack" "JSON.stringify([...document.querySelectorAll('input')].filter(i=>/employmentHistory/.test(i.name)).map(i=>[i.name,i.value]))"
```

**Date fields are MUI X pickers. The hidden input is not the source of truth.**
Keyboard stepping is unreliable. The recipe that works:
1. Set month and day with the React native setter on the hidden input, then
   dispatch `input`. The year will be wrong.
2. Open that field's picker: click the **last** button inside
   `input[name=...].closest('[role=group]')`.
3. Scope every following query to the one **visible** popper:
   `[...document.querySelectorAll('.MuiPickersPopper-root,.MuiPickersLayout-root')].filter(e=>e.offsetParent!==null).pop()`.
   Several pickers are mounted at once. A global query hits the wrong one.
   This was the cause of every earlier failure.
4. Inside that popper click the button whose aria-label matches `/year view/`,
   then the year button whose text is the target year. The field value is now
   correct.
5. Close by `document.body.click()`. **Do not press Escape.** Escape reverts
   the pick.

**Skill rows re-index after any name change.** Always re-resolve the row index
by reading the name input values again before writing years, level, or
checkboxes.

**Level is a MUI Select.** Focus `#mui-component-select-skills.N.level`, press
Enter, then click `[role=option][data-value='Advanced']`.

**`maestri portal key` accepts named keys only.** Digits do not work.

**`maestri portal click` fails on off-screen elements.** Use
`evaluate "(()=>{document.querySelector('...').click();return 1})()"` instead.

## Definition of done

All four employer blocks correct, skills untouched, nothing saved. Then run
`maestri ask "Recruiter " "..."` with a short report of what you changed and
anything you could not do.
