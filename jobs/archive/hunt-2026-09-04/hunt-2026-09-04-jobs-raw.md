# Hunt 2026-09-04, LinkedIn Jobs Search raw captures

Source portal: Jobs Search only
Source surface: jobs-tab
Run: `("typescript" or "node.js") AND "senior" AND "latam"`
Date filter: Past 24 hours, applied through the UI (`f_TPR=r86400`)
Result count shown after filter: 80
Cards reviewed: 15
Capture count: 15
Past week widening: not used

Capture filters used: posting age inside the active window, location shown as Brazil/LatAm/Remote, and posting text containing JavaScript, TypeScript, Node.js, React, or Go. Employment type, workplace type, company origin, seniority, apply destination, and stack mismatch were not used to drop a card.

## 1. Dev Back End Senior

Company: Tamborete
Posting URL: https://www.linkedin.com/jobs/view/4463134353/
Posted age as shown: 14 hours ago
Location as shown: Belo Horizonte, Minas Gerais, Brazil
Workplace type as shown: Hybrid
Employment type as shown: Full-time
Visible applicant count: 27 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: pt
Company origin as shown: not explicit in the posting
Segment: not observable as br-pj; Brazilian-company evidence only, posting states CLT, not PJ
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
A Tamborete é a plataforma de pagamentos padroeira dos pequenos e puxa saco dos gigantes. Gateway, checkout, API Pix e carteira digital para quem vende na internet: do infoprodutor que faturou o primeiro real ao e-commerce que já cansou de ser maltratado por adquirente grande.Se você não nos conhece, passa no nosso Instagram (@tamborete.br). É, aquilo lá é a gente mesmo. E o código por trás daquilo tudo é o que você vai escrever.
A parte séria (porque tem uma)
Por trás das esquetes tem um sistema processando pagamento de verdade, todos os dias. E estamos no meio de uma migração de monolito para microsserviços. Não a de slide de consultoria: a de verdade, com transação passando enquanto a mudança acontece. Autorização, captura, liquidação, estorno, split, conciliação. Aqui, requisição duplicada não é bug: é cobrança duplicada no cartão de alguém.
E vamos ser honestos como somos nos Reels: nosso ambiente ainda não tem tudo mastigado. Regra de negócio que só existe na cabeça de alguém, processo que ninguém escreveu, decisão de arquitetura que precisa sair essa semana. Se você precisa de especificação perfeita pra começar, a gente se admira de longe.
A stack (a de verdade, não a do job description genérico)
Python e Go nos serviços, NestJS nas APIs, Next.js no front (não precisa ser front, precisa desenhar contrato que o front não xingue)
AWS serverless: Lambda como unidade principal, API Gateway, filas e eventos
PostgreSQL no transacional, DynamoDB onde a escala pede
Observabilidade e CI/CD em evolução. Melhorar isso é parte do trabalho, não desculpa

O que você vai fazer
Extrair microsserviços do monolito definindo fronteira, contrato e migração sem parar a operação
Escrever código com idempotência, retry e consistência eventual como hábito, não como resposta decorada de entrevista
Decidir o que vai pra PostgreSQL e o que vai pra DynamoDB, e defender a decisão
Desenhar contratos de API entre serviços, com o front e com parceiros
Testar de forma automatizada porque é assim que se trabalha, não porque alguém mandou
Documentar: hoje tem muita regra de negócio morando na cabeça das pessoas, e cabeça não faz deploy
Usar IA no desenvolvimento com critério: acelerar sim, colocar em produção linha que você não entende, jamais

O que é obrigatório
Profundidade real em pelo menos uma: Python, Go ou Node/NestJS, com disposição comprovada de transitar entre elas
AWS serverless em produção, incluindo as dores: cold start, timeout, limite de payload, conta no fim do mês
PostgreSQL e DynamoDB em produção: modelagem, índice e o critério de quando usar cada um
Já ter vivido uma migração grande e conseguir contar o que deu errado (se nada deu errado, você não estava lá)
Teste automatizado como hábito de anos, não de projeto
Design de API: versionamento, retrocompatibilidade, breaking change comunicado como gente
Morar em BH ou topar o modelo híbrido. Eliminatório: a vaga não é remota, e não adianta perguntar no DM

O que conta muito a favor
Fintech / meios de pagamento: checkout (autorização, captura, liquidação, estorno, chargeback), split, conciliação
Ter trabalhado em PSP, gateway, subadquirente ou adquirente
Pix na prática: integração, webhooks, devolução, limites
Arquitetura orientada a eventos (SQS, SNS, EventBridge, DLQ, ordering)
Infra como código (Serverless Framework, SAM, Terraform, CDK)
Vivência em early stage: construir muito com pouco

Como a gente trabalha
Mão na massa: sênior aqui escreve código todo dia. Todo. Dia.
Proatividade real: sem spec mastigada
Autonomia de ponta a ponta: da decisão de arquitetura ao incidente das 23h (que a gente trabalha pra não existir)
Documentar e distribuir conhecimento
Tolerância a ambiguidade: regra não escrita faz parte do jogo

Modelo, regime e benefícios
CLT, integral · 
Híbrido: 4 dias presenciais + 1 de home office (Santa Lúcia, BH) · escala 5x2
Caju com VA de R$ 1.000/mês
Plano de saúde (não queremos que você passe mal, mas se passar, vai estar bem amparado)
Bônus real por implementações entregues com impacto positivo: entregou, mediu, impactou, recebeu

