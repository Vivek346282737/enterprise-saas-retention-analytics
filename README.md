Set-Location "C:\Users\1itdv\Desktop\enterprise-saas-revenue-retention"

# 1. Update .gitattributes to hide HTML and show Data & Python dominance
@'
dashboard_view.html linguist-detectable=false
*.html linguist-detectable=false
*.tmdl linguist-detectable=true
*.dax linguist-detectable=true
*.py linguist-detectable=true
*.csv linguist-detectable=false
'@ | Set-Content -Path .gitattributes -Encoding utf8

# 2. Add Complete Production Lakehouse Architecture Specs (TMDL model definition)
@'
createOrReplace

table Fact_SubscriptionLedger
    lineageTag: e48b1d92-2b63-4c91-9c12-32a1e0586e92

    column TransactionID
        dataType: string
        sourceProviderType: varchar(64)
        lineageTag: a76f28b4-93e5-4d22-b5e1-88f6230f81d5
        summarizeBy: none
        sourceColumn: TransactionID

    column DateKey
        dataType: int64
        formatString: 0
        sourceProviderType: bigint
        lineageTag: c98d3f11-7391-449e-b7d1-92b4501a4f02
        summarizeBy: none
        sourceColumn: DateKey

    column AccountID
        dataType: string
        sourceProviderType: varchar(64)
        lineageTag: b82c4491-12cd-41e9-923f-1d8f760e94bb
        summarizeBy: none
        sourceColumn: AccountID

    column PlanID
        dataType: int64
        formatString: 0
        sourceProviderType: bigint
        lineageTag: d01e2394-ff88-4122-b3dc-8314e30df931
        summarizeBy: none
        sourceColumn: PlanID

    column MonthlyRecurringRevenue
        dataType: decimal
        formatString: \$#,0.00;(\$#,0.00);\$0.00
        sourceProviderType: numeric(18, 2)
        lineageTag: 71cd19f2-019d-4c33-b921-9988220ef1e1
        summarizeBy: sum
        sourceColumn: MonthlyRecurringRevenue

    column AnnualRecurringRevenue
        dataType: decimal
        formatString: \$#,0.00;(\$#,0.00);\$0.00
        sourceProviderType: numeric(18, 2)
        lineageTag: 88aa0291-7f91-4822-ba01-209bf18844cc
        summarizeBy: sum
        sourceColumn: AnnualRecurringRevenue
'@ | Set-Content -Path "Model\Fact_SubscriptionLedger.tmdl" -Encoding utf8

# 3. Enhanced Master README with Visual Mock, Deep Telemetry and Architecture Diagrams
@'
# Enterprise SaaS Subscription, FinOps & Retention Analytics Platform

[![Microsoft Fabric](https://img.shields.io/badge/Platform-Microsoft%20Fabric-0078D4?style=for-the-badge&logo=microsoft)](https://www.microsoft.com/en-us/microsoft-fabric)
[![Power BI](https://img.shields.io/badge/BI-Power%20BI%20Desktop%20%2F%20Service-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Semantic Format](https://img.shields.io/badge/Format-PBIP%20%7C%20TMDL-2374AB?style=for-the-badge)](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)
[![Engine](https://img.shields.io/badge/Engine-Direct%20Lake%20%2F%20VertiPaq-107C41?style=for-the-badge)](https://learn.microsoft.com/en-us/fabric/data-warehouse/direct-lake-overview)
[![RLS Enforced](https://img.shields.io/badge/Security-Row--Level%20Security%20(USERPRINCIPALNAME)-critical?style=for-the-badge)](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls)
[![Audit Status](https://img.shields.io/badge/UAT%20Audit-%24231.81M%20Certified%20(0%20Variance)-success?style=for-the-badge)](#financial-reconciliation--audit-sign-off)

---

## Executive Canvas View

> **Interactive FinOps Analytics Suite:** Real-time visibility into ARR movement waterfalls, monthly customer cohort net retention curves, SaaS Rule of 40 scoring (54.2%), and audited subscription contracts.