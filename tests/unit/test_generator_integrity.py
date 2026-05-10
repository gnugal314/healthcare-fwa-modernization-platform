from pipelines.python.generate_all_synthetic_data import generate_regions, generate_clients, generate_providers, generate_members, generate_pharmacies, generate_claims


def test_claims_have_referential_keys():
    regions = generate_regions()
    clients = generate_clients()
    providers = generate_providers(10, regions)
    members = generate_members(20, clients, regions)
    pharmacies = generate_pharmacies(8, regions)
    claims = generate_claims(100, providers, members, pharmacies, clients, regions)
    assert claims["provider_key"].isin(providers["provider_key"]).all()
    assert claims["member_key"].isin(members["member_key"]).all()
    assert claims["pharmacy_key"].isin(pharmacies["pharmacy_key"]).all()