Requirements added by the job poster
• 4+ years of work experience with AWS Lambda
• 4+ years of work experience with Amazon Web Services
• 4+ years of work experience with Python
```

## 6. Desenvolvedor full stack

Company: Pasquali Solution
Posting URL: https://www.linkedin.com/jobs/view/4462885469/
Posted age as shown: 18 hours ago
Location as shown: Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: Over 100 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: pt
Company origin as shown: not stated; project described as international
Segment: agency
Recruiter: Raquel Domingues, `Tech Recruiter | Analista de Recrutamento e Seleção | End-to-end Recruitment | Vagas Tech, Hunting e Experiência do Candidato`; Adilma Gomes, `Gerente de Recrutamento e seleção/Tech Recruiter`, job poster
Time-zone overlap requirement: EST
English fluency requirement: Inglês fluente
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
Oportunidade para Full Stack Engineer, com atuação em projeto internacional.Buscamos um profissional com perfil sênior e experiência sólida em desenvolvimento Front-End e Back-End.
Principais requisitos:
Entre 7 e 9 anos de experiência profissional em Engenharia ou Desenvolvimento de Software
Mínimo de 3 anos de experiência com React
Forte experiência com React, JavaScript e TypeScript
Conhecimento em Node.js e Next.js
Experiência com Java e Spring Boot
Mínimo de 2 anos de experiência trabalhando com APIs baseadas em Java
Experiência com consumo de APIs e tratamento de dados assíncronos em Micro Frontends
Experiência com ferramentas de desenvolvimento assistido por IA, como GitHub Copilot e ChatGPT
Vivência com geração de código, refatoração, criação de testes, debugging e documentação com apoio de IA
Experiência em times de Product Engineering ou ambientes orientados a Produto
Vivência trabalhando em parceria com Product Managers e Designers
Experiência com testes, debugging e monitoramento das próprias aplicações
Conhecimento em CI/CD e sistemas de controle de versão
Experiência com monitoramento de aplicações, logs, distributed tracing, métricas e alertas
Vivência com Production Support e escala de on-call
Inglês fluente para atuação com time internacional
Disponibilidade para trabalhar no fuso EST

Requirements added by the job poster
• 3+ years of work experience with JavaScript
• 3+ years of work experience with React.js
• 7+ years of work experience with Java
```

## 7. Senior web software engineer, Brazil

Company: CI&T
Posting URL: https://www.linkedin.com/jobs/view/4454020765/
Posted age as shown: Reposted 1 hour ago
Location as shown: Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: Over 100 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: en
Company origin as shown: more than 25 countries; 8,000 CI&Ters
Segment: agency
Apparent duplicate of existing file: `ciandt-senior-fullstack.md`, same company but different title and URL
English fluency requirement: Advanced English communication skills

Full posting text quoted verbatim:

```text
About the job
At CI&T, we help large enterprises transform the potential of AI into real business impact with AI Deployment, AI-native execution, and tech-integrated business solutions.
With 30 years of experience in technological transformation, we accelerate innovation with expertise in Agentic SDLC, Application modernization, Data & AI, Martech and Business strategy.
We are 8,000 CI&Ters across more than 25 countries, collaborating to build solutions with real impact. AI is already part of how we work, evolve, and innovate every day.

We are looking for an experienced Senior Web Software Engineer to build and deliver enterprise-grade digital solutions as part of a CMS modernization and migration initiative. This is a hands-on development role focused on modern web technologies, particularly JavaScript, TypeScript, React, and Next.js, with familiarity with PHP-based systems to support the migration. The engineer will also be expected to apply AI-assisted development practices to accelerate delivery across the software development lifecycle.

Key Responsibilities
Build, test, and deliver enterprise-grade web solutions using modern technologies such as JavaScript, TypeScript, React, and Next.js, contributing directly to a CMS modernization and migration initiative. Work with CMS platforms, APIs, integrations, and existing PHP-based applications as needed to understand current implementations and support a successful transition to the new solution.

Collaborate with architects and engineering teams to translate requirements into maintainable technical solutions, applying strong software engineering practices around code quality, testing, performance, and security. Use AI-assisted development tools and agentic workflows throughout the SDLC to accelerate coding, testing, debugging, documentation, and technical analysis.

Required Skills & Experience

Strong hands-on experience with modern web application development.

Strong experience with JavaScript and TypeScript.

Hands-on experience with React and Next.js, or directly comparable modern web frameworks.

Solid understanding of software engineering principles, programming logic, clean code, testing, debugging, and maintainability.

Experience with CMS concepts, including content modeling, APIs, integrations, and modern CMS architectures.

Familiarity with PHP-based applications and the ability to read, understand, debug, and navigate an existing PHP codebase. Deep PHP specialization is not required.

Experience analyzing functional and non-functional requirements and contributing to technical implementation decisions.

Practical experience using AI coding assistants or AI-enabled development tools as part of the software development lifecycle.

Ability to design and document technical solutions, integrations, application workflows, and data flows.

Advanced English communication skills for technical discussions, collaboration, and documentation.
```

## 8. Senior Software Engineer – Full Stack (React/Node.js)

Company: IQVIA
Posting URL: https://www.linkedin.com/jobs/view/4461915976/
Posted age as shown: 14 hours ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Hybrid
Employment type as shown: Full-time
Visible applicant count: 10 people clicked apply
Apply destination host: jobs.iqvia.com
Posting language: en
Company origin as shown: global provider in over 100 countries
Segment: not observable as us-direct, br-pj, or agency
English fluency requirement: English fluent, both written and spoken
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
Fullstack Developer (React.js / Node.js)

Offer Description

We are looking for a highly motivated and experienced Senior Software Engineer, who is very used to working as a key member of a lean, Agile product development team. You will play an essential role in designing, building, enhancing and maintaining our bespoke client-facing software products using modern technologies, which are key to the success of our business.

Our software is deployed in Azure, so familiarity with Azure services is a definite advantage. Our backend is deployed on dockerized applications running on Kubernetes. We use different data storage mechanism, depending on the one that fits better the requirements, so you’ll find data in Postgres, Elasticsearch, Snowflake or Databricks. We have frontend applications which are written on React and they communicate through ts-rest.

Requirements Description

Bachelor's or higher degree in computer science, software development or a related field
Substantial relevant development experience and demonstrable capability of working in a role having senior engineer responsibilities (7+)
Experience with Typescript, Node.js, React, Azure or similar cloud services
Ability to write clean, readable, well formed, self-explanatory code
Experience in designing and building complex major components, services or applications, from scratch
Good interpersonal and communication skills, in English, both written and spoken
Hands on experience with core components of the application development environment configuration: GitLab pipelines, Docker

Your Responsibilities

Independently developing or enhancement of new and existing system components, services and applications.
Providing peer support to other developers, through code reviews, peer programming, collaborative technical design, mentoring less experienced folks or assisting in on-boarding new developers.
Write and maintain automated tests to ensure the quality of the codebase
Participating in regular formal and informal team sessions, like sprint-planning, refinement sessions, kick-offs, daily stand-ups and retros.
Helping to continuously improve our CI/CD pipeline, as well as the tools and methods that the team uses, to provide as much value as possible, with high quality, for as little effort as possible
Proactively sharing knowledge and producing “just good enough” documentation

Years Of Experience

7+ years of experience in React.js, Node.js

Required Skills/experience

Must-have

React (JavaScript, front-end)
NodeJS (JavaScript, back-end)
TypeScript

Working with

Continuous Integration / Continuous Delivery environments
Automated Build Pipelines

Desired

Python
Docker
Elasticsearch
PostgreSQL

