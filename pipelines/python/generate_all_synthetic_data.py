import argparse
import random
import uuid
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

SCHEMES = [
    ("UPCODING", "Provider upcoding", "High"),
    ("DOCTOR_SHOPPING", "Doctor shopping", "High"),
    ("EXCESSIVE_OPIOID", "Excessive opioid dispensing", "High"),
    ("PHANTOM_BILLING", "Phantom billing", "Critical"),
    ("DUPLICATE_CLAIM", "Duplicate claims", "Medium"),
    ("PHARMACY_COLLUSION", "Pharmacy collusion", "Critical"),
    ("HIGH_DOLLAR_OUTLIER", "High-dollar outlier claims", "High"),
    ("GEO_CLUSTER", "Suspicious geographic concentration", "Medium"),
    ("RAPID_BURST", "Rapid claim submission bursts", "High"),
]

OPIOIDS = ["Oxycodone", "Hydrocodone", "Fentanyl", "Morphine", "Tramadol"]
NON_OPIOIDS = ["Atorvastatin", "Metformin", "Lisinopril", "Amlodipine", "Omeprazole", "Albuterol"]
SPECIALTIES = ["Family Medicine", "Internal Medicine", "Pain Management", "Orthopedics", "Cardiology", "Psychiatry"]
CLIENT_TYPES = ["Medicare", "Medicaid", "Commercial", "Employer Group"]
STATES = [("MO", "St. Louis", 38.6270, -90.1994), ("IL", "Cook", 41.8781, -87.6298), ("TX", "Harris", 29.7604, -95.3698), ("FL", "Miami-Dade", 25.7617, -80.1918), ("CA", "Los Angeles", 34.0522, -118.2437)]


def date_key(d):
    return int(d.strftime("%Y%m%d"))


def save_df(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path.with_suffix(".csv"), index=False)
    try:
        df.to_parquet(path.with_suffix(".parquet"), index=False)
    except Exception:
        # pyarrow/fastparquet may not be installed in lightweight demo environments.
        pass


def generate_regions(seed=314):
    random.seed(seed)
    rows = []
    for i, (state, county, lat, lon) in enumerate(STATES, 1):
        rows.append({"region_key": i, "state_code": state, "county": county, "market": f"{state}-{county} Market", "latitude": lat, "longitude": lon})
    return pd.DataFrame(rows)


def generate_clients(seed=314):
    Faker.seed(seed); random.seed(seed)
    rows=[]
    for i, ct in enumerate(CLIENT_TYPES, 1):
        rows.append({"client_key": i, "client_id": str(uuid.uuid4()), "client_name": f"{fake.company()} {ct}", "client_type": ct, "market_segment": ct})
    return pd.DataFrame(rows)


def generate_fraud_schemes():
    return pd.DataFrame([{"scheme_key": i, "scheme_code": c, "scheme_name": n, "severity_level": s, "description": f"Synthetic pattern for {n.lower()}."} for i,(c,n,s) in enumerate(SCHEMES,1)])


def generate_dates(start="2025-01-01", end="2026-12-31"):
    dates = pd.date_range(start=start, end=end, freq="D")
    return pd.DataFrame({
        "date_key": [date_key(d.date()) for d in dates],
        "full_date": [d.date().isoformat() for d in dates],
        "calendar_year": [d.year for d in dates],
        "calendar_quarter": [d.quarter for d in dates],
        "month_number": [d.month for d in dates],
        "month_name": [d.strftime("%B") for d in dates],
        "week_of_year": [int(d.strftime("%U")) for d in dates],
    })


