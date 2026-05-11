# Tableau Dashboard Examples

## Executive Summary Dashboard

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Executive FWA Command Center                                                 │
│ Enterprise Healthcare Fraud, Waste & Abuse Analytics Platform                │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Total Exposure │ │ Recovered $    │ │ Avg Risk Score │ │ Fraud Events   │
│ $14.2M         │ │ $4.8M          │ │ 87.4           │ │ 18,432         │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Exposure by Market Segment         │ │ Top High-Risk Providers             │
│                                    │ │                                     │
│  Treemap:                          │ │  Horizontal Bar Chart               │
│  - Medicare                        │ │  - Provider Name                    │
│  - Medicaid                        │ │  - Avg Risk Score                   │
│  - Commercial                      │ │  - Exposure Amount                  │
│  - Employer Groups                 │ │                                     │
└────────────────────────────────────┘ └─────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ Geographic Fraud Exposure Map                                                │
│                                                                              │
│  Bubble/Heat Map                                                             │
│  - Bubble Size = Exposure Amount                                             │
│  - Color = Risk Score                                                        │
│  - Tooltip = Claims, Exposure, Recoveries                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Specialty Risk Analysis            │ │ Recovery vs Exposure                │
│                                    │ │                                     │
│ Heatmap                            │ │ Scatter Plot                        │
│ - Specialty                        │ │ - X = Exposure                      │
│ - Avg Risk Score                   │ │ - Y = Recovered Amount              │
│ - Fraud Detection Count            │ │ - Size = Claim Volume               │
└────────────────────────────────────┘ └─────────────────────────────────────┘
```

---

## Fraud Exposure Dashboard

- Exposure by client, region, scheme, and month
- Paid/denied/stopped/recovered dollar waterfall
- Top investigations by financial impact

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Fraud Exposure Analytics                                                     │
│ Enterprise Exposure Monitoring                                               │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────-┐
│ Total Exposure │ │ Exposure Trend │ │ Avg Exposure   │ │ Exposure Growth │
│ $14.2M         │ │ +12.8%         │ │ $78K           │ │ +4.2% MoM       │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────-┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Monthly Exposure Trend             │ │ Exposure by Fraud Scheme            │
│                                    │ │                                     │
│ Line Chart                         │ │ Stacked Bar / Treemap               │
│ - Month                            │ │ - Upcoding                          │
│ - Exposure Amount                  │ │ - Doctor Shopping                   │
│ - Recovery Overlay                 │ │ - Phantom Billing                   │
└────────────────────────────────────┘ └─────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ Geographic Exposure Hotspots                                                 │
│                                                                              │
│ Density Map / Heatmap                                                        │
│ - Exposure Concentration                                                     │
│ - Suspicious Claim Bursts                                                    │
│ - Opioid Fraud Regions                                                       │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Exposure by Client                 │ │ Exposure by Provider Type           │
│                                    │ │                                     │
│ Horizontal Bars                    │ │ Donut / Packed Bubble               │
│ - Medicare                         │ │ - Physicians                        │
│ - Medicaid                         │ │ - Pharmacies                        │
│ - Commercial                       │ │ - Facilities                        │
└────────────────────────────────────┘ └─────────────────────────────────────┘
```

---

## Provider Risk Dashboard

- Provider risk score distribution
- Top provider outliers by specialty peer group
- Opioid claim rate and denied claim rate
- Investigation conversion status

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Provider Risk Surveillance Dashboard                                         │
│ SIU Operational Monitoring                                                   │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ High-Risk Prov │ │ Avg Risk Score │ │ Fraud Alerts   │ │ Recovered $    │
│ 248            │ │ 87.4           │ │ 1,284          │ │ $4.8M          │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ Top High-Risk Providers                                                      │
│                                                                              │
│ Horizontal Bar Chart                                                         │
│ - Provider Name                                                              │
│ - Risk Score                                                                 │
│ - Exposure Amount                                                            │
│ - Specialty                                                                  │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Specialty Risk Heatmap             │ │ Provider Risk Trend                 │
│                                    │ │                                     │
│ Heatmap                            │ │ Line Chart                          │
│ - Specialty                        │ │ - Month                             │
│ - Avg Risk Score                   │ │ - Avg Risk Score                    │
│ - Fraud Count                      │ │ - Detection Volume                  │
└────────────────────────────────────┘ └─────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ Provider Network Risk Distribution                                           │
│                                                                              │
│ Scatter Plot                                                                 │
│ - X = Exposure                                                               │
│ - Y = Recoveries                                                             │
│ - Color = Risk Score                                                         │
│ - Size = Claims                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Geographic Fraud Heatmap