Nice to have

If you have any of the following skills it will be a very welcome addition: Terraform, Python, ETL, Elasticsearch

If you happen to have SCALA knowhow or would like to learn SCALA and Apache Spark we would be delighted.

Soft Skills

Positive, can-do approach to work, delivering on commitments
Have good communication skills
Solution Oriented
Committed
Structured
Creative

Foreign language

English fluent, both written and spoken
```

## 9. Senior Node/React Developer (BRL 18-24K/month CLT + benefits + bonus)

Company: NOUS LATAM
Posting URL: https://www.linkedin.com/jobs/view/4460751090/
Posted age as shown: 18 hours ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Hybrid
Employment type as shown: Full-time
Visible applicant count: 33 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: en
Company origin as shown: not stated
Segment: not observable as us-direct, br-pj, or agency
Recruiter: Marcio Chede, `Co-founder & CEO | Ex-Bain & Co.`, job poster
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
With modern, cloud-native technologies (including Typescript, AWS, GraphQL) and the freedom to approach problems with fresh thinking, you’ll be building greenfield systems from the ground up. Expect to embed AI, automation, and best-in-class engineering practices into everything you develop.KEY RESPONSABILITIES
Lead the Design & Development - Architect, build, and deploy scalable, high-performance software solutions, covering both client-side and server-side applications.
Technical Leadership - Guide the squad in technical decision-making, ensuring the team follows best practices in code quality, design patterns, architecture, security, and performance.
Hands-On Engineering - Spend most of your time writing and reviewing code, designing APIs, and ensuring high-quality, maintainable software.
Full Stack Development - Build any necessary user-interfaces in collaboration with our UX team, and develop well-functioning APIs, and services.
Mentorship & Coaching - Support and mentor engineers, fostering a culture of continuous learning and technical excellence.
Cloud & Infrastructure - Deploy and manage applications on AWS using Terraform, Kubernetes, and containerized workloads.
Quality & Testing - Champion Test-Driven Development (TDD), automated testing, and CI/CD, ensuring deployments are secure and reliable.

REQUIRED EXPERIENCE:
Tech stack - We use TypeScript (Node.js & React), AWS (EKS, Lambda, Aurora RDS), Kubernetes, GraphQL, Kafka, Mongo. You’re comfortable with all of these, and have extensive knowledge of JavaScript more generally, the AWS ecosystem, and running containerised applications.
Past Experience - You are currently a Lead Engineer or Tech Lead, leading a small team of software engineers.
API & Database Development - You have experience building and running robust, always-on APIs (both RESTful and GraphQL-based) and underlying services/apps including the databases that underpin them.
Test-Driven Development - You're very familiar with testing frameworks such as Jest and Pact.
Cloud & DevOps - You can build, deploy and run your systems end-to-end, with no manual configuration or intervention. We use Terraform and Helm.
CI/CD - You have plenty experience managing and configuring CI/CD pipelines (we use GitHub Actions) for deployments.
Observability Mindset - You believe in measuring everything. You’ve worked with DataDog (or similar) to ensure your team has the necessary visibility into system health.
Tooling & Collaboration - Comfortable working with Git, Confluence, Jira, and modern engineering workflows.
Mentorship & Leadership - You’ve mentored engineers at all levels, providing guidance, reviewing designs, and ensuring your team stays on the right track.
Self-Starter & Problem-Solver - Ability to take a product challenge and develop a working technical solution, balancing pragmatism with engineering excellence.
```

## 10. Full Stack Developer - Senior | Remote (Talent Bank)

Company: TeamEx
Posting URL: https://www.linkedin.com/jobs/view/4461900448/
Posted age as shown: Reposted 17 hours ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: 43 people clicked apply
Apply destination host: teamex.io
Posting language: en
Company origin as shown: not stated
Segment: agency
English fluency requirement: Fluent English is required
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
Related Industries

Technology, SaaS, Startups, Digital Products, FinTech, HealthTech, E-commerce.

Purpose

We work with startups and technology-driven companies that need engineers who can do more than close Jira tickets.

This Talent Bank is for Senior Full Stack Engineers who enjoy owning problems end-to-end; from understanding the customer and what they actually need, to figuring out what should be built, designing the right solution, writing the code, shipping it, and making sure it actually works in production.

What You’ll Bring

Fluent English is required. It doesn't need to be perfect - although we'll certainly appreciate it if it is! - but you should be comfortable communicating directly with native English-speaking clients, collaborating with international teams, and creating clear content for presentations and other professional materials.
6+ years of software engineering experience, with strong full-stack skills across frontend and backend.
Deep experience with modern JavaScript/TypeScript and backend technologies such as Node.js, Python, Java, or Go, plus React and, when relevant, React Native / Expo.
Strong knowledge of APIs (REST/GraphQL), databases (SQL/NoSQL), architecture, testing, Git, and CI/CD, with experience deploying and operating production systems in the cloud.
Hands-on experience with PostgreSQL, third-party integrations, queues, background jobs, webhooks, and event-driven systems is valuable; Docker, Kubernetes, Infrastructure as Code, microservices, and observability are a plus.
Ability to understand customers and their needs, turn product problems into practical technical solutions, and own work from discovery and architecture through deployment and production.
Strong ownership, product thinking, communication, and problem-solving skills - you understand the why, not just the how, and can explain technical trade-offs clearly.
Comfortable working independently, navigating ambiguity, managing priorities, and wearing different hats when needed.
Experience in startups or fast-growing product companies and exposure to AI/LLM integrations are a plus.
Pragmatic by nature: you know when to build the beautiful architecture and when to ship the boring solution.
Curious by default: ambiguity doesn't make you freeze - it makes you investigate.

About This Talent Bank

This is a generic Talent Bank profile, designed to reflect the capabilities we commonly look for across our technology roles. Some of the technical requirements are intentionally informed by specific roles and stacks we've worked with in the past, so the exact stack may vary depending on the opportunity.

Compensation

