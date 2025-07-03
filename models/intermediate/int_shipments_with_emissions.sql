with shipments as (

    select *
    from {{ ref('stg_shipments') }}

),

suppliers as (

    select *
    from {{ ref('stg_suppliers') }}

),

emission_factors as (

    select *
    from {{ ref('stg_emission_factors') }}

),

final as (

    select
        s.shipment_id,
        s.supplier_id,
        sup.supplier_name,
        sup.supplier_country,
        sup.sustainability_rating,
        s.weight_kg,
        s.distance_km,
        s.fuel_type,
        s.ship_date,
        s.delivery_delay_days,
        s.origin_country,
        s.destination_country,
        ef.grams_co2_per_km,
        s.distance_km * ef.grams_co2_per_km as total_co2_grams
    from shipments s
    left join suppliers sup
        on s.supplier_id = sup.supplier_id
    left join emission_factors ef
        on s.fuel_type = ef.fuel_type

)

select *
from final