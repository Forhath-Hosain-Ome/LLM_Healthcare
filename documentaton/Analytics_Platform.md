# Healthcare Analytics Platform - Complete Architecture & Setup Guide

## 📋 Table of Contents
1. [Technology Stack](#technology-stack)
2. [Directory Structure](#directory-structure)
3. [Library Requirements](#library-requirements)
4. [Docker Compose Configuration](#docker-compose-configuration)
5. [Getting Started - Local Setup](#getting-started---local-setup)
6. [Security Architecture](#security-architecture)
7. [Data Flow Architecture](#data-flow-architecture)
8. [Deployment Strategy](#deployment-strategy)
9. [Scalability Considerations](#scalability-considerations)
10. [Development Workflow](#development-workflow)
11. [Next Steps Roadmap](#next-steps-roadmap)

---

## 🏗️ Technology Stack

### Backend Architecture
- **Django 5.1** (Core API, Admin, Auth, CRUD)
- **Django REST Framework 3.15** (REST APIs)
- **FastAPI 0.115** (ML inference microservices)
- **Celery 5.4** (Async tasks, scheduled jobs)
- **RabbitMQ 3.13** (Message broker)

### Frontend
- **React 18.3** (SPA)
- **TypeScript 5.3**
- **Vite 5.0** (Build tool)
- **TanStack Query v5** (Data fetching)
- **Recharts + D3.js + Plotly** (Visualizations)
- **Tailwind CSS 3.4**

### Databases
- **PostgreSQL 16** + **TimescaleDB 2.14** (Primary + time-series)
- **MongoDB 7.0** (Unstructured clinical notes)
- **Redis 7.2** (Cache + Celery broker)

### ML/AI Stack
- **MLflow 2.10** (Model registry, tracking)
- **Apache Airflow 2.8** (ML pipeline orchestration)
- **LangChain 0.1** (LLM orchestration)
- **OpenAI API** (GPT-4 with HIPAA BAA)
- **scikit-learn 1.4, XGBoost 2.0, TensorFlow 2.15**
- **Feast 0.38** (Feature store)

### Integration Layer
- **Mirth Connect 4.4** (HL7v2 MLLP engine)
- **n8n 1.20** (Workflow automation, FHIR REST)
- **HAPI FHIR 6.10** (FHIR server - Java)

### DevOps (Basic Level)
- **Docker 24.x + Docker Compose**
- **GitHub Actions** (CI/CD)
- **Nginx** (Reverse proxy)
- **Portainer** (Docker management UI)

### Monitoring & Observability
- **Prometheus 2.48** (Metrics)
- **Grafana 10.2** (Dashboards)
- **ELK Stack** (Elasticsearch 8.11, Logstash, Kibana)
- **Sentry** (Error tracking)

### Security & Compliance
- **Django Guardian** (Object-level permissions)
- **django-cryptography** (Field-level encryption)
- **django-audit-log** (Audit trail)
- **python-decouple** (Environment variables)

---

## 📁 Complete Directory Structure

```
healthcare-analytics-platform/
│
├── 📦 backend/                          # Django + FastAPI Backend
│   ├── 📁 config/                       # Django project settings
│   │   ├── __init__.py
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py                 # Base settings
│   │   │   ├── development.py          # Local dev settings
│   │   │   ├── production.py           # Production settings
│   │   │   └── testing.py              # Test settings
│   │   ├── urls.py                     # Root URL config
│   │   ├── wsgi.py                     # WSGI entry point
│   │   └── asgi.py                     # ASGI entry point (WebSocket support)
│   │
│   ├── 📁 apps/                         # Django apps (modular)
│   │   │
│   │   ├── 📁 core/                     # Core utilities, base models
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Abstract base models (TimeStampedModel, etc.)
│   │   │   ├── permissions.py          # Custom permission classes
│   │   │   ├── mixins.py               # Reusable mixins
│   │   │   ├── validators.py           # Custom validators
│   │   │   └── utils.py                # Utility functions
│   │   │
│   │   ├── 📁 authentication/           # User auth, RBAC
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # User, Role, Permission models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── permissions.py          # RBAC logic
│   │   │   ├── backends.py             # Custom auth backends
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 patients/                 # Patient management
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Patient, Allergy, Problem, SocialHistory
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── filters.py              # Django-filter classes
│   │   │   ├── signals.py              # Post-save signals
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 admissions/               # Hospital admissions
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Admission, DischargeSummary
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services.py             # Business logic layer
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 clinical/                 # Clinical data (vitals, labs, procedures)
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # VitalSigns, LabResult, Procedure
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 medications/              # Medication management
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Medication, DrugInteraction, Contraindication
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services.py             # Drug interaction checking logic
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 providers/                # Healthcare providers
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Provider, ProviderNote
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 organizations/            # Hospital org structure
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Organization, Department, Unit, Bed
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 predictions/              # ML prediction scores
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # PredictionScore, PredictionModel, ModelVersion
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services.py             # Prediction trigger logic
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 alerts/                   # Clinical alerts system
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Alert, AlertAcknowledgment
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services.py             # Alert generation logic
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 recommendations/          # Clinical recommendations
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Recommendation, ClinicalGuideline
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 analytics/                # Cohorts, dashboards, metrics
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # Cohort, Dashboard, Metric
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services.py             # Complex analytics queries
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 integrations/             # EHR integration endpoints
│   │   │   ├── __init__.py
│   │   │   ├── views.py                # Webhook receivers for HL7/FHIR
│   │   │   ├── urls.py
│   │   │   ├── parsers.py              # HL7/FHIR parsers
│   │   │   ├── tasks.py                # Celery tasks for data ingestion
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 nlp/                      # Clinical NLP services
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # ClinicalEntity
│   │   │   ├── services.py             # NER extraction logic
│   │   │   ├── tasks.py                # Async NLP processing
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 audit/                    # Audit logging
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # AuditLog
│   │   │   ├── middleware.py           # Auto-logging middleware
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │   │
│   │   └── 📁 terminology/              # Medical coding (ICD-10, LOINC, CPT)
│   │       ├── __init__.py
│   │       ├── models.py               # ICD10Code, LOINCCode, CPTCode
│   │       ├── serializers.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       ├── loaders.py              # Code set data loaders
│   │       └── tests.py
│   │
│   ├── 📁 ml_services/                  # FastAPI microservices for ML
│   │   │
│   │   ├── 📁 readmission_service/      # Readmission prediction
│   │   │   ├── __init__.py
│   │   │   ├── main.py                 # FastAPI app
│   │   │   ├── models.py               # Pydantic models
│   │   │   ├── inference.py            # Model inference logic
│   │   │   ├── preprocessing.py        # Feature engineering
│   │   │   ├── config.py               # Service config
│   │   │   └── tests/
│   │   │
│   │   ├── 📁 sepsis_service/           # Sepsis prediction
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   ├── models.py
│   │   │   ├── inference.py
│   │   │   ├── preprocessing.py
│   │   │   └── tests/
│   │   │
│   │   ├── 📁 los_service/              # Length-of-stay forecasting
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   ├── models.py
│   │   │   ├── inference.py
│   │   │   └── tests/
│   │   │
│   │   └── 📁 nlq_service/              # Natural language query (LLM)
│   │       ├── __init__.py
│   │       ├── main.py
│   │       ├── models.py
│   │       ├── llm_client.py           # OpenAI/LangChain wrapper
│   │       ├── sql_generator.py        # NL to SQL translation
│   │       ├── safety_filters.py       # Hallucination prevention
│   │       ├── prompts.py              # LLM prompt templates
│   │       └── tests/
│   │
│   ├── 📁 celery_app/                   # Celery configuration
│   │   ├── __init__.py
│   │   ├── celery.py                   # Celery app initialization
│   │   ├── tasks.py                    # Shared tasks
│   │   ├── schedules.py                # Periodic task schedules
│   │   └── beat_schedule.py            # Celery Beat config
│   │
│   ├── 📁 scripts/                      # Utility scripts
│   │   ├── seed_database.py            # Sample data seeding
│   │   ├── load_medical_codes.py       # ICD-10/LOINC/CPT loaders
│   │   ├── create_superuser.py
│   │   └── migrate_legacy_data.py
│   │
│   ├── 📁 tests/                        # Integration tests
│   │   ├── __init__.py
│   │   ├── test_integration.py
│   │   ├── test_e2e.py
│   │   ├── factories.py                # Factory Boy factories
│   │   └── fixtures/
│   │
│   ├── manage.py                        # Django management
│   ├── requirements/
│   │   ├── base.txt                    # Base dependencies
│   │   ├── development.txt             # Dev dependencies
│   │   ├── production.txt              # Production deps
│   │   └── testing.txt                 # Test deps
│   ├── pytest.ini                       # Pytest configuration
│   ├── .env.example                     # Environment variables template
│   └── README.md
│
├── 📦 frontend/                         # React Frontend
│   ├── 📁 public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── assets/
│   │
│   ├── 📁 src/
│   │   │
│   │   ├── 📁 components/               # Reusable components
│   │   │   ├── 📁 common/              # Common UI components
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Card.tsx
│   │   │   │   ├── Modal.tsx
│   │   │   │   ├── Table.tsx
│   │   │   │   ├── Loading.tsx
│   │   │   │   ├── ErrorBoundary.tsx
│   │   │   │   └── index.ts
│   │   │   │
│   │   │   ├── 📁 forms/               # Form components
│   │   │   │   ├── Input.tsx
│   │   │   │   ├── Select.tsx
│   │   │   │   ├── DatePicker.tsx
│   │   │   │   ├── FormField.tsx
│   │   │   │   └── index.ts
│   │   │   │
│   │   │   ├── 📁 layout/              # Layout components
│   │   │   │   ├── Navbar.tsx
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   ├── Footer.tsx
│   │   │   │   ├── Header.tsx
│   │   │   │   └── DashboardLayout.tsx
│   │   │   │
│   │   │   ├── 📁 charts/              # Chart components
│   │   │   │   ├── LineChart.tsx
│   │   │   │   ├── BarChart.tsx
│   │   │   │   ├── HeatMap.tsx
│   │   │   │   ├── TimeSeriesChart.tsx
│   │   │   │   └── index.ts
│   │   │   │
│   │   │   └── 📁 widgets/             # Dashboard widgets
│   │   │       ├── RiskAlertWidget.tsx
│   │   │       ├── PatientCensusWidget.tsx
│   │   │       ├── KPICard.tsx
│   │   │       └── index.ts
│   │   │
│   │   ├── 📁 features/                 # Feature modules
│   │   │   │
│   │   │   ├── 📁 authentication/
│   │   │   │   ├── Login.tsx
│   │   │   │   ├── Logout.tsx
│   │   │   │   ├── ResetPassword.tsx
│   │   │   │   ├── authSlice.ts        # Redux slice
│   │   │   │   └── authService.ts      # API calls
│   │   │   │
│   │   │   ├── 📁 patients/
│   │   │   │   ├── PatientList.tsx
│   │   │   │   ├── PatientDetail.tsx
│   │   │   │   ├── PatientTimeline.tsx
│   │   │   │   ├── PatientSearch.tsx
│   │   │   │   ├── patientsSlice.ts
│   │   │   │   └── patientsService.ts
│   │   │   │
│   │   │   ├── 📁 admissions/
│   │   │   │   ├── AdmissionList.tsx
│   │   │   │   ├── AdmissionDetail.tsx
│   │   │   │   ├── DischargeForm.tsx
│   │   │   │   ├── admissionsSlice.ts
│   │   │   │   └── admissionsService.ts
│   │   │   │
│   │   │   ├── 📁 clinical/
│   │   │   │   ├── VitalSignsChart.tsx
│   │   │   │   ├── LabResultsTable.tsx
│   │   │   │   ├── ProceduresList.tsx
│   │   │   │   └── clinicalService.ts
│   │   │   │
│   │   │   ├── 📁 predictions/
│   │   │   │   ├── RiskScoreCard.tsx
│   │   │   │   ├── PredictionExplanation.tsx
│   │   │   │   ├── ModelPerformance.tsx
│   │   │   │   └── predictionsService.ts
│   │   │   │
│   │   │   ├── 📁 alerts/
│   │   │   │   ├── AlertList.tsx
│   │   │   │   ├── AlertDetail.tsx
│   │   │   │   ├── AlertNotifications.tsx
│   │   │   │   ├── alertsSlice.ts
│   │   │   │   └── alertsService.ts
│   │   │   │
│   │   │   ├── 📁 dashboards/
│   │   │   │   ├── 📁 clinical/
│   │   │   │   │   ├── ClinicalDashboard.tsx
│   │   │   │   │   ├── PatientCensusView.tsx
│   │   │   │   │   └── RiskAlertPanel.tsx
│   │   │   │   │
│   │   │   │   ├── 📁 operations/
│   │   │   │   │   ├── OperationsDashboard.tsx
│   │   │   │   │   ├── BedManagement.tsx
│   │   │   │   │   ├── StaffingView.tsx
│   │   │   │   │   └── CapacityPlanning.tsx
│   │   │   │   │
│   │   │   │   ├── 📁 executive/
│   │   │   │   │   ├── ExecutiveDashboard.tsx
│   │   │   │   │   ├── QualityMetrics.tsx
│   │   │   │   │   ├── FinancialMetrics.tsx
│   │   │   │   │   └── BenchmarkReports.tsx
│   │   │   │   │
│   │   │   │   └── 📁 analytics/
│   │   │   │       ├── AnalyticsDashboard.tsx
│   │   │   │       ├── ReportBuilder.tsx
│   │   │   │       ├── CohortAnalysis.tsx
│   │   │   │       └── CustomQueries.tsx
│   │   │   │
│   │   │   └── 📁 nlq/                  # Natural language query
│   │   │       ├── ChatInterface.tsx
│   │   │       ├── QueryHistory.tsx
│   │   │       ├── ResultsViewer.tsx
│   │   │       └── nlqService.ts
│   │   │
│   │   ├── 📁 hooks/                    # Custom React hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── usePatients.ts
│   │   │   ├── useAlerts.ts
│   │   │   ├── useWebSocket.ts
│   │   │   └── useDebounce.ts
│   │   │
│   │   ├── 📁 store/                    # Redux store
│   │   │   ├── store.ts
│   │   │   ├── rootReducer.ts
│   │   │   └── middleware.ts
│   │   │
│   │   ├── 📁 services/                 # API services
│   │   │   ├── api.ts                  # Axios instance config
│   │   │   ├── apiClient.ts            # Base API client
│   │   │   └── websocket.ts            # WebSocket client
│   │   │
│   │   ├── 📁 utils/                    # Utility functions
│   │   │   ├── dateUtils.ts
│   │   │   ├── formatters.ts
│   │   │   ├── validators.ts
│   │   │   └── constants.ts
│   │   │
│   │   ├── 📁 types/                    # TypeScript types
│   │   │   ├── patient.types.ts
│   │   │   ├── admission.types.ts
│   │   │   ├── clinical.types.ts
│   │   │   ├── prediction.types.ts
│   │   │   └── index.ts
│   │   │
│   │   ├── 📁 styles/                   # Global styles
│   │   │   ├── globals.css
│   │   │   ├── tailwind.css
│   │   │   └── variables.css
│   │   │
│   │   ├── 📁 routes/                   # React Router
│   │   │   ├── index.tsx
│   │   │   ├── PrivateRoute.tsx
│   │   │   └── routeConfig.ts
│   │   │
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── vite-env.d.ts
│   │
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── .env.example
│   └── README.md
│
├── 📦 ml_pipeline/                      # ML training & experimentation
│   ├── 📁 notebooks/                    # Jupyter notebooks
│   │   ├── 01_data_exploration.ipynb
│   │   ├── 02_feature_engineering.ipynb
│   │   ├── 03_model_training.ipynb
│   │   └── 04_model_evaluation.ipynb
│   │
│   ├── 📁 data/                         # Training data
│   │   ├── raw/
│   │   ├── processed/
│   │   └── features/
│   │
│   ├── 📁 models/                       # Trained model artifacts
│   │   ├── readmission/
│   │   ├── sepsis/
│   │   └── los_forecasting/
│   │
│   ├── 📁 src/                          # Training pipeline code
│   │   ├── 📁 data_preprocessing/
│   │   │   ├── __init__.py
│   │   │   ├── cleaners.py
│   │   │   ├── transformers.py
│   │   │   └── validators.py
│   │   │
│   │   ├── 📁 feature_engineering/
│   │   │   ├── __init__.py
│   │   │   ├── clinical_features.py
│   │   │   ├── temporal_features.py
│   │   │   └── aggregations.py
│   │   │
│   │   ├── 📁 training/
│   │   │   ├── __init__.py
│   │   │   ├── readmission_trainer.py
│   │   │   ├── sepsis_trainer.py
│   │   │   ├── los_trainer.py
│   │   │   └── base_trainer.py
│   │   │
│   │   ├── 📁 evaluation/
│   │   │   ├── __init__.py
│   │   │   ├── metrics.py
│   │   │   ├── validators.py
│   │   │   └── explainability.py       # SHAP values
│   │   │
│   │   └── 📁 deployment/
│   │       ├── __init__.py
│   │       ├── model_registry.py
│   │       └── versioning.py
│   │
│   ├── 📁 dags/                         # Airflow DAGs
│   │   ├── readmission_retraining_dag.py
│   │   ├── sepsis_retraining_dag.py
│   │   ├── data_quality_dag.py
│   │   └── feature_store_update_dag.py
│   │
│   ├── requirements.txt
│   └── README.md
│
├── 📦 integrations/                     # Integration services
│   │
│   ├── 📁 mirth_connect/                # HL7v2 engine
│   │   ├── channels/
│   │   │   ├── adt_inbound.xml         # HL7 ADT channel config
│   │   │   ├── oru_labs.xml            # HL7 ORU (labs) channel
│   │   │   └── mdm_documents.xml       # HL7 MDM (documents)
│   │   ├── code_templates/
│   │   └── README.md
│   │
│   ├── 📁 n8n_workflows/                # n8n automation workflows
│   │   ├── fhir_patient_sync.json      # FHIR patient data sync
│   │   ├── alert_notifications.json    # Alert routing to Slack/Teams
│   │   ├── report_generation.json      # Automated report generation
│   │   └── README.md
│   │
│   └── 📁 fhir_server/                  # HAPI FHIR server (optional)
│       ├── application.yaml
│       └── README.md
│
├── 📦 infrastructure/                   # Infrastructure as Code
│   │
│   ├── 📁 docker/                       # Docker configurations
│   │   ├── Dockerfile.backend          # Django backend
│   │   ├── Dockerfile.ml_service       # FastAPI ML services
│   │   ├── Dockerfile.frontend         # React frontend
│   │   ├── Dockerfile.celery           # Celery worker
│   │   ├── Dockerfile.airflow          # Airflow
│   │   └── docker-compose.yml          # Local development stack
│   │
│   ├── 📁 nginx/                        # Nginx configs
│   │   ├── nginx.conf
│   │   ├── ssl/
│   │   └── conf.d/
│   │       ├── backend.conf
│   │       └── frontend.conf
│   │
│   ├── 📁 scripts/                      # Setup scripts
│   │   ├── setup_dev_env.sh
│   │   ├── init_databases.sh
│   │   ├── seed_data.sh
│   │   └── backup.sh
│   │
│   └── 📁 monitoring/                   # Monitoring configs
│       ├── prometheus.yml
│       ├── grafana/
│       │   └── dashboards/
│       │       ├── system_metrics.json
│       │       ├── application_metrics.json
│       │       └── ml_model_metrics.json
│       └── elasticsearch/
│           └── logstash.conf
│
├── 📦 docs/                             # Documentation
│   ├── api/
│   │   ├── openapi.yaml                # OpenAPI 3.0 spec
│   │   └── postman_collection.json
│   ├── architecture/
│   │   ├── system_architecture.md
│   │   ├── data_flow.md
│   │   └── security_architecture.md
│   ├── deployment/
│   │   ├── local_setup.md
│   │   ├── docker_deployment.md
│   │   └── production_deployment.md
│   └── user_guides/
│       ├── clinician_guide.md
│       ├── operations_guide.md
│       └── admin_guide.md
│
├── 📦 .github/                          # GitHub Actions
│   └── workflows/
│       ├── backend_ci.yml
│       ├── frontend_ci.yml
│       ├── ml_pipeline_ci.yml
│       └── deploy.yml
│
├── .gitignore
├── .dockerignore
├── README.md
└── LICENSE