DOE (Dependent on Experience).
```

## 2. Desenvolvedor (a) Fullstack Sênior- Remoto  

Company: HCLTech
Posting URL: https://www.linkedin.com/jobs/view/4461689765/
Posted age as shown: 18 hours ago
Location as shown: Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: Over 100 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: en
Company origin as shown: global technology company, spread across 60 countries
Segment: agency
Recruiter: Felipe Françozo, `Senior Tech Recruiter at HCLTech| Talent Attraction Latam| Technology Recruitment and Selection Specialist| Talent Acquisition Partner| Business Partner| Human Resources`
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
About HCLTech
HCLTech is a global technology company, spread across 60 countries, delivering industry-leading capabilities centered around digital, engineering, cloud and AI, powered by a broad portfolio of technology services and products. We work with clients across all major verticals, providing industry solutions for Financial Services, Manufacturing, Life Sciences and Healthcare, Technology and Services, Telecom and Media, Retail and CPG, and Public Services. We re powered by our people a global, diverse, multi-generational talent - representing 161 nationalities whose unique spark, perspective and boundless passion drive our culture of proactive value creation and problem-solving.
Description: Pearson PSG Software Engineering Group seeks a Full Stack and AI Engineer to design, develop, and maintain cloud-native applications supporting AI-enhanced content creation, assembly, management, and delivery. The engineer will work across responsive front ends, scalable APIs, Python microservices, integrations, and AWS-based backend systems in collaboration with product, architecture, UX, content, AI, and engineering teams.
Key Responsibilities:
• Build modern web applications using React, TypeScript, JavaScript, Node.js, and Python.• Develop secure, scalable REST APIs, microservices, and event-driven integrations.• Integrate AI, Agentic AI, and LLM capabilities into content workflows.• Design and deploy AWS solutions using Lambda, ECS, DynamoDB, S3, and CloudFront.• Implement automated testing, CI/CD, monitoring, logging, performance optimization, and production support.• Contribute to architecture, code reviews, Agile delivery, engineering standards, and technical mentoring.
Required Qualifications:
• Bachelor’s degree in Computer Science, Software Engineering, or a related field, or equivalent experience.
• 5+ years of software engineering experience with strong Python, React, TypeScript, and JavaScript skills.
• Hands-on experience with REST APIs, microservices, distributed systems, NoSQL databases, and AWS cloud services.
• Knowledge of software design patterns, object-oriented principles, secure coding, Agile, and DevOps practices.
• Strong problem-solving, ownership, communication, and cross-functional collaboration skills.Preferred: Experience with Agentic AI, AI-assisted engineering, LLM integration, Java, Spring Boot, ORM frameworks, relational databases, observability platforms, and education, publishing, digital learning, or content-management solutions.
Skill Matrix
Skill Requirement Proficiency:
Python and backend services Mandatory 4/5
React, TypeScript, and JavaScript Mandatory 4/5
REST APIs, microservices, and distributed systems Mandatory 4/5
AWS: Lambda, ECS, DynamoDB, S3, and CloudFront Mandatory 4/5
NoSQL databases Mandatory 3/5
Agile, DevOps, CI/CD, testing, and secure coding Mandatory 4/5
Agentic AI and LLM integration Good to have 3/5
Java, Spring Boot, ORM, and relational databases Good to have 3/5
Observability and production support Good to have 3/5
```

## 3. Senior Backend Engineer

Company: TRACTIAN
Posting URL: https://www.linkedin.com/jobs/view/4443416703/
Posted age as shown: Reposted 20 hours ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: Over 100 people clicked apply
Apply destination host: careers.tractian.com
Posting language: en
Company origin as shown: software development company; trusted by manufacturers across the Americas
Segment: not observable as br-pj; Brazilian-company evidence only, posting states full-time, not PJ
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
Engineering at TRACTIAN

At TRACTIAN, the Backend Engineering team plays a critical role in building and scaling the infrastructure that powers our entire platform: from our advanced monitoring products to our CMMS (Computerized Maintenance Management System). We design and develop robust systems that handle large volumes of real-time and historical data from industrial assets.

Our team is responsible for crafting and maintaining data-intensive microservices, resilient APIs, and scalable ETL pipelines. We work across multiple domains: from designing relational and non-relational database schemas to implementing event-driven architectures and optimizing performance under high-throughput workloads.

As part of a product-led company, Backend Engineers at TRACTIAN operate with strong ownership. We collaborate closely with firmware, frontend, data, and product teams to deliver high-impact features that directly improve equipment reliability, reduce downtime, and modernize industrial operations.

What you'll do

As a Backend Software Engineer at our company, you will design and build critical APIs, microservices, and ETLs that power our core products, from industrial monitoring systems to our CMMS platform. You’ll play a key role in evolving our backend architecture to meet the demands of scale, performance, and product excellence. Your work will directly impact thousands of users across industries that rely on us to keep their operations running.

Responsibilities

Design, build, and maintain data-intensive, high-performance backend services based on an event-driven architecture.
Develop and maintain APIs and services that power both real-time monitoring features and complex maintenance workflows.
Work closely with a cross-functional team to ensure our backend applications align with the overall product vision and user experience goals.
Optimize applications and data processing workflows for performance, focusing on enhancing speed, efficiency, and reliability across various operating environments
Continuously evolve our systems through refactoring, introducing best practices, and improving maintainability and observability.
Document architectural decisions and technical implementations clearly for the team and future maintainers.

Requirements

Bachelor’s degree in Computer Science, Engineering, or a related technical field.
5+ years of backend development experience, with a strong focus developing user-facing products.
Solid experience in event-driven applications using messaging technologies like Kafka, RabbitMQ, BullMQ or similar.
Strong programming skills in Go, Python, Node.js, and/or Rust.
Deep understanding of microservices architecture and distributed system design.
Proficiency in both relational (e.g., PostgreSQL, ClickHouse) and non-relational databases (e.g., ScyllaDB, Cassandra,, MongoDB), with a focus on performance and scalability.
Experience building mission-critical backend services in high-growth, product-driven environments.
Fluency in Portuguese.

Bonus points