- State/county fraud exposure
- Suspicious concentration clusters
- Pharmacy/provider collusion map

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Geographic Fraud Intelligence                                                │
│ Regional Exposure and Fraud Concentration Monitoring                         │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Fraud Regions  │ │ Exposure Total │ │ Avg Risk Score │ │ Hotspot Count  │
│ 42             │ │ $14.2M         │ │ 87.4           │ │ 18             │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ Fraud Exposure Heatmap                                                       │
│                                                                              │
│ Geographic Density / Bubble Map                                              │
│ - Exposure Concentration                                                     │
│ - Provider Clusters                                                          │
│ - Pharmacy Collusion Regions                                                 │
│ - Opioid Dispensing Hotspots                                                 │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ State-Level Exposure               │ │ County Risk Ranking                 │
│                                    │ │                                     │
│ Filled Map                         │ │ Horizontal Bars                     │
│ - State Color = Exposure           │ │ - County                            │
│ - Tooltip = Fraud Metrics          │ │ - Avg Risk Score                    │
└────────────────────────────────────┘ └─────────────────────────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Fraud Scheme Concentration         │ │ Geographic Trend Analysis           │
│                                    │ │                                     │
│ Treemap                            │ │ Time-Series                         │
│ - Fraud Scheme                     │ │ - Region                            │
│ - Exposure                         │ │ - Fraud Growth                      │
└────────────────────────────────────┘ └─────────────────────────────────────┘
```

---

## Client Portal Dashboard

- Client-specific KPIs only
- Row-level security by client
- Certified semantic data source
- Subscription-ready PDF layout

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Client Fraud Analytics Portal                                                │
│ Secure Self-Service Reporting                                                │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Client Exposure│ │ Recoveries     │ │ Fraud Events   │ │ Active Cases   │
│ $4.8M          │ │ $1.3M          │ │ 842            │ │ 128            │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ Fraud Exposure Trend               │ │ Top Fraud Schemes                   │
│                                    │ │                                     │
│ Line Chart                         │ │ Treemap / Bar Chart                 │
│ - Monthly Exposure                 │ │ - Upcoding                          │
│ - Recoveries                       │ │ - Duplicate Claims                  │
└────────────────────────────────────┘ └─────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ Geographic Exposure Map                                                      │
│                                                                              │
│ Client-specific regional fraud intelligence                                  │
│ - Exposure                                                                   │
│ - Risk                                                                       │
│ - Provider concentration                                                     │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────┐ ┌─────────────────────────────────────┐
│ High-Risk Providers                │ │ Investigation Outcomes              │
│                                    │ │                                     │
│ Ranked Table                       │ │ Donut / Stacked Bars                │
│ - Provider                         │ │ - Open                              │
│ - Exposure                         │ │ - Closed                            │
│ - Risk Score                       │ │ - Recovered                         │
└────────────────────────────────────┘ └─────────────────────────────────────┘
```

---

# Enterprise Dashboard Design Principles

## Recommended Styling

* Clean executive layout
* Minimal borders and clutter
* Dark blue healthcare palette
* Large KPI typography
* Consistent spacing and alignment
* Governed semantic KPI sourcing
* Interactive global filters
* High-information visual hierarchy

## Global Filters

* Market Segment
* Client Name
* State / Region
* Provider Specialty
* Fraud Scheme
* Claim Type
* Date Range

## Tableau Architecture

```text
SQL Server Warehouse
        ↓
Semantic SQL Views
        ↓
Certified Tableau Data Sources
        ↓
Executive Dashboards
        ↓
Secure Client Distribution
```