def generate_providers(n, regions, seed=314):
    Faker.seed(seed); random.seed(seed); np.random.seed(seed)
    rows=[]
    for i in range(1,n+1):
        r = regions.sample(1, random_state=seed+i).iloc[0]
        risky = i <= max(3, n//20)
        rows.append({
            "provider_key": i,
            "provider_id": str(uuid.uuid4()),
            "npi": ''.join(random.choices('0123456789', k=10)),
            "provider_name": fake.name(),
            "specialty": random.choice(SPECIALTIES if not risky else ["Pain Management", "Internal Medicine"]),
            "provider_type": random.choice(["Physician", "Group", "Clinic", "DME Supplier"]),
            "network_status": random.choice(["In Network", "Out of Network"]),
            "region_key": int(r.region_key),
            "effective_start_date": "2025-01-01",
            "effective_end_date": "",
            "is_current": 1,
            "is_synthetic_outlier": int(risky)
        })
    return pd.DataFrame(rows)


def generate_members(n, clients, regions, seed=314):
    Faker.seed(seed+1); random.seed(seed+1)
    rows=[]
    for i in range(1,n+1):
        c=clients.sample(1, random_state=seed+i).iloc[0]
        r=regions.sample(1, random_state=seed+n+i).iloc[0]
        rows.append({"member_key": i, "member_id": str(uuid.uuid4()), "masked_member_id": f"MBR-{uuid.uuid4().hex[:10]}", "birth_year": random.randint(1940, 2015), "gender": random.choice(["F", "M", "U"]), "client_key": int(c.client_key), "region_key": int(r.region_key), "effective_start_date": "2025-01-01", "effective_end_date": "", "is_current": 1})
    return pd.DataFrame(rows)


def generate_pharmacies(n, regions, seed=314):
    Faker.seed(seed+2); random.seed(seed+2); np.random.seed(seed+2)
    chains = ["CarePlus", "HealthScript", "WellRx", "Community Pharmacy", "Metro Drugs"]
    rows=[]
    for i in range(1,n+1):
        r=regions.sample(1, random_state=seed+i).iloc[0]
        rows.append({"pharmacy_key": i, "pharmacy_id": str(uuid.uuid4()), "ncpdp_id": ''.join(random.choices('0123456789', k=7)), "pharmacy_name": f"{random.choice(chains)} #{random.randint(100,999)}", "chain_name": random.choice(chains), "region_key": int(r.region_key), "latitude": float(r.latitude)+np.random.normal(0,0.15), "longitude": float(r.longitude)+np.random.normal(0,0.15), "is_current": 1})
    return pd.DataFrame(rows)


def generate_claims(n, providers, members, pharmacies, clients, regions, seed=314):
    Faker.seed(seed+3); random.seed(seed+3); np.random.seed(seed+3)
    rows=[]
    outlier_providers = providers[providers.is_synthetic_outlier==1]
    hot_region = int(regions.iloc[0].region_key)
    start = date(2025,1,1)
    for i in range(1,n+1):
        fraudulent_pattern = random.random() < 0.12
        p = (outlier_providers.sample(1).iloc[0] if fraudulent_pattern and random.random()<0.55 else providers.sample(1).iloc[0])
        m = members.sample(1).iloc[0]
        ph = pharmacies[pharmacies.region_key==p.region_key].sample(1).iloc[0] if not pharmacies[pharmacies.region_key==p.region_key].empty else pharmacies.sample(1).iloc[0]
        c = clients[clients.client_key==m.client_key].iloc[0]
        rkey = hot_region if fraudulent_pattern and random.random()<0.35 else int(p.region_key)
        service_date = start + timedelta(days=random.randint(0, 700))
        paid_date = service_date + timedelta(days=random.randint(3, 45))
        is_opioid = int((fraudulent_pattern and random.random()<0.45) or random.random()<0.08)
        drug = random.choice(OPIOIDS if is_opioid else NON_OPIOIDS)
        base = np.random.gamma(2.0, 120.0)
        multiplier = random.choice([3,5,8]) if fraudulent_pattern and random.random()<0.3 else 1
        billed = round(base*multiplier + random.uniform(10,250), 2)
        allowed = round(billed*random.uniform(0.45,0.9), 2)
        denied = round(allowed if random.random()<0.08 or (fraudulent_pattern and random.random()<0.12) else 0, 2)
        paid = 0 if denied > 0 else round(allowed*random.uniform(0.65,1.0), 2)
        rows.append({
            "claim_key": i, "claim_id": str(uuid.uuid4()), "service_date_key": date_key(service_date), "paid_date_key": date_key(paid_date),
            "provider_key": int(p.provider_key), "member_key": int(m.member_key), "pharmacy_key": int(ph.pharmacy_key), "client_key": int(c.client_key), "region_key": rkey,
            "claim_type": random.choice(["Rx", "Professional", "Outpatient"]), "diagnosis_code": random.choice(["M54.5","E11.9","I10","F41.9","G89.4"]),
            "procedure_code": random.choice(["99213","99214","99215","80307","G0480","J3490"]), "ndc_code": ''.join(random.choices('0123456789', k=11)),
            "drug_name": drug, "is_opioid": is_opioid, "billed_amount": billed, "allowed_amount": allowed, "paid_amount": paid, "denied_amount": denied,
            "claim_status": "Denied" if denied > 0 else random.choice(["Paid", "Paid", "Paid", "Reversed"]),
            "fraud_injected_flag": int(fraudulent_pattern)
        })
    df=pd.DataFrame(rows)
    # Inject duplicate claim pattern by duplicating a small number of rows with new claim keys.
    dup=df.sample(max(1,n//100), random_state=seed).copy()
    dup["claim_key"] = range(n+1, n+1+len(dup))
    dup["claim_status"] = "Duplicate Review"
    return pd.concat([df, dup], ignore_index=True)


def generate_fraud_events(claims, seed=314):
    random.seed(seed+4); np.random.seed(seed+4)
    suspect = claims[(claims.fraud_injected_flag==1) | (claims.paid_amount > claims.paid_amount.quantile(.97)) | (claims.is_opioid==1)].copy()
    suspect = suspect.sample(min(len(suspect), max(20, len(claims)//6)), random_state=seed)
    rows=[]
    for i, row in enumerate(suspect.itertuples(), 1):
        scheme = random.choice(SCHEMES)
        risk = min(0.99, max(0.05, np.random.beta(4,2) if row.fraud_injected_flag else np.random.beta(2,4)))
        exposure = round(float(row.paid_amount) * random.uniform(0.5, 1.5), 2)
        rows.append({"detection_key": i, "detection_id": str(uuid.uuid4()), "claim_id": row.claim_id, "detection_date_key": row.paid_date_key, "provider_key": row.provider_key, "member_key": row.member_key, "pharmacy_key": row.pharmacy_key, "client_key": row.client_key, "region_key": row.region_key, "scheme_key": SCHEMES.index(scheme)+1, "risk_score": round(risk,4), "suspected_exposure_amount": exposure, "detection_source": random.choice(["Rules", "ML", "Investigator Referral", "Streaming Alert"]), "model_version": "risk_model_v0.1", "alert_status": random.choice(["Open", "Under Review", "Confirmed", "False Positive"] )})
    return pd.DataFrame(rows)


def generate_investigation_actions(events, seed=314):
    random.seed(seed+5)
    rows=[]
    for i, row in enumerate(events.itertuples(),1):
        confirmed = row.alert_status == "Confirmed" or random.random()<0.35
        stopped = round(row.suspected_exposure_amount * random.uniform(0.2,0.85),2) if confirmed else 0
        recovered = round(row.suspected_exposure_amount * random.uniform(0.05,0.35),2) if confirmed else 0
        rows.append({"action_key": i, "action_id": str(uuid.uuid4()), "detection_id": row.detection_id, "action_date_key": row.detection_date_key, "investigator_team": random.choice(["SIU Pharmacy", "SIU Provider", "Client Integrity", "Medicaid Program Integrity"]), "action_type": random.choice(["Provider Outreach", "Payment Hold", "Audit Request", "Referral", "Recovery Letter"]), "action_status": "Closed" if confirmed else random.choice(["Open", "Monitoring"]), "stopped_payment_amount": stopped, "recovered_amount": recovered, "notes": "Synthetic investigation action."})
    return pd.DataFrame(rows)


def create_insert_script(df, table, path, limit=25):
    lines=[f"-- Sample inserts for {table}"]
    for _, row in df.head(limit).iterrows():
        cols=', '.join(f"[{c}]" for c in df.columns)
        vals=[]
        for v in row.values:
            if pd.isna(v) or v == "": vals.append("NULL")
            elif isinstance(v, (int, np.integer, float, np.floating)): vals.append(str(v))
            else: vals.append("'" + str(v).replace("'", "''") + "'")
        lines.append(f"INSERT INTO {table} ({cols}) VALUES ({', '.join(vals)});")
    Path(path).write_text('\n'.join(lines))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--providers', type=int, default=100)
    parser.add_argument('--members', type=int, default=500)
    parser.add_argument('--pharmacies', type=int, default=80)
    parser.add_argument('--claims', type=int, default=5000)
    parser.add_argument('--seed', type=int, default=314)
    parser.add_argument('--out', default='data')
    args=parser.parse_args()

    out=Path(args.out)
    synthetic=out/'synthetic'; bronze=out/'bronze'; silver=out/'silver'; gold=out/'gold'; inserts=out/'sample_sql_inserts'
    for p in [synthetic, bronze, silver, gold, inserts]: p.mkdir(parents=True, exist_ok=True)

    regions=generate_regions(args.seed); clients=generate_clients(args.seed); schemes=generate_fraud_schemes(); dates=generate_dates()
    providers=generate_providers(args.providers, regions, args.seed)
    members=generate_members(args.members, clients, regions, args.seed)
    pharmacies=generate_pharmacies(args.pharmacies, regions, args.seed)
    claims=generate_claims(args.claims, providers, members, pharmacies, clients, regions, args.seed)
    events=generate_fraud_events(claims, args.seed)
    actions=generate_investigation_actions(events, args.seed)

    for name, df in {
        'dim_region': regions, 'dim_client': clients, 'dim_fraud_scheme': schemes, 'dim_date': dates,
        'dim_provider': providers, 'dim_member': members, 'dim_pharmacy': pharmacies,
        'fact_claims': claims, 'fact_fraud_detection': events, 'fact_investigation_actions': actions
    }.items():
        save_df(df, synthetic/name)
        save_df(df, bronze/name)
        save_df(df, silver/name)
        save_df(df, gold/name)
        create_insert_script(df, f"gold.{name}", inserts/f"{name}_sample_inserts.sql")

    print(f"Generated synthetic FWA data under {out.resolve()}")

if __name__ == '__main__':
    main()