Contributions to open-source or personal projects demonstrating backend architecture or data processing expertise.
Fluency in English.
```

## 4. Pessoa Desenvolvedora Backend Sr.

Company: MadeiraMadeira
Posting URL: https://www.linkedin.com/jobs/view/4461912320/
Posted age as shown: 17 hours ago
Location as shown: Brazil
Workplace type as shown: Hybrid, with the posting text stating hybrid or remote from other Brazilian regions
Employment type as shown: Full-time
Visible applicant count: 80 people clicked apply
Apply destination host: careers-madeiramadeira.icims.com
Posting language: pt
Company origin as shown: largest home-products platform in Latin America; origin not stated explicitly
Segment: not observable as br-pj; Brazilian-company evidence only, posting states full-time, not PJ
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
VEM PRA MADEIRA!!! 🧡🦒

Na MadeiraMadeira, acreditamos no poder de reinventar reinventar casas, histórias e, principalmente, pessoas.

Aqui, crescer é parte da jornada. Se você quer ser protagonista, aprender na prática, colaborar ao lado pessoas incríveis e construir projetos que deixem um legado significativo na nossa história seu lugar é aqui com a gente.

Sobre a vaga

A Diretoria de Tecnologia da MadeiraMadeira é composta por mais de 250 pessoas engajadas e determinadas em gerar valor com as melhores soluções em tecnologia e engenharia de dados. Aqui você vai encontrar uma galera apaixonada pelas tendências de tecnologia e que está super disposta a compartilhar conhecimento para crescermos juntos!

Modelo de trabalho Híbrido ou remoto demais regiões do Brasil.

Localização Curitiba/São Paulo

✨Atividades que você vai protagonizar

Atuar no desenvolvimento e manutenção dos sistemas que estão sob responsabilidade do time;
Atuar nas demandas que forem priorizadas para o time;
Entender e resolver de problemas;
Monitorar proativamente indicadores técnicos;
Trabalhar em conjunto com o time para criar as melhores soluções;
Participar das reuniões/cerimônias do time; 
Colaborar com a liderança;
Compartilhar com o time as dúvidas e desafios do dia-a-dia.
Organização de suas atividades considerando maior prioridade e impacto no cliente.

🪑 Para montar o ambiente dos sonhos, não pode faltar

Competências Técnicas/ Hard Skills

Node, Go e PHP 
Conhecimentos em arquiteturas de microsserviços e integrações com APIs
 Conhecimento em Git, Git flow, Docker;
 Otimização de performance.
Conhecimentos em Banco de dados relacionais SQL.

Competências Comportamentais/ Soft Skills

Boa comunicação
Visão sistêmica
Capacidade Analítica
Organização

 Formação Ensino superior em Sistemas da Informação, Ciência da Computação e relacionados completo

🎨 Um toque especial na nossa decoração

Conhecimentos de AWS.
Noções de front end 
Bancos de Dados não Relacionais 
Conhecimentos em Inteligência Artificial
Conhecimentos nas ferramentas AWS (Lambda, SQS, SNS, S3) 
Conhecimento de pipelines CI/CD 
Conhecimento em Monitoramento e Observabilidade 
```

## 5. Engenheiro de software

Company: Cubbo
Posting URL: https://www.linkedin.com/jobs/view/4462870975/
Posted age as shown: 19 hours ago
Location as shown: São Paulo, Brazil
Workplace type as shown: Hybrid, 2 days in person and 3 days remote
Employment type as shown: Full-time
Visible applicant count: 26 people clicked apply
Apply destination host: jobs.alcubbo.com
Posting language: pt
Company origin as shown: operates across Mexico and Brazil; based in Mexico City
Segment: not observable as us-direct, br-pj, or agency
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
Sobre a CUBBO
Somos a CUBBO, uma empresa apoiada por venture capital que constrói a infraestrutura do ecommerce — combinando tecnologia e logística para que as marcas escalem o comércio moderno.Apoiamos marcas conectando toda a jornada de pedidos — da compra à entrega — por meio de tecnologia e operações.Nossa plataforma atende centenas de marcas e processa +1M de pedidos por mês, entregando com velocidade e consistência.Trabalhamos a partir da Cidade do México, onde nossa equipe constrói ferramentas e capacidades logísticas para o comércio moderno.
Nossa Visão
Empoderar marcas para que conquistem liberdade, tornando-nos a plataforma presente em cada transação do comércio moderno.Não estamos aqui apenas para competir; estamos aqui para dominar e redefinir o futuro do comércio moderno. Se você é um jogador AAA, a CUBBO oferece uma plataforma incomparável para fazer parte dessa transformação.
Nossa Missão
Ajudamos o comércio moderno a reduzir fricção e entregar melhores experiências de compra. Nossa plataforma conecta toda a jornada de pedidos — da compra à entrega — por meio de tecnologia, operações e logística.
Localização
São Paulo, Brasil. Modelo híbrido: 2 dias presencial, 3 dias remotamente.
O Cargo
Como Software Engineer na Cubbo, você não estará apenas escrevendo código; você será o arquiteto da espinha dorsal que sustenta o e-commerce moderno na América Latina. Em um cenário onde processamos mais de 1 milhão de pedidos por mês, sua missão é construir sistemas resilientes, escaláveis e de alta performance que conectam o clique de compra do consumidor à entrega final em tempo recorde.Você terá a propriedade técnica de domínios críticos, influenciando diretamente a evolução da nossa plataforma tecnológica. Aqui, a velocidade é nossa aliada e a excelência técnica é o requisito mínimo para quem deseja dominar o mercado. Você será peça-chave para transformar desafios logísticos complexos em soluções de software elegantes que impulsionam o crescimento de marcas globais.Buscamos um talento que se sinta dono do produto, que questione o status quo e que tenha a ambição de deixar um legado na infraestrutura do comércio digital. Se você prospera em ambientes dinâmicos e quer ver o impacto real do seu trabalho em cada pacote que sai de nossos centros de distribuição, o seu lugar é aqui.
Responsabilidades Principais
**Arquitetura e Desenvolvimento**• Desenvolver e manter microsserviços escaláveis utilizando Node.js e tecnologias modernas de nuvem.• Desenhar arquiteturas de sistemas que suportem o alto volume de transações e a complexidade da logística de e-commerce.• Garantir a qualidade do código através de code reviews rigorosos, testes automatizados e boas práticas de engenharia.
**Liderança Técnica e Mentoria**• Liderar discussões técnicas e tomadas de decisão sobre stack tecnológica e padrões de design.• Mentorar engenheiros menos experientes, elevando o nível técnico de todo o time de engenharia.• Promover a cultura de DevOps e automação dentro da estrutura de desenvolvimento.
**Excelência Operacional**• Otimizar a performance de sistemas críticos para garantir baixa latência e alta disponibilidade.• Colaborar estreitamente com times de produto e operações para traduzir necessidades de negócio em soluções técnicas robustas.• Monitorar e agir proativamente sobre a saúde dos sistemas em produção.
Habilidades e Competências
• Mentalidade de Ownership (sentimento de dono) para assumir problemas do início ao fim.• Orientação a resultados com foco constante na experiência do cliente final.• Comunicação clara e assertiva para articular ideias técnicas complexas para stakeholders não técnicos.• Resiliência e adaptabilidade para brilhar no ritmo acelerado de uma startup em hiper-crescimento.
Hard Skills
• Domínio avançado de Ruby e Typescript.• Experiência sólida em arquitetura de microsserviços e sistemas distribuídos.• Conhecimento profundo em bancos de dados SQL relacionais.• Proficiência em serviços de nuvem (AWS ou Google Cloud Platform).• Experiência com mensageria e processamento de eventos (RabbitMQ, Kafka ou Pub/Sub).• Domínio de práticas de CI/CD.
Desejável
• Experiência prévia em empresas de logística, fintech ou e-commerce de alto volume.• Conhecimento em tecnologias de frontend moderno (React.js).• Inglês ou Espanhol avançado para colaboração com times internacionais (México e Espanha).• Experiência com Kubernetes e orquestração de containers.
```
Conhecimento em arquitetura moderna de aplicações web.
… more
About the company
Avanade
607,134 followers

Follow
IT Services and IT Consulting
 • 10001+ employees
 • 16,958 on LinkedIn
Avanade is the world’s leading expert on Microsoft. Trusted by over 7,000 clients worldwide, we deliver AI-driven solutions that unlock the full potential of people and technology, optimize operations, foster innovation and drive growth.
```

## 11. Senior Full-Stack Engineer - Trading API

Company: Jobgether
Posting URL: https://www.linkedin.com/jobs/view/4461922727/
Posted age as shown: 12 hours ago
Location as shown: Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: 8 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: en
Company origin as shown: not stated; partner company and globally distributed team
Segment: agency
Apparent duplicate of existing file: `jobgether-backend-core-apis.md`, same company but different title and URL

Full posting text quoted verbatim:

```text
About the job
This position is listed on behalf of a partner company, who manages all applications and next steps. Our partner is looking for a Senior Full-Stack Engineer - Trading API based in Brazil.

Join a globally distributed engineering team building developer-focused infrastructure for modern financial services and digital trading.

As part of the Trading API team, you will build end-to-end experiences spanning sophisticated frontend interfaces and high-performance backend financial systems.

Your work will help power products used by millions of users and support trading activity across a broad range of financial assets.

You will work across domains including payments, trading, market data, and account infrastructure while contributing to API and product development.

The role combines hands-on engineering with architectural ownership, giving you the opportunity to shape scalable systems and elegant user experiences.

You will collaborate closely with product, engineering, and other stakeholders while taking ownership of high-visibility projects from design through deployment.

This is an ideal opportunity for a senior engineer who enjoys full-stack development, financial technology, and solving complex problems at significant scale.

Accountabilities

Architect, design, implement, and maintain scalable software solutions across the frontend and backend stack.
Develop high-quality product features and user experiences for Trading API customers, spanning trading dashboards and backend services.
Work deeply with financial systems and infrastructure covering areas such as payments, trading, market data, and account management.
Contribute to API design and the development of new capabilities across the broader product ecosystem.
Build performant, intuitive, and visually polished frontend experiences using TypeScript, React, HTML, and modern CSS frameworks.
Develop reliable backend services and components using Golang or another modern systems programming language.
Translate stakeholder and customer requirements into complete, production-ready features.
Own high-visibility projects throughout their lifecycle, from technical design and implementation through testing, deployment, and ongoing improvement.
Collaborate with cross-functional teams to identify technical solutions that balance product requirements, scalability, performance, and maintainability.
Mentor fellow engineers and contribute to technical direction, architectural decisions, and engineering best practices.
Continuously improve the quality, performance, usability, and reliability of systems supporting financial products and services.

Requirements

5+ years of professional full-stack software development experience.
Strong professional experience with Golang and TypeScript/React, with the ability to work effectively across both backend and frontend technologies.
Proficiency in TypeScript and React, including experience creating intuitive, responsive, and performant user interfaces.
Strong knowledge of HTML and modern CSS frameworks, particularly TailwindCSS or comparable technologies.
Proficiency in at least one modern systems programming language such as Golang or C#.
Solid experience with SQL and relational databases, preferably PostgreSQL.
Strong understanding of REST APIs and API design best practices.
Excellent communication and collaboration skills, with the ability to work effectively with technical and non-technical stakeholders.
Demonstrated ability to gather, clarify, and translate stakeholder requirements into well-designed, fully implemented features.
Strong attention to detail and appreciation for design quality, usability, and polished user experiences.
Ability to take ownership of complex projects and drive them from initial design through successful deployment.
Experience working with cloud platforms, preferably Google Cloud Platform, is a plus.
Experience with Docker and Kubernetes is advantageous.
Knowledge of financial markets or experience in fintech is a strong plus.
Experience with algorithmic trading, whether professionally or through personal projects, is advantageous.
Previous experience in a startup or rapidly growing technology environment is a plus.
Experience working effectively in a fully remote environment is beneficial.
Curious, accountable, empathetic, and comfortable taking initiative in a globally distributed team.

Benefits

Competitive salary and stock options.
Health benefits.
$500 one-time home-office setup allowance for new hires.
$150 monthly stipend provided through a company expense card.
Fully remote working environment.
Opportunity to build infrastructure and products supporting millions of users and substantial trading activity.
```

## 12. Engenheiro de Software Node.js - Remote Work

Company: BairesDev
Posting URL: https://www.linkedin.com/jobs/view/4461949690/
Posted age as shown: 1 hour ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: 1 person clicked apply
Apply destination host: applicants.bairesdev.com
Posting language: pt
Company origin as shown: global team, 50 countries, Americas and Caribbean
Segment: agency
Apparent duplicate of existing file: `indi-node-developer.md` is a different company; no exact duplicate found
English fluency requirement: Nível avançado de inglês

Full posting text quoted verbatim:

```text
About the job
At BairesDev®, we've been leading the way in technology projects for over 15 years. We deliver cutting-edge solutions to giants like Google and the most innovative startups in Silicon Valley.
Our diverse 4,000+ team, composed of the world's Top 1% of tech talent, works remotely on roles that drive significant impact worldwide.
When you apply for this position, you're taking the first step in a process that goes beyond the ordinary. We aim to align your passions and skills with our vacancies, setting you on a path to exceptional career development and success.
Engenheiro de Software Node.js at BairesDev
Desenvolva e mantenha aplicações backend usando Node.js para entregar soluções eficientes e escaláveis. Esta função foca na construção de sistemas server-side, colaboração com equipes multifuncionais e implementação de práticas modernas de desenvolvimento para criar APIs e serviços robustos que apoiam objetivos de negócio.
O Que Você Fará:
- Projetar, desenvolver e manter aplicações Node.js e serviços backend.- Escrever código limpo e eficiente seguindo melhores práticas Node.js e padrões de codificação.- Construir e integrar APIs RESTful e microsserviços com bancos de dados e sistemas de terceiros.- Colaborar com desenvolvedores frontend e outros membros da equipe para entregar soluções completas.- Participar de revisões de código e contribuir para iniciativas de melhoria contínua.- Fazer debug e otimizar aplicações para garantir performance e confiabilidade.
O Que Procuramos:
- 3+ anos de experiência com desenvolvimento Node.js.- Sólido conhecimento de JavaScript/TypeScript e programação assíncrona.- Experiência com Express.js ou frameworks backend similares.- Familiaridade com tecnologias de banco de dados e princípios de design de APIs.- Compreensão de melhores práticas de desenvolvimento de software e metodologias de testes.- Nível avançado de inglês.
How we do make your work (and your life) easier:
- 100% remote work (from anywhere).- Excellent compensation in USD or your local currency if preferred- Hardware and software setup for you to work from home.- Flexible hours: create your own schedule.- Paid parental leaves, vacations, and holidays.- Innovative and multicultural work environment: collaborate and learn from the global Top 1% of talent.- Supportive environment with mentorship, promotions, skill development, and diverse growth opportunities.
Apply now and become part of a global team where your unique talents can truly thrive!
```

## 13. Desenvolvedor(a) Backend Pleno - (Node.js)

Company: Capco
Posting URL: https://www.linkedin.com/jobs/view/4462884395/
Posted age as shown: 18 hours ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Hybrid
Employment type as shown: Full-time
Visible applicant count: 39 people clicked apply
Apply destination host: job-boards.greenhouse.io
Posting language: pt
Company origin as shown: global consultancy with 40 offices in the Americas, Europe, and Asia-Pacific
Segment: agency
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
SOBRE A CAPCO

A Capco é uma consultoria global de tecnologia e gestão especializada na transformação digital, oferecendo soluções inovadoras e orientadas por dados para um portfólio crescente de mais de 100 clientes globais, entre eles bancos, pagamentos, mercados de capitais, gestão de patrimônio e ativos, seguros e setor de energia.

Nos destacamos pela abordagem personalizada, focada na construção de parcerias estratégicas de longo prazo e na aceleração de iniciativas digitais. Nossa expertise ganha vida por meio dos Innovation Labs e da cultura premiada #BeYourselfAtWork, que valoriza a diversidade e o talento.

Com presença global nos principais centros financeiros - temos 40 escritórios nas Américas, Europa e Ásia-Pacífico - estamos comprometidos em oferecer soluções práticas e integradas, promovendo colaboração e confiança em cada projeto. Se criatividade e inovação são sua paixão, a Capco é ideal para você. Vamos te apoiar e ajudar a acelerar sua carreira!

Missão: Como Desenvolvedor Backend PLENO, você será responsável por liderar o desenvolvimento e a implementação de soluções robustas e escaláveis para nossos serviços backend, garantindo alta disponibilidade, performance e segurança.

Responsabilidades

Desenvolver e manter serviços backend utilizando Node.js/TypeScript e Nest.js.
Trabalhar com bancos de dados relacionais e não-relacionais para garantir a integridade e eficiência dos dados.
Implementar arquiteturas de microserviços e garantir a comunicação eficiente entre eles.
Utilizar computação em nuvem, especialmente no Google Cloud Platform (GCP), para hospedar e escalar serviços.
Implementar programação assíncrona e mensageria utilizando RabbitMQ, Kafka, PubSub, entre outros.
Utilizar Docker e Kubernetes para orquestração de contêineres e garantir a portabilidade e escalabilidade dos serviços.
Gerenciar controle de versão utilizando GIT e colaborar em equipe seguindo metodologias ágeis.
Configurar processos de CI/CD com Jenkins, pipelines e outras ferramentas para garantir um deploy contínuo e automatizado.
Escrever testes unitários e end-to-end com Jest e Cypress para garantir a qualidade do código.
Utilizar BigQuery para análise e processamento de grandes volumes de dados. O que você precisa ter:
Experiência sólida em desenvolvimento backend utilizando Node.js/TypeScript.
Conhecimento prático em bancos de dados relacionais e não-relacionais.
Experiência comprovada em arquiteturas de microserviços e desenvolvimento utilizando Nest.js.
Familiaridade com computação em nuvem, especialmente no Google Cloud Platform (GCP).
Experiência em programação assíncrona e uso de mensageria.
Conhecimento em Docker e Kubernetes para orquestração de contêineres.
Experiência com controle de versão utilizando GIT e metodologias ágeis.
Vivência em processos de deploy contínuo com Jenkins e pipelines.
Habilidade em escrever testes unitários e end-to-end para garantir a qualidade do código.
Familiaridade com BigQuery para análise de dados.
Conhecimento em Python para ampliar as capacidades de desenvolvimento.
Noções em práticas DevOps para integração e entrega contínua.
Conhecimento em Clean Architecture e GitFlow.
Familiaridade com princípios S.O.L.I.D. de desenvolvimento de software.
```

## 14. Growth Engineer

Company: FX Replay
Posting URL: https://www.linkedin.com/jobs/view/4460738294/
Posted age as shown: 22 hours ago
Location as shown: Brazil
Workplace type as shown: Remote
Employment type as shown: Full-time
Visible applicant count: 70 applicants
Apply destination host: www.linkedin.com (Easy Apply)
Posting language: en
Company origin as shown: not stated; international environment stated
Segment: not observable as us-direct, br-pj, or agency
Apparent duplicate of existing file: none
English fluency requirement: Professional English proficiency

Full posting text quoted verbatim:

```text
About the job
GROWTH ENGINEER
⚠️ PLEASE READ BEFORE APPLYING
To be considered for this role, candidates must meet the following requirements:• Professional English proficiency. You must be comfortable communicating clearly and confidently in English in a fully remote, international environment.• A personal portfolio website is required. Your portfolio should showcase real, live web projects you have designed and/or built, with links to the actual work whenever possible. GitHub profiles, Behance/Dribbble profiles, or a list of repositories alone will not be considered a portfolio.• Hands-on AI-native development experience. This role requires practical experience with Claude Code and AI-native development workflows. Using AI only for basic code generation or autocomplete is not sufficient.Applications that do not meet the requirements above will not be considered.
ABOUT THE ROLE
FX Replay is looking for a Growth Engineer to join our Growth organization and own the technical execution of our web, acquisition, experimentation, and conversion infrastructure.This is not a traditional marketing role and not a core product engineering role.You will operate at the intersection of growth, software engineering, web design, analytics, infrastructure, experimentation, and AI-native development.You should be capable of taking a growth opportunity from idea to production independently: understanding the business objective, designing the experience, building it, integrating the required systems, instrumenting analytics, deploying it, and measuring the outcome.
WHAT YOU'LL OWN
• Build and evolve FX Replay's marketing and growth web experiences using Astro, React, TypeScript, HTML, and CSS.• Create high-quality landing pages, acquisition flows, pricing experiences, onboarding surfaces, and conversion experiments.• Translate ideas and business objectives into polished experiences without requiring constant engineering or design support.• Integrate APIs, payments, authentication, CRM, CMS, marketing platforms, analytics systems, and third-party services.• Own advanced web analytics and tracking architecture, including events, attribution, funnels, conversion tracking, experimentation, and data quality.• Design and execute A/B tests and growth experiments from implementation through measurement.• Own Core Web Vitals, performance, caching, CDN/edge behavior, rendering strategies, technical SEO, structured data, and accessibility.• Understand and operate the supporting infrastructure, including DNS, CDN, hosting, CI/CD, observability, security, and production reliability.• Build and maintain reusable components, design systems, tokens, and patterns for rapid experimentation.
AI-NATIVE GROWTH
AI should be a fundamental part of how you operate.We expect deep practical experience with:• Claude Code as a primary environment for building and operating software.• Creating and orchestrating AI agents for research, development, analytics, testing, and optimization.• Building reusable Skills, commands, instructions, and agent workflows.• Connecting agents to external systems through MCP servers.• Designing workflows where multiple agents can independently research, build, validate, and improve growth initiatives.• Using AI-native design tools alongside Figma and modern design systems.• Using agents to investigate analytics, generate experiments, analyze performance, debug production issues, and accelerate iteration.Using AI to autocomplete code is not enough. We expect you to understand how to design systems of agents that materially increase your execution capacity.
WHAT WE'RE LOOKING FOR
• 5–8+ years of strong technical experience building production web systems.• Deep expertise in JavaScript, TypeScript, React, modern browser technologies, HTML, and CSS.• Strong understanding of APIs, HTTP, networking, caching, CDNs, cloud infrastructure, and web architecture.• Proven experience with high-performance and high-traffic web experiences.• Deep experience with GA4, GTM, PostHog/Amplitude, Segment/CDPs, attribution, event instrumentation, and experimentation platforms.• Strong understanding of conversion optimization, experimentation, funnels, and growth analytics.• Strong visual and product judgment, including Figma, responsive design, interaction design, typography, hierarchy, and design systems.• Strong knowledge of technical SEO, performance, accessibility, observability, and security.• Advanced practical experience with Claude Code, AI agents, Skills, MCPs, and AI-native development workflows.• Ability to operate independently from growth opportunity → design → implementation → instrumentation → deployment → analysis → iteration.
IDEAL PROFILE
You are a technically exceptional Growth Engineer who can operate across marketing, design, software, data, and infrastructure.You do not need an engineer to implement your experiments, a designer to solve every interface decision, or an analyst to tell you whether something worked.You can understand a growth problem, build the complete solution, measure its impact, and continuously improve it.Your leverage comes not only from your technical depth, but from your ability to combine engineering, growth judgment, design quality, analytics, and AI-native execution.
```

## 15. Desenvolvedor(a) Front-End Sênior | React | Híbrido - São Paulo

Company: Avanade
Posting URL: https://www.linkedin.com/jobs/view/4454348218/
Posted age as shown: Reposted 3 hours ago
Location as shown: São Paulo, São Paulo, Brazil
Workplace type as shown: Hybrid
Employment type as shown: Full-time
Visible applicant count: Over 100 people clicked apply
Apply destination host: avanade.com
Posting language: pt
Company origin as shown: global Microsoft expert; worldwide company, 10,001+ employees
Segment: agency
Recruiter: Gabriel Gomes Rodrigues, `Senior Frontend Developer @ Avanade | Tech Leader | Next.js | React | React Native | TypeScript`
Apparent duplicate of existing file: none

Full posting text quoted verbatim:

```text
About the job
Como Desenvolvedor(a) Front-End Sênior, você atuará no desenvolvimento e evolução de soluções digitais voltadas para monetização, publicidade e experiência do usuário. Esta posição tem papel fundamental na construção de integrações com Google Ad Manager (GAM), garantindo a correta gestão, entrega e performance de campanhas publicitárias em plataformas digitais.

Você fará parte de um ambiente colaborativo e inovador, contribuindo com soluções modernas utilizando React e tecnologias associadas, apoiando a transformação digital dos clientes da Avanade.

Venha fazer parte de uma equipe que combina tecnologia, inovação e excelência técnica para construir soluções digitais de alto impacto. Aqui, você terá a oportunidade de trabalhar com tecnologias modernas, participar de projetos estratégicos e desenvolver sua carreira em um ambiente colaborativo e orientado ao aprendizado contínuo. Together we do what matters.

Responsabilidades

Desenvolver e evoluir aplicações front-end utilizando React e TypeScript;
Implementar integrações com Google Ad Manager (GAM);
Construir interfaces performáticas, responsivas e escaláveis;
Integrar aplicações com APIs e serviços externos;
Participar da implementação e otimização de soluções de monetização digital;
Atuar na configuração e gerenciamento de componentes relacionados à entrega de anúncios;
Investigar e solucionar problemas relacionados à exibição, segmentação e performance de campanhas publicitárias;
Colaborar com squads ágeis na definição e implementação de soluções técnicas;
Garantir a qualidade, manutenção e evolução contínua das aplicações.

Qualifications

Habilidades e experiências

Requisitos obrigatórios

Experiência sólida com React;
Experiência com TypeScript;
Experiência com integração de APIs;
Experiência prática com Google Ad Manager (GAM);
Conhecimento em Line Items, Ad Units (Blocos de anúncios), Key Values e Targeting, Google Publisher Tag (GPT), Criativos de imagem, HTML5, nativos e third-party; 
Conhecimento em campanhas Display e Vídeo;
Experiência com integrações utilizando a API SOAP do Google Ad Manager;
Capacidade de diagnosticar e resolver problemas relacionados à entrega e exibição de anúncios;
Perfil hands-on e orientado à solução.
Forte capacidade analítica e de troubleshooting;
Autonomia técnica e senso de responsabilidade; 

Diferenciais

Experiência com Next.js;
Experiência com Node.js e/ou NestJS;
Conhecimento em arquitetura cloud, preferencialmente AWS;
Vivência em plataformas de AdTech, Media ou grandes Publishers;
Conhecimento em arquitetura moderna de aplicações web.
```
